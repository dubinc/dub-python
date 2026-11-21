# IdentityVerificationStatus

The partner's identity verification status. Null means not yet initiated.

## Example Usage

```python
from dub.models.components import IdentityVerificationStatus

value = IdentityVerificationStatus.STARTED
```


## Values

| Name                     | Value                    |
| ------------------------ | ------------------------ |
| `STARTED`                | started                  |
| `SUBMITTED`              | submitted                |
| `APPROVED`               | approved                 |
| `DECLINED`               | declined                 |
| `RESUBMISSION_REQUESTED` | resubmissionRequested    |
| `EXPIRED`                | expired                  |
| `ABANDONED`              | abandoned                |
| `REVIEW`                 | review                   |