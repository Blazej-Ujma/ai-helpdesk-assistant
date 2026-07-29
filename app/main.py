import json

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# Create the FastAPI application
app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Load HTML templates from the templates folder
templates = Jinja2Templates(directory="app/templates")

with open("app/knowledge/faq.json", "r") as file:
    faq_data = json.load(file)

class ChatMessage(BaseModel):
    message: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """
    Display the home page of the AI Helpdesk Assistant.
    """
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )

@app.post("/chat")
def chat(chat_message: ChatMessage):
    message = chat_message.message.lower()

    for faq in faq_data:
        for keyword in faq["keywords"]:
            if keyword in message:
                return {
                    "reply": faq["answer"]
                }

    return {
        "reply": (
            "I could not find a direct solution. "
            "I can create an IT ticket for you."
        )
    }