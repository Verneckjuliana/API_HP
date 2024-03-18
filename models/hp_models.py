from core.configs import settings
from sqlalchemy import Column, Integer, String

class HpModel(settings.DBBaseModel):
    __tablename__ = 'Harry Potter'

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    ano_nasc: str = Column(String(4))