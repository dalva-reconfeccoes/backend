from fastapi_camelcase import CamelModel


class LoginClientSchema(CamelModel):
    email: str
    password: str
