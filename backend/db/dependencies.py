from typing import Generator
from sqlalchemy.orm import Session
from db.session import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """
    获取数据库会话的依赖函数
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_cloud_db() -> Generator:
    """
    获取云数据库会话
    """
    db = CloudSessionLocal()
    try:
        yield db
    finally:
        db.close() 