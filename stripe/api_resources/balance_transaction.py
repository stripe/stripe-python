# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.api_resources.application_fee import ApplicationFee
    from stripe.api_resources.application_fee_refund import (
        ApplicationFeeRefund,
    )
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.connect_collection_transfer import (
        ConnectCollectionTransfer,
    )
    from stripe.api_resources.customer_cash_balance_transaction import (
        CustomerCashBalanceTransaction,
    )
    from stripe.api_resources.dispute import Dispute as DisputeResource
    from stripe.api_resources.issuing.authorization import Authorization
    from stripe.api_resources.issuing.dispute import (
        Dispute as IssuingDisputeResource,
    )
    from stripe.api_resources.issuing.transaction import Transaction
    from stripe.api_resources.payout import Payout
    from stripe.api_resources.platform_tax_fee import PlatformTaxFee
    from stripe.api_resources.refund import Refund
    from stripe.api_resources.reserve_transaction import ReserveTransaction
    from stripe.api_resources.reversal import Reversal
    from stripe.api_resources.tax_deducted_at_source import TaxDeductedAtSource
    from stripe.api_resources.topup import Topup
    from stripe.api_resources.transfer import Transfer


class BalanceTransaction(ListableAPIResource["BalanceTransaction"]):
    """
    Balance transactions represent funds moving through your Stripe account.
    Stripe creates them for every type of transaction that enters or leaves your Stripe account balance.

    Related guide: [Balance transaction types](https://stripe.com/docs/reports/balance-transaction-types)
    """

    OBJECT_NAME: ClassVar[
        Literal["balance_transaction"]
    ] = "balance_transaction"

    class FeeDetail(StripeObject):
        amount: int
        """
        Amount of the fee, in cents.
        """
        application: Optional[str]
        """
        ID of the Connect application that earned the fee.
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        description: Optional[str]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        type: str
        """
        Type of the fee, one of: `application_fee`, `stripe_fee` or `tax`.
        """

    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            created: NotRequired[
                "BalanceTransaction.ListParamsCreated|int|None"
            ]
            currency: NotRequired["str|None"]
            """
            Only return transactions in a certain currency. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            payout: NotRequired["str|None"]
            """
            For automatic Stripe payouts only, only returns transactions that were paid out on the specified payout ID.
            """
            source: NotRequired["str|None"]
            """
            Only returns the original transaction.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            type: NotRequired["str|None"]
            """
            Only returns transactions of the given type. One of: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_inbound`, `obligation_outbound`, `obligation_reversal_inbound`, `obligation_reversal_outbound`, `obligation_payout`, `obligation_payout_failure`, `payment`, `payment_failure_refund`, `payment_refund`, `payment_reversal`, `payout`, `payout_cancel`, `payout_failure`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`.
            """

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    amount: int
    """
    Gross amount of this transaction (in cents (or local equivalent)). A positive value represents funds charged to another party, and a negative value represents funds sent to another party.
    """
    available_on: int
    """
    The date that the transaction's net funds become available in the Stripe balance.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    exchange_rate: Optional[float]
    """
    If applicable, this transaction uses an exchange rate. If money converts from currency A to currency B, then the `amount` in currency A, multipled by the `exchange_rate`, equals the `amount` in currency B. For example, if you charge a customer 10.00 EUR, the PaymentIntent's `amount` is `1000` and `currency` is `eur`. If this converts to 12.34 USD in your Stripe account, the BalanceTransaction's `amount` is `1234`, its `currency` is `usd`, and the `exchange_rate` is `1.234`.
    """
    fee: int
    """
    Fees (in cents (or local equivalent)) paid for this transaction. Represented as a positive integer when assessed.
    """
    fee_details: List[FeeDetail]
    """
    Detailed breakdown of fees (in cents (or local equivalent)) paid for this transaction.
    """
    id: str
    """
    Unique identifier for the object.
    """
    net: int
    """
    Net impact to a Stripe balance (in cents (or local equivalent)). A positive value represents incrementing a Stripe balance, and a negative value decrementing a Stripe balance. You can calculate the net impact of a transaction on a balance by `amount` - `fee`
    """
    object: Literal["balance_transaction"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    reporting_category: str
    """
    Learn more about how [reporting categories](https://stripe.com/docs/reports/reporting-categories) can help you understand balance transactions from an accounting perspective.
    """
    source: Optional[
        ExpandableField[
            Union[
                "ApplicationFee",
                "Charge",
                "ConnectCollectionTransfer",
                "CustomerCashBalanceTransaction",
                "DisputeResource",
                "ApplicationFeeRefund",
                "Authorization",
                "IssuingDisputeResource",
                "Transaction",
                "Payout",
                "PlatformTaxFee",
                "Refund",
                "ReserveTransaction",
                "TaxDeductedAtSource",
                "Topup",
                "Transfer",
                "Reversal",
            ]
        ]
    ]
    """
    This transaction relates to the Stripe object.
    """
    status: str
    """
    The transaction's net funds status in the Stripe balance, which are either `available` or `pending`.
    """
    type: Literal[
        "adjustment",
        "advance",
        "advance_funding",
        "anticipation_repayment",
        "application_fee",
        "application_fee_refund",
        "charge",
        "connect_collection_transfer",
        "contribution",
        "issuing_authorization_hold",
        "issuing_authorization_release",
        "issuing_dispute",
        "issuing_transaction",
        "obligation_inbound",
        "obligation_outbound",
        "obligation_payout",
        "obligation_payout_failure",
        "obligation_reversal_inbound",
        "obligation_reversal_outbound",
        "payment",
        "payment_failure_refund",
        "payment_refund",
        "payment_reversal",
        "payout",
        "payout_cancel",
        "payout_failure",
        "refund",
        "refund_failure",
        "reserve_transaction",
        "reserved_funds",
        "stripe_fee",
        "stripe_fx_fee",
        "tax_fee",
        "topup",
        "topup_reversal",
        "transfer",
        "transfer_cancel",
        "transfer_failure",
        "transfer_refund",
    ]
    """
    Transaction type: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_inbound`, `obligation_outbound`, `obligation_reversal_inbound`, `obligation_reversal_outbound`, `obligation_payout`, `obligation_payout_failure`, `payment`, `payment_failure_refund`, `payment_refund`, `payment_reversal`, `payout`, `payout_cancel`, `payout_failure`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`. Learn more about [balance transaction types and what they represent](https://stripe.com/docs/reports/balance-transaction-types). To classify transactions for accounting purposes, consider `reporting_category` instead.
    """

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["BalanceTransaction.ListParams"]
    ) -> ListObject["BalanceTransaction"]:
        """
        Returns a list of transactions that have contributed to the Stripe account balance (e.g., charges, transfers, and so forth). The transactions are returned in sorted order, with the most recent transactions appearing first.

        Note that this endpoint was previously called “Balance history” and used the path /v1/balance/history.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["BalanceTransaction.RetrieveParams"]
    ) -> "BalanceTransaction":
        """
        Retrieves the balance transaction with the given ID.

        Note that this endpoint previously used the path /v1/balance/history/:id.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {"fee_details": FeeDetail}
