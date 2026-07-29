const quickActionButtons = document.querySelectorAll(".quick-action");
const messageInput = document.querySelector("#user-message");

quickActionButtons.forEach((button) => {
    button.addEventListener("click", () => {
        const message = button.dataset.message;

        messageInput.value = message;
        messageInput.focus();
    });
});

const chatForm = document.querySelector("#chat-form");
const chatMessages = document.querySelector("#chat-messages");

const responses = {
    password:
        "I can help you reset your password. Please open the password reset portal and follow the instructions.",

    outlook:
        "Please restart Outlook first. If it still does not open, restart your computer and try again.",

    vpn:
        "Please check your internet connection and reconnect to the company VPN.",

    default:
        "I could not find a direct solution. I can create an IT ticket for you."
};

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
        typingIndicator.remove();

        const assistantMessage = document.createElement("div");
        assistantMessage.classList.add(
            "assistant-message",
            "message-bubble"
        );

        const lowerMessage = message.toLowerCase();

        if (lowerMessage.includes("password")) {
            assistantMessage.textContent = responses.password;
        } else if (lowerMessage.includes("outlook")) {
            assistantMessage.textContent = responses.outlook;
        } else if (lowerMessage.includes("vpn")) {
            assistantMessage.textContent = responses.vpn;
        } else {
            assistantMessage.textContent = responses.default;
        }

        chatMessages.appendChild(assistantMessage);

        chatMessages.scrollTop = chatMessages.scrollHeight;
    }, 1500);
});
