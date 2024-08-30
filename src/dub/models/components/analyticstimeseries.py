"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
import pydantic
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class AnalyticsTimeseriesTypedDict(TypedDict):
    start: str
    r"""The starting timestamp of the interval"""
    clicks: NotRequired[float]
    r"""The number of clicks in the interval"""
    leads: NotRequired[float]
    r"""The number of leads in the interval"""
    sales: NotRequired[float]
    r"""The number of sales in the interval"""
    sale_amount: NotRequired[float]
    r"""The total amount of sales in the interval"""
    

class AnalyticsTimeseries(BaseModel):
    start: str
    r"""The starting timestamp of the interval"""
    clicks: Optional[float] = 0
    r"""The number of clicks in the interval"""
    leads: Optional[float] = 0
    r"""The number of leads in the interval"""
    sales: Optional[float] = 0
    r"""The number of sales in the interval"""
    sale_amount: Annotated[Optional[float], pydantic.Field(alias="saleAmount")] = 0
    r"""The total amount of sales in the interval"""
    