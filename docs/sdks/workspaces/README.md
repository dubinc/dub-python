# Workspaces
(*workspaces*)

### Available Operations

* [list](#list) - Retrieve a list of workspaces
* [create](#create) - Create a workspace
* [get](#get) - Retrieve a workspace

## list

Retrieve a list of workspaces for the authenticated user.

### Example Usage

```python
import dub

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)


res = s.workspaces.list()

if res.workspace_schemas is not None:
    # handle response
    pass

```


### Response

**[operations.GetWorkspacesResponse](../../models/operations/getworkspacesresponse.md)**
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

Create a new workspace for the authenticated user.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)


res = s.workspaces.create(request=operations.CreateWorkspaceRequestBody(
    name='<value>',
    slug='<value>',
))

if res.workspace_schema is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.CreateWorkspaceRequestBody](../../models/operations/createworkspacerequestbody.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.CreateWorkspaceResponse](../../models/operations/createworkspaceresponse.md)**
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

Retrieve a workspace for the authenticated user.

### Example Usage

```python
import dub

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)


res = s.workspaces.get(id_or_slug='<value>')

if res.workspace_schema is not None:
    # handle response
    pass

```

### Parameters

| Parameter                        | Type                             | Required                         | Description                      |
| -------------------------------- | -------------------------------- | -------------------------------- | -------------------------------- |
| `id_or_slug`                     | *str*                            | :heavy_check_mark:               | The ID or slug of the workspace. |


### Response

**[operations.GetWorkspaceResponse](../../models/operations/getworkspaceresponse.md)**
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
