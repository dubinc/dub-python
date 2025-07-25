"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from dub.utils import FieldMetadata, QueryParamMetadata
from enum import Enum
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListPartnersQueryParamStatus(str, Enum):
    r"""A filter on the list based on the partner's `status` field."""

    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    INVITED = "invited"
    DECLINED = "declined"
    BANNED = "banned"
    ARCHIVED = "archived"


class ListPartnersQueryParamSortBy(str, Enum):
    r"""The field to sort the partners by. The default is `saleAmount`."""

    CREATED_AT = "createdAt"
    CLICKS = "clicks"
    LEADS = "leads"
    SALES = "sales"
    SALE_AMOUNT = "saleAmount"
    COMMISSIONS = "commissions"
    NET_REVENUE = "netRevenue"


class ListPartnersQueryParamSortOrder(str, Enum):
    r"""The sort order. The default is `desc`."""

    ASC = "asc"
    DESC = "desc"


class ListPartnersRequestTypedDict(TypedDict):
    status: NotRequired[ListPartnersQueryParamStatus]
    r"""A filter on the list based on the partner's `status` field."""
    country: NotRequired[str]
    r"""A filter on the list based on the partner's `country` field."""
    sort_by: NotRequired[ListPartnersQueryParamSortBy]
    r"""The field to sort the partners by. The default is `saleAmount`."""
    sort_order: NotRequired[ListPartnersQueryParamSortOrder]
    r"""The sort order. The default is `desc`."""
    tenant_id: NotRequired[str]
    r"""A case-sensitive filter on the list based on the partner's `tenantId` field. The value must be a string. Takes precedence over `search`."""
    include_expanded_fields: NotRequired[bool]
    r"""Whether to include stats fields on the partner (`clicks`, `leads`, `sales`, `saleAmount`, `commissions`, `netRevenue`). If false, those fields will be returned as 0."""
    search: NotRequired[str]
    r"""A search query to filter partners by name, email, or tenantId."""
    page: NotRequired[float]
    r"""The page number for pagination."""
    page_size: NotRequired[float]
    r"""The number of items per page."""


