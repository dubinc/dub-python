# TrackSaleResponseBody

A sale was tracked.


## Fields

| Field               | Type                | Required            | Description         |
| ------------------- | ------------------- | ------------------- | ------------------- |
| `customer_id`       | *str*               | :heavy_check_mark:  | N/A                 |
| `amount`            | *float*             | :heavy_check_mark:  | N/A                 |
| `payment_processor` | *str*               | :heavy_check_mark:  | N/A                 |
| `invoice_id`        | *Optional[str]*     | :heavy_check_mark:  | N/A                 |
| `currency`          | *str*               | :heavy_check_mark:  | N/A                 |
| `metadata`          | Dict[str, *Any*]    | :heavy_check_mark:  | N/A                 |