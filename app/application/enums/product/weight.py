from enum import Enum


class ProductWeightEnum(int, Enum):
    """
    Enum for a product type.
    """

    DEFAULT = 180
    T_SHIRT = 180
    SWEATSHIRT = 700
