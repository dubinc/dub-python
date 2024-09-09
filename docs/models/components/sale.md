# Sale


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `amount`                                                                   | *int*                                                                      | :heavy_check_mark:                                                         | The amount of the sale. Should be passed in cents.                         |
| `payment_processor`                                                        | [components.PaymentProcessor](../../models/components/paymentprocessor.md) | :heavy_check_mark:                                                         | The payment processor via which the sale was made.                         |
| `invoice_id`                                                               | *OptionalNullable[str]*                                                    | :heavy_minus_sign:                                                         | The invoice ID of the sale.                                                |