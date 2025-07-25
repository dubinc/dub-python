# Partner


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `id`                                                              | *str*                                                             | :heavy_check_mark:                                                | The partner's unique ID on Dub.                                   |
| `name`                                                            | *str*                                                             | :heavy_check_mark:                                                | The partner's full legal name.                                    |
| `email`                                                           | *Nullable[str]*                                                   | :heavy_check_mark:                                                | The partner's email address. Should be a unique value across Dub. |
| `image`                                                           | *Nullable[str]*                                                   | :heavy_check_mark:                                                | The partner's avatar image.                                       |
| `payouts_enabled_at`                                              | *Nullable[str]*                                                   | :heavy_check_mark:                                                | The date when the partner enabled payouts.                        |
| `country`                                                         | *Nullable[str]*                                                   | :heavy_check_mark:                                                | The partner's country (required for tax purposes).                |