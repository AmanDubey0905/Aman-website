from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
import shutil
import os
from database import SessionLocal
from models import Document
from services.file_processor import process_document

router = APIRouter(prefix="/documents", tags=["Documents"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
def upload_document(file: UploadFile = File(...), user_id: str = "", db: Session = Depends(get_db)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    doc = Document(name=file.filename, path=file_path, owner_id=user_id)
    db.add(doc)
    db.commit()
    db.refresh(doc)

    return {"message": "Uploaded", "id": doc.id}

@router.get("/")
def get_documents(user_id: str, db: Session = Depends(get_db)):
    return db.query(Document).filter(Document.owner_id == user_id).all()

@router.delete("/{doc_id}")
def delete_document(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if doc:
        os.remove(doc.path)
        db.delete(doc)
        db.commit()
    return {"message": "Deleted"}

@router.post("/process/{doc_id}")
def process_doc(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    text = process_document(doc.path)
    doc.content = text
    doc.status = "processed"
    db.commit()
    return {"message": "Processed"}
