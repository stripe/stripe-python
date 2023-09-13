from inspect import signature
import stripe

methods = [
    (stripe.Account.retrieve_capability, 2),
    (stripe.Account.modify_capability, 2),
    (stripe.Account.list_capabilities, 1),
    (stripe.Account.create_external_account, 1),
    (stripe.Account.retrieve_external_account, 2),
    (stripe.Account.modify_external_account, 2),
    (stripe.Account.delete_external_account, 2),
    (stripe.Account.list_external_accounts, 1),
    (stripe.Account.create_login_link, 1),
    (stripe.Account.create_person, 1),
    (stripe.Account.retrieve_person, 2),
    (stripe.Account.modify_person, 2),
    (stripe.Account.delete_person, 2),
    (stripe.Account.list_persons, 1),
    (stripe.ApplicationFee.create_refund, 1),
    (stripe.ApplicationFee.retrieve_refund, 2),
    (stripe.ApplicationFee.modify_refund, 2),
    (stripe.ApplicationFee.list_refunds, 1),
    (stripe.CreditNote.list_lines, 1),
    (stripe.Customer.create_balance_transaction, 1),
    (stripe.Customer.retrieve_balance_transaction, 2),
    (stripe.Customer.modify_balance_transaction, 2),
    (stripe.Customer.list_balance_transactions, 1),
    (stripe.Customer.retrieve_cash_balance_transaction, 2),
    (stripe.Customer.list_cash_balance_transactions, 1),
    (stripe.Customer.create_source, 1),
    (stripe.Customer.retrieve_source, 2),
    (stripe.Customer.modify_source, 2),
    (stripe.Customer.delete_source, 2),
    (stripe.Customer.list_sources, 1),
    (stripe.Customer.create_tax_id, 1),
    (stripe.Customer.retrieve_tax_id, 2),
    (stripe.Customer.delete_tax_id, 2),
    (stripe.Customer.list_tax_ids, 1),
    (stripe.SubscriptionItem.create_usage_record, 1),
    (stripe.SubscriptionItem.list_usage_record_summaries, 1),
    (stripe.Transfer.create_reversal, 1),
    (stripe.Transfer.retrieve_reversal, 2),
    (stripe.Transfer.modify_reversal, 2),
    (stripe.Transfer.list_reversals, 1),
]

for method, n_ids in methods:
    if n_ids == 1:
        method(
            "id",
            api_key="a",
            idempotency_key="b",
            stripe_version="c",
            stripe_account="d",
            foo="bar",
            bar="baz",
        )
        method("id", foo="bar", bar="baz")
        method(
            "id",
        )
    if n_ids == 2:
        method(
            "id",
            "id_2",
            api_key="a",
            idempotency_key="b",
            stripe_version="c",
            stripe_account="d",
            foo="bar",
            bar="baz",
        )
        method("id", "id_2", foo="bar", bar="baz")
        method(
            "id",
            "id_2",
        )
