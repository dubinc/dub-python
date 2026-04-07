# BulkUpdateCommissionsStatus

The status to apply to every commission in the batch.

## Example Usage

```python
from dub.models.operations import BulkUpdateCommissionsStatus

value = BulkUpdateCommissionsStatus.PENDING
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | pending     |
| `REFUNDED`  | refunded    |
| `DUPLICATE` | duplicate   |
| `CANCELED`  | canceled    |
| `FRAUD`     | fraud       |