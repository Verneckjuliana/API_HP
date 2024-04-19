from fastapi import APIRouter
from api.v1.endpoints import hp, var

api_router = APIRouter()
api_router.include_router(hp.router, prefix="/hp", tags=["hp"])
api_router.include_router(var.router, prefix="/var", tags=["var"])