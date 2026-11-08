from fastapi import APIRouter
from .schemas import RerankRequest, RerankResponse
from .services import rerank_documents

# inference_engine async begain
import asyncio
from inference_engine.task import InferenceTask
from inference_engine.queue_manager import QueueManager
# inference_engine async end

queue_manger = QueueManager()

router = APIRouter()

@router.post("/rerank", response_model=RerankResponse)
def rerank(request: RerankRequest) -> RerankResponse:
    reranked_documents = rerank_documents(request.query, request.documents)
    return RerankResponse(reranked_documents=reranked_documents)


@router.post("/rerank_async")
async def rerank_async(request: RerankRequest):
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    task = InferenceTask(data={'query': request.query, 'documents': request.documents}, future=future)
    await queue_manger.put_task(task)
    result = await future
    
    return {"rerank_async_documents": result}

