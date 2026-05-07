from pydantic import BaseModel
from typing import Optional

class ProdutoCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float
    quantidade: int = 0

class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    preco: Optional[float] = None
    quantidade: Optional[int] = None

class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: Optional[str]
    preco: float
    quantidade: int

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
