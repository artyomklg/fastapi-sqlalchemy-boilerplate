from typing import Generic, TypeVar

from pydantic import BaseModel, Field

TResult = TypeVar("TResult")
TError = TypeVar("TError")


class BaseResponse(BaseModel):
    pass


class OkResponse(BaseResponse, Generic[TResult]):
    status: int = 200
    result: TResult | None = None


class ErrorData(BaseModel, Generic[TError]):
    message: str = "Unknown error occurred"
    data: TError | None = None


class ErrorResponse(BaseResponse, Generic[TError]):
    status: int = 500
    error: ErrorData[TError] = Field(default_factory=ErrorData)
