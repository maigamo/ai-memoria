from typing import Optional
from pydantic import BaseModel

from .base import BaseSchema


class FileBase(BaseModel):
    filename: str
    file_type: str
    file_size: int
    mime_type: str


class FileCreate(FileBase):
    pass


class FileUpdate(FileBase):
    filename: Optional[str] = None
    file_type: Optional[str] = None
    file_size: Optional[int] = None
    mime_type: Optional[str] = None


class FileInDBBase(FileBase, BaseSchema):
    user_id: str
    file_path: str

    class Config:
        from_attributes = True


class File(FileInDBBase):
    pass


class FileInDB(FileInDBBase):
    pass 