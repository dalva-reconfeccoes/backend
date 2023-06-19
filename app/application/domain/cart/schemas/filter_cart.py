from typing import Optional

from fastapi_camelcase import CamelModel


class FilterCartSchema(CamelModel):
    id: Optional[int]
    uuid: Optional[str]
