# QueryParamStatus

Filter the list of partners by their status for your program. `discover` returns the partners that are not in your program and that you have not ignored, ranked by relevance.

## Example Usage

```python
from dub.models.operations import QueryParamStatus

value = QueryParamStatus.DISCOVER
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `DISCOVER`  | discover    |
| `INVITED`   | invited     |
| `RECRUITED` | recruited   |
| `IGNORED`   | ignored     |