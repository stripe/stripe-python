# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import APIResourceTestHelpers
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Dict
from typing import Optional
from typing_extensions import Literal
from typing_extensions import Type

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.issuing.cardholder import Cardholder


class Card(
    CreateableAPIResource["Card"],
    ListableAPIResource["Card"],
    UpdateableAPIResource["Card"],
):
    """
    You can [create physical or virtual cards](https://stripe.com/docs/issuing/cards) that are issued to cardholders.
    """

    OBJECT_NAME = "issuing.card"
    brand: str
    cancellation_reason: Optional[str]
    cardholder: "Cardholder"
    created: str
    currency: str
    cvc: str
    exp_month: int
    exp_year: int
    financial_account: Optional[str]
    id: str
    last4: str
    livemode: bool
    metadata: Dict[str, str]
    number: str
    object: Literal["issuing.card"]
    replaced_by: Optional[ExpandableField["Card"]]
    replacement_for: Optional[ExpandableField["Card"]]
    replacement_reason: Optional[str]
    shipping: Optional[StripeObject]
    spending_controls: StripeObject
    status: str
    type: str
    wallets: Optional[StripeObject]

    class TestHelpers(APIResourceTestHelpers["Card"]):
        _resource_cls: Type["Card"]

        @classmethod
        def _cls_deliver_card(
            cls,
            card,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/deliver".format(
                    card=util.sanitize_id(card)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_deliver_card")
        def deliver_card(self, idempotency_key=None, **params):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/deliver".format(
                    card=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_fail_card(
            cls,
            card,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/fail".format(
                    card=util.sanitize_id(card)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_fail_card")
        def fail_card(self, idempotency_key=None, **params):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/fail".format(
                    card=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_return_card(
            cls,
            card,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/return".format(
                    card=util.sanitize_id(card)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_return_card")
        def return_card(self, idempotency_key=None, **params):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/return".format(
                    card=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_ship_card(
            cls,
            card,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/ship".format(
                    card=util.sanitize_id(card)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_ship_card")
        def ship_card(self, idempotency_key=None, **params):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/ship".format(
                    card=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)


Card.TestHelpers._resource_cls = Card
