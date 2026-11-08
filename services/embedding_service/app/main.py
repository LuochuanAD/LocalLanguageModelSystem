from fastapi import FastAPI
from .router import router

from .asyn_inference import worker_batch, worker_query
from contextlib import asynccontextmanager

app = FastAPI(title="E5 Embedding Service")



@asynccontextmanager
async def lifespan(app):
    worker_batch.start()
    worker_query.start()
    yield

app.include_router(router)