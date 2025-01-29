# Metatags
(*metatags*)

## Overview

### Available Operations

* [get](#get) - Retrieve the metatags for a URL

## get

Retrieve the metatags for a URL.

### Example Usage

```python
from dub import Dub

with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.metatags.get(request={
        "url": "https://dub.co",
    })

    assert res is not None

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetMetatagsRequest](../../models/operations/getmetatagsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |
| `retries`                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)               | :heavy_minus_sign:                                                             | Configuration to override the default retry behavior of the client.            |

### Response

**[operations.GetMetatagsResponseBody](../../models/operations/getmetatagsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4XX, 5XX        | \*/\*           |