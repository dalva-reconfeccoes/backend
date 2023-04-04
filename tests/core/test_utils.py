from app.application.helpers.utils import format_client_name


def test_format_client_name():
    name = "EDUARDO RODRIGUES DE MORAIS"
    format_name = format_client_name(name)
    assert format_name == "Eduardo Rodrigues De Morais"
