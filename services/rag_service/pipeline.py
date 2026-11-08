# pipeline.py

def rag_pipeline(query):
    # 1. embedding（调用你的embedding服务）
    query_vector = call_embedding_service(query)

    # 2. Qdrant检索（本地模块）
    docs = search_vectors(query_vector)

    # 3. rerank（调用服务）
    reranked = call_reranker_service(query, docs)

    # 4. LLM生成（后面加）
    return reranked