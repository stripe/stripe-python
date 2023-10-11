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
from stripe.stripe_object import StripeObject
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, Type

from typing_extensions import TYPE_CHECKING

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

    class DestinationPaymentMethodDetails(StripeObject):
        class BillingDetails(StripeObject):
            class Address(StripeObject):
                city: Optional[str]
                country: Optional[str]
                line1: Optional[str]
                line2: Optional[str]
                postal_code: Optional[str]
                state: Optional[str]

            address: Address
            email: Optional[str]
            name: Optional[str]
            _inner_class_types = {"address": Address}

        class FinancialAccount(StripeObject):
            id: str
            network: Literal["stripe"]

        class UsBankAccount(StripeObject):
            account_holder_type: Optional[Literal["company", "individual"]]
            account_type: Optional[Literal["checking", "savings"]]
            bank_name: Optional[str]
            fingerprint: Optional[str]
            last4: Optional[str]
            network: Literal["ach", "us_domestic_wire"]
            routing_number: Optional[str]

        billing_details: BillingDetails
        financial_account: Optional[FinancialAccount]
        type: Literal["financial_account", "us_bank_account"]
        us_bank_account: Optional[UsBankAccount]
        _inner_class_types = {
            "billing_details": BillingDetails,
            "financial_account": FinancialAccount,
            "us_bank_account": UsBankAccount,
        }

    class EndUserDetails(StripeObject):
        ip_address: Optional[str]
        present: bool

    class ReturnedDetails(StripeObject):
        code: Literal[
            "account_closed",
            "account_frozen",
            "bank_account_restricted",
            "bank_ownership_changed",
            "declined",
            "incorrect_account_holder_name",
            "invalid_account_number",
            "invalid_currency",
            "no_account",
            "other",
        ]
        transaction: ExpandableField["Transaction"]

    class StatusTransitions(StripeObject):
        canceled_at: Optional[int]
        failed_at: Optional[int]
        posted_at: Optional[int]
        returned_at: Optional[int]

    amount: int
    cancelable: bool
    created: int
    currency: str
    customer: Optional[str]
    description: Optional[str]
    destination_payment_method: Optional[str]
    destination_payment_method_details: Optional[
        DestinationPaymentMethodDetails
    ]
    end_user_details: Optional[EndUserDetails]
    expected_arrival_date: int
    financial_account: str
    hosted_regulatory_receipt_url: Optional[str]
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["treasury.outbound_payment"]
    returned_details: Optional[ReturnedDetails]
    statement_descriptor: str
    status: Literal["canceled", "failed", "posted", "processing", "returned"]
    status_transitions: StatusTransitions
    transaction: ExpandableField["Transaction"]

    @classmethod
    def _cls_cancel(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def cancel(self, idempotency_key: Optional[str] = None, **params: Any):
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
        **params: Any
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
        **params: Any
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
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "OutboundPayment":
        instance = cls(id, api_key, **params)
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
            **params: Any
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
        def fail(self, idempotency_key: Optional[str] = None, **params: Any):
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
            **params: Any
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
        def post(self, idempotency_key: Optional[str] = None, **params: Any):
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
            **params: Any
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
            self, idempotency_key: Optional[str] = None, **params: Any
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

    _inner_class_types = {
        "destination_payment_method_details": DestinationPaymentMethodDetails,
        "end_user_details": EndUserDetails,
        "returned_details": ReturnedDetails,
        "status_transitions": StatusTransitions,
    }


OutboundPayment.TestHelpers._resource_cls = OutboundPayment
