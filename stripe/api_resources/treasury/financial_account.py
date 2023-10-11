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
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
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

    class CreateParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        features: NotRequired[
            Optional["FinancialAccount.CreateFeaturesParams"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        platform_restrictions: NotRequired[
            Optional["FinancialAccount.CreatePlatformRestrictionsParams"]
        ]
        supported_currencies: List[str]

    class CreatePlatformRestrictionsParams(TypedDict):
        inbound_flows: NotRequired[
            Optional[Literal["restricted", "unrestricted"]]
        ]
        outbound_flows: NotRequired[
            Optional[Literal["restricted", "unrestricted"]]
        ]

    class CreateFeaturesParams(TypedDict):
        card_issuing: NotRequired[
            Optional["FinancialAccount.CreateFeaturesCardIssuingParams"]
        ]
        deposit_insurance: NotRequired[
            Optional["FinancialAccount.CreateFeaturesDepositInsuranceParams"]
        ]
        financial_addresses: NotRequired[
            Optional["FinancialAccount.CreateFeaturesFinancialAddressesParams"]
        ]
        inbound_transfers: NotRequired[
            Optional["FinancialAccount.CreateFeaturesInboundTransfersParams"]
        ]
        intra_stripe_flows: NotRequired[
            Optional["FinancialAccount.CreateFeaturesIntraStripeFlowsParams"]
        ]
        outbound_payments: NotRequired[
            Optional["FinancialAccount.CreateFeaturesOutboundPaymentsParams"]
        ]
        outbound_transfers: NotRequired[
            Optional["FinancialAccount.CreateFeaturesOutboundTransfersParams"]
        ]

    class CreateFeaturesOutboundTransfersParams(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.CreateFeaturesOutboundTransfersAchParams"
            ]
        ]
        us_domestic_wire: NotRequired[
            Optional[
                "FinancialAccount.CreateFeaturesOutboundTransfersUsDomesticWireParams"
            ]
        ]

    class CreateFeaturesOutboundTransfersUsDomesticWireParams(TypedDict):
        requested: bool

    class CreateFeaturesOutboundTransfersAchParams(TypedDict):
        requested: bool

    class CreateFeaturesOutboundPaymentsParams(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.CreateFeaturesOutboundPaymentsAchParams"
            ]
        ]
        us_domestic_wire: NotRequired[
            Optional[
                "FinancialAccount.CreateFeaturesOutboundPaymentsUsDomesticWireParams"
            ]
        ]

    class CreateFeaturesOutboundPaymentsUsDomesticWireParams(TypedDict):
        requested: bool

    class CreateFeaturesOutboundPaymentsAchParams(TypedDict):
        requested: bool

    class CreateFeaturesIntraStripeFlowsParams(TypedDict):
        requested: bool

    class CreateFeaturesInboundTransfersParams(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.CreateFeaturesInboundTransfersAchParams"
            ]
        ]

    class CreateFeaturesInboundTransfersAchParams(TypedDict):
        requested: bool

    class CreateFeaturesFinancialAddressesParams(TypedDict):
        aba: NotRequired[
            Optional[
                "FinancialAccount.CreateFeaturesFinancialAddressesAbaParams"
            ]
        ]

    class CreateFeaturesFinancialAddressesAbaParams(TypedDict):
        requested: bool

    class CreateFeaturesDepositInsuranceParams(TypedDict):
        requested: bool

    class CreateFeaturesCardIssuingParams(TypedDict):
        requested: bool

    class ListParams(RequestOptions):
        created: NotRequired[
            Optional[Union["FinancialAccount.ListCreatedParams", int]]
        ]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ListCreatedParams(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        features: NotRequired[
            Optional["FinancialAccount.ModifyFeaturesParams"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        platform_restrictions: NotRequired[
            Optional["FinancialAccount.ModifyPlatformRestrictionsParams"]
        ]

    class ModifyPlatformRestrictionsParams(TypedDict):
        inbound_flows: NotRequired[
            Optional[Literal["restricted", "unrestricted"]]
        ]
        outbound_flows: NotRequired[
            Optional[Literal["restricted", "unrestricted"]]
        ]

    class ModifyFeaturesParams(TypedDict):
        card_issuing: NotRequired[
            Optional["FinancialAccount.ModifyFeaturesCardIssuingParams"]
        ]
        deposit_insurance: NotRequired[
            Optional["FinancialAccount.ModifyFeaturesDepositInsuranceParams"]
        ]
        financial_addresses: NotRequired[
            Optional["FinancialAccount.ModifyFeaturesFinancialAddressesParams"]
        ]
        inbound_transfers: NotRequired[
            Optional["FinancialAccount.ModifyFeaturesInboundTransfersParams"]
        ]
        intra_stripe_flows: NotRequired[
            Optional["FinancialAccount.ModifyFeaturesIntraStripeFlowsParams"]
        ]
        outbound_payments: NotRequired[
            Optional["FinancialAccount.ModifyFeaturesOutboundPaymentsParams"]
        ]
        outbound_transfers: NotRequired[
            Optional["FinancialAccount.ModifyFeaturesOutboundTransfersParams"]
        ]

    class ModifyFeaturesOutboundTransfersParams(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.ModifyFeaturesOutboundTransfersAchParams"
            ]
        ]
        us_domestic_wire: NotRequired[
            Optional[
                "FinancialAccount.ModifyFeaturesOutboundTransfersUsDomesticWireParams"
            ]
        ]

    class ModifyFeaturesOutboundTransfersUsDomesticWireParams(TypedDict):
        requested: bool

    class ModifyFeaturesOutboundTransfersAchParams(TypedDict):
        requested: bool

    class ModifyFeaturesOutboundPaymentsParams(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.ModifyFeaturesOutboundPaymentsAchParams"
            ]
        ]
        us_domestic_wire: NotRequired[
            Optional[
                "FinancialAccount.ModifyFeaturesOutboundPaymentsUsDomesticWireParams"
            ]
        ]

    class ModifyFeaturesOutboundPaymentsUsDomesticWireParams(TypedDict):
        requested: bool

    class ModifyFeaturesOutboundPaymentsAchParams(TypedDict):
        requested: bool

    class ModifyFeaturesIntraStripeFlowsParams(TypedDict):
        requested: bool

    class ModifyFeaturesInboundTransfersParams(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.ModifyFeaturesInboundTransfersAchParams"
            ]
        ]

    class ModifyFeaturesInboundTransfersAchParams(TypedDict):
        requested: bool

    class ModifyFeaturesFinancialAddressesParams(TypedDict):
        aba: NotRequired[
            Optional[
                "FinancialAccount.ModifyFeaturesFinancialAddressesAbaParams"
            ]
        ]

    class ModifyFeaturesFinancialAddressesAbaParams(TypedDict):
        requested: bool

    class ModifyFeaturesDepositInsuranceParams(TypedDict):
        requested: bool

    class ModifyFeaturesCardIssuingParams(TypedDict):
        requested: bool

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class RetrieveFeaturesParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class UpdateFeaturesParams(RequestOptions):
        card_issuing: NotRequired[
            Optional["FinancialAccount.UpdateFeaturesCardIssuingParams"]
        ]
        deposit_insurance: NotRequired[
            Optional["FinancialAccount.UpdateFeaturesDepositInsuranceParams"]
        ]
        expand: NotRequired[Optional[List[str]]]
        financial_addresses: NotRequired[
            Optional["FinancialAccount.UpdateFeaturesFinancialAddressesParams"]
        ]
        inbound_transfers: NotRequired[
            Optional["FinancialAccount.UpdateFeaturesInboundTransfersParams"]
        ]
        intra_stripe_flows: NotRequired[
            Optional["FinancialAccount.UpdateFeaturesIntraStripeFlowsParams"]
        ]
        outbound_payments: NotRequired[
            Optional["FinancialAccount.UpdateFeaturesOutboundPaymentsParams"]
        ]
        outbound_transfers: NotRequired[
            Optional["FinancialAccount.UpdateFeaturesOutboundTransfersParams"]
        ]

    class UpdateFeaturesOutboundTransfersParams(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.UpdateFeaturesOutboundTransfersAchParams"
            ]
        ]
        us_domestic_wire: NotRequired[
            Optional[
                "FinancialAccount.UpdateFeaturesOutboundTransfersUsDomesticWireParams"
            ]
        ]

    class UpdateFeaturesOutboundTransfersUsDomesticWireParams(TypedDict):
        requested: bool

    class UpdateFeaturesOutboundTransfersAchParams(TypedDict):
        requested: bool

    class UpdateFeaturesOutboundPaymentsParams(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.UpdateFeaturesOutboundPaymentsAchParams"
            ]
        ]
        us_domestic_wire: NotRequired[
            Optional[
                "FinancialAccount.UpdateFeaturesOutboundPaymentsUsDomesticWireParams"
            ]
        ]

    class UpdateFeaturesOutboundPaymentsUsDomesticWireParams(TypedDict):
        requested: bool

    class UpdateFeaturesOutboundPaymentsAchParams(TypedDict):
        requested: bool

    class UpdateFeaturesIntraStripeFlowsParams(TypedDict):
        requested: bool

    class UpdateFeaturesInboundTransfersParams(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.UpdateFeaturesInboundTransfersAchParams"
            ]
        ]

    class UpdateFeaturesInboundTransfersAchParams(TypedDict):
        requested: bool

    class UpdateFeaturesFinancialAddressesParams(TypedDict):
        aba: NotRequired[
            Optional[
                "FinancialAccount.UpdateFeaturesFinancialAddressesAbaParams"
            ]
        ]

    class UpdateFeaturesFinancialAddressesAbaParams(TypedDict):
        requested: bool

    class UpdateFeaturesDepositInsuranceParams(TypedDict):
        requested: bool

    class UpdateFeaturesCardIssuingParams(TypedDict):
        requested: bool

    active_features: Optional[
        List[
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
    ]
    balance: StripeObject
    country: str
    created: int
    features: Optional["FinancialAccountFeatures"]
    financial_addresses: List[StripeObject]
    id: str
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["treasury.financial_account"]
    pending_features: Optional[
        List[
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
    ]
    platform_restrictions: Optional[StripeObject]
    restricted_features: Optional[
        List[
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
    ]
    status: Literal["closed", "open"]
    status_details: StripeObject
    supported_currencies: List[str]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["FinancialAccount.CreateParams"]
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
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["FinancialAccount.ListParams"]
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
    def modify(
        cls, id, **params: Unpack["FinancialAccount.ModifyParams"]
    ) -> "FinancialAccount":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "FinancialAccount",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["FinancialAccount.RetrieveParams"]
    ) -> "FinancialAccount":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_retrieve_features(
        cls,
        financial_account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["FinancialAccount.RetrieveFeaturesParams"]
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
    def retrieve_features(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["FinancialAccount.RetrieveFeaturesParams"]
    ):
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
        financial_account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["FinancialAccount.UpdateFeaturesParams"]
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
    def update_features(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["FinancialAccount.UpdateFeaturesParams"]
    ):
        return self._request(
            "post",
            "/v1/treasury/financial_accounts/{financial_account}/features".format(
                financial_account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
