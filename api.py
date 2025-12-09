from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from time import sleep

app = FastAPI()

@app.get("/")
async def root():
    return PlainTextResponse("mesage Hola Joswald")