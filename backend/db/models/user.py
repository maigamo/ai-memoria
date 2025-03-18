from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .content import Content  # noqa: F401
    from .file import File  # noqa: F401


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    
    # Relationships
    contents = relationship("Content", back_populates="user")
    files = relationship("File", back_populates="user")
    
    def __repr__(self):
        return f"<User {self.email}>" 