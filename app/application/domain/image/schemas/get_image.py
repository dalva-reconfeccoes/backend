from datetime import datetime
from typing import Optional

from fastapi_camelcase import CamelModel


class GetImageSchema(CamelModel):
    id: int
    uuid: str
    filename: str
    content_type: str
    bucket: str
    is_active: bool
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
