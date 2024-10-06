# AnalyticsTriggers


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `trigger`                                                    | [components.Trigger](../../models/components/trigger.md)     | :heavy_check_mark:                                           | The type of trigger method: link click or QR scan            |
| `clicks`                                                     | *Optional[float]*                                            | :heavy_minus_sign:                                           | The number of clicks from this trigger method                |
| `leads`                                                      | *Optional[float]*                                            | :heavy_minus_sign:                                           | The number of leads from this trigger method                 |
| `sales`                                                      | *Optional[float]*                                            | :heavy_minus_sign:                                           | The number of sales from this trigger method                 |
| `sale_amount`                                                | *Optional[float]*                                            | :heavy_minus_sign:                                           | The total amount of sales from this trigger method, in cents |