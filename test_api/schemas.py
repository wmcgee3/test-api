from pydantic import BaseModel
from pydantic.fields import Field


class BaseLink(BaseModel):
    href: str


class BaseLinks(BaseModel):
    self: BaseLink


class BaseResponse(BaseModel):
    links: BaseLinks = Field(..., alias="_links")


class RootLinks(BaseLinks):
    other: BaseLink


class RootResponse(BaseResponse):
    links: RootLinks = Field(..., alias="_links")
