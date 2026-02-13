from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import documents, chat, collections
from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(documents.router)
app.include_router(chat.router)
app.include_router(collections.router)

@app.get("/")
def root():
    return {"message": "PKB API Running"}
