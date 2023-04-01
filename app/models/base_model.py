from tortoise import timezone
from tortoise.fields import DatetimeField
from tortoise.models import Model


class BaseModel(Model):
    created_at = DatetimeField(auto_now_add=True, default=timezone.now())
    updated_at = DatetimeField(auto_now=True, default=timezone.now())

    class Meta:
        abstract = True
