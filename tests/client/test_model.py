from tortoise import Model

from app.models.client import Client


def test_client_model_should_return_valid_instance_when_valid_data_is_passed(
    client_fake_dict,
):
    client = Client(**client_fake_dict)
    assert isinstance(client, Model)


def test_client_model_should_return_valid_fields_when_valid_data_is_passed(
    client_fake_dict,
):
    client = Client(**client_fake_dict)

    assert isinstance(client.full_name, str)
    assert isinstance(client.email, str)
    assert isinstance(client.password, str)

    assert client.full_name == client_fake_dict["full_name"]
    assert client.email == client_fake_dict["email"]
    assert client.password == client_fake_dict["password"]
