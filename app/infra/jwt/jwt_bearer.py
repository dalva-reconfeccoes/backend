from fastapi import Depends, Request, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import JWTDecodeError

from app.infra.settings import get_settings

settings = get_settings()


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request, authorization: AuthJWT = Depends()):
        try:
            credentials: HTTPAuthorizationCredentials = await super(
                JWTBearer, self
            ).__call__(request)
            authorization.jwt_required()
            return credentials
        except JWTDecodeError as exc:
            raise HTTPException(
                status_code=exc.status_code,
                detail=exc.message,
            )
