from typing import Optional
from fastapi_camelcase import CamelModel


class GetAvailableColorSchema(CamelModel):
    color: str
    selected: bool


class GetAvailableSubTypeSchema(CamelModel):
    type: str
    selected: bool


class GetAvailableSizeSchema(CamelModel):
    size: str
    selected: bool


class GetAvailableFilterProductSchema(CamelModel):
    available_colors: Optional[list[GetAvailableColorSchema]]
    available_types: Optional[list[GetAvailableSubTypeSchema]]
    available_size: Optional[list[GetAvailableSizeSchema]]
