import os
import shutil
from pathlib import Path
from typing import Optional
from fastapi import UploadFile
import aiofiles
import uuid

from core.config import settings


class FileService:
    def __init__(self):
        self.upload_dir = Path(settings.UPLOAD_DIR)
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    async def save_file(self, file: UploadFile, user_id: str) -> Optional[str]:
        """
        保存上传的文件
        """
        try:
            # 生成唯一的文件名
            file_extension = os.path.splitext(file.filename)[1]
            unique_filename = f"{uuid.uuid4()}{file_extension}"
            
            # 创建用户目录
            user_dir = self.upload_dir / user_id
            user_dir.mkdir(exist_ok=True)
            
            # 完整的文件路径
            file_path = user_dir / unique_filename
            
            # 异步保存文件
            async with aiofiles.open(file_path, 'wb') as out_file:
                content = await file.read()
                await out_file.write(content)
            
            return str(file_path)
        except Exception as e:
            print(f"Error saving file: {e}")
            return None

    def delete_file(self, file_path: str) -> bool:
        """
        删除文件
        """
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
            return True
        except Exception as e:
            print(f"Error deleting file: {e}")
            return False

    def get_file_path(self, user_id: str, filename: str) -> str:
        """
        获取文件路径
        """
        return str(self.upload_dir / user_id / filename)

    def get_file_size(self, file_path: str) -> int:
        """
        获取文件大小
        """
        return os.path.getsize(file_path)

    def get_mime_type(self, file_path: str) -> str:
        """
        获取文件的 MIME 类型
        """
        import mimetypes
        mime_type, _ = mimetypes.guess_type(file_path)
        return mime_type or 'application/octet-stream'

    def get_file_type(self, file_path: str) -> str:
        """
        获取文件类型（图片、文档、音频等）
        """
        mime_type = self.get_mime_type(file_path)
        if mime_type.startswith('image/'):
            return 'image'
        elif mime_type.startswith('audio/'):
            return 'audio'
        elif mime_type.startswith('video/'):
            return 'video'
        elif mime_type.startswith('application/pdf'):
            return 'pdf'
        elif mime_type.startswith('text/'):
            return 'text'
        else:
            return 'other'


file_service = FileService() 