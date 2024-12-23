"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.models.components import (
    clickevent as components_clickevent,
    continentcode as components_continentcode,
    countrycode as components_countrycode,
    leadevent as components_leadevent,
    saleevent as components_saleevent,
)
from dub.types import BaseModel
from dub.utils import FieldMetadata, QueryParamMetadata
from enum import Enum
import pydantic
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class QueryParamEvent(str, Enum):
    r"""The type of event to retrieve analytics for. Defaults to 'clicks'."""

    CLICKS = "clicks"
    LEADS = "leads"
    SALES = "sales"


class QueryParamInterval(str, Enum):
    r"""The interval to retrieve events for. Takes precedence over start and end. If undefined, defaults to 24h."""

    TWENTY_FOURH = "24h"
    SEVEND = "7d"
    THIRTYD = "30d"
    NINETYD = "90d"
    YTD = "ytd"
    ONEY = "1y"
    ALL = "all"


class QueryParamTrigger(str, Enum):
    r"""The trigger to retrieve analytics for. If undefined, return both QR and link clicks."""

    QR = "qr"
    LINK = "link"


ListEventsQueryParamTagIdsTypedDict = TypeAliasType(
    "ListEventsQueryParamTagIdsTypedDict", Union[str, List[str]]
)
r"""The tag IDs to retrieve analytics for."""


ListEventsQueryParamTagIds = TypeAliasType(
    "ListEventsQueryParamTagIds", Union[str, List[str]]
)
r"""The tag IDs to retrieve analytics for."""


class Order(str, Enum):
    ASC = "asc"
    DESC = "desc"


class SortBy(str, Enum):
    TIMESTAMP = "timestamp"


class ListEventsRequestTypedDict(TypedDict):
    event: NotRequired[QueryParamEvent]
    r"""The type of event to retrieve analytics for. Defaults to 'clicks'."""
    domain: NotRequired[str]
    r"""The domain to filter analytics for."""
    key: NotRequired[str]
    r"""The short link slug."""
    link_id: NotRequired[str]
    r"""The unique ID of the short link on Dub."""
    external_id: NotRequired[str]
    r"""This is the ID of the link in the your database. Must be prefixed with 'ext_' when passed as a query parameter."""
    interval: NotRequired[QueryParamInterval]
    r"""The interval to retrieve events for. Takes precedence over start and end. If undefined, defaults to 24h."""
    start: NotRequired[str]
    r"""The start date and time when to retrieve analytics from. Takes precedence over `interval`."""
    end: NotRequired[str]
    r"""The end date and time when to retrieve analytics from. If not provided, defaults to the current date. Takes precedence over `interval`."""
    timezone: NotRequired[str]
    r"""The IANA time zone code for aligning timeseries granularity (e.g. America/New_York). Defaults to UTC."""
    country: NotRequired[components_countrycode.CountryCode]
    r"""The country to retrieve analytics for."""
    city: NotRequired[str]
    r"""The city to retrieve analytics for."""
    region: NotRequired[str]
    r"""The ISO 3166-2 region code to retrieve analytics for."""
    continent: NotRequired[components_continentcode.ContinentCode]
    r"""The continent to retrieve analytics for."""
    device: NotRequired[str]
    r"""The device to retrieve analytics for."""
    browser: NotRequired[str]
    r"""The browser to retrieve analytics for."""
    os: NotRequired[str]
    r"""The OS to retrieve analytics for."""
    trigger: NotRequired[QueryParamTrigger]
    r"""The trigger to retrieve analytics for. If undefined, return both QR and link clicks."""
    referer: NotRequired[str]
    r"""The referer to retrieve analytics for."""
    referer_url: NotRequired[str]
    r"""The full referer URL to retrieve analytics for."""
    url: NotRequired[str]
    r"""The URL to retrieve analytics for."""
    tag_id: NotRequired[str]
    r"""Deprecated. Use `tagIds` instead. The tag ID to retrieve analytics for."""
    tag_ids: NotRequired[ListEventsQueryParamTagIdsTypedDict]
    r"""The tag IDs to retrieve analytics for."""
    qr: NotRequired[bool]
    r"""Deprecated. Use the `trigger` field instead. Filter for QR code scans. If true, filter for QR codes only. If false, filter for links only. If undefined, return both."""
    root: NotRequired[bool]
    r"""Filter for root domains. If true, filter for domains only. If false, filter for links only. If undefined, return both."""
    page: NotRequired[float]
    limit: NotRequired[float]
    order: NotRequired[Order]
    sort_by: NotRequired[SortBy]


