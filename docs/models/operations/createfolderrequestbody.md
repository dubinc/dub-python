# CreateFolderRequestBody


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `name`                                                                             | *str*                                                                              | :heavy_check_mark:                                                                 | The name of the folder.                                                            |
| `description`                                                                      | *OptionalNullable[str]*                                                            | :heavy_minus_sign:                                                                 | The description of the folder.                                                     |
| `access_level`                                                                     | [OptionalNullable[operations.AccessLevel]](../../models/operations/accesslevel.md) | :heavy_minus_sign:                                                                 | The access level of the folder within the workspace.                               |