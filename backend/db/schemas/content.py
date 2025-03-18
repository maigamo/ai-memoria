from typing import Optional, Dict, Any
from pydantic import BaseModel

from .base import BaseSchema


class ContentBase(BaseModel):
    type: str
    title: str
    content: str
    meta_info: Optional[Dict[str, Any]] = None


class ContentCreate(ContentBase):
    pass


class ContentUpdate(ContentBase):
    type: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None


class ContentInDBBase(ContentBase, BaseSchema):
    user_id: str

    class Config:
        from_attributes = True


class Content(ContentInDBBase):
    pass


class ContentInDB(ContentInDBBase):
    pass 