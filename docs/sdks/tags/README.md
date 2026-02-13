# Tags

## Overview

### Available Operations

* [list](#list) - Retrieve a list of tags
* [create](#create) - Create a tag
* [delete](#delete) - Delete a tag
* [update](#update) - Update a tag

## list

Retrieve a list of tags for the authenticated workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="getTags" method="get" path="/tags" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.tags.list(request={
        "page_size": 50,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetTagsRequest](../../models/operations/gettagsrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |
| `retries`                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)       | :heavy_minus_sign:                                                     | Configuration to override the default retry behavior of the client.    |

### Response

**[List[components.LinkTagSchemaOutput]](../../models/.md)**

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

Create a tag for the authenticated workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="createTag" method="post" path="/tags" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.tags.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateTagRequestBody](../../models/operations/createtagrequestbody.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |
| `retries`                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                   | :heavy_minus_sign:                                                                 | Configuration to override the default retry behavior of the client.                |

### Response

**[components.LinkTagSchemaOutput](../../models/components/linktagschemaoutput.md)**

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

## delete

Delete a tag from the workspace. All existing links will still work, but they will no longer be associated with this tag.

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteTag" method="delete" path="/tags/{id}" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.tags.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The ID of the tag to delete.                                        |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[operations.DeleteTagResponseBody](../../models/operations/deletetagresponsebody.md)**

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

## update

Update a tag in the workspace.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateTag" method="patch" path="/tags/{id}" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.tags.update(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `id`                                                                                         | *str*                                                                                        | :heavy_check_mark:                                                                           | The ID of the tag to update.                                                                 |
| `request_body`                                                                               | [Optional[operations.UpdateTagRequestBody]](../../models/operations/updatetagrequestbody.md) | :heavy_minus_sign:                                                                           | N/A                                                                                          |
| `retries`                                                                                    | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                             | :heavy_minus_sign:                                                                           | Configuration to override the default retry behavior of the client.                          |

### Response

**[components.LinkTagSchemaOutput](../../models/components/linktagschemaoutput.md)**

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