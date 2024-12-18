# Track
(*track*)

## Overview

### Available Operations

* [lead](#lead) - Track a lead
* [sale](#sale) - Track a sale
* [~~customer~~](#customer) - Track a customer :warning: **Deprecated**

## lead

Track a lead for a short link.

### Example Usage

```python
from dub import Dub

with Dub(
    token="DUB_API_KEY",
) as dub:

    res = dub.track.lead(request={
        "click_id": "<value>",
        "event_name": "Sign up",
        "customer_id": "<value>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.TrackLeadRequestBody](../../models/operations/trackleadrequestbody.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.TrackLeadResponseBody](../../models/operations/trackleadresponsebody.md)**

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

## sale

Track a sale for a short link.

### Example Usage

```python
from dub import Dub
from dub.models import operations

with Dub(
    token="DUB_API_KEY",
) as dub:

    res = dub.track.sale(request={
        "amount": 996500,
        "payment_processor": operations.PaymentProcessor.SHOPIFY,
        "customer_id": "<value>",
        "event_name": "Purchase",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.TrackSaleRequestBody](../../models/operations/tracksalerequestbody.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[operations.TrackSaleResponseBody](../../models/operations/tracksaleresponsebody.md)**

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

## ~~customer~~

Track a customer for an authenticated workspace.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

### Example Usage

```python
from dub import Dub

with Dub(
    token="DUB_API_KEY",
) as dub:

    res = dub.track.customer()

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.TrackCustomerRequestBody](../../models/operations/trackcustomerrequestbody.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.TrackCustomerResponseBody](../../models/operations/trackcustomerresponsebody.md)**

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