# QueryParamStatus

Filter applications by status. One of `pending`, `approved`, or `rejected`. Defaults to `pending`.

## Example Usage

```python
from dub.models.operations import QueryParamStatus

value = QueryParamStatus.PENDING
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `PENDING`  | pending    |
| `APPROVED` | approved   |
| `REJECTED` | rejected   |