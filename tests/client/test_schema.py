from fastapi_camelcase import CamelModel
from pydantic import BaseModel

from app.application.domain.client.schemas import GetClientSchema, PostClientSchema


def test_client_schema_should_return_valid_instance_when_valid_data_is_passed(
    client_fake_dict,
):
    client_schema = GetClientSchema(**client_fake_dict)

    assert isinstance(client_schema, GetClientSchema)
    assert isinstance(client_schema, CamelModel)
    assert isinstance(client_schema, BaseModel)


def test_client_schema_should_return_valid_instance_fields_when_valid_data_is_passed(
    client_fake_dict,
):
    client_schema = GetClientSchema(**client_fake_dict)

    assert isinstance(client_schema.id, int)
    assert isinstance(client_schema.uuid, str)
    assert isinstance(client_schema.email, str)
    assert isinstance(client_schema.full_name, str)
    assert isinstance(client_schema.is_active, bool)

    assert client_schema.id == client_fake_dict["id"]
    assert client_schema.uuid == client_fake_dict["uuid"]
    assert client_schema.email == client_fake_dict["email"]
    assert client_schema.full_name == client_fake_dict["full_name"]


def test_client_post_schema_should_return_valid_instance_when_valid_data_is_passed(
    client_post_fake_dict,
):
    client_schema = PostClientSchema(**client_post_fake_dict)

    assert isinstance(client_schema, PostClientSchema)
    assert isinstance(client_schema, CamelModel)
    assert isinstance(client_schema, BaseModel)
