"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel, Nullable, UNSET_SENTINEL
from pydantic import model_serializer
from typing_extensions import TypedDict


class RegisterDomainRequestBodyTypedDict(TypedDict):
    domain: str
    r"""The domain to claim. We only support .link domains for now."""


class RegisterDomainRequestBody(BaseModel):
    domain: str
    r"""The domain to claim. We only support .link domains for now."""


class RegisterDomainResponseBodyTypedDict(TypedDict):
    r"""The domain was registered."""

    domain: str
    r"""The domain name."""
    status: str
    r"""The status of the domain registration."""
    expiration: Nullable[float]
    r"""The expiration timestamp of the domain (Unix timestamp in milliseconds)."""


class RegisterDomainResponseBody(BaseModel):
    r"""The domain was registered."""

    domain: str
    r"""The domain name."""

    status: str
    r"""The status of the domain registration."""

    expiration: Nullable[float]
    r"""The expiration timestamp of the domain (Unix timestamp in milliseconds)."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["expiration"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
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
