from fastapi_camelcase import CamelModel


class UpdateClientSchema(CamelModel):
    full_name: str
    email: str
    password: str
    is_active: bool = True
