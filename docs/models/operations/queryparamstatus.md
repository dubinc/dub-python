# QueryParamStatus

Filter the list of commissions by their corresponding status.

## Example Usage

```python
from dub.models.operations import QueryParamStatus

value = QueryParamStatus.PENDING
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | pending     |
| `PROCESSED` | processed   |
| `PAID`      | paid        |
| `REFUNDED`  | refunded    |
| `DUPLICATE` | duplicate   |
| `FRAUD`     | fraud       |
| `CANCELED`  | canceled    |
| `HOLD`      | hold        |