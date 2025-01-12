# LinkErrorSchema


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `error`                                            | *str*                                              | :heavy_check_mark:                                 | The error message.                                 |
| `code`                                             | [components.Code](../../models/components/code.md) | :heavy_check_mark:                                 | The error code.                                    |
| `link`                                             | *Optional[Any]*                                    | :heavy_minus_sign:                                 | The link that caused the error.                    |