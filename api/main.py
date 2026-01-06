import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from api.routers import projects_router, user_stories_router


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/html", response_class=HTMLResponse)
def read_html():
    from api.services import basic_html

    return basic_html()


app.include_router(user_stories_router, prefix="", tags=["user_stories"])
app.include_router(projects_router, prefix="/projects", tags=["projects"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
