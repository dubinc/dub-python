# TrackSaleResponseBody

A sale was tracked.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `event_name`                                                                           | *str*                                                                                  | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `customer`                                                                             | [Nullable[operations.TrackSaleCustomer]](../../models/operations/tracksalecustomer.md) | :heavy_check_mark:                                                                     | N/A                                                                                    |
| `sale`                                                                                 | [Nullable[operations.TrackSaleSale]](../../models/operations/tracksalesale.md)         | :heavy_check_mark:                                                                     | N/A                                                                                    |