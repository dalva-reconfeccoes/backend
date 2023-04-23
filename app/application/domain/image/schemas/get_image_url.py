from typing import Optional

from fastapi_camelcase import CamelModel


class GetImageUrlSchema(CamelModel):
    id: int
    uuid: str
    filename: str
    content_type: str
    url: Optional[str]

    class Config:
        orm_mode = True
