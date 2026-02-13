from pydantic import BaseModel

class DocumentOut(BaseModel):
    id: int
    name: str
    status: str

    class Config:
        from_attributes = True

class ChatRequest(BaseModel):
    question: str
    user_id: str
