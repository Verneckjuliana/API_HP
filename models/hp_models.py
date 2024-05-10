from core.configs import settings
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class HpModel(settings.DBBaseModel):
    __tablename__ = 'Personagens'

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    ano_nasc: str = Column(String(4))
    casa: str = Column(String(50))
    varinhas = relationship("VarModel", back_populates="personagem")
