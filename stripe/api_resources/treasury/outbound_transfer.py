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


class OutboundTransfer(
    CreateableAPIResource["OutboundTransfer"],
    ListableAPIResource["OutboundTransfer"],
):
    """
    Use OutboundTransfers to transfer funds from a [FinancialAccount](https://stripe.com/docs/api#financial_accounts) to a PaymentMethod belonging to the same entity. To send funds to a different party, use [OutboundPayments](https://stripe.com/docs/api#outbound_payments) instead. You can send funds over ACH rails or through a domestic wire transfer to a user's own external bank account.

    Simulate OutboundTransfer state changes with the `/v1/test_helpers/treasury/outbound_transfers` endpoints. These methods can only be called on test mode objects.
    """

    OBJECT_NAME = "treasury.outbound_transfer"

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

        class UsBankAccount(StripeObject):
            account_holder_type: Optional[Literal["company", "individual"]]
            account_type: Optional[Literal["checking", "savings"]]
            bank_name: Optional[str]
            fingerprint: Optional[str]
            last4: Optional[str]
            network: Literal["ach", "us_domestic_wire"]
            routing_number: Optional[str]

        billing_details: BillingDetails
        type: Literal["us_bank_account"]
        us_bank_account: Optional[UsBankAccount]
        _inner_class_types = {
            "billing_details": BillingDetails,
            "us_bank_account": UsBankAccount,
        }

    class NetworkDetails(StripeObject):
        class Ach(StripeObject):
            addenda: Optional[str]

        ach: Optional[Ach]
        type: Literal["ach"]
        _inner_class_types = {"ach": Ach}

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
    description: Optional[str]
    destination_payment_method: Optional[str]
    destination_payment_method_details: DestinationPaymentMethodDetails
    expected_arrival_date: int
    financial_account: str
    hosted_regulatory_receipt_url: Optional[str]
    id: str
    livemode: bool
    metadata: Dict[str, str]
    network_details: Optional[NetworkDetails]
    object: Literal["treasury.outbound_transfer"]
    returned_details: Optional[ReturnedDetails]
    statement_descriptor: str
    status: Literal["canceled", "failed", "posted", "processing", "returned"]
    status_transitions: StatusTransitions
    transaction: ExpandableField["Transaction"]

    @classmethod
    def _cls_cancel(
        cls,
        outbound_transfer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/treasury/outbound_transfers/{outbound_transfer}/cancel".format(
                outbound_transfer=util.sanitize_id(outbound_transfer)
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
            "/v1/treasury/outbound_transfers/{outbound_transfer}/cancel".format(
                outbound_transfer=util.sanitize_id(self.get("id"))
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
    ) -> "OutboundTransfer":
        return cast(
            "OutboundTransfer",
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
    ) -> ListObject["OutboundTransfer"]:
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
    ) -> "OutboundTransfer":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    class TestHelpers(APIResourceTestHelpers["OutboundTransfer"]):
        _resource_cls: Type["OutboundTransfer"]

        @classmethod
        def _cls_fail(
            cls,
            outbound_transfer: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail".format(
                    outbound_transfer=util.sanitize_id(outbound_transfer)
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
                "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail".format(
                    outbound_transfer=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_post(
            cls,
            outbound_transfer: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post".format(
                    outbound_transfer=util.sanitize_id(outbound_transfer)
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
                "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post".format(
                    outbound_transfer=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_return_outbound_transfer(
            cls,
            outbound_transfer: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return".format(
                    outbound_transfer=util.sanitize_id(outbound_transfer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_return_outbound_transfer")
        def return_outbound_transfer(
            self, idempotency_key: Optional[str] = None, **params: Any
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return".format(
                    outbound_transfer=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {
        "destination_payment_method_details": DestinationPaymentMethodDetails,
        "network_details": NetworkDetails,
        "returned_details": ReturnedDetails,
        "status_transitions": StatusTransitions,
    }


OutboundTransfer.TestHelpers._resource_cls = OutboundTransfer
