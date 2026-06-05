# RequestBody1


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `type`                                                                   | [operations.RequestBodyType](../../models/operations/requestbodytype.md) | :heavy_check_mark:                                                       | N/A                                                                      |
| `partner_id`                                                             | *str*                                                                    | :heavy_check_mark:                                                       | The ID of the partner to create the commission for.                      |
| `amount`                                                                 | *float*                                                                  | :heavy_check_mark:                                                       | The commission amount in cents.                                          |
| `date_`                                                                  | *OptionalNullable[str]*                                                  | :heavy_minus_sign:                                                       | If not provided, the current date will be used.                          |
| `description`                                                            | *OptionalNullable[str]*                                                  | :heavy_minus_sign:                                                       | The description of the commission.                                       |