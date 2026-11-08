from fastapi import FastAPI
from .router import router

from .asyn_inference import worker
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app):
    worker.start()
    yield
    

app = FastAPI(title="Reranker Service", lifespan=lifespan)

app.include_router(router)