from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import ChatHistory
from schemas import ChatRequest
from services.rag import get_rag_chain

router = APIRouter(prefix="/chat", tags=["Chat"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    chain = get_rag_chain()
    result = chain(request.question)

    history = ChatHistory(
        question=request.question,
        answer=result["result"],
        owner_id=request.user_id
    )
    db.add(history)
    db.commit()

    return {
        "answer": result["result"],
        "sources": result["source_documents"]
    }

@router.get("/")
def get_history(user_id: str, db: Session = Depends(get_db)):
    return db.query(ChatHistory).filter(ChatHistory.owner_id == user_id).all()
