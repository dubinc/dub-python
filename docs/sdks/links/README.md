# Links
(*links*)

### Available Operations

* [list](#list) - Retrieve a list of links
* [create](#create) - Create a new link
* [count](#count) - Retrieve the number of links
* [get](#get) - Retrieve a link
* [delete](#delete) - Delete a link
* [update](#update) - Update a link
* [create_many](#create_many) - Bulk create links
* [upsert](#upsert) - Upsert a link

## list

Retrieve a list of links for the authenticated workspace. The list will be paginated and the provided query parameters allow filtering the returned links.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)


res = s.links.list(request=operations.GetLinksRequest())

if res.link_schemas is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetLinksRequest](../../models/operations/getlinksrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetLinksResponse](../../models/operations/getlinksresponse.md)**
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

## create

Create a new link for the authenticated workspace.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)


res = s.links.create(request=operations.CreateLinkRequestBody(
    url='https://google/com',
    external_id='123456',
    tag_ids=[
        'clux0rgak00011...',
    ],
))

if res.link_schema is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.CreateLinkRequestBody](../../models/operations/createlinkrequestbody.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.CreateLinkResponse](../../models/operations/createlinkresponse.md)**
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

## count

Retrieve the number of links for the authenticated workspace. The provided query parameters allow filtering the returned links.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)


res = s.links.count(request=operations.GetLinksCountRequest())

if res.number is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetLinksCountRequest](../../models/operations/getlinkscountrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetLinksCountResponse](../../models/operations/getlinkscountresponse.md)**
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

## get

Retrieve the info for a link.

### Example Usage

```python
import dub

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)


res = s.links.get(domain='<value>', key='<value>', link_id='clux0rgak00011...', external_id='ext_123456')

if res.link_schema is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     | Example                                                                                                         |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `domain`                                                                                                        | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |                                                                                                                 |
| `key`                                                                                                           | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | The key of the link to retrieve. E.g. for `d.to/github`, the key is `github`.                                   |                                                                                                                 |
| `link_id`                                                                                                       | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | The unique ID of the short link.                                                                                | clux0rgak00011...                                                                                               |
| `external_id`                                                                                                   | *Optional[str]*                                                                                                 | :heavy_minus_sign:                                                                                              | This is the ID of the link in the your database. Must be prefixed with `ext_` when passed as a query parameter. | ext_123456                                                                                                      |


### Response

**[operations.GetLinkInfoResponse](../../models/operations/getlinkinforesponse.md)**
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

## delete

Delete a link for the authenticated workspace.

### Example Usage

```python
import dub

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)


res = s.links.delete(link_id='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                             | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `link_id`                                                                                                                             | *str*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | The id of the link to delete. You may use either `linkId` (obtained via `/links/info` endpoint) or `externalId` prefixed with `ext_`. |


### Response

**[operations.DeleteLinkResponse](../../models/operations/deletelinkresponse.md)**
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

## update

Update a link for the authenticated workspace. If there's no change, returns it as it is.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)


res = s.links.update(link_id='<value>', request_body=operations.UpdateLinkRequestBody(
    url='https://google/com',
    external_id='123456',
    tag_ids=[
        'clux0rgak00011...',
    ],
))

if res.link_schema is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                             | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `link_id`                                                                                                                             | *str*                                                                                                                                 | :heavy_check_mark:                                                                                                                    | The id of the link to update. You may use either `linkId` (obtained via `/links/info` endpoint) or `externalId` prefixed with `ext_`. |
| `request_body`                                                                                                                        | [Optional[operations.UpdateLinkRequestBody]](../../models/operations/updatelinkrequestbody.md)                                        | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |


### Response

**[operations.UpdateLinkResponse](../../models/operations/updatelinkresponse.md)**
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

## create_many

Bulk create up to 100 links for the authenticated workspace.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)


res = s.links.create_many(request=[
    operations.RequestBody(
        url='https://google/com',
        external_id='123456',
        tag_ids=[
            'clux0rgak00011...',
        ],
    ),
])

if res.link_schemas is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                        | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `request`                                        | [List[operations.RequestBody]](../../models/.md) | :heavy_check_mark:                               | The request object to use for the request.       |


### Response

**[operations.BulkCreateLinksResponse](../../models/operations/bulkcreatelinksresponse.md)**
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

## upsert

Upsert a link for the authenticated workspace by its URL. If a link with the same URL already exists, return it (or update it if there are any changes). Otherwise, a new link will be created.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)


res = s.links.upsert(request=operations.UpsertLinkRequestBody(
    url='https://google/com',
    external_id='123456',
    tag_ids=[
        'clux0rgak00011...',
    ],
))

if res.link_schema is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpsertLinkRequestBody](../../models/operations/upsertlinkrequestbody.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.UpsertLinkResponse](../../models/operations/upsertlinkresponse.md)**
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
