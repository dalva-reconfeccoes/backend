from app.models.image import Image


def test_image_model_should_return_valid_fields_when_valid_data_is_passed(
    image_fake_dict,
):
    image = Image(**image_fake_dict)

    assert isinstance(image.uuid, str)
    assert isinstance(image.filename, str)
    assert isinstance(image.content_type, str)
    assert isinstance(image.bucket, str)
    assert isinstance(image.is_active, bool)
