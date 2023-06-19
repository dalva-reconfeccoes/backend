from enum import Enum


class DeliveryTypeEnum(str, Enum):
    """
    Enum for a product type.
    """

    CORREIOS_PAC = "PAC"
    CORREIOS_SEDEX = "SEDEX"
