from tortoise.fields import (
    ForeignKeyField,
    IntField,
    FloatField,
    BooleanField,
    ReverseRelation,
)

from app.application.abstracts.database.base_model import BaseModel


class Cart(BaseModel):
    step = IntField(null=True, default=0)
    total_value = FloatField(null=True)
    is_finished = BooleanField(default=False)
    client = ForeignKeyField("models.Client", related_name="cart", null=True)
    selected_products = ReverseRelation["SelectedProduct"]

    class Meta:
        table = "cart"
        ordering = ["-id"]
