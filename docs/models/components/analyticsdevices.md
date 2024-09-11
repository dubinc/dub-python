# AnalyticsDevices


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `device`                                             | *str*                                                | :heavy_check_mark:                                   | The name of the device                               |
| `clicks`                                             | *Optional[float]*                                    | :heavy_minus_sign:                                   | The number of clicks from this device                |
| `leads`                                              | *Optional[float]*                                    | :heavy_minus_sign:                                   | The number of leads from this device                 |
| `sales`                                              | *Optional[float]*                                    | :heavy_minus_sign:                                   | The number of sales from this device                 |
| `sale_amount`                                        | *Optional[float]*                                    | :heavy_minus_sign:                                   | The total amount of sales from this device, in cents |