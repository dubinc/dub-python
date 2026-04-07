# QueryParamInterval

The interval to retrieve analytics for. If undefined, defaults to 24h.

## Example Usage

```python
from dub.models.operations import QueryParamInterval

value = QueryParamInterval.TWENTY_FOURH
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `TWENTY_FOURH` | 24h            |
| `SEVEND`       | 7d             |
| `THIRTYD`      | 30d            |
| `NINETYD`      | 90d            |
| `ONEY`         | 1y             |
| `MTD`          | mtd            |
| `QTD`          | qtd            |
| `YTD`          | ytd            |
| `ALL`          | all            |