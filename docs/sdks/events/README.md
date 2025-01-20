# Events
(*events*)

## Overview

### Available Operations

* [list](#list) - Retrieve a list of events

## list

Retrieve a paginated list of events for the authenticated workspace.

### Example Usage

```python
from dub import Dub
from dub.models import operations

with Dub(
    token="DUB_API_KEY",
) as dub:

    res = dub.events.list(request={
        "event": operations.QueryParamEvent.CLICKS,
        "interval": operations.QueryParamInterval.TWENTY_FOURH,
        "timezone": "America/New_York",
        "city": "New York",
        "device": "Desktop",
        "browser": "Chrome",
        "os": "Windows",
        "referer": "google.com",
        "referer_url": "https://dub.co/blog",
        "page": 1,
        "limit": 100,
        "sort_order": operations.QueryParamSortOrder.DESC,
        "sort_by": operations.QueryParamSortBy.TIMESTAMP,
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.ListEventsRequest](../../models/operations/listeventsrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `retries`                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)             | :heavy_minus_sign:                                                           | Configuration to override the default retry behavior of the client.          |

### Response

**[operations.ListEventsResponseBody](../../models/operations/listeventsresponsebody.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
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
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |