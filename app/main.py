from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Tell FastAPI where HTML templates are
templates = Jinja2Templates(directory="app/templates")

# Serve static files like CSS
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "Hello World!",
            "message": "Welcome to my first FastAPI website!"
        }
    )