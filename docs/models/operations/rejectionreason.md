# RejectionReason

The reason for rejecting the submission.

## Example Usage

```python
from dub.models.operations import RejectionReason

value = RejectionReason.INVALID_PROOF
```


## Values

| Name                    | Value                   |
| ----------------------- | ----------------------- |
| `INVALID_PROOF`         | invalidProof            |
| `DUPLICATE_SUBMISSION`  | duplicateSubmission     |
| `OUT_OF_TIME_WINDOW`    | outOfTimeWindow         |
| `DID_NOT_MEET_CRITERIA` | didNotMeetCriteria      |
| `OTHER`                 | other                   |