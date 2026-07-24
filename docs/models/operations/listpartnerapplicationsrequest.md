# ListPartnerApplicationsRequest


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  | Example                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `country`                                                    | *Optional[str]*                                              | :heavy_minus_sign:                                           | A filter on the list based on the partner's `country` field. | US                                                           |
| `group_id`                                                   | *Optional[str]*                                              | :heavy_minus_sign:                                           | A filter on the list based on the partner's `groupId` field. | grp_123                                                      |
| `page`                                                       | *Optional[int]*                                              | :heavy_minus_sign:                                           | The page number for pagination.                              | 1                                                            |
| `page_size`                                                  | *Optional[int]*                                              | :heavy_minus_sign:                                           | The number of items per page.                                | 50                                                           |