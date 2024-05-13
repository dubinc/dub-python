# ForbiddenError


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `code`                                                              | [errors.ForbiddenCode](../../models/errors/forbiddencode.md)        | :heavy_check_mark:                                                  | A short code indicating the error code returned.                    | forbidden                                                           |
| `message`                                                           | *str*                                                               | :heavy_check_mark:                                                  | A human readable explanation of what went wrong.                    | The requested resource was not found.                               |
| `doc_url`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A link to our documentation with more details about this error code | https://dub.co/docs/api-reference/errors#forbidden                  |