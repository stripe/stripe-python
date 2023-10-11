# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.mandate import Mandate
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.setup_attempt import SetupAttempt


class SetupIntent(
    CreateableAPIResource["SetupIntent"],
    ListableAPIResource["SetupIntent"],
    UpdateableAPIResource["SetupIntent"],
):
    """
    A SetupIntent guides you through the process of setting up and saving a customer's payment credentials for future payments.
    For example, you can use a SetupIntent to set up and save your customer's card without immediately collecting a payment.
    Later, you can use [PaymentIntents](https://stripe.com/docs/api#payment_intents) to drive the payment flow.

    Create a SetupIntent when you're ready to collect your customer's payment credentials.
    Don't maintain long-lived, unconfirmed SetupIntents because they might not be valid.
    The SetupIntent transitions through multiple [statuses](https://stripe.com/docs/payments/intents#intent-statuses) as it guides
    you through the setup process.

    Successful SetupIntents result in payment credentials that are optimized for future payments.
    For example, cardholders in [certain regions](https://stripe.com/guides/strong-customer-authentication) might need to be run through
    [Strong Customer Authentication](https://stripe.com/docs/strong-customer-authentication) during payment method collection
    to streamline later [off-session payments](https://stripe.com/docs/payments/setup-intents).
    If you use the SetupIntent with a [Customer](https://stripe.com/docs/api#setup_intent_object-customer),
    it automatically attaches the resulting payment method to that Customer after successful setup.
    We recommend using SetupIntents or [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage) on
    PaymentIntents to save payment methods to prevent saving invalid or unoptimized payment methods.

    By using SetupIntents, you can reduce friction for your customers, even as regulations change over time.

    Related guide: [Setup Intents API](https://stripe.com/docs/payments/setup-intents)
    """

    OBJECT_NAME = "setup_intent"
    application: Optional[ExpandableField["Application"]]
    attach_to_self: Optional[bool]
    automatic_payment_methods: Optional[StripeObject]
    cancellation_reason: Optional[
        Literal["abandoned", "duplicate", "requested_by_customer"]
    ]
    client_secret: Optional[str]
    created: int
    customer: Optional[ExpandableField["Customer"]]
    description: Optional[str]
    flow_directions: Optional[List[Literal["inbound", "outbound"]]]
    id: str
    last_setup_error: Optional[StripeObject]
    latest_attempt: Optional[ExpandableField["SetupAttempt"]]
    livemode: bool
    mandate: Optional[ExpandableField["Mandate"]]
    metadata: Optional[Dict[str, str]]
    next_action: Optional[StripeObject]
    object: Literal["setup_intent"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    payment_method: Optional[ExpandableField["PaymentMethod"]]
    payment_method_configuration_details: Optional[StripeObject]
    payment_method_options: Optional[StripeObject]
    payment_method_types: List[str]
    single_use_mandate: Optional[ExpandableField["Mandate"]]
    status: Literal[
        "canceled",
        "processing",
        "requires_action",
        "requires_confirmation",
        "requires_payment_method",
        "succeeded",
    ]
    usage: str

    @classmethod
    def _cls_cancel(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/setup_intents/{intent}/cancel".format(
                intent=util.sanitize_id(intent)
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
            "/v1/setup_intents/{intent}/cancel".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_confirm(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/setup_intents/{intent}/confirm".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_confirm")
    def confirm(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/setup_intents/{intent}/confirm".format(
                intent=util.sanitize_id(self.get("id"))
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
    ) -> "SetupIntent":
        return cast(
            "SetupIntent",
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
    ) -> ListObject["SetupIntent"]:
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
    def modify(cls, id, **params: Any) -> "SetupIntent":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "SetupIntent",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "SetupIntent":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_verify_microdeposits(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/setup_intents/{intent}/verify_microdeposits".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_verify_microdeposits")
    def verify_microdeposits(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/setup_intents/{intent}/verify_microdeposits".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
