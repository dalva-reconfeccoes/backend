from fastapi_camelcase import CamelModel


class PostAddressSchema(CamelModel):
    cep: str
    district: str
    city: str
    street: str
    uf: str
    complement: str
    neighborhood: str
    number: int
