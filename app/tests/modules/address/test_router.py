from fastapi import status

END_POINT = "/api/address/"


def test_router_address_calculate_freight_should_return_200(
    test_app_with_db, address_calculate_freight_fake_dict
):
    response = test_app_with_db.post(
        f"{END_POINT}calculate-freight",
        json=address_calculate_freight_fake_dict,
    )
    assert response.status_code == status.HTTP_200_OK


def test_router_address_calculate_freight_options_should_return_200(
    test_app_with_db, address_calculate_freight_fake_dict
):
    response = test_app_with_db.post(
        f"{END_POINT}calculate-freight-options",
        json=address_calculate_freight_fake_dict,
    )
    assert response.status_code == status.HTTP_200_OK
