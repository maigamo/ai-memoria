from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
import os

from core import security
from core.config import settings
from db import crud, schemas
from db.dependencies import get_db
from services.file_service import file_service
from db.models.user import User
from services.sync_service import sync_service

router = APIRouter()


@router.post("/upload", response_model=schemas.File)
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(security.get_current_active_user)
):
    """
    上传文件
    """
    # 检查文件大小
    file_size = 0
    file_content = await file.read()
    file_size = len(file_content)
    await file.seek(0)  # 重置文件指针
    
    if file_size > settings.MAX_FILE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="文件大小超过限制"
        )
    
    # 检查文件类型
    if file.content_type not in settings.ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="不支持的文件类型"
        )
    
    # 保存文件
    file_path = await file_service.save_file(file, current_user.id)
    
    # 创建文件记录
    db_file = crud.file.create_with_user(
        db=db,
        obj_in={
            "filename": file.filename,
            "file_path": file_path,
            "file_type": file_service.get_file_type(file.content_type),
            "file_size": file_size,
            "mime_type": file.content_type
        },
        user_id=current_user.id
    )
    
    return db_file


@router.get("/download/{file_id}")
async def download_file(
    file_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.get_current_active_user)
):
    """
    下载文件
    """
    # 获取文件记录
    db_file = crud.file.get(db, id=file_id)
    if not db_file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="文件不存在"
        )
    
    # 检查文件所有权
    if db_file.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权访问此文件"
        )
    
    # 检查文件是否存在
    file_path = file_service.get_file_path(current_user.id, db_file.file_path)
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="文件不存在"
        )
    
    # 返回文件
    return FileResponse(
        path=file_path,
        filename=db_file.filename,
        media_type=db_file.mime_type
    )


@router.get("/list", response_model=List[schemas.File])
def list_files(
    db: Session = Depends(get_db),
    current_user: User = Depends(security.get_current_active_user)
):
    """
    获取用户的文件列表
    """
    return crud.file.get_by_user(db, user_id=current_user.id)


@router.delete("/{file_id}")
async def delete_file(
    file_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(security.get_current_active_user)
):
    """
    删除文件
    """
    # 获取文件记录
    db_file = crud.file.get(db, id=file_id)
    if not db_file:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="文件不存在"
        )
    
    # 检查文件所有权
    if db_file.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="无权删除此文件"
        )
    
    # 删除物理文件
    file_path = file_service.get_file_path(current_user.id, db_file.file_path)
    await file_service.delete_file(file_path)
    
    # 删除数据库记录
    crud.file.remove(db, id=file_id)
    
    return {"message": "文件已删除"}


@router.post("/sync")
async def sync_user_files(
    db: Session = Depends(get_db),
    current_user: User = Depends(security.get_current_active_user)
):
    """
    同步用户的文件
    """
    await sync_service.sync_files(db, current_user.id)
    return {"message": "文件同步完成"}


@router.post("/restore")
async def restore_user_files(
    db: Session = Depends(get_db),
    current_user: User = Depends(security.get_current_active_user)
):
    """
    从同步目录恢复用户的文件
    """
    await sync_service.restore_files(db, current_user.id)
    return {"message": "文件恢复完成"}


@router.get("/sync/status")
def get_sync_status(
    current_user: User = Depends(security.get_current_active_user)
):
    """
    获取用户的同步状态
    """
    return sync_service.get_sync_status(current_user.id) 