class ListEventsRequest(BaseModel):
    event: Annotated[
        Optional[QueryParamEvent],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = QueryParamEvent.CLICKS
    r"""The type of event to retrieve analytics for. Defaults to 'clicks'."""

    domain: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The domain to filter analytics for."""

    key: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The short link slug."""

    link_id: Annotated[
        Optional[str],
        pydantic.Field(alias="linkId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The unique ID of the short link on Dub."""

    external_id: Annotated[
        Optional[str],
        pydantic.Field(alias="externalId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""This is the ID of the link in the your database. Must be prefixed with 'ext_' when passed as a query parameter."""

    interval: Annotated[
        Optional[QueryParamInterval],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = QueryParamInterval.TWENTY_FOURH
    r"""The interval to retrieve events for. Takes precedence over start and end. If undefined, defaults to 24h."""

    start: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The start date and time when to retrieve analytics from. Takes precedence over `interval`."""

    end: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The end date and time when to retrieve analytics from. If not provided, defaults to the current date. Takes precedence over `interval`."""

    timezone: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = "UTC"
    r"""The IANA time zone code for aligning timeseries granularity (e.g. America/New_York). Defaults to UTC."""

    country: Annotated[
        Optional[components_countrycode.CountryCode],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The country to retrieve analytics for."""

    city: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The city to retrieve analytics for."""

    region: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The ISO 3166-2 region code to retrieve analytics for."""

    continent: Annotated[
        Optional[components_continentcode.ContinentCode],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The continent to retrieve analytics for."""

    device: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The device to retrieve analytics for."""

    browser: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The browser to retrieve analytics for."""

    os: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The OS to retrieve analytics for."""

    trigger: Annotated[
        Optional[QueryParamTrigger],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The trigger to retrieve analytics for. If undefined, return both QR and link clicks."""

    referer: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The referer to retrieve analytics for."""

    referer_url: Annotated[
        Optional[str],
        pydantic.Field(alias="refererUrl"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The full referer URL to retrieve analytics for."""

    url: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The URL to retrieve analytics for."""

    tag_id: Annotated[
        Optional[str],
        pydantic.Field(alias="tagId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Deprecated. Use `tagIds` instead. The tag ID to retrieve analytics for."""

    tag_ids: Annotated[
        Optional[ListEventsQueryParamTagIds],
        pydantic.Field(alias="tagIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The tag IDs to retrieve analytics for."""

    qr: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Deprecated. Use the `trigger` field instead. Filter for QR code scans. If true, filter for QR codes only. If false, filter for links only. If undefined, return both."""

    root: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Filter for root domains. If true, filter for domains only. If false, filter for links only. If undefined, return both."""

    page: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 1

    limit: Annotated[
        Optional[float],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 100

    order: Annotated[
        Optional[Order],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = Order.DESC

    sort_by: Annotated[
        Optional[SortBy],
        pydantic.Field(alias="sortBy"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = SortBy.TIMESTAMP


ListEventsResponseBodyTypedDict = TypeAliasType(
    "ListEventsResponseBodyTypedDict",
    Union[
        List[components_clickevent.ClickEventTypedDict],
        List[components_leadevent.LeadEventTypedDict],
        List[components_saleevent.SaleEventTypedDict],
    ],
)
r"""A list of events"""


ListEventsResponseBody = TypeAliasType(
    "ListEventsResponseBody",
    Union[
        List[components_clickevent.ClickEvent],
        List[components_leadevent.LeadEvent],
        List[components_saleevent.SaleEvent],
    ],
)
r"""A list of events"""
