from typing import List, Optional

from sqlalchemy.orm import Session

from db.crud.base import CRUDBase
from db.models import Content
from schemas.content import ContentCreate, ContentUpdate


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
        self, db: Session, *, content_type: str, skip: int = 0, limit: int = 100
    ) -> List[Content]:
        return (
            db.query(self.model)
            .filter(Content.type == content_type)
            .offset(skip)
            .limit(limit)
            .all()
        )


content = CRUDContent(Content) 