# AnalyticsEventNames


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `event_name`                                             | *str*                                                    | :heavy_check_mark:                                       | The name of the conversion event (lead or sale)          |
| `clicks`                                                 | *Optional[float]*                                        | :heavy_minus_sign:                                       | The number of clicks from this event name                |
| `leads`                                                  | *Optional[float]*                                        | :heavy_minus_sign:                                       | The number of leads from this event name                 |
| `sales`                                                  | *Optional[float]*                                        | :heavy_minus_sign:                                       | The number of sales from this event name                 |
| `sale_amount`                                            | *Optional[float]*                                        | :heavy_minus_sign:                                       | The total amount of sales from this event name, in cents |