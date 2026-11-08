project_root/
│
├── inference_engine/          ⭐ 核心（
│   ├── queue_manager.py       # 队列管理
│   ├── batch_scheduler.py     # 批处理调度
│   ├── worker.py              # worker执行器
│   ├── task.py                # 请求封装
│   └── config.py              # 配置（batch size等）
│
├── embedding_service/
│   └── service.py
│
├── reranker_service/
│   └── service.py
│
├── llm_service/
│   └── service.py



请求1 \
请求2  \
请求3   →  队列 → 批处理 → 一次 model.encode()
请求4  /
请求5 /

embedding_service
  ├── queue
  ├── worker x 3
  ├── batch_size x 64

QUEUE_TIMEOUT = 50ms
INFERENCE_TIMEOUT = 200ms
TOTAL_TIMEOUT = 300ms

reranker_service
  ├── queue
  ├── worker x 2
  ├── batch_size x 64
QUEUE_TIMEOUT = 100ms
INFERENCE_TIMEOUT = 500ms
TOTAL_TIMEOUT = 800ms

llm_service
  ├── queue
  ├── worker x 1
  ├── batch_size x 1

QUEUE_TIMEOUT = 500ms ~ 2s
INFERENCE_TIMEOUT = 5s ~ 30s
TOTAL_TIMEOUT = 10s ~ 60s
