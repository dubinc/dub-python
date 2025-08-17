<!-- Start SDK Example Usage [usage] -->
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

The same SDK client can also be used to make asynchronous requests by importing asyncio.
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

The same SDK client can also be used to make asynchronous requests by importing asyncio.
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