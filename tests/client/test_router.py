import pytest
from fastapi import status

END_POINT = "/api/clients/"


def test_router_get_clients_should_be_return_200_when_get_all_clients(
    test_app_with_db, access_token
):
    response = test_app_with_db.get(END_POINT, headers=access_token)
    assert response.status_code == status.HTTP_200_OK


def test_router_client_create_should_be_return_201_when_post_client(
    test_app_with_db, client_post_fake_dict, access_token
):
    response = test_app_with_db.post(
        END_POINT, json=client_post_fake_dict, headers=access_token
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_router_client_create_should_be_return_400_when_post_client(
    test_app_with_db, client_post_fake_dict, access_token
):
    response = test_app_with_db.post(
        END_POINT, json=client_post_fake_dict, headers=access_token
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.fixture
def client_created(test_app_with_db, client_post_fake_dict, access_token):
    client_post_fake_dict["email"] = "email2@example.com"
    created = test_app_with_db.post(
        END_POINT, json=client_post_fake_dict, headers=access_token
    )
    return created.json()


def test_router_get_client_should_be_return_200_when_post_client(
    test_app_with_db, client_created, access_token
):
    response = test_app_with_db.get(
        f"{END_POINT}{client_created.get('id')}", headers=access_token
    )

    assert response.status_code == status.HTTP_200_OK


def test_router_get_client_by_email_should_be_return_200_when_post_client(
    test_app_with_db, client_created, access_token
):
    clients = test_app_with_db.get(END_POINT, headers=access_token)
    email = clients.json().get("items")[0].get("email")

    response = test_app_with_db.get(f"{END_POINT}email/{email}", headers=access_token)

    assert response.status_code == status.HTTP_200_OK


def test_router_put_client_should_be_return_200_when_payload_valid(
    test_app_with_db, client_put_fake_dict, access_token
):
    clients = test_app_with_db.get(END_POINT, headers=access_token)
    payload = clients.json().get("items")[0]

    payload["full_name"] = client_put_fake_dict["full_name"]
    payload["password"] = client_put_fake_dict["password"]
    payload["is_active"] = client_put_fake_dict["is_active"]

    response = test_app_with_db.put(
        f"{END_POINT}{payload.get('id')}", json=payload, headers=access_token
    )

    assert response.status_code == status.HTTP_200_OK


def test_login_client_should_be_return_400_when_payload_invalid(
    test_app_with_db, client_login_fake_dict, access_token
):
    response = test_app_with_db.post(
        f"{END_POINT}login", json=client_login_fake_dict, headers=access_token
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
