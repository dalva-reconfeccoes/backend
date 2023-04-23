from fastapi_camelcase import CamelModel


class RegisterImageSchema(CamelModel):
    filename: str
    content_type: str
    bucket: str
    product_id: str
