from sqlalchemy.orm import Session
from sqlalchemy import text
from core.config import settings
from core.security import get_password_hash
from db.models.user import User
from db.models.base import Base
from db.session import engine

from core.initial_data import first_superuser
from db import crud, schemas


def init_db(db: Session) -> None:
    """
    初始化数据库，创建默认超级用户
    """
    # 检查是否已初始化
    result = db.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='init_marker'"))
    if result.scalar() is None:
        # 创建初始化标记表
        db.execute(text("CREATE TABLE init_marker (id INTEGER PRIMARY KEY, initialized BOOLEAN)"))
        db.commit()
        
        # 创建默认超级用户
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            full_name=settings.FIRST_SUPERUSER_FULL_NAME,
            is_superuser=True,
        )
        crud.user.create(db, obj_in=user_in)
        
        # 标记为已初始化
        db.execute(text("INSERT INTO init_marker (id, initialized) VALUES (1, TRUE)"))
        db.commit() 