# inference_engine async begain
import asyncio
from inference_engine.queue_manager import QueueManager
from inference_engine.batch_scheduler import BatchScheduler
from inference_engine.worker import InferenceWorker
from config.loader import ConfigLoader
# inference_engine async end

from .services import rerank_documents

_, runtime_config = ConfigLoader.get_service_config("reranker_service")

queue_manger = QueueManager(max_queue_size=runtime_config.max_queue_size, queue_timeout=runtime_config.queue_timeout)

def process_fn(batch_inputs):
    results = []
    for item in batch_inputs:
        query = item['query']
        documents = item['documents']

        reranked_docs = rerank_documents(query, documents)
        results.append(reranked_docs)

    return results



batch_scheduler = BatchScheduler(queue_manger, process_fn, batch_size=runtime_config.batch_size, batch_timeout=runtime_config.batch_timeout)
worker = InferenceWorker(batch_scheduler, worker_count=runtime_config.worker_count, inference_timeout=runtime_config.inference_timeout, total_timeout=runtime_config.total_timeout)
