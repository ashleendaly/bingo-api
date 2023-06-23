from fastapi import FastAPI
from src.routes import bingo
from src.repository.instance import bingo_repository

app = FastAPI(title="Bingo API", docs_url="/")
app.include_router(bingo.router, prefix="/bingo", tags=["bingo"])
app.state.bingo_repository = bingo_repository
