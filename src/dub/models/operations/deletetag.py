"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from dub.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class DeleteTagRequestTypedDict(TypedDict):
    id: str
    r"""The ID of the tag to delete."""


class DeleteTagRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the tag to delete."""


class DeleteTagResponseBodyTypedDict(TypedDict):
    r"""The deleted tag ID."""

    id: str
    r"""The ID of the deleted tag."""


class DeleteTagResponseBody(BaseModel):
    r"""The deleted tag ID."""

    id: str
    r"""The ID of the deleted tag."""
