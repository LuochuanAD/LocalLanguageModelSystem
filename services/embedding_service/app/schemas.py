from pydantic import BaseModel
from typing import List

class EmbeddingRequest(BaseModel):
    text: str

class BatchEmbeddingRequest(BaseModel):
    texts: List[str]
    is_query: bool = False

class EmbeddingResponse(BaseModel):
    vector: List[float]

class BatchEmbeddingResponse(BaseModel):
    vectors: List[List[float]]
      