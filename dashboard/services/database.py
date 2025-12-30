from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# =============================
# Configurações do Banco
# =============================

DB_USER = "root"
DB_PASSWORD = "root"
DB_HOST = "mysql"          # nome do serviço no docker-compose
DB_PORT = "3306"
DB_NAME = "db_super_store"

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# =============================
# Engine
# =============================

engine = create_engine(
    DATABASE_URL,
    echo=False,            # True se quiser ver SQL no log
    pool_pre_ping=True
)

# =============================
# Session
# =============================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# =============================
# Base (models)
# =============================

Base = declarative_base()

# =============================
# Dependency (FastAPI)
# =============================

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
