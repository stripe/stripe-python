# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, Union
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

    OBJECT_NAME = "balance_transaction"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            created: NotRequired[
                "BalanceTransaction.ListParamsCreated|int|None"
            ]
            currency: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            payout: NotRequired["str|None"]
            source: NotRequired["str|None"]
            starting_after: NotRequired["str|None"]
            type: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    amount: int
    available_on: int
    created: int
    currency: str
    description: Optional[str]
    exchange_rate: Optional[float]
    fee: int
    fee_details: List[StripeObject]
    id: str
    net: int
    object: Literal["balance_transaction"]
    reporting_category: str
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
    status: str
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

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["BalanceTransaction.ListParams"]
    ) -> ListObject["BalanceTransaction"]:
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
        instance = cls(id, **params)
        instance.refresh()
        return instance
