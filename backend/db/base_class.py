from datetime import datetime
from typing import Any

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, DateTime


class Base(DeclarativeBase):
    """
    SQLAlchemy 模型的基类
    """
    id: Any
    __name__: str

    # 生成表名
    @declared_attr
    def __tablename__(cls) -> str:
        """
        根据类名自动生成表名
        """
        return cls.__name__.lower()
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow) 