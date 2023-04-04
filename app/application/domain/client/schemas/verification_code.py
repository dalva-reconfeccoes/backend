from fastapi_camelcase import CamelModel


class VerificationCodeSchema(CamelModel):
    email: str
    code: str
