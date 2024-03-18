from typing import Optional
from pydantic import BaseModel as SCBaseModel

class HpSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    ano: str

    class Config:
        orm_mode = True