from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from core import security
from db import crud, schemas
from db.dependencies import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.Content])
def read_contents(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: Any = Depends(security.get_current_active_user),
) -> Any:
    """
    Retrieve contents.
    """
    contents = crud.content.get_by_user_id(
        db=db, user_id=current_user.id, skip=skip, limit=limit
    )
    return contents


@router.post("/", response_model=schemas.Content)
def create_content(
    *,
    db: Session = Depends(get_db),
    content_in: schemas.ContentCreate,
    current_user: Any = Depends(security.get_current_active_user),
) -> Any:
    """
    Create new content.
    """
    content = crud.content.create_with_user(
        db=db, obj_in=content_in, user_id=current_user.id
    )
    return content


@router.get("/{content_id}", response_model=schemas.Content)
def read_content(
    *,
    db: Session = Depends(get_db),
    content_id: str,
    current_user: Any = Depends(security.get_current_active_user),
) -> Any:
    """
    Get content by ID.
    """
    content = crud.content.get(db=db, id=content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    if content.user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return content


@router.put("/{content_id}", response_model=schemas.Content)
def update_content(
    *,
    db: Session = Depends(get_db),
    content_id: str,
    content_in: schemas.ContentUpdate,
    current_user: Any = Depends(security.get_current_active_user),
) -> Any:
    """
    Update content.
    """
    content = crud.content.get(db=db, id=content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    if content.user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    content = crud.content.update(db=db, db_obj=content, obj_in=content_in)
    return content


@router.delete("/{content_id}", response_model=schemas.Content)
def delete_content(
    *,
    db: Session = Depends(get_db),
    content_id: str,
    current_user: Any = Depends(security.get_current_active_user),
) -> Any:
    """
    Delete content.
    """
    content = crud.content.get(db=db, id=content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    if content.user_id != current_user.id:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    content = crud.content.remove(db=db, id=content_id)
    return content


@router.get("/type/{content_type}", response_model=List[schemas.Content])
def read_contents_by_type(
    *,
    db: Session = Depends(get_db),
    content_type: str,
    skip: int = 0,
    limit: int = 100,
    current_user: Any = Depends(security.get_current_active_user),
) -> Any:
    """
    按类型获取内容列表
    """
    contents = crud.content.get_by_type(
        db=db, content_type=content_type, skip=skip, limit=limit
    )
    return contents 