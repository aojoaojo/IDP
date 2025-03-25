from fastapi import FastAPI
from routers import empresa, candidato
from models import Base
from config import engine

app = FastAPI()

app.include_router(empresa.router)
app.include_router(candidato.router)

