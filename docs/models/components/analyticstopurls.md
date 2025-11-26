# AnalyticsTopUrls


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `url`                                                 | *str*                                                 | :heavy_check_mark:                                    | The full destination URL (including query parameters) |
| `clicks`                                              | *Optional[float]*                                     | :heavy_minus_sign:                                    | The number of clicks from this URL                    |
| `leads`                                               | *Optional[float]*                                     | :heavy_minus_sign:                                    | The number of leads from this URL                     |
| `sales`                                               | *Optional[float]*                                     | :heavy_minus_sign:                                    | The number of sales from this URL                     |
| `sale_amount`                                         | *Optional[float]*                                     | :heavy_minus_sign:                                    | The total amount of sales from this URL, in cents     |