from datetime import datetime
from typing import Optional

#from multiplataform_development_i.domain.util.utils import Validate
from pydantic import BaseModel, ConfigDict


class TarefaDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    titulo: str
    description: str
    status: str
    created_at: str

class TarefaCreateDTO(BaseModel):
    id: int
    titulo: str
    description: str
    status: str
    created_at: str

class TarefaUpdateDTO(BaseModel):
    titulo: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None