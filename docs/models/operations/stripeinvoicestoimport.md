# StripeInvoicesToImport

Import paid Stripe invoices for the customer and create a commission for each. Pass `all` to import every unimported, paid invoice, or an array of Stripe invoice IDs to import only those invoices. Refunded invoices are not imported. When not provided, create a single manual sale event using `sale.amount`


## Supported Types

### `operations.StripeInvoicesToImport1`

```python
value: operations.StripeInvoicesToImport1 = /* values here */
```

### `List[str]`

```python
value: List[str] = /* values here */
```

