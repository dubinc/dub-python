# RejectionReason

The reason for rejecting the partner application. This will be shared with the partner via email.

## Example Usage

```python
from dub.models.operations import RejectionReason

value = RejectionReason.NEEDS_MORE_DETAIL
```


## Values

| Name                         | Value                        |
| ---------------------------- | ---------------------------- |
| `NEEDS_MORE_DETAIL`          | needsMoreDetail              |
| `DOES_NOT_MEET_REQUIREMENTS` | doesNotMeetRequirements      |
| `NOT_THE_RIGHT_FIT`          | notTheRightFit               |
| `OTHER`                      | other                        |