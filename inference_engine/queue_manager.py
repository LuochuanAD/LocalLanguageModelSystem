import asyncio


class QueueManager:
    def __init__(self, max_queue_size=1000, queue_timeout=0.1):
        self.queue = asyncio.Queue(maxsize=max_queue_size)
        self.queue_timeout = queue_timeout

    async def put_task(self, task):
        await self.queue.put(task)

    async def get_batch(self, batch_size):
        batch = []
        for _ in range(batch_size):
            try:
                task = await asyncio.wait_for(self.queue.get(), timeout=self.queue_timeout)
                batch.append(task)
            except asyncio.TimeoutError:
                break
        return batch