from app.application.domain.product.schemas.get_available_filter_product import (
    GetAvailableFilterProductSchema,
    GetAvailableColorSchema,
    GetAvailableSubTypeSchema,
    GetAvailableSizeSchema,
)
from app.application.domain.product.abstracts.base_product_usecase import (
    BaseProductUseCase,
)


class GetAvailableFilterProductsUseCase(BaseProductUseCase):
    def __init__(self):
        super().__init__(None)

    async def _set_available_size(self, available_size, quantities):
        for qtd in quantities:
            if qtd.available > 0:
                item_filter = GetAvailableSizeSchema(size=qtd.size, selected=False)
                if item_filter not in available_size:
                    available_size.append(item_filter)

    async def _set_available_color_and_sub_type(
        self, available_colors, available_types, prod, quantities
    ):
        for qtd in quantities:
            if qtd.available > 0:
                item_color = GetAvailableColorSchema(color=prod.color, selected=False)
                if item_color not in available_colors:
                    available_colors.append(item_color)

                item_type = GetAvailableSubTypeSchema(
                    type=prod.sub_type, selected=False
                )
                if item_type not in available_types:
                    available_types.append(item_type)
                break

    async def _get_available_filter(self, products):
        available_colors = []
        available_types = []
        available_size = []
        for prod in products:
            quantities = await prod.quantities
            await self._set_available_color_and_sub_type(
                available_colors, available_types, prod, quantities
            )
            await self._set_available_size(available_size, quantities)
        return available_colors, available_size, available_types

    async def execute(self) -> GetAvailableFilterProductSchema:
        products = await self._repository.get_all()
        (
            available_colors,
            available_size,
            available_types,
        ) = await self._get_available_filter(products)
        return GetAvailableFilterProductSchema(
            available_colors=available_colors,
            available_types=available_types,
            available_size=available_size,
        )
