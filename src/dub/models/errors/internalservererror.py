"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from dub import utils
from enum import Enum
from typing import Optional


class InternalServerErrorCode(str, Enum):
    r"""A short code indicating the error code returned."""
    INTERNAL_SERVER_ERROR = 'internal_server_error'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InternalServerErrorError:
    code: InternalServerErrorCode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code') }})
    r"""A short code indicating the error code returned."""
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    r"""A human readable explanation of what went wrong."""
    doc_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('doc_url'), 'exclude': lambda f: f is None }})
    r"""A link to our documentation with more details about this error code"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class InternalServerError(Exception):
    r"""The server has encountered a situation it does not know how to handle."""
    error: InternalServerErrorError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))