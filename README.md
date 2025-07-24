<div align="center">
  <img src="https://github.com/dubinc/dub/assets/28986134/3815d859-afaa-48f9-a9b3-c09964e4d404" alt="Dub.co Python SDK to interact with APIs.">
  <h3>Dub.co Python SDK</h3>
  <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
  </a>
</div>

<br/>

Learn more about the Dub.co Python SDK in the [official documentation](https://dub.co/docs/sdks/python/overview).

<!-- Start Summary [summary] -->
## Summary

Dub API: Dub is link management infrastructure for companies to create marketing campaigns, link sharing features, and referral programs.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
  * [SDK Installation](#sdk-installation)
  * [SDK Example Usage](#sdk-example-usage)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Authentication](#authentication)
  * [Retries](#retries)
  * [Pagination](#pagination)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
  * [IDE Support](#ide-support)
* [Development](#development)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install dub
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add dub
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from dub python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "dub",
# ]
# ///

from dub import Dub

sdk = Dub(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example 1

```python
# Synchronous Example
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.links.create(request={
        "url": "https://google.com",
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
    })

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from dub import Dub

async def main():

    async with Dub(
        token="DUB_API_KEY",
    ) as d_client:

        res = await d_client.links.create_async(request={
            "url": "https://google.com",
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
        })

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```

### Example 2

```python
# Synchronous Example
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.links.upsert(request={
        "url": "https://google.com",
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
    })

    assert res is not None

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from dub import Dub

async def main():

    async with Dub(
        token="DUB_API_KEY",
    ) as d_client:

        res = await d_client.links.upsert_async(request={
            "url": "https://google.com",
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
        })

        assert res is not None

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [analytics](docs/sdks/analytics/README.md)

* [retrieve](docs/sdks/analytics/README.md#retrieve) - Retrieve analytics for a link, a domain, or the authenticated workspace.

### [commissions](docs/sdks/commissions/README.md)

* [list](docs/sdks/commissions/README.md#list) - Get commissions for a program.
* [update](docs/sdks/commissions/README.md#update) - Update a commission.

### [customers](docs/sdks/customers/README.md)

* [list](docs/sdks/customers/README.md#list) - Retrieve a list of customers
* [~~create~~](docs/sdks/customers/README.md#create) - Create a customer :warning: **Deprecated**
* [get](docs/sdks/customers/README.md#get) - Retrieve a customer
* [update](docs/sdks/customers/README.md#update) - Update a customer
* [delete](docs/sdks/customers/README.md#delete) - Delete a customer

### [domains](docs/sdks/domains/README.md)

* [create](docs/sdks/domains/README.md#create) - Create a domain
* [list](docs/sdks/domains/README.md#list) - Retrieve a list of domains
* [update](docs/sdks/domains/README.md#update) - Update a domain
* [delete](docs/sdks/domains/README.md#delete) - Delete a domain
* [register](docs/sdks/domains/README.md#register) - Register a domain
* [check_status](docs/sdks/domains/README.md#check_status) - Check the availability of one or more domains


### [embed_tokens](docs/sdks/embedtokens/README.md)

* [referrals](docs/sdks/embedtokens/README.md#referrals) - Create a referrals embed token

### [events](docs/sdks/events/README.md)

* [list](docs/sdks/events/README.md#list) - Retrieve a list of events

### [folders](docs/sdks/folders/README.md)

* [create](docs/sdks/folders/README.md#create) - Create a folder
* [list](docs/sdks/folders/README.md#list) - Retrieve a list of folders
* [update](docs/sdks/folders/README.md#update) - Update a folder
* [delete](docs/sdks/folders/README.md#delete) - Delete a folder

### [links](docs/sdks/links/README.md)

* [create](docs/sdks/links/README.md#create) - Create a link
* [list](docs/sdks/links/README.md#list) - Retrieve a list of links
* [count](docs/sdks/links/README.md#count) - Retrieve links count
* [get](docs/sdks/links/README.md#get) - Retrieve a link
* [update](docs/sdks/links/README.md#update) - Update a link
* [delete](docs/sdks/links/README.md#delete) - Delete a link
* [create_many](docs/sdks/links/README.md#create_many) - Bulk create links
* [update_many](docs/sdks/links/README.md#update_many) - Bulk update links
* [delete_many](docs/sdks/links/README.md#delete_many) - Bulk delete links
* [upsert](docs/sdks/links/README.md#upsert) - Upsert a link

### [partners](docs/sdks/partners/README.md)

* [create](docs/sdks/partners/README.md#create) - Create a partner
* [list](docs/sdks/partners/README.md#list) - List all partners
* [create_link](docs/sdks/partners/README.md#create_link) - Create a link for a partner
* [retrieve_links](docs/sdks/partners/README.md#retrieve_links) - Retrieve a partner's links.
* [upsert_link](docs/sdks/partners/README.md#upsert_link) - Upsert a link for a partner
* [analytics](docs/sdks/partners/README.md#analytics) - Retrieve analytics for a partner

### [qr_codes](docs/sdks/qrcodes/README.md)

* [get](docs/sdks/qrcodes/README.md#get) - Retrieve a QR code

### [tags](docs/sdks/tags/README.md)

* [create](docs/sdks/tags/README.md#create) - Create a tag
* [list](docs/sdks/tags/README.md#list) - Retrieve a list of tags
* [update](docs/sdks/tags/README.md#update) - Update a tag
* [delete](docs/sdks/tags/README.md#delete) - Delete a tag

### [track](docs/sdks/track/README.md)

* [lead](docs/sdks/track/README.md#lead) - Track a lead
* [sale](docs/sdks/track/README.md#sale) - Track a sale

### [workspaces](docs/sdks/workspaces/README.md)

* [get](docs/sdks/workspaces/README.md#get) - Retrieve a workspace
* [update](docs/sdks/workspaces/README.md#update) - Update a workspace

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`DubError`](./src/dub/models/errors/duberror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
from dub import Dub
from dub.models import errors


with Dub(
    token="DUB_API_KEY",
) as d_client:
    res = None
    try:

        res = d_client.links.create(request={
            "url": "https://google.com",
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
        })

        assert res is not None

        # Handle response
        print(res)


    except errors.DubError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.BadRequest):
            print(e.data.error)  # errors.Error
```

### Error Classes
**Primary errors:**
* [`DubError`](./src/dub/models/errors/duberror.py): The base class for HTTP error responses.
  * [`BadRequest`](./src/dub/models/errors/badrequest.py): The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). Status code `400`.
  * [`Unauthorized`](./src/dub/models/errors/unauthorized.py): Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response. Status code `401`.
  * [`Forbidden`](./src/dub/models/errors/forbidden.py): The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server. Status code `403`.
  * [`NotFound`](./src/dub/models/errors/notfound.py): The server cannot find the requested resource. Status code `404`.
  * [`Conflict`](./src/dub/models/errors/conflict.py): This response is sent when a request conflicts with the current state of the server. Status code `409`.
  * [`InviteExpired`](./src/dub/models/errors/inviteexpired.py): This response is sent when the requested content has been permanently deleted from server, with no forwarding address. Status code `410`.
  * [`UnprocessableEntity`](./src/dub/models/errors/unprocessableentity.py): The request was well-formed but was unable to be followed due to semantic errors. Status code `422`.
  * [`RateLimitExceeded`](./src/dub/models/errors/ratelimitexceeded.py): The user has sent too many requests in a given amount of time ("rate limiting"). Status code `429`.
  * [`InternalServerError`](./src/dub/models/errors/internalservererror.py): The server has encountered a situation it does not know how to handle. Status code `500`.

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`DubError`](./src/dub/models/errors/duberror.py)**:
* [`ResponseValidationError`](./src/dub/models/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from dub import Dub


with Dub(
    server_url="https://api.dub.co",
    token="DUB_API_KEY",
) as d_client:

    res = d_client.links.create(request={
        "url": "https://google.com",
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
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from dub import Dub
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Dub(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from dub import Dub
from dub.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Dub(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name    | Type | Scheme      |
| ------- | ---- | ----------- |
| `token` | http | HTTP Bearer |

To authenticate with the API the `token` parameter must be set when initializing the SDK client instance. For example:
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.links.create(request={
        "url": "https://google.com",
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
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from dub import Dub
from dub.utils import BackoffStrategy, RetryConfig


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.links.create(request={
        "url": "https://google.com",
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
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    assert res is not None

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from dub import Dub
from dub.utils import BackoffStrategy, RetryConfig


with Dub(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    token="DUB_API_KEY",
) as d_client:

    res = d_client.links.create(request={
        "url": "https://google.com",
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
    })

    assert res is not None

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Pagination [pagination] -->
## Pagination

Some of the endpoints in this SDK support pagination. To use pagination, you make your SDK calls as usual, but the
returned response object will have a `Next` method that can be called to pull down the next group of results. If the
return value of `Next` is `None`, then there are no more pages to be fetched.

Here's an example of one such pagination call:
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.links.list(request={
        "page_size": 50,
    })

    while res is not None:
        # Handle items

        res = res.next()

```
<!-- End Pagination [pagination] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Dub` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from dub import Dub
def main():

    with Dub(
        token="DUB_API_KEY",
    ) as d_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Dub(
        token="DUB_API_KEY",
    ) as d_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from dub import Dub
import logging

logging.basicConfig(level=logging.DEBUG)
s = Dub(debug_logger=logging.getLogger("dub"))
```
<!-- End Debugging [debug] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
