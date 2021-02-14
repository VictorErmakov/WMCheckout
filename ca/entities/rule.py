from typing import Optional, Literal
from .product import Product

PROMO_TYPES = Literal["Total", "Product", ""]
PROMO_MEASUREMENTS = Literal["percentage", "currency"]


class PromotionalRule:
    """Promotional rule

    Attributes:
        name:   Meaningful string representation of Promotional rule
        discount_type:  Type of discount. Can be total or product type.
            Total type - Rule applied to total sum
            Product type - Rule applied to specific product
        product:    Product to what rule will be apply.
            Required only if discount type of rule is applying by products
        target_quantity:    On what quantity of products, or sum (based on discount type), rule will be triggered
        measure:    Measure of rule. Can be percentage or currency
        discount_amount:    Amount of rule measure, that will trigger the rule
    """

    def __init__(
        self,
        name: str,
        discount_type: PROMO_TYPES,
        product: Optional[Product],
        target_quantity: int,
        measure: PROMO_MEASUREMENTS,
        discount_amount: float,
    ) -> None:
        self.name = name
        self.type = discount_type
        self.product = product
        self.target_quantity = target_quantity
        self.discount_amount = discount_amount
        self.measure = measure
