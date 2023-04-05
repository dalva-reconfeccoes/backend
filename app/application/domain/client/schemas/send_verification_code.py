from fastapi_camelcase import CamelModel


class SendVerificationCodeSchema(CamelModel):
    email: str
