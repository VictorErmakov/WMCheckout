from typing import TypedDict
from enum import Enum


class CartType(TypedDict):
    Product: int


class PromoDiscountType(Enum):
    TOTAL = "TOTAL"
    PRODUCT = "PRODUCT"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __eq__(self, other) -> bool:
        return self.value == other


class PromoMeasurementsType(Enum):
    PERCENTAGE = "PERCENTAGE"
    CURRENCY = "CURRENCY"

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_

    def __eq__(self, other) -> bool:
        return self.value == other