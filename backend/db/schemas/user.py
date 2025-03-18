from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict

from .base import BaseSchema


class UserBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase, BaseSchema):
    pass


class User(UserBase):
    id: int
    email: EmailStr


class UserInDB(UserInDBBase):
    hashed_password: str 