from fastapi_camelcase import CamelModel


class SimpleMessageSchema(CamelModel):
    message: str
