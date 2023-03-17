#!/usr/bin/python3
"""Farm module - main file."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .todos import todos_router

app: FastAPI = FastAPI()
origins: list[str] = ["http://127.0.0.1:3000",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["FARM App"])
async def root() -> dict:
    """Root url for farm application."""
    return {"message": "Welcome to FARM app."}


app.include_router(router=todos_router)
