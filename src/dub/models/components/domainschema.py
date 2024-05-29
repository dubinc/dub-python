"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from dub import utils
from enum import Enum
from typing import Optional


class Type(str, Enum):
    r"""The type of redirect to use for this domain."""
    REDIRECT = 'redirect'
    REWRITE = 'rewrite'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DomainSchema:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The unique identifier of the domain."""
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""The domain name."""
    expired_url: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expiredUrl') }})
    r"""The URL to redirect to when a link under this domain has expired."""
    target: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target') }})
    r"""The page your users will get redirected to when they visit your domain."""
    type: Type = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The type of redirect to use for this domain."""
    verified: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('verified'), 'exclude': lambda f: f is None }})
    r"""Whether the domain is verified."""
    primary: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primary'), 'exclude': lambda f: f is None }})
    r"""Whether the domain is the primary domain for the workspace."""
    archived: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('archived'), 'exclude': lambda f: f is None }})
    r"""Whether the domain is archived."""
    noindex: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('noindex'), 'exclude': lambda f: f is None }})
    r"""Prevent search engines from indexing the domain."""
    placeholder: Optional[str] = dataclasses.field(default='https://dub.co/help/article/what-is-dub', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('placeholder'), 'exclude': lambda f: f is None }})
    r"""Provide context to your teammates in the link creation modal by showing them an example of a link to be shortened."""
    clicks: Optional[float] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clicks'), 'exclude': lambda f: f is None }})
    r"""The number of clicks on the domain."""
    
