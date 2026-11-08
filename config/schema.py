from dataclasses import dataclass

@dataclass
class ModelConfig:
    type: str
    model_name: str
    device: str = "cpu"

@dataclass
class RuntimeConfig:
    batch_size: int
    batch_timeout: float
    max_queue_size: int
    worker_count: int
    queue_timeout: float
    inference_timeout: float
    total_timeout: float
    rate_limit: int
    enable_cache: bool