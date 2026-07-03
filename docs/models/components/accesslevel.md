# AccessLevel

The workspace-level access level settings for the folder. Default is `write` which allows full access to the folder for all team members. The other options are `read` (view-only access) and `null` (no access) and are only available on Business plans and above.

## Example Usage

```python
from dub.models.components import AccessLevel

value = AccessLevel.WRITE
```


## Values

| Name    | Value   |
| ------- | ------- |
| `WRITE` | write   |
| `READ`  | read    |