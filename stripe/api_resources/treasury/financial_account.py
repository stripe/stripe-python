# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.treasury.financial_account_features import (
        FinancialAccountFeatures,
    )


class FinancialAccount(
    CreateableAPIResource["FinancialAccount"],
    ListableAPIResource["FinancialAccount"],
    UpdateableAPIResource["FinancialAccount"],
):
    """
    Stripe Treasury provides users with a container for money called a FinancialAccount that is separate from their Payments balance.
    FinancialAccounts serve as the source and destination of Treasury's money movement APIs.
    """

    OBJECT_NAME = "treasury.financial_account"
    active_features: List[
        Literal[
            "card_issuing",
            "deposit_insurance",
            "financial_addresses.aba",
            "inbound_transfers.ach",
            "intra_stripe_flows",
            "outbound_payments.ach",
            "outbound_payments.us_domestic_wire",
            "outbound_transfers.ach",
            "outbound_transfers.us_domestic_wire",
            "remote_deposit_capture",
        ]
    ]
    balance: StripeObject
    country: str
    created: int
    features: "FinancialAccountFeatures"
    financial_addresses: List[StripeObject]
    id: str
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["treasury.financial_account"]
    pending_features: List[
        Literal[
            "card_issuing",
            "deposit_insurance",
            "financial_addresses.aba",
            "inbound_transfers.ach",
            "intra_stripe_flows",
            "outbound_payments.ach",
            "outbound_payments.us_domestic_wire",
            "outbound_transfers.ach",
            "outbound_transfers.us_domestic_wire",
            "remote_deposit_capture",
        ]
    ]
    platform_restrictions: Optional[StripeObject]
    restricted_features: List[
        Literal[
            "card_issuing",
            "deposit_insurance",
            "financial_addresses.aba",
            "inbound_transfers.ach",
            "intra_stripe_flows",
            "outbound_payments.ach",
            "outbound_payments.us_domestic_wire",
            "outbound_transfers.ach",
            "outbound_transfers.us_domestic_wire",
            "remote_deposit_capture",
        ]
    ]
    status: Literal["closed", "open"]
    status_details: StripeObject
    supported_currencies: List[str]

    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ) -> "FinancialAccount":
        return cast(
            "FinancialAccount",
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
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ) -> ListObject["FinancialAccount"]:
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
    def modify(cls, id, **params) -> "FinancialAccount":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "FinancialAccount",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(cls, id, api_key=None, **params) -> "FinancialAccount":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_retrieve_features(
        cls,
        financial_account,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "get",
            "/v1/treasury/financial_accounts/{financial_account}/features".format(
                financial_account=util.sanitize_id(financial_account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_retrieve_features")
    def retrieve_features(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/treasury/financial_accounts/{financial_account}/features".format(
                financial_account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_update_features(
        cls,
        financial_account,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/treasury/financial_accounts/{financial_account}/features".format(
                financial_account=util.sanitize_id(financial_account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_update_features")
    def update_features(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/treasury/financial_accounts/{financial_account}/features".format(
                financial_account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
