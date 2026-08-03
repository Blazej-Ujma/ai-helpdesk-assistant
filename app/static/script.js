const quickActionButtons = document.querySelectorAll(".quick-action");
const messageInput = document.querySelector("#user-message");
const chatForm = document.querySelector("#chat-form");
const chatMessages = document.querySelector("#chat-messages");

quickActionButtons.forEach((button) => {
    button.addEventListener("click", () => {
        messageInput.value = button.dataset.message;
        messageInput.focus();
    });
});

function formatAssistantReply(reply, container) {
    const cleanedReply = reply.trim();

    // Find numbered steps such as "1.", "1)", "2." or "2)".
    const stepPattern = /(?:^|\s)(\d+)[.)]\s+/g;
    const matches = [...cleanedReply.matchAll(stepPattern)];

    // If no numbered steps exist, show the answer as normal text.
    if (matches.length === 0) {
        const paragraph = document.createElement("p");
        paragraph.textContent = cleanedReply;
        container.appendChild(paragraph);
        return;
    }

    // Everything before the first numbered step becomes the title.
    const titleText = cleanedReply
        .slice(0, matches[0].index)
        .trim();

    if (titleText) {
        const title = document.createElement("p");
        title.classList.add("assistant-title");
        title.textContent = titleText;
        container.appendChild(title);
    }

    const list = document.createElement("ol");
    list.classList.add("assistant-steps");

    matches.forEach((match, index) => {
        const stepStart = match.index + match[0].length;
        const nextStepStart =
            index + 1 < matches.length
                ? matches[index + 1].index
                : cleanedReply.length;

        let stepText = cleanedReply
            .slice(stepStart, nextStepStart)
            .trim();

        let closingMessage = "";

        // Separate the final ticket sentence from the last list item.
        const closingMarker = stepText.indexOf("➡️");

        if (closingMarker !== -1) {
            closingMessage = stepText
                .slice(closingMarker)
                .trim();

            stepText = stepText
                .slice(0, closingMarker)
                .trim();
        }

        const item = document.createElement("li");
        item.textContent = stepText;
        list.appendChild(item);

        if (closingMessage) {
            list.dataset.closingMessage = closingMessage;
        }
    });

    container.appendChild(list);

    if (list.dataset.closingMessage) {
        const closing = document.createElement("p");
        closing.classList.add("assistant-closing");
        closing.textContent = list.dataset.closingMessage;
        container.appendChild(closing);
    }
}

chatForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const message = messageInput.value.trim();

    if (message === "") {
        return;
    }

    const userMessage = document.createElement("div");
    userMessage.classList.add("user-message", "message-bubble");
    userMessage.textContent = message;
    chatMessages.appendChild(userMessage);

    const typingIndicator = document.createElement("div");
    typingIndicator.classList.add("typing-indicator");
    typingIndicator.textContent = "AI is typing...";
    chatMessages.appendChild(typingIndicator);

    chatMessages.scrollTop = chatMessages.scrollHeight;

    messageInput.value = "";
    messageInput.focus();

    setTimeout(() => {
        fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Server request failed.");
                }

                return response.json();
            })
            .then((data) => {
                typingIndicator.remove();

                const assistantMessage = document.createElement("div");
                assistantMessage.classList.add(
                    "assistant-message",
                    "message-bubble"
                );

                formatAssistantReply(data.reply, assistantMessage);

                chatMessages.appendChild(assistantMessage);
                chatMessages.scrollTop = chatMessages.scrollHeight;
            })
            .catch((error) => {
                console.error(error);
                typingIndicator.remove();

                const assistantMessage = document.createElement("div");
                assistantMessage.classList.add(
                    "assistant-message",
                    "message-bubble"
                );

                assistantMessage.textContent =
                    "An unexpected error occurred. Please try again.";

                chatMessages.appendChild(assistantMessage);
                chatMessages.scrollTop = chatMessages.scrollHeight;
            });
    }, 1500);
});