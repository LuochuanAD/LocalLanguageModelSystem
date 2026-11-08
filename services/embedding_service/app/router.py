from fastapi import APIRouter
from app.schemas import (
    EmbeddingRequest,
    BatchEmbeddingRequest,
    EmbeddingResponse,
    BatchEmbeddingResponse,
)
from app.service import embed_query, embed_batch, embed_passage

# inference_engine async begain
import asyncio
from inference_engine.task import InferenceTask
from inference_engine.queue_manager import QueueManager
# inference_engine async end

queue_manger = QueueManager()



router = APIRouter()

@router.get("/")
def root():
    return {"message": "Welcome to the E5 Embedding Service!"}  

@router.post("/embed", response_model=EmbeddingResponse)
def embed(request: EmbeddingRequest):
    vector = embed_query(request.text)
    return {"vector": vector}

@router.post("/embed_batch", response_model=BatchEmbeddingResponse)
def batch_embed(request: BatchEmbeddingRequest):
    vectors = embed_batch(request.texts, is_query=request.is_query)
    return {"vectors": vectors}

@router.post("/embed_query_async")
async def embed_query_async(request: EmbeddingRequest):
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    task = InferenceTask(data=request.text, future=future)
    await queue_manger.put_task(task)
    result = await future
    
    return {"rerank_async_documents": result}

@router.post("/embed_batch_async")
async def embed_batch_async(request: BatchEmbeddingRequest):
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    task = InferenceTask(data={"texts": request.texts, "is_query": request.is_query}, future=future)
    await queue_manger.put_task(task)
    result = await future
    
    return {"rerank_async_documents": result}


