from core.configs import settings
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class VarModel(settings.DBBaseModel):
    __tablename__ = 'Varinhas'

    id_varinha: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    material: str = Column(String(50))
    personagens = relationship('HpModel', backref='varinha')