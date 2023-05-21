from app.application.domain.product.schemas.get_product import GetProductSchema
from app.application.domain.product.abstracts.base_product_usecase import (
    BaseProductUseCase,
)


class GetAllProductUseCase(BaseProductUseCase):
    def __init__(self):
        super().__init__(None)

    async def execute(self) -> [GetProductSchema]:
        products = await self._repository.get_all()
        return [await self._serializer(prod) for prod in products]
