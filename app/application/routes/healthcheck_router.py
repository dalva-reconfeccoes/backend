from fastapi import APIRouter, Depends, Request

from app.infra.log import AppLog

router = APIRouter()


@router.get(
    "/health-check",
    description="Router to check health application",
    dependencies=[Depends(AppLog())],
)
async def healthcheck(_request: Request):
    return {"msg": "Application running"}
