from pydantic import BaseModel
from datetime import datetime

class ProdutosSchema(BaseModel):
    id: int
    item: str
    peso: float
    numero_caixas: int

class UsuariosSchema(BaseModel):
    id:int
    username:str
    password:str
    created_at:datetime
    updated_at:datetime

