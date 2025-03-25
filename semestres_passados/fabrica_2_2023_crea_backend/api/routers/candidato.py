from typing import Optional
import uuid
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import status, Depends
from sqlalchemy.orm import Session
from models import Candidato, Usuario, Endereco
from sqlalchemy.exc import SQLAlchemyError
from config import get_db

class EnderecoCreate(BaseModel):
    cep: str
    numero: Optional[str] = None
    endereco: str
    complemento: Optional[str] = None
    bairro: str
    cidade: str
    uf: str
    tipo: str
class UsuarioCandidatoCreate(BaseModel):
    email: str
    senha: str
    acesso: str
    nome_candidato: str
    telefone: Optional[str] = None
    exp_profissional: Optional[str] = None
    formacao_academica: Optional[str] = None
    habilidades: Optional[str] = None
    linguas_faladas: Optional[str] = None
    endereco: EnderecoCreate

class CandidatoView(BaseModel):
    email: str
    acesso: str
    nome_candidato: str
    telefone: Optional[str] = None
    exp_profissional: Optional[str] = None
    formacao_academica: Optional[str] = None
    habilidades: Optional[str] = None
    linguas_faladas: Optional[str] = None
    endereco: EnderecoCreate


router = APIRouter(
    prefix="/candidatos",
    tags=["candidatos"],
    # dependencies=[Depends(get_token_header)], # TODO Implementar autenticação
    responses={404: {"description": "Not found"}},
)



@router.post("/candidatos/", response_model=CandidatoView, status_code=status.HTTP_201_CREATED)
def create_candidato(candidato: UsuarioCandidatoCreate, db: Session = Depends(get_db)):
    try:
        # Cria o Endereco primeiro
        db_endereco = Endereco(
            endereco_id=uuid.uuid4(),
            cep=candidato.endereco.cep,
            numero=candidato.endereco.numero,
            endereco=candidato.endereco.endereco,
            complemento=candidato.endereco.complemento,
            bairro=candidato.endereco.bairro,
            cidade=candidato.endereco.cidade,
            uf=candidato.endereco.uf,
            tipo=candidato.endereco.tipo
        )

        # Cria o Usuario
        db_usuario = Usuario(
            usuario_id=uuid.uuid4(),
            email=candidato.email,
            senha=candidato.senha,
            acesso='Candidato'
        )

        # Cria o Candidato
        db_candidato = Candidato(
            nome_candidato=candidato.nome_candidato,
            candidato_id = uuid.uuid4(),
            telefone=candidato.telefone,
            email=candidato.email,
            exp_profissional=candidato.exp_profissional,
            formacao_academica=candidato.formacao_academica,
            habilidades=candidato.habilidades,
            linguas_faladas=candidato.linguas_faladas,
            usuario_id=db_usuario.usuario_id,
            endereco_id=db_endereco.endereco_id
        )
        candidatoView = CandidatoView(
            email=candidato.email,
            acesso='Candidato',
            nome_candidato=candidato.nome_candidato,
            telefone=candidato.telefone,
            exp_profissional=candidato.exp_profissional,
            formacao_academica=candidato.formacao_academica,
            habilidades=candidato.habilidades,
            linguas_faladas=candidato.linguas_faladas,
            endereco=candidato.endereco
        )
        # Adiciona as entidades e commita a transação
        db.add_all([db_endereco, db_usuario, db_candidato])
        db.commit()
        db.refresh(db_candidato)

        return candidatoView
    
    except SQLAlchemyError as e:
        db.rollback()
        raise e
