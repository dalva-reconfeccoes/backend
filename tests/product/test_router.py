from fastapi import status

END_POINT = "/api/products/"


def test_router_get_products_should_be_return_200_when_get_all_products(
    test_app_with_db, product_created
):
    response = test_app_with_db.get(END_POINT)
    assert response.status_code == status.HTTP_200_OK


def test_router_product_create_should_be_return_400_when_post_product(
    test_app_with_db, access_token, product_created, product_fake_dict
):
    response = test_app_with_db.post(
        END_POINT, json=product_fake_dict, headers=access_token
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_router_get_product_should_be_return_200_when_post_product(
    test_app_with_db, product_created
):
    response = test_app_with_db.get(f"{END_POINT}{product_created.get('uuid')}")
    assert response.status_code == status.HTTP_200_OK


def test_router_register_quantity_product_should_be_return_201_when_post_product(
    test_app_with_db, new_quantity_fake_dict, access_token
):
    response = test_app_with_db.post(
        f"{END_POINT}quantity", json=[new_quantity_fake_dict], headers=access_token
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_router_get_available_filter_products_should_be_return_200_when_get_product(
    test_app_with_db, access_token
):
    response = test_app_with_db.get(f"{END_POINT}available/filter")
    assert response.status_code == status.HTTP_200_OK


def test_router_filter_available_products_should_be_return_200_when_pass_valid_filter(
    test_app_with_db, access_token
):
    data = {"colors": ["#000000"], "subTypes": ["Básica"], "sizes": ["PP"]}
    response = test_app_with_db.post(f"{END_POINT}filter", json=data)
    assert response.status_code == status.HTTP_200_OK


def test_router_filter_available_products_should_be_return_200_when_no_pass_values_on_filter(
    test_app_with_db, access_token
):
    data = {"colors": [], "subTypes": [], "sizes": []}
    response = test_app_with_db.post(f"{END_POINT}filter", json=data)
    assert response.status_code == status.HTTP_200_OK
