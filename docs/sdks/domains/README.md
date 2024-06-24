# Domains
(*domains*)

### Available Operations

* [list](#list) - Retrieve a list of domains
* [create](#create) - Create a domain
* [delete](#delete) - Delete a domain
* [update](#update) - Update a domain
* [set_primary](#set_primary) - Set a domain as primary
* [transfer](#transfer) - Transfer a domain

## list

Retrieve a list of domains associated with the authenticated workspace.

### Example Usage

```python
import dub

s = dub.Dub(
    token="DUB_API_KEY",
)


res = s.domains.list()

if res.domain_schemas is not None:
    # handle response
    pass

```


### Response

**[operations.ListDomainsResponse](../../models/operations/listdomainsresponse.md)**
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

Create a domain for the authenticated workspace.

### Example Usage

```python
import dub

s = dub.Dub(
    token="DUB_API_KEY",
)


res = s.domains.create(slug='acme.com', expired_url='https://acme.com/expired', archived=False, placeholder='https://dub.co/help/article/what-is-dub')

if res.domain_schema is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        | Example                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `slug`                                                                                                             | *str*                                                                                                              | :heavy_check_mark:                                                                                                 | Name of the domain.                                                                                                | acme.com                                                                                                           |
| `expired_url`                                                                                                      | *Optional[str]*                                                                                                    | :heavy_minus_sign:                                                                                                 | Redirect users to a specific URL when any link under this domain has expired.                                      | https://acme.com/expired                                                                                           |
| `archived`                                                                                                         | *Optional[bool]*                                                                                                   | :heavy_minus_sign:                                                                                                 | Whether to archive this domain. `false` will unarchive a previously archived domain.                               | false                                                                                                              |
| `placeholder`                                                                                                      | *Optional[str]*                                                                                                    | :heavy_minus_sign:                                                                                                 | Provide context to your teammates in the link creation modal by showing them an example of a link to be shortened. | https://dub.co/help/article/what-is-dub                                                                            |


### Response

**[operations.CreateDomainResponse](../../models/operations/createdomainresponse.md)**
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

Delete a domain from a workspace. It cannot be undone. This will also delete all the links associated with the domain.

### Example Usage

```python
import dub

s = dub.Dub(
    token="DUB_API_KEY",
)


res = s.domains.delete(slug='acme.com')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `slug`             | *str*              | :heavy_check_mark: | The domain name.   | acme.com           |


### Response

**[operations.DeleteDomainResponse](../../models/operations/deletedomainresponse.md)**
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

Update a domain for the authenticated workspace.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
)


res = s.domains.update(slug='acme.com', request_body=operations.UpdateDomainRequestBody(
    slug='acme.com',
    expired_url='https://acme.com/expired',
    archived=False,
    placeholder='https://dub.co/help/article/what-is-dub',
))

if res.domain_schema is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        | Example                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `slug`                                                                                             | *str*                                                                                              | :heavy_check_mark:                                                                                 | The domain name.                                                                                   | acme.com                                                                                           |
| `request_body`                                                                                     | [Optional[operations.UpdateDomainRequestBody]](../../models/operations/updatedomainrequestbody.md) | :heavy_minus_sign:                                                                                 | N/A                                                                                                |                                                                                                    |


### Response

**[operations.UpdateDomainResponse](../../models/operations/updatedomainresponse.md)**
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

## set_primary

Set a domain as primary for the authenticated workspace.

### Example Usage

```python
import dub

s = dub.Dub(
    token="DUB_API_KEY",
)


res = s.domains.set_primary(slug='acme.com')

if res.domain_schema is not None:
    # handle response
    pass

```

### Parameters

| Parameter          | Type               | Required           | Description        | Example            |
| ------------------ | ------------------ | ------------------ | ------------------ | ------------------ |
| `slug`             | *str*              | :heavy_check_mark: | The domain name.   | acme.com           |


### Response

**[operations.SetPrimaryDomainResponse](../../models/operations/setprimarydomainresponse.md)**
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

## transfer

Transfer a domain to another workspace within the authenticated account.

### Example Usage

```python
import dub
from dub.models import operations

s = dub.Dub(
    token="DUB_API_KEY",
)


res = s.domains.transfer(slug='acme.com', request_body=operations.TransferDomainRequestBody(
    new_workspace_id='<value>',
))

if res.domain_schema is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            | Example                                                                                                |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `slug`                                                                                                 | *str*                                                                                                  | :heavy_check_mark:                                                                                     | The domain name.                                                                                       | acme.com                                                                                               |
| `request_body`                                                                                         | [Optional[operations.TransferDomainRequestBody]](../../models/operations/transferdomainrequestbody.md) | :heavy_minus_sign:                                                                                     | N/A                                                                                                    |                                                                                                        |


### Response

**[operations.TransferDomainResponse](../../models/operations/transferdomainresponse.md)**
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
