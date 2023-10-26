# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.payment_intent import PaymentIntent


class Dispute(
    ListableAPIResource["Dispute"], UpdateableAPIResource["Dispute"]
):
    """
    A dispute occurs when a customer questions your charge with their card issuer.
    When this happens, you have the opportunity to respond to the dispute with
    evidence that shows that the charge is legitimate.

    Related guide: [Disputes and fraud](https://stripe.com/docs/disputes)
    """

    OBJECT_NAME: ClassVar[Literal["dispute"]] = "dispute"
    if TYPE_CHECKING:

        class CloseParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ListParams(RequestOptions):
            charge: NotRequired["str|None"]
            """
            Only return disputes associated to the charge specified by this charge ID.
            """
            created: NotRequired["Dispute.ListParamsCreated|int|None"]
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
            payment_intent: NotRequired["str|None"]
            """
            Only return disputes associated to the PaymentIntent specified by this PaymentIntent ID.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
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

        class ModifyParams(RequestOptions):
            evidence: NotRequired["Dispute.ModifyParamsEvidence|None"]
            """
            Evidence to upload, to respond to a dispute. Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            submit: NotRequired["bool|None"]
            """
            Whether to immediately submit evidence to the bank. If `false`, evidence is staged on the dispute. Staged evidence is visible in the API and Dashboard, and can be submitted to the bank by making another request with this attribute set to `true` (the default).
            """

        class ModifyParamsEvidence(TypedDict):
            access_activity_log: NotRequired["str|None"]
            """
            Any server or activity logs showing proof that the customer accessed or downloaded the purchased digital product. This information should include IP addresses, corresponding timestamps, and any detailed recorded activity. Has a maximum character count of 20,000.
            """
            billing_address: NotRequired["str|None"]
            """
            The billing address provided by the customer.
            """
            cancellation_policy: NotRequired["str|None"]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your subscription cancellation policy, as shown to the customer.
            """
            cancellation_policy_disclosure: NotRequired["str|None"]
            """
            An explanation of how and when the customer was shown your refund policy prior to purchase. Has a maximum character count of 20,000.
            """
            cancellation_rebuttal: NotRequired["str|None"]
            """
            A justification for why the customer's subscription was not canceled. Has a maximum character count of 20,000.
            """
            customer_communication: NotRequired["str|None"]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any communication with the customer that you feel is relevant to your case. Examples include emails proving that the customer received the product or service, or demonstrating their use of or satisfaction with the product or service.
            """
            customer_email_address: NotRequired["str|None"]
            """
            The email address of the customer.
            """
            customer_name: NotRequired["str|None"]
            """
            The name of the customer.
            """
            customer_purchase_ip: NotRequired["str|None"]
            """
            The IP address that the customer used when making the purchase.
            """
            customer_signature: NotRequired["str|None"]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) A relevant document or contract showing the customer's signature.
            """
            duplicate_charge_documentation: NotRequired["str|None"]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation for the prior charge that can uniquely identify the charge, such as a receipt, shipping label, work order, etc. This document should be paired with a similar document from the disputed payment that proves the two payments are separate.
            """
            duplicate_charge_explanation: NotRequired["str|None"]
            """
            An explanation of the difference between the disputed charge versus the prior charge that appears to be a duplicate. Has a maximum character count of 20,000.
            """
            duplicate_charge_id: NotRequired["str|None"]
            """
            The Stripe ID for the prior charge which appears to be a duplicate of the disputed charge.
            """
            product_description: NotRequired["str|None"]
            """
            A description of the product or service that was sold. Has a maximum character count of 20,000.
            """
            receipt: NotRequired["str|None"]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any receipt or message sent to the customer notifying them of the charge.
            """
            refund_policy: NotRequired["str|None"]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Your refund policy, as shown to the customer.
            """
            refund_policy_disclosure: NotRequired["str|None"]
            """
            Documentation demonstrating that the customer was shown your refund policy prior to purchase. Has a maximum character count of 20,000.
            """
            refund_refusal_explanation: NotRequired["str|None"]
            """
            A justification for why the customer is not entitled to a refund. Has a maximum character count of 20,000.
            """
            service_date: NotRequired["str|None"]
            """
            The date on which the customer received or began receiving the purchased service, in a clear human-readable format.
            """
            service_documentation: NotRequired["str|None"]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation showing proof that a service was provided to the customer. This could include a copy of a signed contract, work order, or other form of written agreement.
            """
            shipping_address: NotRequired["str|None"]
            """
            The address to which a physical product was shipped. You should try to include as complete address information as possible.
            """
            shipping_carrier: NotRequired["str|None"]
            """
            The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc. If multiple carriers were used for this purchase, please separate them with commas.
            """
            shipping_date: NotRequired["str|None"]
            """
            The date on which a physical product began its route to the shipping address, in a clear human-readable format.
            """
            shipping_documentation: NotRequired["str|None"]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Documentation showing proof that a product was shipped to the customer at the same address the customer provided to you. This could include a copy of the shipment receipt, shipping label, etc. It should show the customer's full shipping address, if possible.
            """
            shipping_tracking_number: NotRequired["str|None"]
            """
            The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.
            """
            uncategorized_file: NotRequired["str|None"]
            """
            (ID of a [file upload](https://stripe.com/docs/guides/file-upload)) Any additional evidence or statements.
            """
            uncategorized_text: NotRequired["str|None"]
            """
            Any additional evidence or statements. Has a maximum character count of 20,000.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    amount: int
    """
    Disputed amount. Usually the amount of the charge, but it can differ (usually because of currency fluctuation or because only part of the order is disputed).
    """
    balance_transactions: List["BalanceTransaction"]
    """
    List of zero, one, or two balance transactions that show funds withdrawn and reinstated to your Stripe account as a result of this dispute.
    """
    charge: ExpandableField["Charge"]
    """
    ID of the charge that's disputed.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    evidence: StripeObject
    evidence_details: StripeObject
    id: str
    """
    Unique identifier for the object.
    """
    is_charge_refundable: bool
    """
    If true, it's still possible to refund the disputed payment. After the payment has been fully refunded, no further funds are withdrawn from your Stripe account as a result of this dispute.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    network_reason_code: Optional[str]
    """
    Network-dependent reason code for the dispute.
    """
    object: Literal["dispute"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    """
    ID of the PaymentIntent that's disputed.
    """
    payment_method_details: Optional[StripeObject]
    reason: str
    """
    Reason given by cardholder for dispute. Possible values are `bank_cannot_process`, `check_returned`, `credit_not_processed`, `customer_initiated`, `debit_not_authorized`, `duplicate`, `fraudulent`, `general`, `incorrect_account_details`, `insufficient_funds`, `product_not_received`, `product_unacceptable`, `subscription_canceled`, or `unrecognized`. Learn more about [dispute reasons](https://stripe.com/docs/disputes/categories).
    """
    status: Literal[
        "lost",
        "needs_response",
        "under_review",
        "warning_closed",
        "warning_needs_response",
        "warning_under_review",
        "won",
    ]
    """
    Current status of dispute. Possible values are `warning_needs_response`, `warning_under_review`, `warning_closed`, `needs_response`, `under_review`, `won`, or `lost`.
    """

    @classmethod
    def _cls_close(
        cls,
        dispute: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Dispute.CloseParams"]
    ) -> "Dispute":
        return cast(
            "Dispute",
            cls._static_request(
                "post",
                "/v1/disputes/{dispute}/close".format(
                    dispute=util.sanitize_id(dispute)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def close(
        cls,
        dispute: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Dispute.CloseParams"]
    ) -> "Dispute":
        ...

    @overload
    def close(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Dispute.CloseParams"]
    ) -> "Dispute":
        ...

    @class_method_variant("_cls_close")
    def close(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Dispute.CloseParams"]
    ) -> "Dispute":
        return cast(
            "Dispute",
            self._request(
                "post",
                "/v1/disputes/{dispute}/close".format(
                    dispute=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Dispute.ListParams"]
    ) -> ListObject["Dispute"]:
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
    def modify(
        cls, id: str, **params: Unpack["Dispute.ModifyParams"]
    ) -> "Dispute":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Dispute",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Dispute.RetrieveParams"]
    ) -> "Dispute":
        instance = cls(id, **params)
        instance.refresh()
        return instance
