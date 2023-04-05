from datetime import datetime
from typing import Optional

from fastapi_camelcase import CamelModel


class GetClientSchema(CamelModel):
    id: int
    uuid: str
    email: str
    full_name: str
    is_juridical: bool
    email_is_verified: bool
    is_active: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
