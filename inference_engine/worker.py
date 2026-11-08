import asyncio

class InferenceWorker:
    def __init__(self, batch_scheduler, worker_count=1, inference_timeout=10.0, total_timeout=30.0):
        self.batch_scheduler = batch_scheduler
        self.worker_count = worker_count
        self.inference_timeout = inference_timeout
        self.total_timeout = total_timeout
        
    def start(self):
        asyncio.create_task(self.batch_scheduler.start())
        