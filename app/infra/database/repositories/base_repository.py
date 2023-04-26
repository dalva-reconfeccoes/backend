from tortoise import Model
from tortoise.exceptions import BaseORMException


class BaseRepository:
    def __init__(self):
        self.entity = Model

    async def create(self, payload: dict):
        return await self.entity.create(**payload)

    async def update(self, payload: dict, _id: int) -> Model:
        await self.entity.filter(id=_id).update(**payload)
        return await self.get_by_id(_id)

    async def get_all(self) -> list:
        return await self.entity.all()

    async def get_by_id(self, _id: int) -> [dict, None]:
        return await self.entity.get_or_none(id=_id)

    async def delete(self, _id: int) -> bool:
        try:
            await self.entity.filter(id=_id).delete()
            return True
        except BaseORMException:
            return False

    async def get_or_none(self, **kwargs):
        return await self.entity.get_or_none(**kwargs)
