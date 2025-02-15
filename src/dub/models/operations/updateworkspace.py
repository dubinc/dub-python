"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from dub.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateWorkspaceRequestBodyTypedDict(TypedDict):
    name: NotRequired[str]
    slug: NotRequired[str]
    logo: NotRequired[str]
    conversion_enabled: NotRequired[bool]
    allowed_hostnames: NotRequired[List[str]]


class UpdateWorkspaceRequestBody(BaseModel):
    name: Optional[str] = None

    slug: Optional[str] = None

    logo: Optional[str] = None

    conversion_enabled: Annotated[
        Optional[bool], pydantic.Field(alias="conversionEnabled")
    ] = None

    allowed_hostnames: Annotated[
        Optional[List[str]], pydantic.Field(alias="allowedHostnames")
    ] = None


class UpdateWorkspaceRequestTypedDict(TypedDict):
    id_or_slug: str
    r"""The ID or slug of the workspace to update."""
    request_body: NotRequired[UpdateWorkspaceRequestBodyTypedDict]


class UpdateWorkspaceRequest(BaseModel):
    id_or_slug: Annotated[
        str,
        pydantic.Field(alias="idOrSlug"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]
    r"""The ID or slug of the workspace to update."""

    request_body: Annotated[
        Optional[UpdateWorkspaceRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
