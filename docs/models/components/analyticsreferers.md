# AnalyticsReferers


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `referer`                                                    | *str*                                                        | :heavy_check_mark:                                           | The name of the referer. If unknown, this will be `(direct)` |
| `clicks`                                                     | *Optional[float]*                                            | :heavy_minus_sign:                                           | The number of clicks from this referer                       |
| `leads`                                                      | *Optional[float]*                                            | :heavy_minus_sign:                                           | The number of leads from this referer                        |
| `sales`                                                      | *Optional[float]*                                            | :heavy_minus_sign:                                           | The number of sales from this referer                        |
| `sale_amount`                                                | *Optional[float]*                                            | :heavy_minus_sign:                                           | The total amount of sales from this referer, in cents        |