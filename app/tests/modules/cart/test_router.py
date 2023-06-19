from fastapi import status

END_POINT = "/api/cart/"


def test_router_get_cart_should_return_200(test_app_with_db, cart_created):
    response = test_app_with_db.get(
        f"{END_POINT}{cart_created.get('uuid')}",
    )
    assert response.status_code == status.HTTP_200_OK


def test_router_cart_add_product_should_return_200(
    test_app_with_db, cart_created, post_cart_fake_dict
):
    response = test_app_with_db.post(
        f"{END_POINT}{cart_created.get('uuid')}/add-product/", json=post_cart_fake_dict
    )
    assert response.status_code == status.HTTP_200_OK


def test_router_cart_remove_product_should_return_200(
    test_app_with_db, cart_created, post_cart_fake_dict
):
    response_add = test_app_with_db.post(
        f"{END_POINT}{cart_created.get('uuid')}/add-product/", json=post_cart_fake_dict
    )
    assert response_add.status_code == status.HTTP_200_OK
    cart = response_add.json()
    product = cart.get("selectedProducts").pop()
    response_del = test_app_with_db.delete(
        f"{END_POINT}{cart_created.get('uuid')}/remove-product/{product.get('uuid')}"
    )
    assert response_del.status_code == status.HTTP_200_OK
