# AnalyticsTimeseries


## Fields

| Field                                               | Type                                                | Required                                            | Description                                         |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| `start`                                             | *str*                                               | :heavy_check_mark:                                  | The starting timestamp of the interval              |
| `clicks`                                            | *Optional[float]*                                   | :heavy_minus_sign:                                  | The number of clicks in the interval                |
| `leads`                                             | *Optional[float]*                                   | :heavy_minus_sign:                                  | The number of leads in the interval                 |
| `sales`                                             | *Optional[float]*                                   | :heavy_minus_sign:                                  | The number of sales in the interval                 |
| `sale_amount`                                       | *Optional[float]*                                   | :heavy_minus_sign:                                  | The total amount of sales in the interval, in cents |