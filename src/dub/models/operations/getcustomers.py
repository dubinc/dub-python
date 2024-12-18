"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict


class ResponseBodyTypedDict(TypedDict):
    id: str
    r"""The unique identifier of the customer in Dub."""
    external_id: str
    r"""Unique identifier for the customer in the client's app."""
    name: str
    r"""Name of the customer."""
    created_at: str
    r"""The date the customer was created."""
    email: NotRequired[Nullable[str]]
    r"""Email of the customer."""
    avatar: NotRequired[Nullable[str]]
    r"""Avatar URL of the customer."""


class ResponseBody(BaseModel):
    id: str
    r"""The unique identifier of the customer in Dub."""

    external_id: Annotated[str, pydantic.Field(alias="externalId")]
    r"""Unique identifier for the customer in the client's app."""

    name: str
    r"""Name of the customer."""

    created_at: Annotated[str, pydantic.Field(alias="createdAt")]
    r"""The date the customer was created."""

    email: OptionalNullable[str] = UNSET
    r"""Email of the customer."""

    avatar: OptionalNullable[str] = UNSET
    r"""Avatar URL of the customer."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["email", "avatar"]
        nullable_fields = ["email", "avatar"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
