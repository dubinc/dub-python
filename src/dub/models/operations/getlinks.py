"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.models.components import linkschema as components_linkschema
from dub.types import BaseModel
from dub.utils import FieldMetadata, QueryParamMetadata
from enum import Enum
import pydantic
from typing import Callable, List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


QueryParamTagIdsTypedDict = TypeAliasType(
    "QueryParamTagIdsTypedDict", Union[str, List[str]]
)
r"""The tag IDs to filter the links by."""


QueryParamTagIds = TypeAliasType("QueryParamTagIds", Union[str, List[str]])
r"""The tag IDs to filter the links by."""


QueryParamTagNamesTypedDict = TypeAliasType(
    "QueryParamTagNamesTypedDict", Union[str, List[str]]
)
r"""The unique name of the tags assigned to the short link (case insensitive)."""


QueryParamTagNames = TypeAliasType("QueryParamTagNames", Union[str, List[str]])
r"""The unique name of the tags assigned to the short link (case insensitive)."""


class Sort(str, Enum):
    r"""The field to sort the links by. The default is `createdAt`, and sort order is always descending."""

    CREATED_AT = "createdAt"
    CLICKS = "clicks"
    LAST_CLICKED = "lastClicked"


class GetLinksRequestTypedDict(TypedDict):
    domain: NotRequired[str]
    r"""The domain to filter the links by. E.g. `ac.me`. If not provided, all links for the workspace will be returned."""
    tag_id: NotRequired[str]
    r"""Deprecated. Use `tagIds` instead. The tag ID to filter the links by."""
    tag_ids: NotRequired[QueryParamTagIdsTypedDict]
    r"""The tag IDs to filter the links by."""
    tag_names: NotRequired[QueryParamTagNamesTypedDict]
    r"""The unique name of the tags assigned to the short link (case insensitive)."""
    search: NotRequired[str]
    r"""The search term to filter the links by. The search term will be matched against the short link slug and the destination url."""
    user_id: NotRequired[str]
    r"""The user ID to filter the links by."""
    show_archived: NotRequired[bool]
    r"""Whether to include archived links in the response. Defaults to `false` if not provided."""
    with_tags: NotRequired[bool]
    r"""DEPRECATED. Filter for links that have at least one tag assigned to them."""
    sort: NotRequired[Sort]
    r"""The field to sort the links by. The default is `createdAt`, and sort order is always descending."""
    page: NotRequired[float]
    r"""The page number for pagination."""
    page_size: NotRequired[float]
    r"""The number of items per page."""


class GetLinksRequest(BaseModel):
    domain: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The domain to filter the links by. E.g. `ac.me`. If not provided, all links for the workspace will be returned."""

    tag_id: Annotated[
        Optional[str],
        pydantic.Field(alias="tagId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Deprecated. Use `tagIds` instead. The tag ID to filter the links by."""

    tag_ids: Annotated[
        Optional[QueryParamTagIds],
        pydantic.Field(alias="tagIds"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The tag IDs to filter the links by."""

    tag_names: Annotated[
        Optional[QueryParamTagNames],
        pydantic.Field(alias="tagNames"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The unique name of the tags assigned to the short link (case insensitive)."""

    search: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The search term to filter the links by. The search term will be matched against the short link slug and the destination url."""

    user_id: Annotated[
        Optional[str],
        pydantic.Field(alias="userId"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""The user ID to filter the links by."""

    show_archived: Annotated[
        Optional[bool],
        pydantic.Field(alias="showArchived"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = True
    r"""Whether to include archived links in the response. Defaults to `false` if not provided."""

    with_tags: Annotated[
        Optional[bool],
        pydantic.Field(alias="withTags"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = True
    r"""DEPRECATED. Filter for links that have at least one tag assigned to them."""

    sort: Annotated[
        Optional[Sort],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = Sort.CREATED_AT
    r"""The field to sort the links by. The default is `createdAt`, and sort order is always descending."""

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


class GetLinksResponseTypedDict(TypedDict):
    result: List[components_linkschema.LinkSchemaTypedDict]


class GetLinksResponse(BaseModel):
    next: Callable[[], Optional[GetLinksResponse]]

    result: List[components_linkschema.LinkSchema]
