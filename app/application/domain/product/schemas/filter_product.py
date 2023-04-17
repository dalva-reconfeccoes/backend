from typing import Optional

from fastapi_camelcase import CamelModel


class FilterProductSchema(CamelModel):
    id: Optional[int]
    uuid: Optional[str]
    header: Optional[str]
