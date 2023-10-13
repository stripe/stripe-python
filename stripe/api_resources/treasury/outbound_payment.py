# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    APIResourceTestHelpers,
    CreateableAPIResource,
    ListableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    Type,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.api_resources.treasury.transaction import Transaction


class OutboundPayment(
    CreateableAPIResource["OutboundPayment"],
    ListableAPIResource["OutboundPayment"],
):
    """
    Use OutboundPayments to send funds to another party's external bank account or [FinancialAccount](https://stripe.com/docs/api#financial_accounts). To send money to an account belonging to the same user, use an [OutboundTransfer](https://stripe.com/docs/api#outbound_transfers).

    Simulate OutboundPayment state changes with the `/v1/test_helpers/treasury/outbound_payments` endpoints. These methods can only be called on test mode objects.
    """

    OBJECT_NAME = "treasury.outbound_payment"
    if TYPE_CHECKING:

        class CancelParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateParams(RequestOptions):
            amount: int
            currency: str
            customer: NotRequired["str|None"]
            description: NotRequired["str|None"]
            destination_payment_method: NotRequired["str|None"]
            destination_payment_method_data: NotRequired[
                "OutboundPayment.CreateParamsDestinationPaymentMethodData|None"
            ]
            destination_payment_method_options: NotRequired[
                "OutboundPayment.CreateParamsDestinationPaymentMethodOptions|None"
            ]
            end_user_details: NotRequired[
                "OutboundPayment.CreateParamsEndUserDetails|None"
            ]
            expand: NotRequired["List[str]|None"]
            financial_account: str
            metadata: NotRequired["Dict[str, str]|None"]
            statement_descriptor: NotRequired["str|None"]

        class CreateParamsEndUserDetails(TypedDict):
            ip_address: NotRequired["str|None"]
            present: bool

        class CreateParamsDestinationPaymentMethodOptions(TypedDict):
            us_bank_account: NotRequired[
                "Literal['']|OutboundPayment.CreateParamsDestinationPaymentMethodOptionsUsBankAccount|None"
            ]

        class CreateParamsDestinationPaymentMethodOptionsUsBankAccount(
            TypedDict,
        ):
            network: NotRequired["Literal['ach', 'us_domestic_wire']|None"]

        class CreateParamsDestinationPaymentMethodData(TypedDict):
            billing_details: NotRequired[
                "OutboundPayment.CreateParamsDestinationPaymentMethodDataBillingDetails|None"
            ]
            financial_account: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            type: Literal["financial_account", "us_bank_account"]
            us_bank_account: NotRequired[
                "OutboundPayment.CreateParamsDestinationPaymentMethodDataUsBankAccount|None"
            ]

        class CreateParamsDestinationPaymentMethodDataUsBankAccount(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            account_number: NotRequired["str|None"]
            account_type: NotRequired["Literal['checking', 'savings']|None"]
            financial_connections_account: NotRequired["str|None"]
            routing_number: NotRequired["str|None"]

        class CreateParamsDestinationPaymentMethodDataBillingDetails(
            TypedDict
        ):
            address: NotRequired[
                "Literal['']|OutboundPayment.CreateParamsDestinationPaymentMethodDataBillingDetailsAddress|None"
            ]
            email: NotRequired["Literal['']|str|None"]
            name: NotRequired["Literal['']|str|None"]
            phone: NotRequired["Literal['']|str|None"]

        class CreateParamsDestinationPaymentMethodDataBillingDetailsAddress(
            TypedDict,
        ):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ListParams(RequestOptions):
            customer: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            financial_account: str
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired[
                "Literal['canceled', 'failed', 'posted', 'processing', 'returned']|None"
            ]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class FailParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class PostParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ReturnOutboundPaymentParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            returned_details: NotRequired[
                "OutboundPayment.ReturnOutboundPaymentParamsReturnedDetails|None"
            ]

        class ReturnOutboundPaymentParamsReturnedDetails(TypedDict):
            code: NotRequired[
                "Literal['account_closed', 'account_frozen', 'bank_account_restricted', 'bank_ownership_changed', 'declined', 'incorrect_account_holder_name', 'invalid_account_number', 'invalid_currency', 'no_account', 'other']|None"
            ]

    amount: int
    cancelable: bool
    created: int
    currency: str
    customer: Optional[str]
    description: Optional[str]
    destination_payment_method: Optional[str]
    destination_payment_method_details: Optional[StripeObject]
    end_user_details: Optional[StripeObject]
    expected_arrival_date: int
    financial_account: str
    hosted_regulatory_receipt_url: Optional[str]
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["treasury.outbound_payment"]
    returned_details: Optional[StripeObject]
    statement_descriptor: str
    status: Literal["canceled", "failed", "posted", "processing", "returned"]
    status_transitions: StripeObject
    transaction: ExpandableField["Transaction"]

    @classmethod
    def _cls_cancel(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["OutboundPayment.CancelParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/treasury/outbound_payments/{id}/cancel".format(
                id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["OutboundPayment.CancelParams"]
    ):
        return self._request(
            "post",
            "/v1/treasury/outbound_payments/{id}/cancel".format(
                id=util.sanitize_id(self.get("id"))
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
        **params: Unpack["OutboundPayment.CreateParams"]
    ) -> "OutboundPayment":
        return cast(
            "OutboundPayment",
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
        **params: Unpack["OutboundPayment.ListParams"]
    ) -> ListObject["OutboundPayment"]:
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
        cls, id: str, **params: Unpack["OutboundPayment.RetrieveParams"]
    ) -> "OutboundPayment":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    class TestHelpers(APIResourceTestHelpers["OutboundPayment"]):
        _resource_cls: Type["OutboundPayment"]

        @classmethod
        def _cls_fail(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["OutboundPayment.FailParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/fail".format(
                    id=util.sanitize_id(id)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_fail")
        def fail(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["OutboundPayment.FailParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/fail".format(
                    id=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_post(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["OutboundPayment.PostParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/post".format(
                    id=util.sanitize_id(id)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_post")
        def post(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["OutboundPayment.PostParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/post".format(
                    id=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_return_outbound_payment(
            cls,
            id: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["OutboundPayment.ReturnOutboundPaymentParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/return".format(
                    id=util.sanitize_id(id)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_return_outbound_payment")
        def return_outbound_payment(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["OutboundPayment.ReturnOutboundPaymentParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/treasury/outbound_payments/{id}/return".format(
                    id=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)


OutboundPayment.TestHelpers._resource_cls = OutboundPayment
