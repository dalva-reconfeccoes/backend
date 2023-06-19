from datetime import datetime
from fastapi_camelcase import CamelModel


class CalculatedFreightCorreiosSchema(CamelModel):
    value: float
    deadline: int
    delivery_type: str
    estimated_delivery_date: datetime
