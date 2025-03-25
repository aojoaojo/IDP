from config import SessionLocal
from pydantic import BaseModel
from fastapi import FastAPI, status, Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import *
from sqlalchemy.exc import SQLAlchemyError
from typing import List
from sqlalchemy import text
from config import engine

class VagaCreate(BaseModel):
    id_vaga: int
    id_empresa: int
    nivel_experiencia: str
    cargo: str
    regime_trabalho: str
    salario: float
    beneficios: str
    status: str
    habilidade_necessaria: str
    
class VagaUpdate(BaseModel):
    id_vaga: int | None = None
    id_empresa: int | None = None
    nivel_experiencia: str | None = None
    cargo: str | None = None
    regime_trabalho: str | None = None
    salario: float | None = None
    beneficios: str | None = None
    status: str | None = None
    habilidade_necessaria: str | None = None
    
class VagaResponse(BaseModel):
    id_vaga: int
    id_empresa: int
    nivel_experiencia: str
    cargo: str
    regime_trabalho: str
    salario: float
    beneficios: str
    status: str
    habilidade_necessaria: str
    
router = APIRouter(
    tags=["vaga"],
    # dependencies=[Depends(get_token_header)], # TODO: Implementar autenticação
    responses={404: {"description": "Not found"}},
)

@router.post("/vaga/", response_model=VagaCreate, status_code=status.HTTP_201_CREATED)
def create_vaga(vaga: VagaCreate, db: Session): # TODO Implementar autenticação
    db_vaga = Vaga(
        id_vaga=vaga.id_vaga,
        id_empresa=vaga.id_empresa,
        nivel_experiencia=vaga.nivel_experiencia,
        cargo=vaga.cargo,
        regime_trabalho=vaga.regime_trabalho,
        salario=vaga.salario,
        beneficios=vaga.beneficios,
        status=vaga.status,
        habilidade_necessaria=vaga.habilidade_necessaria
    )
    db.add(db_vaga)
    db.commit()
    db.refresh(db_vaga)
    return db_vaga

@router.put("/vaga/{id_vaga}", response_model=VagaUpdate)
def update_vaga(id_vaga: int, vaga: VagaUpdate, db: Session):
    db_vaga = db.query(Vaga).filter(Vaga.id_vaga == id_vaga).first()
    if not db_vaga:
        raise HTTPException(status_code=404, detail="Vaga não encontrada")
    db_vaga.id_vaga = vaga.id_vaga
    db_vaga.id_empresa = vaga.id_empresa
    db_vaga.nivel_experiencia = vaga.nivel_experiencia
    db_vaga.cargo = vaga.cargo
    db_vaga.regime_trabalho = vaga.regime_trabalho
    db_vaga.salario = vaga.salario
    db_vaga.beneficios = vaga.beneficios
    db_vaga.status = vaga.status
    db_vaga.habilidade_necessaria = vaga.habilidade_necessaria
    db.commit()
    db.refresh(db_vaga)
    return db_vaga

@router.get("/vaga/{id_vaga}", response_model=VagaResponse) #lista vagas por id
def read_vaga(id_vaga: int, db: Session):
    db_vaga = db.query(Vaga).filter(Vaga.id_vaga == id_vaga).first()
    if not db_vaga:
        raise HTTPException(status_code=404, detail="Vaga não encontrada")
    return db_vaga

@router.get("/vagas/", response_model=List[VagaResponse]) #lista todas as vagas
def read_vagas(db: Session):
    db_vagas = db.query(Vaga).all()
    return db_vagas

@router.delete("/vaga/{id_vaga}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vaga(id_vaga: int, db: Session):
    db_vaga = db.query(Vaga).filter(Vaga.id_vaga == id_vaga).first()
    if not db_vaga:
        raise HTTPException(status_code=404, detail="Vaga não encontrada")
    db.delete(db_vaga)
    db.commit()
    return {"ok": True}