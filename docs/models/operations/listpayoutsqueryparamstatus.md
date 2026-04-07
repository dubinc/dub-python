# ListPayoutsQueryParamStatus

Filter the list of payouts by their corresponding status.

## Example Usage

```python
from dub.models.operations import ListPayoutsQueryParamStatus

value = ListPayoutsQueryParamStatus.PENDING
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `PENDING`    | pending      |
| `PROCESSING` | processing   |
| `PROCESSED`  | processed    |
| `SENT`       | sent         |
| `COMPLETED`  | completed    |
| `FAILED`     | failed       |
| `CANCELED`   | canceled     |