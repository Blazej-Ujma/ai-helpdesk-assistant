from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Create the FastAPI application
app = FastAPI()

# Load HTML templates from the templates folder
templates = Jinja2Templates(directory="app/templates")


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