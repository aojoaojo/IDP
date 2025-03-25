from sqlalchemy import create_engine, Column, String, Text, DECIMAL, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Endereco(Base):
    __tablename__ = 'endereco'

    endereco_id = Column(UUID(as_uuid=True), primary_key=True)
    cep = Column(String(10), nullable=False)
    numero = Column(String(10))
    endereco = Column(String(255), nullable=False)
    complemento = Column(String(255))
    bairro = Column(String(255), nullable=False)
    cidade = Column(String(255), nullable=False)
    uf = Column(String(2), nullable=False)
    tipo = Column(String(10), nullable=False)
    
class Usuario(Base):
    __tablename__ = 'usuario'

    usuario_id = Column(UUID(as_uuid=True), primary_key=True)
    email = Column(String(255), nullable=False)
    senha = Column(String(255), nullable=False)
    acesso = Column(String(10), nullable=False)

class Empresa(Base):
    __tablename__ = 'empresa'

    empresa_id = Column(UUID(as_uuid=True), primary_key=True)
    nome_empresa = Column(String(255), nullable=False)
    descricao = Column(Text)
    telefone = Column(String(20))
    email = Column(String(255))
    endereco_id = Column(UUID(as_uuid=True), ForeignKey('endereco.endereco_id'))
    tipo = Column(String(10), nullable=False)
    usuario_id = Column(UUID(as_uuid=True), ForeignKey('usuario.usuario_id'), nullable=False)

    endereco = relationship("Endereco")
    usuario = relationship("Usuario")

class Candidato(Base):
    __tablename__ = 'candidato'

    candidato_id = Column(UUID(as_uuid=True), primary_key=True)
    nome_candidato = Column(String(255), nullable=False)
    telefone = Column(String(20))
    email = Column(String(255))
    exp_profissional = Column(Text)
    formacao_academica = Column(Text)
    habilidades = Column(Text)
    linguas_faladas = Column(Text)
    endereco_id = Column(UUID(as_uuid=True), ForeignKey('endereco.endereco_id'))
    usuario_id = Column(UUID(as_uuid=True), ForeignKey('usuario.usuario_id'), nullable=False)

    endereco = relationship("Endereco")
    usuario = relationship("Usuario")

class Vaga(Base):
    __tablename__ = 'vaga'

    vaga_id = Column(UUID(as_uuid=True), primary_key=True)
    cargo = Column(String(255))
    salario = Column(DECIMAL(10, 2))
    empresa_id = Column(UUID(as_uuid=True), ForeignKey('empresa.empresa_id'), nullable=False)
    regime_contratacao = Column(String(255))
    nome_empresa = Column(String(255))
    nivel_exp = Column(String(255))
    regime_trabalho = Column(String(255))
    status = Column(String(20), nullable=False)
    beneficios = Column(Text)
    descricao = Column(Text)

    empresa = relationship("Empresa")

class Candidatura(Base):
    __tablename__ = 'candidatura'

    candidatura_id = Column(UUID(as_uuid=True), primary_key=True)
    vaga_id = Column(UUID(as_uuid=True), ForeignKey('vaga.vaga_id'), nullable=False)
    candidato_id = Column(UUID(as_uuid=True), ForeignKey('candidato.candidato_id'), nullable=False)

    vaga = relationship("Vaga")
    candidato = relationship("Candidato")
