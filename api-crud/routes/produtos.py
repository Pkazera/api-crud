from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models.produto import Produto
from schemas import ProdutoCreate, ProdutoUpdate, ProdutoResponse
from auth import verificar_token

router = APIRouter()

# ── GET /produtos ──────────────────────────────────────────────
@router.get("/", response_model=List[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()

# ── GET /produtos/:id ──────────────────────────────────────────
@router.get("/{id}", response_model=ProdutoResponse)
def buscar_produto(id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

# ── POST /produtos  (requer JWT) ───────────────────────────────
@router.post("/", response_model=ProdutoResponse, status_code=201)
def criar_produto(
    dados: ProdutoCreate,
    db: Session = Depends(get_db),
    _: dict = Depends(verificar_token)
):
    novo = Produto(**dados.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

# ── PUT /produtos/:id  (requer JWT) ───────────────────────────
@router.put("/{id}", response_model=ProdutoResponse)
def atualizar_produto(
    id: int,
    dados: ProdutoUpdate,
    db: Session = Depends(get_db),
    _: dict = Depends(verificar_token)
):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(produto, campo, valor)
    db.commit()
    db.refresh(produto)
    return produto

# ── DELETE /produtos/:id  (requer JWT) ────────────────────────
@router.delete("/{id}", status_code=204)
def deletar_produto(
    id: int,
    db: Session = Depends(get_db),
    _: dict = Depends(verificar_token)
):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(produto)
    db.commit()
