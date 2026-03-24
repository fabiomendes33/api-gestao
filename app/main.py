from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import users, items

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Gestão",
    description="API RESTful completa com autenticação JWT, CRUD de usuários e itens.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(items.router)

@app.get("/", tags=["Root"])
def root():
    return {"message": "API de Gestão v1.0 — Online ✅"}
