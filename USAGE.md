<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from dub import Dub

s = Dub(
    token="DUB_API_KEY",
)

res = s.links.create(request={
    "url": "https://google.com",
    "external_id": "123456",
    "tag_ids": "[\"clux0rgak00011...\"]",
})

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from dub import Dub

async def main():
    s = Dub(
        token="DUB_API_KEY",
    )
    res = await s.links.create_async(request={
        "url": "https://google.com",
        "external_id": "123456",
        "tag_ids": "[\"clux0rgak00011...\"]",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```

```python
# Synchronous Example
from dub import Dub

s = Dub(
    token="DUB_API_KEY",
)

res = s.links.upsert(request={
    "url": "https://google.com",
    "external_id": "123456",
    "tag_ids": [
        "clux0rgak00011...",
    ],
})

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from dub import Dub

async def main():
    s = Dub(
        token="DUB_API_KEY",
    )
    res = await s.links.upsert_async(request={
        "url": "https://google.com",
        "external_id": "123456",
        "tag_ids": "[\"clux0rgak00011...\"]",
    })
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->