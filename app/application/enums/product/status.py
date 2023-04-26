from enum import Enum


class ProductStatusEnum(str, Enum):
    """
    Enum for a product type.
    """

    AVAILABLE = "Disponivel"
    UNAVAILABLE = "Indisponivel"
