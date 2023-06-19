from fastapi_camelcase import CamelModel
from pydantic import BaseModel

from app.application.domain.address.schemas.calculate_freight import (
    CalculateFreightSchema,
)
from app.application.domain.address.schemas.calculate_freight_options import (
    CalculateFreightOptionsSchema,
)
from app.application.domain.address.schemas.calculated_freight_correios import (
    CalculatedFreightCorreiosSchema,
)
from app.application.domain.address.schemas.get_address import GetAddressSchema
from app.application.domain.address.schemas.post_address import PostAddressSchema
from app.application.domain.address.schemas.update_address import UpdateAddressSchema


def test_post_address_schema_should_return_valid_instance_when_valid_data_is_passed(
    address_fake_dict,
):
    schema = PostAddressSchema(**address_fake_dict)
    assert isinstance(schema, PostAddressSchema)
    assert isinstance(schema, CamelModel)
    assert isinstance(schema, BaseModel)


def test_get_address_schema_should_return_valid_instance_when_valid_data_is_passed(
    address_fake_dict,
):
    schema = GetAddressSchema(**address_fake_dict)
    assert isinstance(schema, GetAddressSchema)
    assert isinstance(schema, CamelModel)
    assert isinstance(schema, BaseModel)


def test_update_address_schema_should_return_valid_instance_when_valid_data_is_passed(
    address_fake_dict,
):
    schema = UpdateAddressSchema(**address_fake_dict)
    assert isinstance(schema, UpdateAddressSchema)
    assert isinstance(schema, CamelModel)
    assert isinstance(schema, BaseModel)


def test_update_address_schema_should_return_valid_instance_when_no_data_is_passed():
    schema = UpdateAddressSchema()
    assert isinstance(schema, UpdateAddressSchema)
    assert isinstance(schema, CamelModel)
    assert isinstance(schema, BaseModel)


def test_calculate_freight_schema_should_return_valid_instance_when_valid_data_is_passed(
    address_calculate_freight_fake_dict,
):
    schema = CalculateFreightSchema(**address_calculate_freight_fake_dict)
    assert isinstance(schema, CalculateFreightSchema)
    assert isinstance(schema, CamelModel)
    assert isinstance(schema, BaseModel)


def test_calculate_freight_options_schema_should_return_valid_instance_when_valid_data_is_passed(
    address_calculate_freight_fake_dict,
):
    schema = CalculateFreightOptionsSchema(**address_calculate_freight_fake_dict)
    assert isinstance(schema, CalculateFreightOptionsSchema)
    assert isinstance(schema, CamelModel)
    assert isinstance(schema, BaseModel)


def test_calculated_freight_correios_schema_should_return_valid_instance_when_valid_data_is_passed(
    address_calculated_freight_correios_fake_dict,
):
    schema = CalculatedFreightCorreiosSchema(
        **address_calculated_freight_correios_fake_dict
    )
    assert isinstance(schema, CalculatedFreightCorreiosSchema)
    assert isinstance(schema, CamelModel)
    assert isinstance(schema, BaseModel)
