from datetime import datetime
from typing import Any, Dict, Optional
from uuid import UUID

from pydantic import BaseModel


class ContentBase(BaseModel):
    type: Optional[str] = None  # text, image, audio
    title: Optional[str] = None
    content: Optional[str] = None
    meta_info: Optional[Dict[str, Any]] = None


class ContentCreate(ContentBase):
    type: str
    user_id: UUID


class ContentUpdate(ContentBase):
    pass


class ContentInDBBase(ContentBase):
    id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Content(ContentInDBBase):
    pass


class ContentInDB(ContentInDBBase):
    pass 