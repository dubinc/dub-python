# AnalyticsRefererUrls


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `referer_url`                                                     | *str*                                                             | :heavy_check_mark:                                                | The full URL of the referer. If unknown, this will be `(direct)`  |
| `clicks`                                                          | *Optional[float]*                                                 | :heavy_minus_sign:                                                | The number of clicks from this referer to this URL                |
| `leads`                                                           | *Optional[float]*                                                 | :heavy_minus_sign:                                                | The number of leads from this referer to this URL                 |
| `sales`                                                           | *Optional[float]*                                                 | :heavy_minus_sign:                                                | The number of sales from this referer to this URL                 |
| `sale_amount`                                                     | *Optional[float]*                                                 | :heavy_minus_sign:                                                | The total amount of sales from this referer to this URL, in cents |