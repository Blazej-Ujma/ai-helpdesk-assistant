import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Create the FastAPI application
app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Load HTML templates from the templates folder
templates = Jinja2Templates(directory="app/templates")

with open("app/knowledge/faq.json", "r") as file:
    faq_data = json.load(file)

with open("app/tickets.json", "r") as file:
    tickets = json.load(file)

class ChatMessage(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

@app.get("/test-ai")
def test_ai():
    response = client.responses.create(
        model="gpt-5",
        input="Say hello in one short sentence."
    )

    return {
        "reply": response.output_text
    }

@app.get("/test-ai")
def test_ai():
    response = client.responses.create(
        model="gpt-5",
        input="Say hello in one short sentence."
    )

    return {
        "reply": response.output_text
    }

previous_response_id = None

@app.post("/chat")
def chat(chat_message: ChatMessage):
    global previous_response_id

    message = chat_message.message.lower()

    # First, search the local FAQ knowledge base.
    for faq in faq_data:
        for keyword in faq["keywords"]:
            if keyword in message:
                return {
                    "reply": faq["answer"]
                }

    try:
        request_data = {
            "model": "gpt-5",
            "instructions": (
                "You are an internal IT helpdesk assistant. "
                "Answer in very simple English for users with little technical knowledge. "
                "Use a maximum of 4 short troubleshooting steps. "
                "Avoid technical words and explain every action clearly. "
                "Keep the answer short. "
                "Use the previous conversation context when the user sends a short follow-up. "
                "Do not invent company-specific information. "
                "If the user asks for human support, if administrator access is required, "
                "or if the problem cannot be solved safely with simple troubleshooting steps, "
                "respond exactly in this format:\n"
                "CREATE_TICKET\n"
                "Title: <short ticket title>\n"
                "Description: <clear one-paragraph summary for the IT technician>\n"
                "Do not write anything before CREATE_TICKET. "
                "If the issue can be solved safely, do not create a ticket."
            ),
            "input": chat_message.message,
            "reasoning": {
                "effort": "minimal"
            },
            "max_output_tokens": 800
        }

        if previous_response_id is not None:
            request_data["previous_response_id"] = previous_response_id

        response = client.responses.create(**request_data)

        previous_response_id = response.id
        reply = response.output_text.strip()

        # Create a structured ticket when the AI requests human support.
        if reply.startswith("CREATE_TICKET"):
            lines = reply.splitlines()

            title = "AI Generated Ticket"
            description_parts = []
            reading_description = False

            for line in lines:
                clean_line = line.strip()

                if clean_line.startswith("Title:"):
                    title = clean_line.removeprefix("Title:").strip()

                elif clean_line.startswith("Description:"):
                    first_description_line = clean_line.removeprefix(
                        "Description:"
                    ).strip()

                    if first_description_line:
                        description_parts.append(first_description_line)

                    reading_description = True

                elif reading_description and clean_line:
                    description_parts.append(clean_line)

            description = " ".join(description_parts).strip()

            if description == "":
                description = (
                    "The user requires human IT support. "
                    f"Original request: {chat_message.message}"
                )

            ticket_id = len(tickets) + 1

            new_ticket = {
                "id": ticket_id,
                "title": title,
                "description": description,
                "status": "open",
                "created_by": "AI Helpdesk Assistant"
            }

            tickets.append(new_ticket)

            with open("app/tickets.json", "w") as file:
                json.dump(tickets, file, indent=4)

            return {
                "reply": (
                    "Human IT support is required for this issue.\n\n"
                    "An IT support ticket has been created automatically.\n"
                    f"Ticket number: #{ticket_id:04d}"
                )
            }

        # Return a normal AI answer.
        return {
            "reply": reply
        }

    except Exception as e:
        print(e)
        ticket_id = len(tickets) + 1

        new_ticket = {
            "id": ticket_id,
            "title": "AI Service Error",
            "description": (
                "The AI service was unavailable while processing this request. "
                f"Original request: {chat_message.message}"
            ),
            "status": "open",
            "created_by": "AI Helpdesk Assistant"
        }

        tickets.append(new_ticket)

        with open("app/tickets.json", "w") as file:
            json.dump(tickets, file, indent=4)

        return {
            "reply": (
                "The AI service is currently unavailable. "
                "An IT support ticket has been created automatically.\n"
                f"Ticket number: #{ticket_id:04d}"
            )
        }