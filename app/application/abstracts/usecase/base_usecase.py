from abc import ABCMeta

from fastapi import HTTPException, status
from fastapi_camelcase import CamelModel

from app.application.abstracts.usecase.enum import ErrorsUseCaseEnum
from app.application.helpers.utils import clean_none_values_dict
from app.infra.database.repositories.base_repository import BaseRepository


class BaseUseCase(metaclass=ABCMeta):
    def __init__(
        self,
        model_name: str,
        payload: CamelModel,
        repository: BaseRepository,
    ):
        self._payload = payload
        self._repository = repository
        self._model_name = model_name
        self._errors = ErrorsUseCaseEnum

    async def _validate_db(self, **kwargs):
        model = await self._repository.get_or_none(**kwargs)
        if model is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=self._errors.NOT_FOUND.format(model=self._model_name),
            )
        return model

    async def _validate_already_exists_db(self, **kwargs):
        model = await self._repository.get_or_none(**kwargs)
        if model is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=self._errors.ALREADY_REGISTERED.format(model=self._model_name),
            )

    async def _filter_db(self, **kwargs):
        model = await self._repository.get_or_none(**kwargs)
        return model

    async def _validate_values_payload(self):
        clean_dict = await clean_none_values_dict(self._payload.dict())
        if len(clean_dict.keys()) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=self._errors.PARAMETERS_NOT_FOUND,
            )
        self._payload_clean = clean_dict
