<!-- Start SDK Example Usage [usage] -->
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
<!-- End SDK Example Usage [usage] -->