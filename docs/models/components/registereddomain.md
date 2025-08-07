# RegisteredDomain

The registered domain record.


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `id`                                        | *str*                                       | :heavy_check_mark:                          | The ID of the registered domain record.     |
| `auto_renewal_disabled_at`                  | *Nullable[str]*                             | :heavy_check_mark:                          | The date the domain auto-renew is disabled. |
| `created_at`                                | *str*                                       | :heavy_check_mark:                          | The date the domain was created.            |
| `expires_at`                                | *str*                                       | :heavy_check_mark:                          | The date the domain expires.                |
| `renewal_fee`                               | *float*                                     | :heavy_check_mark:                          | The fee to renew the domain.                |