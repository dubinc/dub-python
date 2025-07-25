"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from dub.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class Status(str, Enum):
    r"""Useful for marking a commission as refunded, duplicate, canceled, or fraudulent. Takes precedence over `amount` and `modifyAmount`. When a commission is marked as refunded, duplicate, canceled, or fraudulent, it will be omitted from the payout, and the payout amount will be recalculated accordingly. Paid commissions cannot be updated."""

    REFUNDED = "refunded"
    DUPLICATE = "duplicate"
    CANCELED = "canceled"
    FRAUD = "fraud"


class UpdateCommissionRequestBodyTypedDict(TypedDict):
    amount: NotRequired[float]
    r"""The new absolute amount for the sale. Paid commissions cannot be updated."""
    modify_amount: NotRequired[float]
    r"""Modify the current sale amount: use positive values to increase the amount, negative values to decrease it. Takes precedence over `amount`. Paid commissions cannot be updated."""
    currency: NotRequired[str]
    r"""The currency of the sale amount to update. Accepts ISO 4217 currency codes."""
    status: NotRequired[Status]
    r"""Useful for marking a commission as refunded, duplicate, canceled, or fraudulent. Takes precedence over `amount` and `modifyAmount`. When a commission is marked as refunded, duplicate, canceled, or fraudulent, it will be omitted from the payout, and the payout amount will be recalculated accordingly. Paid commissions cannot be updated."""


class UpdateCommissionRequestBody(BaseModel):
    amount: Optional[float] = None
    r"""The new absolute amount for the sale. Paid commissions cannot be updated."""

    modify_amount: Annotated[Optional[float], pydantic.Field(alias="modifyAmount")] = (
        None
    )
    r"""Modify the current sale amount: use positive values to increase the amount, negative values to decrease it. Takes precedence over `amount`. Paid commissions cannot be updated."""

    currency: Optional[str] = "usd"
    r"""The currency of the sale amount to update. Accepts ISO 4217 currency codes."""

    status: Optional[Status] = None
    r"""Useful for marking a commission as refunded, duplicate, canceled, or fraudulent. Takes precedence over `amount` and `modifyAmount`. When a commission is marked as refunded, duplicate, canceled, or fraudulent, it will be omitted from the payout, and the payout amount will be recalculated accordingly. Paid commissions cannot be updated."""


class UpdateCommissionRequestTypedDict(TypedDict):
    id: str
    r"""The commission's unique ID on Dub."""
    request_body: NotRequired[UpdateCommissionRequestBodyTypedDict]


class UpdateCommissionRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The commission's unique ID on Dub."""

    request_body: Annotated[
        Optional[UpdateCommissionRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None


class UpdateCommissionType(str, Enum):
    CLICK = "click"
    LEAD = "lead"
    SALE = "sale"
    CUSTOM = "custom"


class UpdateCommissionStatus(str, Enum):
    PENDING = "pending"
    PROCESSED = "processed"
    PAID = "paid"
    REFUNDED = "refunded"
    DUPLICATE = "duplicate"
    FRAUD = "fraud"
    CANCELED = "canceled"


class UpdateCommissionPartnerTypedDict(TypedDict):
    id: str
    r"""The partner's unique ID on Dub."""
    name: str
    r"""The partner's full legal name."""
    email: Nullable[str]
    r"""The partner's email address. Should be a unique value across Dub."""
    image: Nullable[str]
    r"""The partner's avatar image."""
    payouts_enabled_at: Nullable[str]
    r"""The date when the partner enabled payouts."""
    country: Nullable[str]
    r"""The partner's country (required for tax purposes)."""


class UpdateCommissionPartner(BaseModel):
    id: str
    r"""The partner's unique ID on Dub."""

    name: str
    r"""The partner's full legal name."""

    email: Nullable[str]
    r"""The partner's email address. Should be a unique value across Dub."""

    image: Nullable[str]
    r"""The partner's avatar image."""

    payouts_enabled_at: Annotated[
        Nullable[str], pydantic.Field(alias="payoutsEnabledAt")
    ]
    r"""The date when the partner enabled payouts."""

    country: Nullable[str]
    r"""The partner's country (required for tax purposes)."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["email", "image", "payoutsEnabledAt", "country"]
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


class UpdateCommissionCustomerTypedDict(TypedDict):
    id: str
    r"""The unique ID of the customer. You may use either the customer's `id` on Dub (obtained via `/customers` endpoint) or their `externalId` (unique ID within your system, prefixed with `ext_`, e.g. `ext_123`)."""
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
    country: NotRequired[Nullable[str]]
    r"""Country of the customer."""
    sales: NotRequired[Nullable[float]]
    r"""Total number of sales for the customer."""
    sale_amount: NotRequired[Nullable[float]]
    r"""Total amount of sales for the customer."""


class UpdateCommissionCustomer(BaseModel):
    id: str
    r"""The unique ID of the customer. You may use either the customer's `id` on Dub (obtained via `/customers` endpoint) or their `externalId` (unique ID within your system, prefixed with `ext_`, e.g. `ext_123`)."""

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

    country: OptionalNullable[str] = UNSET
    r"""Country of the customer."""

    sales: OptionalNullable[float] = UNSET
    r"""Total number of sales for the customer."""

    sale_amount: Annotated[
        OptionalNullable[float], pydantic.Field(alias="saleAmount")
    ] = UNSET
    r"""Total amount of sales for the customer."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["email", "avatar", "country", "sales", "saleAmount"]
        nullable_fields = ["email", "avatar", "country", "sales", "saleAmount"]
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


class UpdateCommissionResponseBodyTypedDict(TypedDict):
    r"""The updated commission."""

    id: str
    r"""The commission's unique ID on Dub."""
    amount: float
    earnings: float
    currency: str
    status: UpdateCommissionStatus
    invoice_id: Nullable[str]
    description: Nullable[str]
    quantity: float
    created_at: str
    updated_at: str
    partner: UpdateCommissionPartnerTypedDict
    type: NotRequired[UpdateCommissionType]
    user_id: NotRequired[Nullable[str]]
    r"""The user who created the manual commission."""
    customer: NotRequired[Nullable[UpdateCommissionCustomerTypedDict]]


class UpdateCommissionResponseBody(BaseModel):
    r"""The updated commission."""

    id: str
    r"""The commission's unique ID on Dub."""

    amount: float

    earnings: float

    currency: str

    status: UpdateCommissionStatus

    invoice_id: Annotated[Nullable[str], pydantic.Field(alias="invoiceId")]

    description: Nullable[str]

    quantity: float

    created_at: Annotated[str, pydantic.Field(alias="createdAt")]

    updated_at: Annotated[str, pydantic.Field(alias="updatedAt")]

    partner: UpdateCommissionPartner

    type: Optional[UpdateCommissionType] = None

    user_id: Annotated[OptionalNullable[str], pydantic.Field(alias="userId")] = UNSET
    r"""The user who created the manual commission."""

    customer: OptionalNullable[UpdateCommissionCustomer] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["type", "userId", "customer"]
        nullable_fields = ["invoiceId", "description", "userId", "customer"]
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
