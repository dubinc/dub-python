# EmbedTokens
(*embed_tokens*)

## Overview

### Available Operations

* [referrals](#referrals) - Create a referrals embed token

## referrals

Create a referrals embed token for the given partner/tenant.

### Example Usage

```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.embed_tokens.referrals(request={
        "program_id": "<id>",
        "partner": {
            "name": "<value>",
            "email": "Letha_Wuckert2@yahoo.com",
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
        },
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.CreateReferralsEmbedTokenRequestBody](../../models/operations/createreferralsembedtokenrequestbody.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |
| `retries`                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                   | :heavy_minus_sign:                                                                                                 | Configuration to override the default retry behavior of the client.                                                |

### Response

**[operations.CreateReferralsEmbedTokenResponseBody](../../models/operations/createreferralsembedtokenresponsebody.md)**

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