# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    APIResourceTestHelpers,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal, Type
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.issuing.card import Card
    from stripe.api_resources.issuing.cardholder import Cardholder
    from stripe.api_resources.issuing.token import Token
    from stripe.api_resources.issuing.transaction import Transaction


class Authorization(
    ListableAPIResource["Authorization"],
    UpdateableAPIResource["Authorization"],
):
    """
    When an [issued card](https://stripe.com/docs/issuing) is used to make a purchase, an Issuing `Authorization`
    object is created. [Authorizations](https://stripe.com/docs/issuing/purchases/authorizations) must be approved for the
    purchase to be completed successfully.

    Related guide: [Issued card authorizations](https://stripe.com/docs/issuing/purchases/authorizations)
    """

    OBJECT_NAME = "issuing.authorization"

    class AmountDetails(StripeObject):
        atm_fee: Optional[int]
        cashback_amount: Optional[int]

    class MerchantData(StripeObject):
        category: str
        category_code: str
        city: Optional[str]
        country: Optional[str]
        name: Optional[str]
        network_id: str
        postal_code: Optional[str]
        state: Optional[str]
        terminal_id: Optional[str]
        url: Optional[str]

    class NetworkData(StripeObject):
        acquiring_institution_id: Optional[str]

    class PendingRequest(StripeObject):
        class AmountDetails(StripeObject):
            atm_fee: Optional[int]
            cashback_amount: Optional[int]

        amount: int
        amount_details: Optional[AmountDetails]
        currency: str
        is_amount_controllable: bool
        merchant_amount: int
        merchant_currency: str
        _inner_class_types = {"amount_details": AmountDetails}

    class RequestHistory(StripeObject):
        class AmountDetails(StripeObject):
            atm_fee: Optional[int]
            cashback_amount: Optional[int]

        amount: int
        amount_details: Optional[AmountDetails]
        approved: bool
        authorization_code: Optional[str]
        created: int
        currency: str
        merchant_amount: int
        merchant_currency: str
        reason: Literal[
            "account_disabled",
            "card_active",
            "card_inactive",
            "cardholder_inactive",
            "cardholder_verification_required",
            "insufficient_funds",
            "not_allowed",
            "spending_controls",
            "suspected_fraud",
            "verification_failed",
            "webhook_approved",
            "webhook_declined",
            "webhook_error",
            "webhook_timeout",
        ]
        reason_message: Optional[str]
        _inner_class_types = {"amount_details": AmountDetails}

    class Treasury(StripeObject):
        received_credits: List[str]
        received_debits: List[str]
        transaction: Optional[str]

    class VerificationData(StripeObject):
        class ThreeDSecure(StripeObject):
            result: Literal[
                "attempt_acknowledged", "authenticated", "failed", "required"
            ]

        address_line1_check: Literal["match", "mismatch", "not_provided"]
        address_postal_code_check: Literal["match", "mismatch", "not_provided"]
        cvc_check: Literal["match", "mismatch", "not_provided"]
        expiry_check: Literal["match", "mismatch", "not_provided"]
        postal_code: Optional[str]
        three_d_secure: Optional[ThreeDSecure]
        _inner_class_types = {"three_d_secure": ThreeDSecure}

    amount: int
    amount_details: Optional[AmountDetails]
    approved: bool
    authorization_method: Literal[
        "chip", "contactless", "keyed_in", "online", "swipe"
    ]
    balance_transactions: List["BalanceTransaction"]
    card: "Card"
    cardholder: Optional[ExpandableField["Cardholder"]]
    created: int
    currency: str
    id: str
    livemode: bool
    merchant_amount: int
    merchant_currency: str
    merchant_data: MerchantData
    metadata: Dict[str, str]
    network_data: Optional[NetworkData]
    object: Literal["issuing.authorization"]
    pending_request: Optional[PendingRequest]
    request_history: List[RequestHistory]
    status: Literal["closed", "pending", "reversed"]
    token: Optional[ExpandableField["Token"]]
    transactions: List["Transaction"]
    treasury: Optional[Treasury]
    verification_data: VerificationData
    wallet: Optional[str]

    @classmethod
    def _cls_approve(
        cls,
        authorization: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/issuing/authorizations/{authorization}/approve".format(
                authorization=util.sanitize_id(authorization)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_approve")
    def approve(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/issuing/authorizations/{authorization}/approve".format(
                authorization=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_decline(
        cls,
        authorization: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/issuing/authorizations/{authorization}/decline".format(
                authorization=util.sanitize_id(authorization)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_decline")
    def decline(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/issuing/authorizations/{authorization}/decline".format(
                authorization=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["Authorization"]:
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
    def modify(cls, id, **params: Any) -> "Authorization":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Authorization",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Authorization":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    class TestHelpers(APIResourceTestHelpers["Authorization"]):
        _resource_cls: Type["Authorization"]

        @classmethod
        def _cls_capture(
            cls,
            authorization: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/capture".format(
                    authorization=util.sanitize_id(authorization)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_capture")
        def capture(
            self, idempotency_key: Optional[str] = None, **params: Any
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/capture".format(
                    authorization=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def create(
            cls,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/authorizations",
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @classmethod
        def _cls_expire(
            cls,
            authorization: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/expire".format(
                    authorization=util.sanitize_id(authorization)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_expire")
        def expire(self, idempotency_key: Optional[str] = None, **params: Any):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/expire".format(
                    authorization=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_increment(
            cls,
            authorization: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/increment".format(
                    authorization=util.sanitize_id(authorization)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_increment")
        def increment(
            self, idempotency_key: Optional[str] = None, **params: Any
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/increment".format(
                    authorization=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_reverse(
            cls,
            authorization: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/reverse".format(
                    authorization=util.sanitize_id(authorization)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_reverse")
        def reverse(
            self, idempotency_key: Optional[str] = None, **params: Any
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{authorization}/reverse".format(
                    authorization=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {
        "amount_details": AmountDetails,
        "merchant_data": MerchantData,
        "network_data": NetworkData,
        "pending_request": PendingRequest,
        "request_history": RequestHistory,
        "treasury": Treasury,
        "verification_data": VerificationData,
    }


Authorization.TestHelpers._resource_cls = Authorization
