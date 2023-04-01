from fastapi_camelcase import CamelModel


class JWTClientSchema(CamelModel):
    email: str
    access_token: str
