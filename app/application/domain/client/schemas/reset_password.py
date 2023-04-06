from fastapi_camelcase import CamelModel


class ResetPasswordSchema(CamelModel):
    email: str
    password: str
