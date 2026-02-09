# Bounties

## Overview

### Available Operations

* [list_submissions](#list_submissions) - List bounty submissions
* [approve_submission](#approve_submission) - Approve a bounty submission
* [reject_submission](#reject_submission) - Reject a bounty submission

## list_submissions

List all submissions for a specific bounty in your partner program.

### Example Usage

<!-- UsageSnippet language="python" operationID="listBountySubmissions" method="get" path="/bounties/{bountyId}/submissions" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.bounties.list_submissions(request={
        "bounty_id": "<id>",
        "page_size": 50,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ListBountySubmissionsRequest](../../models/operations/listbountysubmissionsrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |
| `retries`                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                   | :heavy_minus_sign:                                                                                 | Configuration to override the default retry behavior of the client.                                |

### Response

**[List[operations.ListBountySubmissionsResponseBody]](../../models/.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Unauthorized        | 401                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.NotFound            | 404                        | application/json           |
| errors.Conflict            | 409                        | application/json           |
| errors.InviteExpired       | 410                        | application/json           |
| errors.UnprocessableEntity | 422                        | application/json           |
| errors.RateLimitExceeded   | 429                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## approve_submission

Approve a bounty submission. Optionally specify a custom reward amount.

### Example Usage

<!-- UsageSnippet language="python" operationID="approveBountySubmission" method="post" path="/bounties/{bountyId}/submissions/{submissionId}/approve" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.bounties.approve_submission(request={
        "bounty_id": "<id>",
        "submission_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.ApproveBountySubmissionRequest](../../models/operations/approvebountysubmissionrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |
| `retries`                                                                                              | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                       | :heavy_minus_sign:                                                                                     | Configuration to override the default retry behavior of the client.                                    |

### Response

**[operations.ApproveBountySubmissionResponseBody](../../models/operations/approvebountysubmissionresponsebody.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Unauthorized        | 401                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.NotFound            | 404                        | application/json           |
| errors.Conflict            | 409                        | application/json           |
| errors.InviteExpired       | 410                        | application/json           |
| errors.UnprocessableEntity | 422                        | application/json           |
| errors.RateLimitExceeded   | 429                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |

## reject_submission

Reject a bounty submission with a specified reason and optional note.

### Example Usage

<!-- UsageSnippet language="python" operationID="rejectBountySubmission" method="post" path="/bounties/{bountyId}/submissions/{submissionId}/reject" -->
```python
from dub import Dub


with Dub(
    token="DUB_API_KEY",
) as d_client:

    res = d_client.bounties.reject_submission(request={
        "bounty_id": "<id>",
        "submission_id": "<id>",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RejectBountySubmissionRequest](../../models/operations/rejectbountysubmissionrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |
| `retries`                                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                     | :heavy_minus_sign:                                                                                   | Configuration to override the default retry behavior of the client.                                  |

### Response

**[operations.RejectBountySubmissionResponseBody](../../models/operations/rejectbountysubmissionresponsebody.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.BadRequest          | 400                        | application/json           |
| errors.Unauthorized        | 401                        | application/json           |
| errors.Forbidden           | 403                        | application/json           |
| errors.NotFound            | 404                        | application/json           |
| errors.Conflict            | 409                        | application/json           |
| errors.InviteExpired       | 410                        | application/json           |
| errors.UnprocessableEntity | 422                        | application/json           |
| errors.RateLimitExceeded   | 429                        | application/json           |
| errors.InternalServerError | 500                        | application/json           |
| errors.SDKError            | 4XX, 5XX                   | \*/\*                      |