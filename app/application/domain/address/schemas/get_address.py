from datetime import datetime
from typing import Optional

from fastapi_camelcase import CamelModel


class GetAddressSchema(CamelModel):
    id: int
    uuid: str
    cep: str
    district: str
    city: str
    street: str
    uf: str
    complement: str
    neighborhood: str
    number: int
    is_active: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
