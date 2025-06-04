# Partners
(*partners*)

## Overview

### Available Operations

* [create](#create) - Create a partner
* [create_link](#create_link) - Create a link for a partner
* [retrieve_links](#retrieve_links) - Retrieve a partner's links.
* [upsert_link](#upsert_link) - Upsert a link for a partner
* [analytics](#analytics) - Retrieve analytics for a partner

## create

Create a partner for a program. If partner exists, automatically enrolls them.

### Example Usage

```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.create(request={
        "program_id": "<id>",
        "name": "<value>",
        "email": "Summer50@yahoo.com",
        "link_props": {
            "external_id": "123456",
            "tag_ids": [
                "clux0rgak00011...",
            ],
            "test_variants": [
                {
                    "url": "https://example.com/variant-1",
                    "percentage": 50,
                },
                {
                    "url": "https://example.com/variant-2",
                    "percentage": 50,
                },
            ],
        },
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.CreatePartnerRequestBody](../../models/operations/createpartnerrequestbody.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |
| `retries`                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                           | :heavy_minus_sign:                                                                         | Configuration to override the default retry behavior of the client.                        |

### Response

**[operations.CreatePartnerResponseBody](../../models/operations/createpartnerresponsebody.md)**

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

## create_link

Create a link for a partner that is enrolled in your program.

### Example Usage

```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.create_link(request={
        "program_id": "<id>",
        "link_props": {
            "external_id": "123456",
            "tag_ids": [
                "clux0rgak00011...",
            ],
            "test_variants": [
                {
                    "url": "https://example.com/variant-1",
                    "percentage": 50,
                },
                {
                    "url": "https://example.com/variant-2",
                    "percentage": 50,
                },
            ],
        },
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreatePartnerLinkRequestBody](../../models/operations/createpartnerlinkrequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[components.LinkSchema](../../models/components/linkschema.md)**

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

## retrieve_links

Retrieve a partner's links by their partner ID or tenant ID.

### Example Usage

```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.retrieve_links(request={
        "program_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.RetrieveLinksRequest](../../models/operations/retrievelinksrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[List[operations.Link]](../../models/.md)**

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

## upsert_link

Upsert a link for a partner that is enrolled in your program. If a link with the same URL already exists, return it (or update it if there are any changes). Otherwise, a new link will be created.

### Example Usage

```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.upsert_link(request={
        "program_id": "<id>",
        "link_props": {
            "external_id": "123456",
            "tag_ids": [
                "clux0rgak00011...",
            ],
            "test_variants": [
                {
                    "url": "https://example.com/variant-1",
                    "percentage": 50,
                },
                {
                    "url": "https://example.com/variant-2",
                    "percentage": 50,
                },
            ],
        },
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpsertPartnerLinkRequestBody](../../models/operations/upsertpartnerlinkrequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[components.LinkSchema](../../models/components/linkschema.md)**

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

## analytics

Retrieve analytics for a partner within a program. The response type vary based on the `groupBy` query parameter.

### Example Usage

```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.analytics(request={
        "timezone": "America/New_York",
        "program_id": "<id>",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.RetrievePartnerAnalyticsRequest](../../models/operations/retrievepartneranalyticsrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |
| `retries`                                                                                                | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                         | :heavy_minus_sign:                                                                                       | Configuration to override the default retry behavior of the client.                                      |

### Response

**[operations.RetrievePartnerAnalyticsResponseBody](../../models/operations/retrievepartneranalyticsresponsebody.md)**

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