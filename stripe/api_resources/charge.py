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
from stripe.util import class_method_variant
from typing import (
    ClassVar,
    Dict,
    Iterator,
    List,
    Optional,
    Union,
    cast,
    overload,
)
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

    OBJECT_NAME: ClassVar[Literal["charge"]] = "charge"
    if TYPE_CHECKING:

        class CaptureParams(RequestOptions):
            amount: NotRequired["int|None"]
            """
            The amount to capture, which must be less than or equal to the original amount. Any additional amount will be automatically refunded.
            """
            application_fee: NotRequired["int|None"]
            """
            An application fee to add on to this charge.
            """
            application_fee_amount: NotRequired["int|None"]
            """
            An application fee amount to add on to this charge, which must be less than or equal to the original amount.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            receipt_email: NotRequired["str|None"]
            """
            The email address to send this charge's receipt to. This will override the previously-specified email address for this charge, if one was set. Receipts will not be sent in test mode.
            """
            statement_descriptor: NotRequired["str|None"]
            """
            For card charges, use `statement_descriptor_suffix` instead. Otherwise, you can use this value as the complete description of a charge on your customers' statements. Must contain at least one letter, maximum 22 characters.
            """
            statement_descriptor_suffix: NotRequired["str|None"]
            """
            Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.
            """
            transfer_data: NotRequired["Charge.CaptureParamsTransferData|None"]
            """
            An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details.
            """
            transfer_group: NotRequired["str|None"]
            """
            A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details.
            """

        class CaptureParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            """
            The amount transferred to the destination account, if specified. By default, the entire charge amount is transferred to the destination account.
            """

        class CreateParams(RequestOptions):
            amount: NotRequired["int|None"]
            """
            Amount intended to be collected by this payment. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
            """
            application_fee: NotRequired["int|None"]
            application_fee_amount: NotRequired["int|None"]
            """
            A fee in cents (or local equivalent) that will be applied to the charge and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the `Stripe-Account` header in order to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/connect/direct-charges#collecting-fees).
            """
            capture: NotRequired["bool|None"]
            """
            Whether to immediately capture the charge. Defaults to `true`. When `false`, the charge issues an authorization (or pre-authorization), and will need to be [captured](https://stripe.com/docs/api#capture_charge) later. Uncaptured charges expire after a set number of days (7 by default). For more information, see the [authorizing charges and settling later](https://stripe.com/docs/charges/placing-a-hold) documentation.
            """
            currency: NotRequired["str|None"]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            customer: NotRequired["str|None"]
            """
            The ID of an existing customer that will be charged in this request.
            """
            description: NotRequired["str|None"]
            """
            An arbitrary string which you can attach to a `Charge` object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing.
            """
            destination: NotRequired["Charge.CreateParamsDestination|None"]
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            on_behalf_of: NotRequired["str|None"]
            """
            The Stripe account ID for which these funds are intended. Automatically set if you use the `destination` parameter. For details, see [Creating Separate Charges and Transfers](https://stripe.com/docs/connect/separate-charges-and-transfers#on-behalf-of).
            """
            radar_options: NotRequired["Charge.CreateParamsRadarOptions|None"]
            """
            Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
            """
            receipt_email: NotRequired["str|None"]
            """
            The email address to which this charge's [receipt](https://stripe.com/docs/dashboard/receipts) will be sent. The receipt will not be sent until the charge is paid, and no receipts will be sent for test mode charges. If this charge is for a [Customer](https://stripe.com/docs/api/customers/object), the email address specified here will override the customer's email address. If `receipt_email` is specified for a charge in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails).
            """
            shipping: NotRequired["Charge.CreateParamsShipping|None"]
            """
            Shipping information for the charge. Helps prevent fraud on charges for physical goods.
            """
            source: NotRequired["str|None"]
            """
            A payment source to be charged. This can be the ID of a [card](https://stripe.com/docs/api#cards) (i.e., credit or debit card), a [bank account](https://stripe.com/docs/api#bank_accounts), a [source](https://stripe.com/docs/api#sources), a [token](https://stripe.com/docs/api#tokens), or a [connected account](https://stripe.com/docs/connect/account-debits#charging-a-connected-account). For certain sources---namely, [cards](https://stripe.com/docs/api#cards), [bank accounts](https://stripe.com/docs/api#bank_accounts), and attached [sources](https://stripe.com/docs/api#sources)---you must also pass the ID of the associated customer.
            """
            statement_descriptor: NotRequired["str|None"]
            """
            For card charges, use `statement_descriptor_suffix` instead. Otherwise, you can use this value as the complete description of a charge on your customers' statements. Must contain at least one letter, maximum 22 characters.
            """
            statement_descriptor_suffix: NotRequired["str|None"]
            """
            Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.
            """
            transfer_data: NotRequired["Charge.CreateParamsTransferData|None"]
            """
            An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details.
            """
            transfer_group: NotRequired["str|None"]
            """
            A string that identifies this transaction as part of a group. For details, see [Grouping transactions](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options).
            """

        class CreateParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            """
            The amount transferred to the destination account, if specified. By default, the entire charge amount is transferred to the destination account.
            """
            destination: str
            """
            ID of an existing, connected Stripe account.
            """

        class CreateParamsShipping(TypedDict):
            address: "Charge.CreateParamsShippingAddress"
            """
            Shipping address.
            """
            carrier: NotRequired["str|None"]
            """
            The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.
            """
            name: str
            """
            Recipient name.
            """
            phone: NotRequired["str|None"]
            """
            Recipient phone (including extension).
            """
            tracking_number: NotRequired["str|None"]
            """
            The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.
            """

        class CreateParamsShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class CreateParamsRadarOptions(TypedDict):
            session: NotRequired["str|None"]
            """
            A [Radar Session](https://stripe.com/docs/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
            """

        class CreateParamsDestination(TypedDict):
            account: str
            """
            ID of an existing, connected Stripe account.
            """
            amount: NotRequired["int|None"]
            """
            The amount to transfer to the destination account without creating an `Application Fee` object. Cannot be combined with the `application_fee` parameter. Must be less than or equal to the charge amount.
            """

        class ListParams(RequestOptions):
            created: NotRequired["Charge.ListParamsCreated|int|None"]
            customer: NotRequired["str|None"]
            """
            Only return charges for the customer specified by this customer ID.
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
            payment_intent: NotRequired["str|None"]
            """
            Only return charges that were created by the PaymentIntent specified by this PaymentIntent ID.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            transfer_group: NotRequired["str|None"]
            """
            Only return charges for this transfer group.
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
            customer: NotRequired["str|None"]
            """
            The ID of an existing customer that will be associated with this request. This field may only be updated if there is no existing associated customer with this charge.
            """
            description: NotRequired["str|None"]
            """
            An arbitrary string which you can attach to a charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            fraud_details: NotRequired["Charge.ModifyParamsFraudDetails|None"]
            """
            A set of key-value pairs you can attach to a charge giving information about its riskiness. If you believe a charge is fraudulent, include a `user_report` key with a value of `fraudulent`. If you believe a charge is safe, include a `user_report` key with a value of `safe`. Stripe will use the information you send to improve our fraud detection algorithms.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            receipt_email: NotRequired["str|None"]
            """
            This is the email address that the receipt for this charge will be sent to. If this field is updated, then a new email receipt will be sent to the updated address.
            """
            shipping: NotRequired["Charge.ModifyParamsShipping|None"]
            """
            Shipping information for the charge. Helps prevent fraud on charges for physical goods.
            """
            transfer_group: NotRequired["str|None"]
            """
            A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details.
            """

        class ModifyParamsShipping(TypedDict):
            address: "Charge.ModifyParamsShippingAddress"
            """
            Shipping address.
            """
            carrier: NotRequired["str|None"]
            """
            The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.
            """
            name: str
            """
            Recipient name.
            """
            phone: NotRequired["str|None"]
            """
            Recipient phone (including extension).
            """
            tracking_number: NotRequired["str|None"]
            """
            The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.
            """

        class ModifyParamsShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class ModifyParamsFraudDetails(TypedDict):
            user_report: Union[Literal[""], Literal["fraudulent", "safe"]]
            """
            Either `safe` or `fraudulent`.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class SearchParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            page: NotRequired["str|None"]
            """
            A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            """
            query: str
            """
            The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for charges](https://stripe.com/docs/search#query-fields-for-charges).
            """

    amount: int
    """
    Amount intended to be collected by this payment. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
    """
    amount_captured: int
    """
    Amount in cents (or local equivalent) captured (can be less than the amount attribute on the charge if a partial capture was made).
    """
    amount_refunded: int
    """
    Amount in cents (or local equivalent) refunded (can be less than the amount attribute on the charge if a partial refund was issued).
    """
    application: Optional[ExpandableField["Application"]]
    """
    ID of the Connect application that created the charge.
    """
    application_fee: Optional[ExpandableField["ApplicationFee"]]
    """
    The application fee (if any) for the charge. [See the Connect documentation](https://stripe.com/docs/connect/direct-charges#collecting-fees) for details.
    """
    application_fee_amount: Optional[int]
    """
    The amount of the application fee (if any) requested for the charge. [See the Connect documentation](https://stripe.com/docs/connect/direct-charges#collecting-fees) for details.
    """
    authorization_code: Optional[str]
    """
    Authorization code on the charge.
    """
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    """
    ID of the balance transaction that describes the impact of this charge on your account balance (not including refunds or disputes).
    """
    billing_details: StripeObject
    calculated_statement_descriptor: Optional[str]
    """
    The full statement descriptor that is passed to card networks, and that is displayed on your customers' credit card and bank statements. Allows you to see what the statement descriptor looks like after the static and dynamic portions are combined.
    """
    captured: bool
    """
    If the charge was created without capturing, this Boolean represents whether it is still uncaptured or has since been captured.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    customer: Optional[ExpandableField["Customer"]]
    """
    ID of the customer this charge is for if one exists.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    disputed: bool
    """
    Whether the charge has been disputed.
    """
    failure_balance_transaction: Optional[
        ExpandableField["BalanceTransaction"]
    ]
    """
    ID of the balance transaction that describes the reversal of the balance on your account due to payment failure.
    """
    failure_code: Optional[str]
    """
    Error code explaining reason for charge failure if available (see [the errors section](https://stripe.com/docs/error-codes) for a list of codes).
    """
    failure_message: Optional[str]
    """
    Message to user further explaining reason for charge failure if available.
    """
    fraud_details: Optional[StripeObject]
    """
    Information on fraud assessments for the charge.
    """
    id: str
    """
    Unique identifier for the object.
    """
    invoice: Optional[ExpandableField["Invoice"]]
    """
    ID of the invoice this charge is for if one exists.
    """
    level3: Optional[StripeObject]
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["charge"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: Optional[ExpandableField["Account"]]
    """
    The account (if any) the charge was made on behalf of without triggering an automatic transfer. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers) for details.
    """
    outcome: Optional[StripeObject]
    """
    Details about whether the payment was accepted, and why. See [understanding declines](https://stripe.com/docs/declines) for details.
    """
    paid: bool
    """
    `true` if the charge succeeded, or was successfully authorized for later capture.
    """
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    """
    ID of the PaymentIntent associated with this charge, if one exists.
    """
    payment_method: Optional[str]
    """
    ID of the payment method used in this charge.
    """
    payment_method_details: Optional[StripeObject]
    """
    Details about the payment method at the time of the transaction.
    """
    radar_options: Optional[StripeObject]
    """
    Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
    """
    receipt_email: Optional[str]
    """
    This is the email address that the receipt for this charge was sent to.
    """
    receipt_number: Optional[str]
    """
    This is the transaction number that appears on email receipts sent for this charge. This attribute will be `null` until a receipt has been sent.
    """
    receipt_url: Optional[str]
    """
    This is the URL to view the receipt for this charge. The receipt is kept up-to-date to the latest state of the charge, including any refunds. If the charge is for an Invoice, the receipt will be stylized as an Invoice receipt.
    """
    refunded: bool
    """
    Whether the charge has been fully refunded. If the charge is only partially refunded, this attribute will still be false.
    """
    refunds: Optional[ListObject["Refund"]]
    """
    A list of refunds that have been applied to the charge.
    """
    review: Optional[ExpandableField["Review"]]
    """
    ID of the review associated with this charge if one exists.
    """
    shipping: Optional[StripeObject]
    """
    Shipping information for the charge.
    """
    source: Optional[Union["Account", "BankAccount", "Card", "Source"]]
    """
    This is a legacy field that will be removed in the future. It contains the Source, Card, or BankAccount object used for the charge. For details about the payment method used for this charge, refer to `payment_method` or `payment_method_details` instead.
    """
    source_transfer: Optional[ExpandableField["Transfer"]]
    """
    The transfer ID which created this charge. Only present if the charge came from another Stripe account. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details.
    """
    statement_descriptor: Optional[str]
    """
    For card charges, use `statement_descriptor_suffix` instead. Otherwise, you can use this value as the complete description of a charge on your customers' statements. Must contain at least one letter, maximum 22 characters.
    """
    statement_descriptor_suffix: Optional[str]
    """
    Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.
    """
    status: Literal["failed", "pending", "succeeded"]
    """
    The status of the payment is either `succeeded`, `pending`, or `failed`.
    """
    transfer: Optional[ExpandableField["Transfer"]]
    """
    ID of the transfer to the `destination` account (only applicable if the charge was created using the `destination` parameter).
    """
    transfer_data: Optional[StripeObject]
    """
    An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details.
    """
    transfer_group: Optional[str]
    """
    A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details.
    """

    @classmethod
    def _cls_capture(
        cls,
        charge: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Charge.CaptureParams"]
    ) -> "Charge":
        return cast(
            "Charge",
            cls._static_request(
                "post",
                "/v1/charges/{charge}/capture".format(
                    charge=util.sanitize_id(charge)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def capture(
        cls,
        charge: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Charge.CaptureParams"]
    ) -> "Charge":
        ...

    @overload
    def capture(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Charge.CaptureParams"]
    ) -> "Charge":
        ...

    @class_method_variant("_cls_capture")
    def capture(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Charge.CaptureParams"]
    ) -> "Charge":
        return cast(
            "Charge",
            self._request(
                "post",
                "/v1/charges/{charge}/capture".format(
                    charge=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
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
    def modify(
        cls, id: str, **params: Unpack["Charge.ModifyParams"]
    ) -> "Charge":
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
    ) -> Iterator["Charge"]:
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
