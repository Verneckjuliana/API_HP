from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.var_models import VarModel
from schemas.var_schema import VarSchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=VarSchema)
async def post_hp(var: VarSchema, db: AsyncSession = Depends(get_session)):
    novo_var = VarModel(nome=var.nome, material=var.material)
    db.add(novo_var)
    await db.commit()

    return novo_var

@router.get("/", response_model=List[VarSchema])
async def get_vars(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(VarModel)
        result = await session.execute(query)
        vars: List[VarModel] = result.scalars().all()

        return vars

@router.get("/{var_id}", response_model=VarSchema, status_code=status.HTTP_200_OK)
async def get_var(var_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(VarModel).filter(VarModel.id == var_id)
        result = await session.execute(query)
        var = result.scalar_one_or_none()

        if var:
            return var
        else:
            raise HTTPException(detail="Varinha não encontrada", status_code=status.HTTP_404_NOT_FOUND)

@router.put("/{var_id}", response_model=VarSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_var(var_id: int, var: VarSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(VarModel).filter(VarModel.id == var_id)
        result = await session.execute(query)
        var_up = result.scalar_one_or_none()

        if var_up:
            var_up.nome = var.nome
            var_up.material = var.material

            await session.commit()
            return var_up

        else:
            raise HTTPException(detail="Varinha não encontrada", status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/{var_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_var(var_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(VarModel).filter(VarModel.id == var_id)
        result = await session.execute(query)
        var_del = result.scalar_one_or_none()

        if var_del:
            await session.delete(var_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(detail="Varinha não encontrada", status_code=status.HTTP_404_NOT_FOUND)
