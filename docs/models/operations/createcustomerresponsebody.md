# CreateCustomerResponseBody

The customer was created.


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `id`                                                    | *str*                                                   | :heavy_check_mark:                                      | The unique identifier of the customer in Dub.           |
| `external_id`                                           | *str*                                                   | :heavy_check_mark:                                      | Unique identifier for the customer in the client's app. |
| `name`                                                  | *str*                                                   | :heavy_check_mark:                                      | Name of the customer.                                   |
| `created_at`                                            | *str*                                                   | :heavy_check_mark:                                      | The date the customer was created.                      |
| `email`                                                 | *OptionalNullable[str]*                                 | :heavy_minus_sign:                                      | Email of the customer.                                  |
| `avatar`                                                | *OptionalNullable[str]*                                 | :heavy_minus_sign:                                      | Avatar URL of the customer.                             |