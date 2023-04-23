from fastapi import status

END_POINT = "/api/products/"


def test_router_get_products_should_be_return_200_when_get_all_products(
    test_app_with_db, product_created
):
    response = test_app_with_db.get(END_POINT)
    assert response.status_code == status.HTTP_200_OK


def test_router_product_create_should_be_return_400_when_post_product(
    test_app_with_db, product_fake_dict
):
    response = test_app_with_db.post(END_POINT, json=product_fake_dict)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_router_get_product_should_be_return_200_when_post_product(
    test_app_with_db, product_created
):
    response = test_app_with_db.get(f"{END_POINT}{product_created.get('uuid')}")
    assert response.status_code == status.HTTP_200_OK