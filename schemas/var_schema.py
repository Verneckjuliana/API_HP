from typing import Optional
from pydantic import BaseModel as SCBaseModel

class VarSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    material: str
    personagens: str

    class Config:
        orm_mode = True