# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.api_resources.search_result_object import SearchResultObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.application_fee import ApplicationFee
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.bank_account import BankAccount
    from stripe.api_resources.card import Card
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.refund import Refund
    from stripe.api_resources.review import Review
    from stripe.api_resources.source import Source
    from stripe.api_resources.transfer import Transfer


class Charge(
    CreateableAPIResource["Charge"],
    ListableAPIResource["Charge"],
    SearchableAPIResource["Charge"],
    UpdateableAPIResource["Charge"],
):
    """
    The `Charge` object represents a single attempt to move money into your Stripe account.
    PaymentIntent confirmation is the most common way to create Charges, but transferring
    money to a different Stripe account through Connect also creates Charges.
    Some legacy payment flows create Charges directly, which is not recommended for new integrations.
    """

    OBJECT_NAME = "charge"
    if TYPE_CHECKING:

        class CaptureParams(RequestOptions):
            amount: NotRequired["int|None"]
            application_fee: NotRequired["int|None"]
            application_fee_amount: NotRequired["int|None"]
            expand: NotRequired["List[str]|None"]
            receipt_email: NotRequired["str|None"]
            statement_descriptor: NotRequired["str|None"]
            statement_descriptor_suffix: NotRequired["str|None"]
            transfer_data: NotRequired["Charge.CaptureParamsTransferData|None"]
            transfer_group: NotRequired["str|None"]

        class CaptureParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]

        class CreateParams(RequestOptions):
            amount: NotRequired["int|None"]
            application_fee: NotRequired["int|None"]
            application_fee_amount: NotRequired["int|None"]
            capture: NotRequired["bool|None"]
            currency: NotRequired["str|None"]
            customer: NotRequired["str|None"]
            description: NotRequired["str|None"]
            destination: NotRequired["Charge.CreateParamsDestination|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            on_behalf_of: NotRequired["str|None"]
            radar_options: NotRequired["Charge.CreateParamsRadarOptions|None"]
            receipt_email: NotRequired["str|None"]
            shipping: NotRequired["Charge.CreateParamsShipping|None"]
            source: NotRequired["str|None"]
            statement_descriptor: NotRequired["str|None"]
            statement_descriptor_suffix: NotRequired["str|None"]
            transfer_data: NotRequired["Charge.CreateParamsTransferData|None"]
            transfer_group: NotRequired["str|None"]

        class CreateParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            destination: str

        class CreateParamsShipping(TypedDict):
            address: "Charge.CreateParamsShippingAddress"
            carrier: NotRequired["str|None"]
            name: str
            phone: NotRequired["str|None"]
            tracking_number: NotRequired["str|None"]

        class CreateParamsShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsRadarOptions(TypedDict):
            session: NotRequired["str|None"]

        class CreateParamsDestination(TypedDict):
            account: str
            amount: NotRequired["int|None"]

        class ListParams(RequestOptions):
            created: NotRequired["Charge.ListParamsCreated|int|None"]
            customer: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            payment_intent: NotRequired["str|None"]
            starting_after: NotRequired["str|None"]
            transfer_group: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            customer: NotRequired["str|None"]
            description: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            fraud_details: NotRequired["Charge.ModifyParamsFraudDetails|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            receipt_email: NotRequired["str|None"]
            shipping: NotRequired["Charge.ModifyParamsShipping|None"]
            transfer_group: NotRequired["str|None"]

        class ModifyParamsShipping(TypedDict):
            address: "Charge.ModifyParamsShippingAddress"
            carrier: NotRequired["str|None"]
            name: str
            phone: NotRequired["str|None"]
            tracking_number: NotRequired["str|None"]

        class ModifyParamsShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ModifyParamsFraudDetails(TypedDict):
            user_report: Union[Literal[""], Literal["fraudulent", "safe"]]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class SearchParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            page: NotRequired["str|None"]
            query: str

    amount: int
    amount_captured: int
    amount_refunded: int
    application: Optional[ExpandableField["Application"]]
    application_fee: Optional[ExpandableField["ApplicationFee"]]
    application_fee_amount: Optional[int]
    authorization_code: Optional[str]
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    billing_details: StripeObject
    calculated_statement_descriptor: Optional[str]
    captured: bool
    created: int
    currency: str
    customer: Optional[ExpandableField["Customer"]]
    description: Optional[str]
    disputed: bool
    failure_balance_transaction: Optional[
        ExpandableField["BalanceTransaction"]
    ]
    failure_code: Optional[str]
    failure_message: Optional[str]
    fraud_details: Optional[StripeObject]
    id: str
    invoice: Optional[ExpandableField["Invoice"]]
    level3: Optional[StripeObject]
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["charge"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    outcome: Optional[StripeObject]
    paid: bool
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    payment_method: Optional[str]
    payment_method_details: Optional[StripeObject]
    radar_options: Optional[StripeObject]
    receipt_email: Optional[str]
    receipt_number: Optional[str]
    receipt_url: Optional[str]
    refunded: bool
    refunds: Optional[ListObject["Refund"]]
    review: Optional[ExpandableField["Review"]]
    shipping: Optional[StripeObject]
    source: Optional[Union["Account", "BankAccount", "Card", "Source"]]
    source_transfer: Optional[ExpandableField["Transfer"]]
    statement_descriptor: Optional[str]
    statement_descriptor_suffix: Optional[str]
    status: Literal["failed", "pending", "succeeded"]
    transfer: Optional[ExpandableField["Transfer"]]
    transfer_data: Optional[StripeObject]
    transfer_group: Optional[str]

    @classmethod
    def _cls_capture(
        cls,
        charge: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Charge.CaptureParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/charges/{charge}/capture".format(
                charge=util.sanitize_id(charge)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_capture")
    def capture(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Charge.CaptureParams"]
    ):
        return self._request(
            "post",
            "/v1/charges/{charge}/capture".format(
                charge=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Charge.CreateParams"]
    ) -> "Charge":
        return cast(
            "Charge",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Charge.ListParams"]
    ) -> ListObject["Charge"]:
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
    def modify(cls, id, **params: Unpack["Charge.ModifyParams"]) -> "Charge":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Charge",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Charge.RetrieveParams"]
    ) -> "Charge":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def search(
        cls, *args, **kwargs: Unpack["Charge.SearchParams"]
    ) -> SearchResultObject["Charge"]:
        return cls._search(search_url="/v1/charges/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(
        cls, *args, **kwargs: Unpack["Charge.SearchParams"]
    ):
        return cls.search(*args, **kwargs).auto_paging_iter()

    def mark_as_fraudulent(self, idempotency_key=None):
        params = {"fraud_details": {"user_report": "fraudulent"}}
        url = self.instance_url()
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def mark_as_safe(self, idempotency_key=None):
        params = {"fraud_details": {"user_report": "safe"}}
        url = self.instance_url()
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self
