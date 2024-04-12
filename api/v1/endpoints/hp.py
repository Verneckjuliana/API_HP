from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.hp_models import HpModel
from schemas.hp_schema import HpSchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=HpSchema)
async def post_hp(hp: HpSchema, db: AsyncSession = Depends(get_session)):
    novo_hp = HpModel(nome=hp.nome, ano_nasc=hp.ano_nasc, casa=hp.casa)
    db.add(novo_hp)
    await db.commit()

    return novo_hp

@router.get("/", response_model=List[HpSchema])
async def get_hps(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(HpModel)
        result = await session.execute(query)
        hps: List[HpModel] = result.scalars().all()

        return hps

@router.get("/{hp_id}", response_model=HpSchema, status_code=status.HTTP_200_OK)
async def get_hp(hp_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(HpModel).filter(HpModel.id == hp_id)
        result = await session.execute(query)
        hp = result.scalar_one_or_none()

        if hp:
            return hp
        else:
            raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)

@router.put("/{hp_id}", response_model=HpSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_hp(hp_id: int, hp: HpSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(HpModel).filter(HpModel.id == hp_id)
        result = await session.execute(query)
        hp_up = result.scalar_one_or_none()

        if hp_up:
            hp_up.nome = hp.nome
            hp_up.ano_nasc = hp.ano_nasc
            hp_up.casa = hp.casa

            await session.commit()
            return hp_up

        else:
            raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/{hp_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hp(hp_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(HpModel).filter(HpModel.id == hp_id)
        result = await session.execute(query)
        hp_del = result.scalar_one_or_none()

        if hp_del:
            await session.delete(hp_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(detail="Personagem não encontrado", status_code=status.HTTP_404_NOT_FOUND)
