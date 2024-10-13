# AnalyticsContinents


## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `continent`                                                                                       | [components.Continent](../../models/components/continent.md)                                      | :heavy_check_mark:                                                                                | The 2-letter ISO 3166-1 code representing the continent associated with the location of the user. |
| `clicks`                                                                                          | *Optional[float]*                                                                                 | :heavy_minus_sign:                                                                                | The number of clicks from this continent                                                          |
| `leads`                                                                                           | *Optional[float]*                                                                                 | :heavy_minus_sign:                                                                                | The number of leads from this continent                                                           |
| `sales`                                                                                           | *Optional[float]*                                                                                 | :heavy_minus_sign:                                                                                | The number of sales from this continent                                                           |
| `sale_amount`                                                                                     | *Optional[float]*                                                                                 | :heavy_minus_sign:                                                                                | The total amount of sales from this continent, in cents                                           |