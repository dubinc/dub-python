# ReapplicationTimeframe

The mode for reapplying for the program. `instant`: The partner can reapply immediately. `standard`: The partner can reapply after 30 days. `never`: The partner can never reapply for the program. Defaults to `standard` if undefined.

## Example Usage

```python
from dub.models.operations import ReapplicationTimeframe

value = ReapplicationTimeframe.INSTANT
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `INSTANT`  | instant    |
| `STANDARD` | standard   |
| `NEVER`    | never      |