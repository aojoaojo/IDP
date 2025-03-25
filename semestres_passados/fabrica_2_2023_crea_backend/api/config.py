from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:123456@localhost/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
db = SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
try:
    # Tente criar uma conexão
    connection = engine.connect()

    # Use o MetaData para refletir as tabelas do banco de dados
    metadata = MetaData()
    metadata.reflect(bind=engine)

    # Obtenha os nomes das tabelas
    table_names = metadata.tables.keys()

    # Print os nomes das tabelas
    print("Nomes das tabelas:")
    for table_name in table_names:
        print(table_name)

    print("Conexão bem-sucedida!")

except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
