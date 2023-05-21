from tortoise import Model

from app.application.abstracts.database.base_model import BaseModel
from app.models.quantity import Quantity


def test_quantity_model_should_return_valid_fields_when_valid_data_is_passed(
    quantity_fake_dict,
):
    quantity = Quantity(**quantity_fake_dict)

    assert isinstance(quantity, Model)
    assert isinstance(quantity, BaseModel)
    assert isinstance(quantity.uuid, str)
    assert isinstance(quantity.size, str)
    assert isinstance(quantity.available, int)
    assert isinstance(quantity.purchased, int)
