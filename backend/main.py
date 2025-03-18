from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.api import api_router
from core.config import settings
from db.init_db import init_db
from db.session import SessionLocal, engine
from db.base_class import Base
import logging
import argparse

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    应用程序生命周期管理
    """
    # 启动时创建数据库表并初始化
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        init_db(db)
    finally:
        db.close()
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

# 设置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Welcome to AI-Memoria API"}

if __name__ == "__main__":
    import uvicorn
    
    # 添加命令行参数解析
    parser = argparse.ArgumentParser(description="AI-Memoria 后端服务")
    parser.add_argument("--host", type=str, default=settings.HOST, help="服务器监听地址 (默认: 0.0.0.0)")
    parser.add_argument("--port", type=int, default=settings.PORT, help="服务器监听端口 (默认: 10012)")
    args = parser.parse_args()
    
    host = args.host
    port = args.port
    local_ip = settings.LOCAL_IP
    
    logging.info(f"本机IP地址: {local_ip}")
    logging.info(f"服务启动于: http://{local_ip if host == '0.0.0.0' else host}:{port}")
    logging.info(f"接口文档: http://{local_ip if host == '0.0.0.0' else host}:{port}/docs")
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=True
    )