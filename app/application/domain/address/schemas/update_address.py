from typing import Optional

from fastapi_camelcase import CamelModel


class UpdateAddressSchema(CamelModel):
    cep: Optional[str]
    district: Optional[str]
    city: Optional[str]
    street: Optional[str]
    uf: Optional[str]
    complement: Optional[str]
    neighborhood: Optional[str]
    number: Optional[int]
    is_active: Optional[bool]
