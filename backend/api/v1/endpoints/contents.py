from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db import crud, schemas
from db.dependencies import get_db
from core.security import get_current_active_user
from db.models.user import User

router = APIRouter()

@router.get("/", response_model=List[schemas.Content])
def list_contents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """
    获取当前用户的内容列表
    """
    return crud.content.get_by_user(db, user_id=current_user.id)

@router.post("/", response_model=schemas.Content)
def create_content(
    *,
    db: Session = Depends(get_db),
    content_in: schemas.ContentCreate,
    current_user: User = Depends(get_current_active_user)
):
    """
    创建新内容
    """
    return crud.content.create_with_user(
        db=db, obj_in=content_in, user_id=current_user.id
    )

@router.get("/{content_id}", response_model=schemas.Content)
def read_content(
    *,
    db: Session = Depends(get_db),
    content_id: int,
    current_user: User = Depends(get_current_active_user)
):
    """
    获取特定内容
    """
    content = crud.content.get(db=db, id=content_id)
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="内容不存在"
        )
    if content.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权访问此内容"
        )
    return content

@router.put("/{content_id}", response_model=schemas.Content)
def update_content(
    *,
    db: Session = Depends(get_db),
    content_id: int,
    content_in: schemas.ContentUpdate,
    current_user: User = Depends(get_current_active_user)
):
    """
    更新内容
    """
    content = crud.content.get(db=db, id=content_id)
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="内容不存在"
        )
    if content.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权修改此内容"
        )
    return crud.content.update(db=db, db_obj=content, obj_in=content_in)

@router.delete("/{content_id}")
def delete_content(
    *,
    db: Session = Depends(get_db),
    content_id: int,
    current_user: User = Depends(get_current_active_user)
):
    """
    删除内容
    """
    content = crud.content.get(db=db, id=content_id)
    if not content:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="内容不存在"
        )
    if content.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权删除此内容"
        )
    crud.content.remove(db=db, id=content_id)
    return {"message": "内容已删除"} 