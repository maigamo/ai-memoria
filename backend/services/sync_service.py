import os
import shutil
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session

from core.config import settings
from db import crud
from db.models.file import File
from services.file_service import file_service

class SyncService:
    def __init__(self):
        self.sync_dir = os.path.join(settings.UPLOAD_DIR, "sync")
        os.makedirs(self.sync_dir, exist_ok=True)
    
    async def sync_files(self, db: Session, user_id: int) -> None:
        """
        同步用户的文件
        """
        # 获取用户的所有文件
        files = crud.file.get_by_user(db, user_id=user_id)
        
        # 创建用户的同步目录
        user_sync_dir = os.path.join(self.sync_dir, str(user_id))
        os.makedirs(user_sync_dir, exist_ok=True)
        
        # 同步每个文件
        for file in files:
            await self._sync_file(file, user_sync_dir)
    
    async def _sync_file(self, file: File, user_sync_dir: str) -> None:
        """
        同步单个文件
        """
        # 获取源文件路径
        source_path = file_service.get_file_path(file.user_id, file.file_path)
        
        # 如果源文件不存在，跳过
        if not os.path.exists(source_path):
            return
        
        # 构建目标文件路径
        target_path = os.path.join(user_sync_dir, file.file_path)
        
        # 确保目标目录存在
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        # 如果目标文件不存在或源文件更新，则复制
        if not os.path.exists(target_path) or \
           os.path.getmtime(source_path) > os.path.getmtime(target_path):
            shutil.copy2(source_path, target_path)
    
    async def restore_files(self, db: Session, user_id: int) -> None:
        """
        从同步目录恢复文件
        """
        # 获取用户的同步目录
        user_sync_dir = os.path.join(self.sync_dir, str(user_id))
        
        # 如果同步目录不存在，返回
        if not os.path.exists(user_sync_dir):
            return
        
        # 获取用户的所有文件
        files = crud.file.get_by_user(db, user_id=user_id)
        
        # 恢复每个文件
        for file in files:
            await self._restore_file(file, user_sync_dir)
    
    async def _restore_file(self, file: File, user_sync_dir: str) -> None:
        """
        恢复单个文件
        """
        # 构建源文件路径（同步目录中的文件）
        source_path = os.path.join(user_sync_dir, file.file_path)
        
        # 如果源文件不存在，跳过
        if not os.path.exists(source_path):
            return
        
        # 获取目标文件路径
        target_path = file_service.get_file_path(file.user_id, file.file_path)
        
        # 确保目标目录存在
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        # 如果目标文件不存在或源文件更新，则复制
        if not os.path.exists(target_path) or \
           os.path.getmtime(source_path) > os.path.getmtime(target_path):
            shutil.copy2(source_path, target_path)
    
    def get_sync_status(self, user_id: int) -> dict:
        """
        获取用户的同步状态
        """
        user_sync_dir = os.path.join(self.sync_dir, str(user_id))
        
        if not os.path.exists(user_sync_dir):
            return {
                "synced": False,
                "last_sync": None,
                "file_count": 0
            }
        
        # 获取最后同步时间
        last_sync = datetime.fromtimestamp(os.path.getmtime(user_sync_dir))
        
        # 获取同步文件数量
        file_count = sum([len(files) for _, _, files in os.walk(user_sync_dir)])
        
        return {
            "synced": True,
            "last_sync": last_sync,
            "file_count": file_count
        }

sync_service = SyncService() 