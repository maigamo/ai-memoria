from typing import List, Optional
from sqlalchemy.orm import Session

from db.crud.base import CRUDBase
from db.models.file import File
from db.schemas.file import FileCreate, FileUpdate


class CRUDFile(CRUDBase[File, FileCreate, FileUpdate]):
    def get_by_user_id(
        self, db: Session, *, user_id: str, skip: int = 0, limit: int = 100
    ) -> List[File]:
        return (
            db.query(self.model)
            .filter(File.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_type(
        self, db: Session, *, file_type: str, skip: int = 0, limit: int = 100
    ) -> List[File]:
        return (
            db.query(self.model)
            .filter(File.file_type == file_type)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create_with_user(
        self, db: Session, *, obj_in: FileCreate, user_id: str, file_path: str
    ) -> File:
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data, user_id=user_id, file_path=file_path)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


file = CRUDFile(File) 