# CheckDomainStatusResponseBody


## Fields

| Field                                   | Type                                    | Required                                | Description                             |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `domain`                                | *str*                                   | :heavy_check_mark:                      | The domain name.                        |
| `available`                             | *bool*                                  | :heavy_check_mark:                      | Whether the domain is available.        |
| `price`                                 | *Nullable[str]*                         | :heavy_check_mark:                      | The price description.                  |
| `premium`                               | *Nullable[bool]*                        | :heavy_check_mark:                      | Whether the domain is a premium domain. |