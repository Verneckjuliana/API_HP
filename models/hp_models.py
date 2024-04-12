from core.configs import settings
from sqlalchemy import Column, Integer, String, ForeignKey

class HpModel(settings.DBBaseModel):
    __tablename__ = 'Personagens'

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    ano_nasc: str = Column(String(4))
    casa: str = Column(String(50))
    id_varinha: int = Column(Integer(), ForeignKey('Varinhas.id_varinha'))
    






