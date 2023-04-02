from enum import Enum


class ProductSexEnum(str, Enum):
    """
    Enum for a product sex.
    """

    MALE = "Masculino"
    FEMALE = "Faminino"
    UNISEX = "Unissex"