class ListPartnersRequest(BaseModel):
    status: Annotated[
        Optional[ListPartnersQueryParamStatus],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A filter on the list based on the partner's `status` field."""

    country: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A filter on the list based on the partner's `country` field."""

    sort_by: Annotated[
        Optional[ListPartnersQueryParamSortBy],
        pydantic.Field(alias="sortBy"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = ListPartnersQueryParamSortBy.SALE_AMOUNT
    r"""The field to sort the partners by. The default is `saleAmount`."""

    sort_order: Annotated[
        Optional[ListPartnersQueryParamSortOrder],
        pydantic.Field(alias="sortOrder"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = ListPartnersQueryParamSortOrder.DESC
    r"""The sort order. The default is `desc`."""

    tenant_id: Annotated[
        Optional[str],
        pydantic.Field(alias="tenantId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A case-sensitive filter on the list based on the partner's `tenantId` field. The value must be a string. Takes precedence over `search`."""

    include_expanded_fields: Annotated[
        Optional[bool],
        pydantic.Field(alias="includeExpandedFields"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Whether to include stats fields on the partner (`clicks`, `leads`, `sales`, `saleAmount`, `commissions`, `netRevenue`). If false, those fields will be returned as 0."""

    search: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""A search query to filter partners by name, email, or tenantId."""

    page: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1
    r"""The page number for pagination."""

    page_size: Annotated[
        Optional[float],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 100
    r"""The number of items per page."""


class ListPartnersStatus(str, Enum):
    r"""The status of the partner's enrollment in the program."""

    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    INVITED = "invited"
    DECLINED = "declined"
    BANNED = "banned"
    ARCHIVED = "archived"


class ListPartnersLinkTypedDict(TypedDict):
    id: str
    r"""The unique ID of the short link."""
    domain: str
    r"""The domain of the short link. If not provided, the primary domain for the workspace will be used (or `dub.sh` if the workspace has no domains)."""
    key: str
    r"""The short link slug. If not provided, a random 7-character slug will be generated."""
    short_link: str
    r"""The full URL of the short link, including the https protocol (e.g. `https://dub.sh/try`)."""
    url: str
    r"""The destination URL of the short link."""
    clicks: NotRequired[float]
    r"""The number of clicks on the short link."""
    leads: NotRequired[float]
    r"""The number of leads the short links has generated."""
    sales: NotRequired[float]
    r"""The number of sales the short links has generated."""
    sale_amount: NotRequired[float]
    r"""The total dollar amount of sales the short links has generated (in cents)."""


class ListPartnersLink(BaseModel):
    id: str
    r"""The unique ID of the short link."""

    domain: str
    r"""The domain of the short link. If not provided, the primary domain for the workspace will be used (or `dub.sh` if the workspace has no domains)."""

    key: str
    r"""The short link slug. If not provided, a random 7-character slug will be generated."""

    short_link: Annotated[str, pydantic.Field(alias="shortLink")]
    r"""The full URL of the short link, including the https protocol (e.g. `https://dub.sh/try`)."""

    url: str
    r"""The destination URL of the short link."""

    clicks: Optional[float] = 0
    r"""The number of clicks on the short link."""

    leads: Optional[float] = 0
    r"""The number of leads the short links has generated."""

    sales: Optional[float] = 0
    r"""The number of sales the short links has generated."""

    sale_amount: Annotated[Optional[float], pydantic.Field(alias="saleAmount")] = 0
    r"""The total dollar amount of sales the short links has generated (in cents)."""


class ListPartnersBannedReason(str, Enum):
    r"""If the partner was banned from the program, this is the reason for the ban."""

    TOS_VIOLATION = "tos_violation"
    INAPPROPRIATE_CONTENT = "inappropriate_content"
    FAKE_TRAFFIC = "fake_traffic"
    FRAUD = "fraud"
    SPAM = "spam"
    BRAND_ABUSE = "brand_abuse"


class ListPartnersResponseBodyTypedDict(TypedDict):
    id: str
    r"""The partner's unique ID on Dub."""
    name: str
    r"""The partner's full legal name."""
    email: Nullable[str]
    r"""The partner's email address. Should be a unique value across Dub."""
    image: Nullable[str]
    r"""The partner's avatar image."""
    country: Nullable[str]
    r"""The partner's country (required for tax purposes)."""
    paypal_email: Nullable[str]
    r"""The partner's PayPal email (for receiving payouts via PayPal)."""
    stripe_connect_id: Nullable[str]
    r"""The partner's Stripe Connect ID (for receiving payouts via Stripe)."""
    payouts_enabled_at: Nullable[str]
    r"""The date when the partner enabled payouts."""
    partner_id: str
    r"""The partner's unique ID on Dub."""
    tenant_id: Nullable[str]
    r"""The partner's unique ID within your database. Can be useful for associating the partner with a user in your database and retrieving/update their data in the future."""
    program_id: str
    r"""The program's unique ID on Dub."""
    created_at: str
    status: ListPartnersStatus
    r"""The status of the partner's enrollment in the program."""
    links: Nullable[List[ListPartnersLinkTypedDict]]
    r"""The partner's referral links in this program."""
    description: NotRequired[Nullable[str]]
    r"""A brief description of the partner and their background."""
    total_commissions: NotRequired[float]
    r"""The total commissions paid to the partner for their referrals. Defaults to 0 if `includeExpandedFields` is false."""
    click_reward_id: NotRequired[Nullable[str]]
    lead_reward_id: NotRequired[Nullable[str]]
    sale_reward_id: NotRequired[Nullable[str]]
    discount_id: NotRequired[Nullable[str]]
    application_id: NotRequired[Nullable[str]]
    r"""If the partner submitted an application to join the program, this is the ID of the application."""
    banned_at: NotRequired[Nullable[str]]
    r"""If the partner was banned from the program, this is the date of the ban."""
    banned_reason: NotRequired[Nullable[ListPartnersBannedReason]]
    r"""If the partner was banned from the program, this is the reason for the ban."""
    clicks: NotRequired[float]
    r"""The total number of clicks on the partner's links. Defaults to 0 if `includeExpandedFields` is false."""
    leads: NotRequired[float]
    r"""The total number of leads generated by the partner's links. Defaults to 0 if `includeExpandedFields` is false."""
    sales: NotRequired[float]
    r"""The total number of sales generated by the partner's links. Defaults to 0 if `includeExpandedFields` is false."""
    sale_amount: NotRequired[float]
    r"""The total amount of sales (in cents) generated by the partner's links. Defaults to 0 if `includeExpandedFields` is false."""
    net_revenue: NotRequired[float]
    r"""The total net revenue generated by the partner. Defaults to 0 if `includeExpandedFields` is false."""
    website: NotRequired[Nullable[str]]
    r"""The partner's website URL (including the https protocol)."""
    website_txt_record: NotRequired[Nullable[str]]
    website_verified_at: NotRequired[Nullable[str]]
    youtube: NotRequired[Nullable[str]]
    r"""The partner's YouTube channel username (e.g. `johndoe`)."""
    youtube_verified_at: NotRequired[Nullable[str]]
    youtube_subscriber_count: NotRequired[Nullable[float]]
    youtube_view_count: NotRequired[Nullable[float]]
    twitter: NotRequired[Nullable[str]]
    r"""The partner's Twitter username (e.g. `johndoe`)."""
    twitter_verified_at: NotRequired[Nullable[str]]
    linkedin: NotRequired[Nullable[str]]
    r"""The partner's LinkedIn username (e.g. `johndoe`)."""
    linkedin_verified_at: NotRequired[Nullable[str]]
    instagram: NotRequired[Nullable[str]]
    r"""The partner's Instagram username (e.g. `johndoe`)."""
    instagram_verified_at: NotRequired[Nullable[str]]
    tiktok: NotRequired[Nullable[str]]
    r"""The partner's TikTok username (e.g. `johndoe`)."""
    tiktok_verified_at: NotRequired[Nullable[str]]


class ListPartnersResponseBody(BaseModel):
    id: str
    r"""The partner's unique ID on Dub."""

    name: str
    r"""The partner's full legal name."""

    email: Nullable[str]
    r"""The partner's email address. Should be a unique value across Dub."""

    image: Nullable[str]
    r"""The partner's avatar image."""

    country: Nullable[str]
    r"""The partner's country (required for tax purposes)."""

    paypal_email: Annotated[Nullable[str], pydantic.Field(alias="paypalEmail")]
    r"""The partner's PayPal email (for receiving payouts via PayPal)."""

    stripe_connect_id: Annotated[Nullable[str], pydantic.Field(alias="stripeConnectId")]
    r"""The partner's Stripe Connect ID (for receiving payouts via Stripe)."""

    payouts_enabled_at: Annotated[
        Nullable[str], pydantic.Field(alias="payoutsEnabledAt")
    ]
    r"""The date when the partner enabled payouts."""

    partner_id: Annotated[str, pydantic.Field(alias="partnerId")]
    r"""The partner's unique ID on Dub."""

    tenant_id: Annotated[Nullable[str], pydantic.Field(alias="tenantId")]
    r"""The partner's unique ID within your database. Can be useful for associating the partner with a user in your database and retrieving/update their data in the future."""

    program_id: Annotated[str, pydantic.Field(alias="programId")]
    r"""The program's unique ID on Dub."""

    created_at: Annotated[str, pydantic.Field(alias="createdAt")]

    status: ListPartnersStatus
    r"""The status of the partner's enrollment in the program."""

    links: Nullable[List[ListPartnersLink]]
    r"""The partner's referral links in this program."""

    description: OptionalNullable[str] = UNSET
    r"""A brief description of the partner and their background."""

    total_commissions: Annotated[
        Optional[float], pydantic.Field(alias="totalCommissions")
    ] = 0
    r"""The total commissions paid to the partner for their referrals. Defaults to 0 if `includeExpandedFields` is false."""

    click_reward_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="clickRewardId")
    ] = UNSET

    lead_reward_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="leadRewardId")
    ] = UNSET

    sale_reward_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="saleRewardId")
    ] = UNSET

    discount_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="discountId")
    ] = UNSET

    application_id: Annotated[
        OptionalNullable[str], pydantic.Field(alias="applicationId")
    ] = UNSET
    r"""If the partner submitted an application to join the program, this is the ID of the application."""

    banned_at: Annotated[OptionalNullable[str], pydantic.Field(alias="bannedAt")] = (
        UNSET
    )
    r"""If the partner was banned from the program, this is the date of the ban."""

    banned_reason: Annotated[
        OptionalNullable[ListPartnersBannedReason], pydantic.Field(alias="bannedReason")
    ] = UNSET
    r"""If the partner was banned from the program, this is the reason for the ban."""

    clicks: Optional[float] = 0
    r"""The total number of clicks on the partner's links. Defaults to 0 if `includeExpandedFields` is false."""

    leads: Optional[float] = 0
    r"""The total number of leads generated by the partner's links. Defaults to 0 if `includeExpandedFields` is false."""

    sales: Optional[float] = 0
    r"""The total number of sales generated by the partner's links. Defaults to 0 if `includeExpandedFields` is false."""

    sale_amount: Annotated[Optional[float], pydantic.Field(alias="saleAmount")] = 0
    r"""The total amount of sales (in cents) generated by the partner's links. Defaults to 0 if `includeExpandedFields` is false."""

    net_revenue: Annotated[Optional[float], pydantic.Field(alias="netRevenue")] = 0
    r"""The total net revenue generated by the partner. Defaults to 0 if `includeExpandedFields` is false."""

    website: OptionalNullable[str] = UNSET
    r"""The partner's website URL (including the https protocol)."""

    website_txt_record: Annotated[
        OptionalNullable[str], pydantic.Field(alias="websiteTxtRecord")
    ] = UNSET

    website_verified_at: Annotated[
        OptionalNullable[str], pydantic.Field(alias="websiteVerifiedAt")
    ] = UNSET

    youtube: OptionalNullable[str] = UNSET
    r"""The partner's YouTube channel username (e.g. `johndoe`)."""

    youtube_verified_at: Annotated[
        OptionalNullable[str], pydantic.Field(alias="youtubeVerifiedAt")
    ] = UNSET

    youtube_subscriber_count: Annotated[
        OptionalNullable[float], pydantic.Field(alias="youtubeSubscriberCount")
    ] = UNSET

    youtube_view_count: Annotated[
        OptionalNullable[float], pydantic.Field(alias="youtubeViewCount")
    ] = UNSET

    twitter: OptionalNullable[str] = UNSET
    r"""The partner's Twitter username (e.g. `johndoe`)."""

    twitter_verified_at: Annotated[
        OptionalNullable[str], pydantic.Field(alias="twitterVerifiedAt")
    ] = UNSET

    linkedin: OptionalNullable[str] = UNSET
    r"""The partner's LinkedIn username (e.g. `johndoe`)."""

    linkedin_verified_at: Annotated[
        OptionalNullable[str], pydantic.Field(alias="linkedinVerifiedAt")
    ] = UNSET

    instagram: OptionalNullable[str] = UNSET
    r"""The partner's Instagram username (e.g. `johndoe`)."""

    instagram_verified_at: Annotated[
        OptionalNullable[str], pydantic.Field(alias="instagramVerifiedAt")
    ] = UNSET

    tiktok: OptionalNullable[str] = UNSET
    r"""The partner's TikTok username (e.g. `johndoe`)."""

    tiktok_verified_at: Annotated[
        OptionalNullable[str], pydantic.Field(alias="tiktokVerifiedAt")
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "description",
            "totalCommissions",
            "clickRewardId",
            "leadRewardId",
            "saleRewardId",
            "discountId",
            "applicationId",
            "bannedAt",
            "bannedReason",
            "clicks",
            "leads",
            "sales",
            "saleAmount",
            "netRevenue",
            "website",
            "websiteTxtRecord",
            "websiteVerifiedAt",
            "youtube",
            "youtubeVerifiedAt",
            "youtubeSubscriberCount",
            "youtubeViewCount",
            "twitter",
            "twitterVerifiedAt",
            "linkedin",
            "linkedinVerifiedAt",
            "instagram",
            "instagramVerifiedAt",
            "tiktok",
            "tiktokVerifiedAt",
        ]
        nullable_fields = [
            "email",
            "image",
            "description",
            "country",
            "paypalEmail",
            "stripeConnectId",
            "payoutsEnabledAt",
            "tenantId",
            "links",
            "clickRewardId",
            "leadRewardId",
            "saleRewardId",
            "discountId",
            "applicationId",
            "bannedAt",
            "bannedReason",
            "website",
            "websiteTxtRecord",
            "websiteVerifiedAt",
            "youtube",
            "youtubeVerifiedAt",
            "youtubeSubscriberCount",
            "youtubeViewCount",
            "twitter",
            "twitterVerifiedAt",
            "linkedin",
            "linkedinVerifiedAt",
            "instagram",
            "instagramVerifiedAt",
            "tiktok",
            "tiktokVerifiedAt",
        ]
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
