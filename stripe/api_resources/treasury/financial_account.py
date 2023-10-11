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
            Optional["FinancialAccount.CreateParamsFeatures"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        platform_restrictions: NotRequired[
            Optional["FinancialAccount.CreateParamsPlatformRestrictions"]
        ]
        supported_currencies: List[str]

    class CreateParamsPlatformRestrictions(TypedDict):
        inbound_flows: NotRequired[
            Optional[Literal["restricted", "unrestricted"]]
        ]
        outbound_flows: NotRequired[
            Optional[Literal["restricted", "unrestricted"]]
        ]

    class CreateParamsFeatures(TypedDict):
        card_issuing: NotRequired[
            Optional["FinancialAccount.CreateParamsFeaturesCardIssuing"]
        ]
        deposit_insurance: NotRequired[
            Optional["FinancialAccount.CreateParamsFeaturesDepositInsurance"]
        ]
        financial_addresses: NotRequired[
            Optional["FinancialAccount.CreateParamsFeaturesFinancialAddresses"]
        ]
        inbound_transfers: NotRequired[
            Optional["FinancialAccount.CreateParamsFeaturesInboundTransfers"]
        ]
        intra_stripe_flows: NotRequired[
            Optional["FinancialAccount.CreateParamsFeaturesIntraStripeFlows"]
        ]
        outbound_payments: NotRequired[
            Optional["FinancialAccount.CreateParamsFeaturesOutboundPayments"]
        ]
        outbound_transfers: NotRequired[
            Optional["FinancialAccount.CreateParamsFeaturesOutboundTransfers"]
        ]

    class CreateParamsFeaturesOutboundTransfers(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.CreateParamsFeaturesOutboundTransfersAch"
            ]
        ]
        us_domestic_wire: NotRequired[
            Optional[
                "FinancialAccount.CreateParamsFeaturesOutboundTransfersUsDomesticWire"
            ]
        ]

    class CreateParamsFeaturesOutboundTransfersUsDomesticWire(TypedDict):
        requested: bool

    class CreateParamsFeaturesOutboundTransfersAch(TypedDict):
        requested: bool

    class CreateParamsFeaturesOutboundPayments(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.CreateParamsFeaturesOutboundPaymentsAch"
            ]
        ]
        us_domestic_wire: NotRequired[
            Optional[
                "FinancialAccount.CreateParamsFeaturesOutboundPaymentsUsDomesticWire"
            ]
        ]

    class CreateParamsFeaturesOutboundPaymentsUsDomesticWire(TypedDict):
        requested: bool

    class CreateParamsFeaturesOutboundPaymentsAch(TypedDict):
        requested: bool

    class CreateParamsFeaturesIntraStripeFlows(TypedDict):
        requested: bool

    class CreateParamsFeaturesInboundTransfers(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.CreateParamsFeaturesInboundTransfersAch"
            ]
        ]

    class CreateParamsFeaturesInboundTransfersAch(TypedDict):
        requested: bool

    class CreateParamsFeaturesFinancialAddresses(TypedDict):
        aba: NotRequired[
            Optional[
                "FinancialAccount.CreateParamsFeaturesFinancialAddressesAba"
            ]
        ]

    class CreateParamsFeaturesFinancialAddressesAba(TypedDict):
        requested: bool

    class CreateParamsFeaturesDepositInsurance(TypedDict):
        requested: bool

    class CreateParamsFeaturesCardIssuing(TypedDict):
        requested: bool

    class ListParams(RequestOptions):
        created: NotRequired[
            Optional[Union["FinancialAccount.ListParamsCreated", int]]
        ]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ListParamsCreated(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        features: NotRequired[
            Optional["FinancialAccount.ModifyParamsFeatures"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        platform_restrictions: NotRequired[
            Optional["FinancialAccount.ModifyParamsPlatformRestrictions"]
        ]

    class ModifyParamsPlatformRestrictions(TypedDict):
        inbound_flows: NotRequired[
            Optional[Literal["restricted", "unrestricted"]]
        ]
        outbound_flows: NotRequired[
            Optional[Literal["restricted", "unrestricted"]]
        ]

    class ModifyParamsFeatures(TypedDict):
        card_issuing: NotRequired[
            Optional["FinancialAccount.ModifyParamsFeaturesCardIssuing"]
        ]
        deposit_insurance: NotRequired[
            Optional["FinancialAccount.ModifyParamsFeaturesDepositInsurance"]
        ]
        financial_addresses: NotRequired[
            Optional["FinancialAccount.ModifyParamsFeaturesFinancialAddresses"]
        ]
        inbound_transfers: NotRequired[
            Optional["FinancialAccount.ModifyParamsFeaturesInboundTransfers"]
        ]
        intra_stripe_flows: NotRequired[
            Optional["FinancialAccount.ModifyParamsFeaturesIntraStripeFlows"]
        ]
        outbound_payments: NotRequired[
            Optional["FinancialAccount.ModifyParamsFeaturesOutboundPayments"]
        ]
        outbound_transfers: NotRequired[
            Optional["FinancialAccount.ModifyParamsFeaturesOutboundTransfers"]
        ]

    class ModifyParamsFeaturesOutboundTransfers(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.ModifyParamsFeaturesOutboundTransfersAch"
            ]
        ]
        us_domestic_wire: NotRequired[
            Optional[
                "FinancialAccount.ModifyParamsFeaturesOutboundTransfersUsDomesticWire"
            ]
        ]

    class ModifyParamsFeaturesOutboundTransfersUsDomesticWire(TypedDict):
        requested: bool

    class ModifyParamsFeaturesOutboundTransfersAch(TypedDict):
        requested: bool

    class ModifyParamsFeaturesOutboundPayments(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.ModifyParamsFeaturesOutboundPaymentsAch"
            ]
        ]
        us_domestic_wire: NotRequired[
            Optional[
                "FinancialAccount.ModifyParamsFeaturesOutboundPaymentsUsDomesticWire"
            ]
        ]

    class ModifyParamsFeaturesOutboundPaymentsUsDomesticWire(TypedDict):
        requested: bool

    class ModifyParamsFeaturesOutboundPaymentsAch(TypedDict):
        requested: bool

    class ModifyParamsFeaturesIntraStripeFlows(TypedDict):
        requested: bool

    class ModifyParamsFeaturesInboundTransfers(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.ModifyParamsFeaturesInboundTransfersAch"
            ]
        ]

    class ModifyParamsFeaturesInboundTransfersAch(TypedDict):
        requested: bool

    class ModifyParamsFeaturesFinancialAddresses(TypedDict):
        aba: NotRequired[
            Optional[
                "FinancialAccount.ModifyParamsFeaturesFinancialAddressesAba"
            ]
        ]

    class ModifyParamsFeaturesFinancialAddressesAba(TypedDict):
        requested: bool

    class ModifyParamsFeaturesDepositInsurance(TypedDict):
        requested: bool

    class ModifyParamsFeaturesCardIssuing(TypedDict):
        requested: bool

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class RetrieveFeaturesParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class UpdateFeaturesParams(RequestOptions):
        card_issuing: NotRequired[
            Optional["FinancialAccount.UpdateFeaturesParamsCardIssuing"]
        ]
        deposit_insurance: NotRequired[
            Optional["FinancialAccount.UpdateFeaturesParamsDepositInsurance"]
        ]
        expand: NotRequired[Optional[List[str]]]
        financial_addresses: NotRequired[
            Optional["FinancialAccount.UpdateFeaturesParamsFinancialAddresses"]
        ]
        inbound_transfers: NotRequired[
            Optional["FinancialAccount.UpdateFeaturesParamsInboundTransfers"]
        ]
        intra_stripe_flows: NotRequired[
            Optional["FinancialAccount.UpdateFeaturesParamsIntraStripeFlows"]
        ]
        outbound_payments: NotRequired[
            Optional["FinancialAccount.UpdateFeaturesParamsOutboundPayments"]
        ]
        outbound_transfers: NotRequired[
            Optional["FinancialAccount.UpdateFeaturesParamsOutboundTransfers"]
        ]

    class UpdateFeaturesParamsOutboundTransfers(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.UpdateFeaturesParamsOutboundTransfersAch"
            ]
        ]
        us_domestic_wire: NotRequired[
            Optional[
                "FinancialAccount.UpdateFeaturesParamsOutboundTransfersUsDomesticWire"
            ]
        ]

    class UpdateFeaturesParamsOutboundTransfersUsDomesticWire(TypedDict):
        requested: bool

    class UpdateFeaturesParamsOutboundTransfersAch(TypedDict):
        requested: bool

    class UpdateFeaturesParamsOutboundPayments(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.UpdateFeaturesParamsOutboundPaymentsAch"
            ]
        ]
        us_domestic_wire: NotRequired[
            Optional[
                "FinancialAccount.UpdateFeaturesParamsOutboundPaymentsUsDomesticWire"
            ]
        ]

    class UpdateFeaturesParamsOutboundPaymentsUsDomesticWire(TypedDict):
        requested: bool

    class UpdateFeaturesParamsOutboundPaymentsAch(TypedDict):
        requested: bool

    class UpdateFeaturesParamsIntraStripeFlows(TypedDict):
        requested: bool

    class UpdateFeaturesParamsInboundTransfers(TypedDict):
        ach: NotRequired[
            Optional[
                "FinancialAccount.UpdateFeaturesParamsInboundTransfersAch"
            ]
        ]

    class UpdateFeaturesParamsInboundTransfersAch(TypedDict):
        requested: bool

    class UpdateFeaturesParamsFinancialAddresses(TypedDict):
        aba: NotRequired[
            Optional[
                "FinancialAccount.UpdateFeaturesParamsFinancialAddressesAba"
            ]
        ]

    class UpdateFeaturesParamsFinancialAddressesAba(TypedDict):
        requested: bool

    class UpdateFeaturesParamsDepositInsurance(TypedDict):
        requested: bool

    class UpdateFeaturesParamsCardIssuing(TypedDict):
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
