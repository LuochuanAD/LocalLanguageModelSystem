from pydantic import BaseModel

class RerankRequest(BaseModel):
    query: str
    documents: list[str]
class RerankResponse(BaseModel):
    reranked_documents: list[str]  