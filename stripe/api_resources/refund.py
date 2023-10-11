# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    APIResourceTestHelpers,
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, Type, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.reversal import Reversal


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

    OBJECT_NAME = "refund"

    class CancelParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class CreateParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        charge: NotRequired[Optional[str]]
        currency: NotRequired[Optional[str]]
        customer: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        instructions_email: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        origin: NotRequired[Optional[Literal["customer_balance"]]]
        payment_intent: NotRequired[Optional[str]]
        reason: NotRequired[
            Optional[
                Literal["duplicate", "fraudulent", "requested_by_customer"]
            ]
        ]
        refund_application_fee: NotRequired[Optional[bool]]
        reverse_transfer: NotRequired[Optional[bool]]

    class ListParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ModifyParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ExpireParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    amount: int
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    charge: Optional[ExpandableField["Charge"]]
    created: int
    currency: str
    description: Optional[str]
    failure_balance_transaction: Optional[
        ExpandableField["BalanceTransaction"]
    ]
    failure_reason: Optional[str]
    id: str
    instructions_email: Optional[str]
    metadata: Optional[Dict[str, str]]
    next_action: Optional[StripeObject]
    object: Literal["refund"]
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    reason: Optional[
        Literal[
            "duplicate",
            "expired_uncaptured_charge",
            "fraudulent",
            "requested_by_customer",
        ]
    ]
    receipt_number: Optional[str]
    source_transfer_reversal: Optional[ExpandableField["Reversal"]]
    status: Optional[str]
    transfer_reversal: Optional[ExpandableField["Reversal"]]

    @classmethod
    def _cls_cancel(
        cls,
        refund: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Refund.CancelParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/refunds/{refund}/cancel".format(
                refund=util.sanitize_id(refund)
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
        **params: Unpack["Refund.CancelParams"]
    ):
        return self._request(
            "post",
            "/v1/refunds/{refund}/cancel".format(
                refund=util.sanitize_id(self.get("id"))
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
        **params: Unpack["Refund.CreateParams"]
    ) -> "Refund":
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
        **params: Unpack["Refund.ListParams"]
    ) -> ListObject["Refund"]:
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
    def modify(cls, id, **params: Unpack["Refund.ModifyParams"]) -> "Refund":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Refund",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Refund.RetrieveParams"]
    ) -> "Refund":
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
            **params: Unpack["Refund.ExpireParams"]
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/refunds/{refund}/expire".format(
                    refund=util.sanitize_id(refund)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_expire")
        def expire(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["Refund.ExpireParams"]
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/refunds/{refund}/expire".format(
                    refund=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)


Refund.TestHelpers._resource_cls = Refund
