from fastapi import FastAPI
from database import engine, Base
from routes import produtos, auth

# Cria as tabelas no banco se não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API CRUD - Produtos", version="1.0.0")

# Rotas
app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(produtos.router, prefix="/produtos", tags=["Produtos"])

@app.get("/")
def root():
    return {"message": "API CRUD funcionando!"}
