from app.application.helpers import utils


def test_format_client_name():
    name = "EDUARDO RODRIGUES DE MORAIS"
    format_name = utils.format_name(name)
    assert format_name == "Eduardo Rodrigues De Morais"
