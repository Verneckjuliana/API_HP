from core.configs import settings
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey

class VarModel(settings.DBBaseModel):
    __tablename__ = 'Varinhas'

    id_varinha: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    material: str = Column(String(50))
    personagem_id: int = Column(Integer(), ForeignKey('Personagens.id'))
    personagem = relationship("HpModel", back_populates="varinhas")
