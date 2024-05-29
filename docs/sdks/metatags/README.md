# Metatags
(*metatags*)

### Available Operations

* [get](#get) - Retrieve the metatags for a URL

## get

Retrieve the metatags for a URL.

### Example Usage

```python
import dub

s = dub.Dub(
    token="DUB_API_KEY",
    workspace_id='<value>',
)


res = s.metatags.get(url='https://dub.co')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                         | Type                              | Required                          | Description                       | Example                           |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `url`                             | *str*                             | :heavy_check_mark:                | The URL to retrieve metatags for. | https://dub.co                    |


### Response

**[operations.GetMetatagsResponse](../../models/operations/getmetatagsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4xx-5xx         | */*             |
