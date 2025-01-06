# GetCustomerRequest


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `id`                                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | The unique identifier of the customer in Dub.                                       |
| `include_expanded_fields`                                                           | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | Whether to include expanded fields on the customer (`link`, `partner`, `discount`). |