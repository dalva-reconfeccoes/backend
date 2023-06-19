from tortoise import Model

from app.models.cart import Cart


def test_address_model_should_return_valid_instance_when_valid_data_is_passed(
    cart_fake_dict,
):
    model = Cart(**cart_fake_dict)
    assert isinstance(model, Model)


def test_address_model_should_return_valid_fields_when_valid_data_is_passed(
    cart_fake_dict,
):
    model = Cart(**cart_fake_dict)

    assert isinstance(model.uuid, str)
    assert isinstance(model.step, int)
    assert isinstance(model.total_value, float)
