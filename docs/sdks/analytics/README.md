# Analytics
(*analytics*)

### Available Operations

* [~~timeseries~~](#timeseries) - Retrieve timeseries click analytics :warning: **Deprecated** Use `timeseries` instead.
* [~~country~~](#country) - Retrieve top countries by clicks :warning: **Deprecated** Use `countries` instead.
* [~~city~~](#city) - Retrieve top cities by clicks :warning: **Deprecated** Use `cities` instead.
* [~~device~~](#device) - Retrieve top devices by clicks :warning: **Deprecated** Use `devices` instead.
* [~~browser~~](#browser) - Retrieve top browsers by clicks :warning: **Deprecated** Use `browsers` instead.
* [~~os~~](#os) - Retrieve top OS by clicks :warning: **Deprecated** Use `os` instead.
* [~~referer~~](#referer) - Retrieve top referers by clicks :warning: **Deprecated** Use `referers` instead.
* [~~top_links~~](#top_links) - Retrieve top links by clicks :warning: **Deprecated** Use `top_links` instead.
* [~~top_urls~~](#top_urls) - Retrieve top URLs by clicks :warning: **Deprecated** Use `top_urls` instead.

## ~~timeseries~~

Retrieve timeseries click analytics for a link, a domain, or the authenticated workspace over a period of time.

> :warning: **DEPRECATED**: This method is deprecated. Use dub.analytics.clicks.timeseries instead.. Use `timeseries` instead.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)

res = s.analytics.timeseries(request=operations.GetTimeseriesByClicksDeprecatedRequest())

if res.response_bodies is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetTimeseriesByClicksDeprecatedRequest](../../models/operations/gettimeseriesbyclicksdeprecatedrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.GetTimeseriesByClicksDeprecatedResponse](../../models/operations/gettimeseriesbyclicksdeprecatedresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Unauthorized        | 401                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.NotFound            | 404                        | application/json           |
| errors.Conflict            | 409                        | application/json           |
| errors.InviteExpired       | 410                        | application/json           |
| errors.UnprocessableEntity | 422                        | application/json           |
| errors.RateLimitExceeded   | 429                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## ~~country~~

Retrieve the top countries by number of clicks for a link, a domain, or the authenticated workspace.

> :warning: **DEPRECATED**: This method is deprecated. Use dub.analytics.clicks.countries instead.. Use `countries` instead.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)

res = s.analytics.country(request=operations.GetCountriesByClicksDeprecatedRequest())

if res.clicks_by_countries is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetCountriesByClicksDeprecatedRequest](../../models/operations/getcountriesbyclicksdeprecatedrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetCountriesByClicksDeprecatedResponse](../../models/operations/getcountriesbyclicksdeprecatedresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Unauthorized        | 401                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.NotFound            | 404                        | application/json           |
| errors.Conflict            | 409                        | application/json           |
| errors.InviteExpired       | 410                        | application/json           |
| errors.UnprocessableEntity | 422                        | application/json           |
| errors.RateLimitExceeded   | 429                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## ~~city~~

Retrieve the top countries by number of clicks for a link, a domain, or the authenticated workspace.

> :warning: **DEPRECATED**: This method is deprecated. Use dub.analytics.clicks.cities instead.. Use `cities` instead.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)

res = s.analytics.city(request=operations.GetCitiesByClicksDeprecatedRequest())

if res.clicks_by_cities is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [operations.GetCitiesByClicksDeprecatedRequest](../../models/operations/getcitiesbyclicksdeprecatedrequest.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetCitiesByClicksDeprecatedResponse](../../models/operations/getcitiesbyclicksdeprecatedresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Unauthorized        | 401                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.NotFound            | 404                        | application/json           |
| errors.Conflict            | 409                        | application/json           |
| errors.InviteExpired       | 410                        | application/json           |
| errors.UnprocessableEntity | 422                        | application/json           |
| errors.RateLimitExceeded   | 429                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## ~~device~~

Retrieve the top devices by number of clicks for a link, a domain, or the authenticated workspace.

> :warning: **DEPRECATED**: This method is deprecated. Use dub.analytics.clicks.devices instead.. Use `devices` instead.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)

res = s.analytics.device(request=operations.GetDevicesByClicksDeprecatedRequest())

if res.response_bodies is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetDevicesByClicksDeprecatedRequest](../../models/operations/getdevicesbyclicksdeprecatedrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetDevicesByClicksDeprecatedResponse](../../models/operations/getdevicesbyclicksdeprecatedresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Unauthorized        | 401                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.NotFound            | 404                        | application/json           |
| errors.Conflict            | 409                        | application/json           |
| errors.InviteExpired       | 410                        | application/json           |
| errors.UnprocessableEntity | 422                        | application/json           |
| errors.RateLimitExceeded   | 429                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## ~~browser~~

Retrieve the top browsers by number of clicks for a link, a domain, or the authenticated workspace.

> :warning: **DEPRECATED**: This method is deprecated. Use dub.analytics.clicks.browsers instead.. Use `browsers` instead.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)

res = s.analytics.browser(request=operations.GetBrowsersByClicksDeprecatedRequest())

if res.response_bodies is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetBrowsersByClicksDeprecatedRequest](../../models/operations/getbrowsersbyclicksdeprecatedrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetBrowsersByClicksDeprecatedResponse](../../models/operations/getbrowsersbyclicksdeprecatedresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Unauthorized        | 401                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.NotFound            | 404                        | application/json           |
| errors.Conflict            | 409                        | application/json           |
| errors.InviteExpired       | 410                        | application/json           |
| errors.UnprocessableEntity | 422                        | application/json           |
| errors.RateLimitExceeded   | 429                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## ~~os~~

Retrieve the top OS by number of clicks for a link, a domain, or the authenticated workspace.

> :warning: **DEPRECATED**: This method is deprecated. Use dub.analytics.clicks.os instead.. Use `os` instead.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)

res = s.analytics.os(request=operations.GetOSByClicksDeprecatedRequest())

if res.response_bodies is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetOSByClicksDeprecatedRequest](../../models/operations/getosbyclicksdeprecatedrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetOSByClicksDeprecatedResponse](../../models/operations/getosbyclicksdeprecatedresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Unauthorized        | 401                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.NotFound            | 404                        | application/json           |
| errors.Conflict            | 409                        | application/json           |
| errors.InviteExpired       | 410                        | application/json           |
| errors.UnprocessableEntity | 422                        | application/json           |
| errors.RateLimitExceeded   | 429                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## ~~referer~~

Retrieve the top referers by number of clicks for a link, a domain, or the authenticated workspace.

> :warning: **DEPRECATED**: This method is deprecated. Use dub.analytics.clicks.referers instead.. Use `referers` instead.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)

res = s.analytics.referer(request=operations.GetReferersByClicksDeprecatedRequest())

if res.response_bodies is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetReferersByClicksDeprecatedRequest](../../models/operations/getreferersbyclicksdeprecatedrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetReferersByClicksDeprecatedResponse](../../models/operations/getreferersbyclicksdeprecatedresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Unauthorized        | 401                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.NotFound            | 404                        | application/json           |
| errors.Conflict            | 409                        | application/json           |
| errors.InviteExpired       | 410                        | application/json           |
| errors.UnprocessableEntity | 422                        | application/json           |
| errors.RateLimitExceeded   | 429                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## ~~top_links~~

Retrieve the top links by number of clicks for a domain or the authenticated workspace.

> :warning: **DEPRECATED**: This method is deprecated. Use dub.analytics.clicks.topLinks instead.. Use `top_links` instead.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)

res = s.analytics.top_links(request=operations.GetTopLinksByClicksDeprecatedRequest())

if res.response_bodies is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.GetTopLinksByClicksDeprecatedRequest](../../models/operations/gettoplinksbyclicksdeprecatedrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.GetTopLinksByClicksDeprecatedResponse](../../models/operations/gettoplinksbyclicksdeprecatedresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Unauthorized        | 401                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.NotFound            | 404                        | application/json           |
| errors.Conflict            | 409                        | application/json           |
| errors.InviteExpired       | 410                        | application/json           |
| errors.UnprocessableEntity | 422                        | application/json           |
| errors.RateLimitExceeded   | 429                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |

## ~~top_urls~~

Retrieve the top URLs by number of clicks for a given short link.

> :warning: **DEPRECATED**: This method is deprecated. Use dub.analytics.clicks.topUrls instead.. Use `top_urls` instead.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)

res = s.analytics.top_urls(request=operations.GetTopURLsByClicksDeprecatedRequest())

if res.response_bodies is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetTopURLsByClicksDeprecatedRequest](../../models/operations/gettopurlsbyclicksdeprecatedrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetTopURLsByClicksDeprecatedResponse](../../models/operations/gettopurlsbyclicksdeprecatedresponse.md)**
### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Unauthorized        | 401                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.NotFound            | 404                        | application/json           |
| errors.Conflict            | 409                        | application/json           |
| errors.InviteExpired       | 410                        | application/json           |
| errors.UnprocessableEntity | 422                        | application/json           |
| errors.RateLimitExceeded   | 429                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4xx-5xx                    | */*                        |
