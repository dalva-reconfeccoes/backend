from typing import Optional

from fastapi_camelcase import CamelModel


class FilterClientSchema(CamelModel):
    id: Optional[int]
    uuid: Optional[str]
    email: Optional[str]
