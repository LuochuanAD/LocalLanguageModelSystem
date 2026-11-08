import asyncio


class BatchScheduler:
    def __init__(self, queue_manager, process_fn, batch_size=32, batch_timeout=0.1):
        self.queue_manager = queue_manager
        self.process_fn = process_fn
        self.max_batch_size = batch_size
        self.batch_timeout = batch_timeout

    async def start(self):
        while True:
            batch = await self.queue_manager.get_batch(self.max_batch_size, self.batch_timeout)
            if not batch:
                continue

            inputs = [task.data for task in batch]

            results = self.process_fn(inputs)

            for task, result in zip(batch, results):
                task.future.set_result(result)

