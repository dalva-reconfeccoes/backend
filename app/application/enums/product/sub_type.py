from enum import Enum


class ProductSubTypeEnum(str, Enum):
    """
    Enum for a product sub type.
    """

    REGULAR = "Básica"
    POLO = "Polo"
    LONG_SLEEVE = "Manga Longa"
    TANK_TOP = "Regata"
    RAGLAN = "Raglan"
