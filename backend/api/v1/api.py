from fastapi import APIRouter

from api.v1.endpoints import auth, users, contents, files, health

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(contents.router, prefix="/contents", tags=["contents"])
api_router.include_router(files.router, prefix="/files", tags=["files"])
api_router.include_router(health.router, prefix="/health-check", tags=["system"]) 