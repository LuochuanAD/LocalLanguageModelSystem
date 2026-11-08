LLM_SERVICE_CONFIG = {
    "llm_model_name": "gpt-3.5-turbo",
    
    "batch_size": 4,
    "batch_timeout": 0.05,

    "max_queue_size": 50,
    "worker_count": 1,

    "queue_timeout": 0.2,
    "inference_timeout": 2.0,
    "total_timeout": 3.0,

    "rate_limit": 10,
    "enable_cache": False,

}