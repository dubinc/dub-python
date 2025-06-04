# RegisterDomainResponseBody

The domain was registered.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `domain`                                                                 | *str*                                                                    | :heavy_check_mark:                                                       | The domain name.                                                         |
| `status`                                                                 | *str*                                                                    | :heavy_check_mark:                                                       | The status of the domain registration.                                   |
| `expiration`                                                             | *Nullable[float]*                                                        | :heavy_check_mark:                                                       | The expiration timestamp of the domain (Unix timestamp in milliseconds). |