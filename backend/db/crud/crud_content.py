from typing import List, Optional
from sqlalchemy.orm import Session

from db.crud.base import CRUDBase
from db.models.content import Content
from db.schemas.content import ContentCreate, ContentUpdate


class CRUDContent(CRUDBase[Content, ContentCreate, ContentUpdate]):
    def get_by_user_id(
        self, db: Session, *, user_id: str, skip: int = 0, limit: int = 100
    ) -> List[Content]:
        return (
            db.query(self.model)
            .filter(Content.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_type(
        self, db: Session, *, type: str, skip: int = 0, limit: int = 100
    ) -> List[Content]:
        return (
            db.query(self.model)
            .filter(Content.type == type)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create_with_user(
        self, db: Session, *, obj_in: ContentCreate, user_id: str
    ) -> Content:
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data, user_id=user_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


content = CRUDContent(Content) 