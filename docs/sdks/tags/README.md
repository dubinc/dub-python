# Tags
(*tags*)

### Available Operations

* [list](#list) - Retrieve a list of tags
* [create](#create) - Create a new tag

## list

Retrieve a list of tags for the authenticated workspace.

### Example Usage

```python
import dub

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)

res = s.tags.list()

if res.tag_schemas is not None:
    # handle response
    pass

```


### Response

**[operations.GetTagsResponse](../../models/operations/gettagsresponse.md)**
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

Create a new tag for the authenticated workspace.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)

res = s.tags.create(tag='<value>', color=operations.Color.BLUE)

if res.tag_schema is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `tag`                                                                                                                            | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | The name of the tag to create.                                                                                                   |
| `color`                                                                                                                          | [Optional[operations.Color]](../../models/operations/color.md)                                                                   | :heavy_minus_sign:                                                                                                               | The color of the tag. If not provided, a random color will be used from the list: red, yellow, green, blue, purple, pink, brown. |


### Response

**[operations.CreateTagResponse](../../models/operations/createtagresponse.md)**
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
