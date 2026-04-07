# Mode

The mode to use for tracking the lead event. `async` will not block the request; `wait` will block the request until the lead event is fully recorded in Dub; `deferred` will defer the lead event creation to a subsequent request.

## Example Usage

```python
from dub.models.operations import Mode

value = Mode.ASYNC
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `ASYNC`    | async      |
| `WAIT`     | wait       |
| `DEFERRED` | deferred   |