# LinkErrorSchema


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `link`                                             | *Optional[Any]*                                    | :heavy_minus_sign:                                 | The link that caused the error.                    |
| `error`                                            | *str*                                              | :heavy_check_mark:                                 | The error message.                                 |
| `code`                                             | [components.Code](../../models/components/code.md) | :heavy_check_mark:                                 | The error code.                                    |