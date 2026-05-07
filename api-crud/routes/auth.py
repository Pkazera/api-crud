from fastapi import APIRouter, HTTPException
from schemas import LoginRequest, TokenResponse
from auth import criar_token
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

# Usuário fixo para simplificar (pode evoluir para tabela de usuários)
USUARIO = os.getenv("ADMIN_USER", "admin")
SENHA   = os.getenv("ADMIN_PASS", "admin123")

@router.post("/login", response_model=TokenResponse)
def login(dados: LoginRequest):
    if dados.username != USUARIO or dados.password != SENHA:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = criar_token({"sub": dados.username})
    return {"access_token": token, "token_type": "bearer"}
