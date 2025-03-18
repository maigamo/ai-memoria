from fastapi import APIRouter
from core.config import settings

router = APIRouter()

@router.get("")
async def health_check():
    """
    健康检查端点
    
    返回服务器状态信息
    """
    return {
        "status": "ok",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "server_ip": settings.LOCAL_IP,
        "server_port": settings.PORT
    } 