# Partners

## Overview

### Available Operations

* [list](#list) - List all partners
* [create](#create) - Create or update a partner
* [retrieve_links](#retrieve_links) - Retrieve a partner's links.
* [create_link](#create_link) - Create a link for a partner
* [upsert_link](#upsert_link) - Upsert a link for a partner
* [list_network](#list_network) - List all partners in the network
* [analytics](#analytics) - Retrieve analytics for a partner
* [ban](#ban) - Ban a partner
* [deactivate](#deactivate) - Deactivate a partner
* [update_tags](#update_tags) - Update the tags of partners
* [update_group](#update_group) - Update the group of partners

## list

List all partners for a partner program.

### Example Usage

<!-- UsageSnippet language="python" operationID="listPartners" method="get" path="/partners" -->
```python
from dub import Dub
from dub.models import operations


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.list(request={
        "group_id": "grp_123",
        "status": operations.ListPartnersQueryParamStatus.APPROVED,
        "country": "US",
        "email": "panic@thedis.co",
        "tenant_id": "1K0NM7HCN944PEMZ3CQPH43H8",
        "search": "john",
        "page": 1,
        "page_size": 50,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListPartnersRequest](../../models/operations/listpartnersrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |

### Response

**[List[operations.ListPartnersResponseBody]](../../models/.md)**

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

## create

Creates a partner and enrolls them in the program. If that email is already enrolled, the enrollment is returned unchanged, except a different `tenantId` replaces the current one when it is not already associated with another partner in the program.

### Example Usage

<!-- UsageSnippet language="python" operationID="createPartner" method="post" path="/partners" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.create(request={
        "email": "Summer50@yahoo.com",
        "link_props": {
            "external_id": "123456",
            "tag_ids": [
                "clux0rgak00011...",
            ],
            "test_variants": [
                {
                    "url": "https://example.com/variant-1",
                    "percentage": 50.0,
                },
                {
                    "url": "https://example.com/variant-2",
                    "percentage": 50.0,
                },
            ],
        },
    })

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

## retrieve_links

Retrieve a partner's links by their partner ID or tenant ID.

### Example Usage

<!-- UsageSnippet language="python" operationID="retrievePartnerLinks" method="get" path="/partners/links" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.retrieve_links(request={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RetrievePartnerLinksRequest](../../models/operations/retrievepartnerlinksrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |
| `retries`                                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                 | :heavy_minus_sign:                                                                               | Configuration to override the default retry behavior of the client.                              |

### Response

**[List[operations.RetrievePartnerLinksResponseBody]](../../models/.md)**

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

<!-- UsageSnippet language="python" operationID="createPartnerLink" method="post" path="/partners/links" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.create_link(request={
        "link_props": {
            "external_id": "123456",
            "tag_ids": [
                "clux0rgak00011...",
            ],
            "test_variants": [
                {
                    "url": "https://example.com/variant-1",
                    "percentage": 50.0,
                },
                {
                    "url": "https://example.com/variant-2",
                    "percentage": 50.0,
                },
            ],
        },
    })

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

## upsert_link

Upsert a link for a partner that is enrolled in your program. If a link with the same URL already exists, return it (or update it if there are any changes). Otherwise, a new link will be created.

### Example Usage

<!-- UsageSnippet language="python" operationID="upsertPartnerLink" method="put" path="/partners/links/upsert" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.upsert_link(request={
        "url": "https://bad-intent.org/",
        "link_props": {
            "external_id": "123456",
            "tag_ids": [
                "clux0rgak00011...",
            ],
            "test_variants": [
                {
                    "url": "https://example.com/variant-1",
                    "percentage": 50.0,
                },
                {
                    "url": "https://example.com/variant-2",
                    "percentage": 50.0,
                },
            ],
        },
    })

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

## list_network

List the partners in the Dub partner network for your program. The partner network must be enabled for the program.

### Example Usage

<!-- UsageSnippet language="python" operationID="listNetworkPartners" method="get" path="/partners/network" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.list_network(request={
        "page": 1,
        "page_size": 50,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.ListNetworkPartnersRequest](../../models/operations/listnetworkpartnersrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |
| `retries`                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                               | :heavy_minus_sign:                                                                             | Configuration to override the default retry behavior of the client.                            |

### Response

**[List[components.NetworkPartner]](../../models/.md)**

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

<!-- UsageSnippet language="python" operationID="retrievePartnerAnalytics" method="get" path="/partners/analytics" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.analytics(request={
        "timezone": "America/New_York",
        "query": "metadata['key']:'value'",
    })

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

## ban

Ban a partner from your program. This will disable all links and mark all commissions as canceled.

### Example Usage

<!-- UsageSnippet language="python" operationID="banPartner" method="post" path="/partners/ban" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.ban()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.BanPartnerRequestBody](../../models/operations/banpartnerrequestbody.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[operations.BanPartnerResponseBody](../../models/operations/banpartnerresponsebody.md)**

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

## deactivate

This will deactivate the partner from your program and disable all their active links. Their commissions and payouts will remain intact. You can reactivate them later if needed.

### Example Usage

<!-- UsageSnippet language="python" operationID="deactivatePartner" method="post" path="/partners/deactivate" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.deactivate()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.DeactivatePartnerRequestBody](../../models/operations/deactivatepartnerrequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.DeactivatePartnerResponseBody](../../models/operations/deactivatepartnerresponsebody.md)**

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

## update_tags

Add and remove partner tags on up to 100 partners enrolled in your program. Tags that a partner already has are not added again, and tags a partner does not have are skipped on removal. The call fails without changes if any partner is not enrolled in your program or any tag is not in your program.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePartnerTags" method="post" path="/partners/update-tags" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.update_tags(request={
        "partner_ids": [
            "pn_1JRQ9DY1X0PDS2G0WGZ7EYTXD",
        ],
        "add_tag_ids": [
            "ptag_1JRQ9DY1X0PDS2G0WGZ7EYTXD",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.UpdatePartnerTagsRequestBody](../../models/operations/updatepartnertagsrequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[operations.UpdatePartnerTagsResponseBody](../../models/operations/updatepartnertagsresponsebody.md)**

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

## update_group

Move up to 100 partners enrolled in your program into a group. They get the group's rewards and discount. Partners already in the group are skipped, unless `disableGroupMove` is set, in which case their setting is updated and they're counted. The call fails without changes if any partner is not enrolled in your program.

### Example Usage

<!-- UsageSnippet language="python" operationID="updatePartnersGroup" method="post" path="/partners/update-group" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.partners.update_group(request={
        "partner_ids": [
            "pn_1JRQ9DY1X0PDS2G0WGZ7EYTXD",
        ],
        "group_id": "grp_1JRQ9DY1X0PDS2G0WGZ7EYTXD",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.UpdatePartnersGroupRequestBody](../../models/operations/updatepartnersgrouprequestbody.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.UpdatePartnersGroupResponseBody](../../models/operations/updatepartnersgroupresponsebody.md)**

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