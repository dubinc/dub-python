"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from dub.utils import FieldMetadata, PathParamMetadata, RequestMetadata
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateCustomerRequestBodyTypedDict(TypedDict):
    email: NotRequired[Nullable[str]]
    r"""Email of the customer in the client's app."""
    name: NotRequired[Nullable[str]]
    r"""Name of the customer in the client's app. If not provided, a random name will be generated."""
    avatar: NotRequired[Nullable[str]]
    r"""Avatar URL of the customer in the client's app."""
    external_id: NotRequired[str]
    r"""Unique identifier for the customer in the client's app."""


class UpdateCustomerRequestBody(BaseModel):
    email: OptionalNullable[str] = UNSET
    r"""Email of the customer in the client's app."""

    name: OptionalNullable[str] = UNSET
    r"""Name of the customer in the client's app. If not provided, a random name will be generated."""

    avatar: OptionalNullable[str] = UNSET
    r"""Avatar URL of the customer in the client's app."""

    external_id: Annotated[Optional[str], pydantic.Field(alias="externalId")] = None
    r"""Unique identifier for the customer in the client's app."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["email", "name", "avatar", "externalId"]
        nullable_fields = ["email", "name", "avatar"]
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


class UpdateCustomerRequestTypedDict(TypedDict):
    id: str
    r"""The unique identifier of the customer in Dub."""
    request_body: NotRequired[UpdateCustomerRequestBodyTypedDict]


class UpdateCustomerRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The unique identifier of the customer in Dub."""

    request_body: Annotated[
        Optional[UpdateCustomerRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class UpdateCustomerResponseBodyTypedDict(TypedDict):
    r"""The customer was updated."""

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


class UpdateCustomerResponseBody(BaseModel):
    r"""The customer was updated."""

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