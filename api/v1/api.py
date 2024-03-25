from fastapi import APIRouter
from api.v1.endpoints import hp

api_router = APIRouter()
api_router.include_router(hp.router, prefix="/hp", tags=["hp"])