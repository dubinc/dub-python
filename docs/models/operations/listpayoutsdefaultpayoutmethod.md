# ListPayoutsDefaultPayoutMethod

The partner's default payout method. Connect: Bank account payouts via Stripe Connect; Stablecoin: USDC payouts directly to a crypto wallet; PayPal: Payouts via PayPal

## Example Usage

```python
from dub.models.operations import ListPayoutsDefaultPayoutMethod

value = ListPayoutsDefaultPayoutMethod.CONNECT
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `CONNECT`    | connect      |
| `STABLECOIN` | stablecoin   |
| `PAYPAL`     | paypal       |