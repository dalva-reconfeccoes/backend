from enum import Enum


class ProductTypeEnum(str, Enum):
    """
    Enum for a product type.
    """

    T_SHIRT = "Camiseta"
    SWEATSHIRT = "Moletom"
