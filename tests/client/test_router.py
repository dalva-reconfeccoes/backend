from fastapi import status

END_POINT = "/api/clients/"


def test_router_get_clients_should_be_return_200_when_get_all_clients(
    test_app_with_db, access_token
):
    response = test_app_with_db.get(END_POINT, headers=access_token)
    assert response.status_code == status.HTTP_200_OK


def test_router_client_create_should_be_return_400_when_post_client(
    test_app_with_db, client_created, client_post_fake_dict
):
    response = test_app_with_db.post(END_POINT, json=client_post_fake_dict)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_router_get_client_should_be_return_200_when_post_client(
    test_app_with_db, client_created, access_token
):
    response = test_app_with_db.get(f"{END_POINT}{client_created.get('uuid')}")
    assert response.status_code == status.HTTP_200_OK


def test_router_get_client_by_email_should_be_return_200_when_post_client(
    test_app_with_db, access_token
):
    clients = test_app_with_db.get(END_POINT, headers=access_token)
    email = clients.json().get("items")[0].get("email")

    response = test_app_with_db.get(
        f"{END_POINT}email/?email={email}", headers=access_token
    )

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


def test_email_verification_client_should_be_return_200_when_payload_valid(
    test_app_with_db, client_created
):
    response = test_app_with_db.post(
        f"{END_POINT}verification",
        json={"email": client_created.get("email")},
    )
    assert response.status_code == status.HTTP_200_OK


def test_verify_email_client_should_be_return_400_when_invalid_code(
    test_app_with_db, client_created
):
    response = test_app_with_db.post(
        f"{END_POINT}verify",
        json={"email": client_created.get("email"), "code": "123456"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


def test_reset_password_client_should_be_return_200_when_payload_valid(
    test_app_with_db, client_created
):
    response_change_password = test_app_with_db.post(
        f"{END_POINT}reset-password",
        json={"email": client_created.get("email"), "password": "12345678"},
    )
    assert response_change_password.status_code == status.HTTP_200_OK

    response_login = test_app_with_db.post(
        f"{END_POINT}login",
        json={"email": client_created.get("email"), "password": "12345678"},
    )
    assert response_login.status_code == status.HTTP_200_OK


def test_reset_password_client_should_be_return_400_when_invalid_payload_valid(
    test_app_with_db, client_created
):
    response_change_password = test_app_with_db.post(
        f"{END_POINT}reset-password",
        json={"email": client_created.get("email"), "password": "22255577"},
    )
    assert response_change_password.status_code == status.HTTP_200_OK

    response_login = test_app_with_db.post(
        f"{END_POINT}login",
        json={"email": client_created.get("email"), "password": "11111111"},
    )
    assert response_login.status_code == status.HTTP_400_BAD_REQUEST
