from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from db.base_class import Base

# 创建数据库引擎
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False} if settings.SQLALCHEMY_DATABASE_URI.startswith("sqlite") else {}
)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 获取数据库会话
def get_db():
    """
    获取数据库会话
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_cloud_db():
    """
    获取云数据库会话
    """
    db = CloudSessionLocal()
    try:
        yield db
    finally:
        db.close() 