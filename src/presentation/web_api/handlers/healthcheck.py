from fastapi import APIRouter, status

from src.presentation.web_api.handlers.responses.common import OkResponse

healthcheck_router = APIRouter(
    prefix="/healthcheck",
    tags=["healthcheck"],
)


OK_STATUS = OkResponse()


@healthcheck_router.get("", status_code=status.HTTP_200_OK)
async def get_status() -> OkResponse[None]:
    return OK_STATUS
