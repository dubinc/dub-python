# BulkUpdateLinksRequestBody


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `data`                                                               | [operations.Data](../../models/operations/data.md)                   | :heavy_check_mark:                                                   | N/A                                                                  |
| `link_ids`                                                           | List[*str*]                                                          | :heavy_minus_sign:                                                   | The IDs of the links to update. Takes precedence over `externalIds`. |
| `external_ids`                                                       | List[*str*]                                                          | :heavy_minus_sign:                                                   | The external IDs of the links to update as stored in your database.  |