from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_index() -> FileResponse:
    return FileResponse("index.html")


@app.get("/game")
async def click() -> FileResponse:
    return FileResponse("game.html")
