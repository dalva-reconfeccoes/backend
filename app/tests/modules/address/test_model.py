from tortoise import Model

from app.models.address import Address


def test_address_model_should_return_valid_instance_when_valid_data_is_passed(
    address_fake_dict,
):
    address = Address(**address_fake_dict)
    assert isinstance(address, Model)


def test_address_model_should_return_valid_fields_when_valid_data_is_passed(
    address_fake_dict,
):
    address = Address(**address_fake_dict)

    assert isinstance(address.district, str)
    assert isinstance(address.cep, str)
    assert isinstance(address.city, str)
    assert isinstance(address.street, str)
    assert isinstance(address.uf, str)
    assert isinstance(address.complement, str)
    assert isinstance(address.neighborhood, str)
    assert isinstance(address.number, int)
