from enum import Enum


class ProductSizeEnum(str, Enum):
    """
    Enum for a product size.
    """

    SIZE_PP = "PP"
    SIZE_P = "P"
    SIZE_M = "M"
    SIZE_G = "G"
    SIZE_GG = "GG"
    SIZE_EXG = "EXG"
