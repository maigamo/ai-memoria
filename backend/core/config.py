import os
import socket
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings


def get_local_ip():
    """获取本机IP地址"""
    try:
        # 通过连接外部服务器获取本机IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        # 如果连接失败，则返回localhost
        return "127.0.0.1"


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "AI-Memoria"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "AI Memoria - 智能记忆助手"
    
    # 自动获取本机IP
    LOCAL_IP: str = get_local_ip()
    
    # CORS配置
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:10011", 
        "http://127.0.0.1:10011",
        f"http://{get_local_ip()}:10011"
    ]
    
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    
    # 服务器配置
    HOST: str = os.getenv("HOST", "0.0.0.0")  # 默认监听所有网络接口
    PORT: int = int(os.getenv("PORT", "10012"))
    
    # 数据库配置
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "aimemoria"
    POSTGRES_PORT: str = "5432"
    
    # SQLite配置
    SQLITE_DATABASE_URL: str = "sqlite:///./aimemoria.db"
    
    # 数据库URI
    SQLALCHEMY_DATABASE_URI: str = SQLITE_DATABASE_URL
    
    # JWT配置
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days
    
    # 文件上传配置
    UPLOAD_DIR: str = "data/uploads"
    MAX_FILE_SIZE: int = 50 * 1024 * 1024  # 50MB
    ALLOWED_FILE_TYPES: List[str] = [
        "image/jpeg",
        "image/png",
        "image/gif",
        "audio/mpeg",
        "audio/wav",
        "application/pdf",
        "text/plain"
    ]
    
    # 默认用户配置
    FIRST_SUPERUSER: str = "aimemoria@example.com"
    FIRST_SUPERUSER_PASSWORD: str = "admin123"
    FIRST_SUPERUSER_FULL_NAME: str = "AI Memoria Admin"
    
    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()