from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .api.v1.endpoints import script_endpoint
app = FastAPI()
templates = Jinja2Templates(directory=r"D:\data\toolshelf\dist")
app.include_router(script_endpoint.router, prefix="/api/v1")

@app.get("/", response_class=HTMLResponse)
def get_html():
    return templates.TemplateResponse("index.html", {"request": {}})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8050)