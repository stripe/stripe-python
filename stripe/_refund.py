# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import _util
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._test_helpers import APIResourceTestHelpers
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import Literal, NotRequired, Type, Unpack, TYPE_CHECKING
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe._balance_transaction import BalanceTransaction
    from stripe._charge import Charge
    from stripe._payment_intent import PaymentIntent
    from stripe._reversal import Reversal


class Refund(
    CreateableAPIResource["Refund"],
    ListableAPIResource["Refund"],
    UpdateableAPIResource["Refund"],
):
    """
    Refund objects allow you to refund a previously created charge that isn't
    refunded yet. Funds are refunded to the credit or debit card that's
    initially charged.

    Related guide: [Refunds](https://stripe.com/docs/refunds)
    """

    OBJECT_NAME: ClassVar[Literal["refund"]] = "refund"

    class DestinationDetails(StripeObject):
        class Affirm(StripeObject):
            pass

        class AfterpayClearpay(StripeObject):
            pass

        class Alipay(StripeObject):
            pass

        class AuBankTransfer(StripeObject):
            pass

        class Blik(StripeObject):
            reference: Optional[str]
            """
            The reference assigned to the refund.
            """
            reference_status: Optional[str]
            """
            Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.
            """

        class BrBankTransfer(StripeObject):
            reference: Optional[str]
            """
            The reference assigned to the refund.
            """
            reference_status: Optional[str]
            """
            Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.
            """

        class Card(StripeObject):
            reference: Optional[str]
            """
            Value of the reference number assigned to the refund.
            """
            reference_status: Optional[str]
            """
            Status of the reference number on the refund. This can be `pending`, `available` or `unavailable`.
            """
            reference_type: Optional[str]
            """
            Type of the reference number assigned to the refund.
            """
            type: Literal["pending", "refund", "reversal"]
            """
            The type of refund. This can be `refund`, `reversal`, or `pending`.
            """

        class Cashapp(StripeObject):
            pass

        class CustomerCashBalance(StripeObject):
            pass

        class Eps(StripeObject):
            pass

        class EuBankTransfer(StripeObject):
            reference: Optional[str]
            """
            The reference assigned to the refund.
            """
            reference_status: Optional[str]
            """
            Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.
            """

        class GbBankTransfer(StripeObject):
            reference: Optional[str]
            """
            The reference assigned to the refund.
            """
            reference_status: Optional[str]
            """
            Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.
            """

        class Giropay(StripeObject):
            pass

        class Grabpay(StripeObject):
            pass

        class JpBankTransfer(StripeObject):
            reference: Optional[str]
            """
            The reference assigned to the refund.
            """
            reference_status: Optional[str]
            """
            Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.
            """

        class Klarna(StripeObject):
            pass

        class MxBankTransfer(StripeObject):
            reference: Optional[str]
            """
            The reference assigned to the refund.
            """
            reference_status: Optional[str]
            """
            Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.
            """

        class P24(StripeObject):
            reference: Optional[str]
            """
            The reference assigned to the refund.
            """
            reference_status: Optional[str]
            """
            Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.
            """

        class Paynow(StripeObject):
            pass

        class Paypal(StripeObject):
            pass

        class Pix(StripeObject):
            pass

        class Revolut(StripeObject):
            pass

        class Sofort(StripeObject):
            pass

        class ThBankTransfer(StripeObject):
            reference: Optional[str]
            """
            The reference assigned to the refund.
            """
            reference_status: Optional[str]
            """
            Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.
            """

        class UsBankTransfer(StripeObject):
            reference: Optional[str]
            """
            The reference assigned to the refund.
            """
            reference_status: Optional[str]
            """
            Status of the reference on the refund. This can be `pending`, `available` or `unavailable`.
            """

        class WechatPay(StripeObject):
            pass

        class Zip(StripeObject):
            pass

        affirm: Optional[Affirm]
        afterpay_clearpay: Optional[AfterpayClearpay]
        alipay: Optional[Alipay]
        au_bank_transfer: Optional[AuBankTransfer]
        blik: Optional[Blik]
        br_bank_transfer: Optional[BrBankTransfer]
        card: Optional[Card]
        cashapp: Optional[Cashapp]
        customer_cash_balance: Optional[CustomerCashBalance]
        eps: Optional[Eps]
        eu_bank_transfer: Optional[EuBankTransfer]
        gb_bank_transfer: Optional[GbBankTransfer]
        giropay: Optional[Giropay]
        grabpay: Optional[Grabpay]
        jp_bank_transfer: Optional[JpBankTransfer]
        klarna: Optional[Klarna]
        mx_bank_transfer: Optional[MxBankTransfer]
        p24: Optional[P24]
        paynow: Optional[Paynow]
        paypal: Optional[Paypal]
        pix: Optional[Pix]
        revolut: Optional[Revolut]
        sofort: Optional[Sofort]
        th_bank_transfer: Optional[ThBankTransfer]
        type: str
        """
        The type of transaction-specific details of the payment method used in the refund (e.g., `card`). An additional hash is included on `destination_details` with a name matching this value. It contains information specific to the refund transaction.
        """
        us_bank_transfer: Optional[UsBankTransfer]
        wechat_pay: Optional[WechatPay]
        zip: Optional[Zip]
        _inner_class_types = {
            "affirm": Affirm,
            "afterpay_clearpay": AfterpayClearpay,
            "alipay": Alipay,
            "au_bank_transfer": AuBankTransfer,
            "blik": Blik,
            "br_bank_transfer": BrBankTransfer,
            "card": Card,
            "cashapp": Cashapp,
            "customer_cash_balance": CustomerCashBalance,
            "eps": Eps,
            "eu_bank_transfer": EuBankTransfer,
            "gb_bank_transfer": GbBankTransfer,
            "giropay": Giropay,
            "grabpay": Grabpay,
            "jp_bank_transfer": JpBankTransfer,
            "klarna": Klarna,
            "mx_bank_transfer": MxBankTransfer,
            "p24": P24,
            "paynow": Paynow,
            "paypal": Paypal,
            "pix": Pix,
            "revolut": Revolut,
            "sofort": Sofort,
            "th_bank_transfer": ThBankTransfer,
            "us_bank_transfer": UsBankTransfer,
            "wechat_pay": WechatPay,
            "zip": Zip,
        }

    class NextAction(StripeObject):
        class DisplayDetails(StripeObject):
            class EmailSent(StripeObject):
                email_sent_at: int
                """
                The timestamp when the email was sent.
                """
                email_sent_to: str
                """
                The recipient's email address.
                """

            email_sent: EmailSent
            expires_at: int
            """
            The expiry timestamp.
            """
            _inner_class_types = {"email_sent": EmailSent}

        display_details: Optional[DisplayDetails]
        """
        Contains the refund details.
        """
        type: str
        """
        Type of the next action to perform.
        """
        _inner_class_types = {"display_details": DisplayDetails}

    class CancelParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParams(RequestOptions):
        amount: NotRequired["int"]
        charge: NotRequired["str"]
        """
        The identifier of the charge to refund.
        """
        currency: NotRequired["str"]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        customer: NotRequired["str"]
        """
        Customer whose customer balance to refund from.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        instructions_email: NotRequired["str"]
        """
        For payment methods without native refund support (e.g., Konbini, PromptPay), use this email from the customer to receive refund instructions.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        origin: NotRequired["Literal['customer_balance']"]
        """
        Origin of the refund
        """
        payment_intent: NotRequired["str"]
        """
        The identifier of the PaymentIntent to refund.
        """
        reason: NotRequired[
            "Literal['duplicate', 'fraudulent', 'requested_by_customer']"
        ]
        """
        String indicating the reason for the refund. If set, possible values are `duplicate`, `fraudulent`, and `requested_by_customer`. If you believe the charge to be fraudulent, specifying `fraudulent` as the reason will add the associated card and email to your [block lists](https://stripe.com/docs/radar/lists), and will also help us improve our fraud detection algorithms.
        """
        refund_application_fee: NotRequired["bool"]
        """
        Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.
        """
        reverse_transfer: NotRequired["bool"]
        """
        Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).

        A transfer can be reversed only by the application that created the charge.
        """

    class ListParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ModifyParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class ExpireParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    amount: int
    """
    Amount, in cents (or local equivalent).
    """
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    """
    Balance transaction that describes the impact on your account balance.
    """
    charge: Optional[ExpandableField["Charge"]]
    """
    ID of the charge that's refunded.
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
    An arbitrary string attached to the object. You can use this for displaying to users (available on non-card refunds only).
    """
    destination_details: Optional[DestinationDetails]
    failure_balance_transaction: Optional[
        ExpandableField["BalanceTransaction"]
    ]
    """
    After the refund fails, this balance transaction describes the adjustment made on your account balance that reverses the initial balance transaction.
    """
    failure_reason: Optional[str]
    """
    Provides the reason for the refund failure. Possible values are: `lost_or_stolen_card`, `expired_or_canceled_card`, `charge_for_pending_refund_disputed`, `insufficient_funds`, `declined`, `merchant_request`, or `unknown`.
    """
    id: str
    """
    Unique identifier for the object.
    """
    instructions_email: Optional[str]
    """
    For payment methods without native refund support (for example, Konbini, PromptPay), provide an email address for the customer to receive refund instructions.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    next_action: Optional[NextAction]
    object: Literal["refund"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    """
    ID of the PaymentIntent that's refunded.
    """
    reason: Optional[
        Literal[
            "duplicate",
            "expired_uncaptured_charge",
            "fraudulent",
            "requested_by_customer",
        ]
    ]
    """
    Reason for the refund, which is either user-provided (`duplicate`, `fraudulent`, or `requested_by_customer`) or generated by Stripe internally (`expired_uncaptured_charge`).
    """
    receipt_number: Optional[str]
    """
    This is the transaction number that appears on email receipts sent for this refund.
    """
    source_transfer_reversal: Optional[ExpandableField["Reversal"]]
    """
    The transfer reversal that's associated with the refund. Only present if the charge came from another Stripe account.
    """
    status: Optional[str]
    """
    Status of the refund. This can be `pending`, `requires_action`, `succeeded`, `failed`, or `canceled`. Learn more about [failed refunds](https://stripe.com/docs/refunds#failed-refunds).
    """
    transfer_reversal: Optional[ExpandableField["Reversal"]]
    """
    This refers to the transfer reversal object if the accompanying transfer reverses. This is only applicable if the charge was created using the destination parameter.
    """

    @classmethod
    def _cls_cancel(
        cls,
        refund: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Refund.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Refund":
        """
        Cancels a refund with a status of requires_action.

        You can't cancel refunds in other states. Only refunds for payment methods that require customer action can enter the requires_action state.
        """
        return cast(
            "Refund",
            cls._static_request(
                "post",
                "/v1/refunds/{refund}/cancel".format(
                    refund=_util.sanitize_id(refund)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def cancel(
        refund: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Refund.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Refund":
        """
        Cancels a refund with a status of requires_action.

        You can't cancel refunds in other states. Only refunds for payment methods that require customer action can enter the requires_action state.
        """
        ...

    @overload
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Refund.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Refund":
        """
        Cancels a refund with a status of requires_action.

        You can't cancel refunds in other states. Only refunds for payment methods that require customer action can enter the requires_action state.
        """
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "Refund.CancelParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Refund":
        """
        Cancels a refund with a status of requires_action.

        You can't cancel refunds in other states. Only refunds for payment methods that require customer action can enter the requires_action state.
        """
        return cast(
            "Refund",
            self._request(
                "post",
                "/v1/refunds/{refund}/cancel".format(
                    refund=_util.sanitize_id(self.get("id"))
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
        **params: Unpack[
            "Refund.CreateParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "Refund":
        """
        When you create a new refund, you must specify a Charge or a PaymentIntent object on which to create it.

        Creating a new refund will refund a charge that has previously been created but not yet refunded.
        Funds will be refunded to the credit or debit card that was originally charged.

        You can optionally refund only part of a charge.
        You can do so multiple times, until the entire charge has been refunded.

        Once entirely refunded, a charge can't be refunded again.
        This method will raise an error when called on an already-refunded charge,
        or when trying to refund more money than is left on a charge.
        """
        return cast(
            "Refund",
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
        **params: Unpack[
            "Refund.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["Refund"]:
        """
        You can see a list of the refunds belonging to a specific charge. Note that the 10 most recent refunds are always available by default on the charge object. If you need more than those 10, you can use this API method and the limit and starting_after parameters to page through additional refunds.
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
    def modify(
        cls, id: str, **params: Unpack["Refund.ModifyParams"]
    ) -> "Refund":
        """
        Updates the refund that you specify by setting the values of the passed parameters. Any parameters that you don't provide remain unchanged.

        This request only accepts metadata as an argument.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Refund",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Refund.RetrieveParams"]
    ) -> "Refund":
        """
        Retrieves the details of an existing refund.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    class TestHelpers(APIResourceTestHelpers["Refund"]):
        _resource_cls: Type["Refund"]

        @classmethod
        def _cls_expire(
            cls,
            refund: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "Refund.ExpireParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "Refund":
            """
            Expire a refund with a status of requires_action.
            """
            return cast(
                "Refund",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/refunds/{refund}/expire".format(
                        refund=_util.sanitize_id(refund)
                    ),
                    api_key=api_key,
                    stripe_version=stripe_version,
                    stripe_account=stripe_account,
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def expire(
            refund: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack[
                "Refund.ExpireParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "Refund":
            """
            Expire a refund with a status of requires_action.
            """
            ...

        @overload
        def expire(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "Refund.ExpireParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "Refund":
            """
            Expire a refund with a status of requires_action.
            """
            ...

        @class_method_variant("_cls_expire")
        def expire(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack[
                "Refund.ExpireParams"
            ]  # pyright: ignore[reportGeneralTypeIssues]
        ) -> "Refund":
            """
            Expire a refund with a status of requires_action.
            """
            return cast(
                "Refund",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/refunds/{refund}/expire".format(
                        refund=_util.sanitize_id(self.resource.get("id"))
                    ),
                    idempotency_key=idempotency_key,
                    params=params,
                ),
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {
        "destination_details": DestinationDetails,
        "next_action": NextAction,
    }


Refund.TestHelpers._resource_cls = Refund
