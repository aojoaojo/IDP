from fastapi import APIRouter

router = APIRouter(
    tags=["empresa"],
    # dependencies=[Depends(get_token_header)], # TODO: Implementar autenticação
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def read_root():
    return {"Hello": "World"}

# @router.get("/get_empresa")
# def read_empresas():
#     db = SessionLocal()
#     with engine.connect() as con:
#         rs = con.execute(text('SELECT * FROM empresa'))
#         print(rs)
#     if not rs:
#         raise HTTPException(status_code=404, detail="Empresa não encontrada")
    
#     result_list = [row._asdict() for row in rs]
#     return result_list


# @router.post("/localizacao", response_model=LocalizacaoCreate)
# def create_localizacao(localizacao: LocalizacaoCreate):
#     db = SessionLocal()
#     db_localizacao = Localizacao(
#         IDLocalizacao=localizacao.id_localizacao,
#         CEP=localizacao.cep,
#         Cidade=localizacao.cidade,
#         Municipio=localizacao.municipio,
#         Bairro=localizacao.bairro,
#         Complemento=localizacao.complemento)
#     db.add(db_localizacao)
#     db.commit()
#     db.refresh(db_localizacao)
#     return db_localizacao

# @router.post("/empresa/", response_model=EmpresaCreate)
# def create_empresa(empresa: EmpresaCreate):
#     db = SessionLocal()
#     db_empresa = Empresa(
#         Nome=empresa.nome,
#         IDEmpresa = empresa.id_empresa,
#         IDLocalizacao = empresa.id_localizacao,
#         Localizacoes = empresa.localizacoes,
#         IDEmail = empresa.id_email,
#         IDTelefone=empresa.id_telefone)
#     db.add(db_empresa)
#     db.commit()
#     db.refresh(db_empresa)
#     return db_empresa

# @router.put("/empresa/{id_empresa}", response_model=EmpresaUpdate)
# def update_empresa(IDEmpresa: int, empresa_update: EmpresaUpdate):
#     db = SessionLocal()
#     db_empresa = db.query(Empresa).filter(Empresa.id == IDEmpresa).first()

#     if not db_empresa:
#         raise HTTPException(status_code=404, detail="Empresa não encontrada")

#     for var, value in vars(empresa_update).items():
#         if value is not None:
#             setattr(db_empresa, var, value)

#     db.commit()
#     db.refresh(db_empresa)
#     return db_empresa

# @router.delete("/empresa/{id_empresa}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_empresa(IDEmpresa: int):
#     db = SessionLocal()
#     db_empresa = db.query(Empresa).filter(Empresa.id == IDEmpresa).first()

#     if not db_empresa:
#         db.close()
#         raise HTTPException(status_code=404, detail="Empresa não encontrada")

#     db.delete(db_empresa)
#     db.commit()
#     db.close()
#     return {"detail": "Empresa excluída com sucesso"}