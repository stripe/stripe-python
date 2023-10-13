# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

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
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            features: NotRequired["FinancialAccount.CreateParamsFeatures|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            platform_restrictions: NotRequired[
                "FinancialAccount.CreateParamsPlatformRestrictions|None"
            ]
            supported_currencies: List[str]

        class CreateParamsPlatformRestrictions(TypedDict):
            inbound_flows: NotRequired[
                "Literal['restricted', 'unrestricted']|None"
            ]
            outbound_flows: NotRequired[
                "Literal['restricted', 'unrestricted']|None"
            ]

        class CreateParamsFeatures(TypedDict):
            card_issuing: NotRequired[
                "FinancialAccount.CreateParamsFeaturesCardIssuing|None"
            ]
            deposit_insurance: NotRequired[
                "FinancialAccount.CreateParamsFeaturesDepositInsurance|None"
            ]
            financial_addresses: NotRequired[
                "FinancialAccount.CreateParamsFeaturesFinancialAddresses|None"
            ]
            inbound_transfers: NotRequired[
                "FinancialAccount.CreateParamsFeaturesInboundTransfers|None"
            ]
            intra_stripe_flows: NotRequired[
                "FinancialAccount.CreateParamsFeaturesIntraStripeFlows|None"
            ]
            outbound_payments: NotRequired[
                "FinancialAccount.CreateParamsFeaturesOutboundPayments|None"
            ]
            outbound_transfers: NotRequired[
                "FinancialAccount.CreateParamsFeaturesOutboundTransfers|None"
            ]

        class CreateParamsFeaturesOutboundTransfers(TypedDict):
            ach: NotRequired[
                "FinancialAccount.CreateParamsFeaturesOutboundTransfersAch|None"
            ]
            us_domestic_wire: NotRequired[
                "FinancialAccount.CreateParamsFeaturesOutboundTransfersUsDomesticWire|None"
            ]

        class CreateParamsFeaturesOutboundTransfersUsDomesticWire(TypedDict):
            requested: bool

        class CreateParamsFeaturesOutboundTransfersAch(TypedDict):
            requested: bool

        class CreateParamsFeaturesOutboundPayments(TypedDict):
            ach: NotRequired[
                "FinancialAccount.CreateParamsFeaturesOutboundPaymentsAch|None"
            ]
            us_domestic_wire: NotRequired[
                "FinancialAccount.CreateParamsFeaturesOutboundPaymentsUsDomesticWire|None"
            ]

        class CreateParamsFeaturesOutboundPaymentsUsDomesticWire(TypedDict):
            requested: bool

        class CreateParamsFeaturesOutboundPaymentsAch(TypedDict):
            requested: bool

        class CreateParamsFeaturesIntraStripeFlows(TypedDict):
            requested: bool

        class CreateParamsFeaturesInboundTransfers(TypedDict):
            ach: NotRequired[
                "FinancialAccount.CreateParamsFeaturesInboundTransfersAch|None"
            ]

        class CreateParamsFeaturesInboundTransfersAch(TypedDict):
            requested: bool

        class CreateParamsFeaturesFinancialAddresses(TypedDict):
            aba: NotRequired[
                "FinancialAccount.CreateParamsFeaturesFinancialAddressesAba|None"
            ]

        class CreateParamsFeaturesFinancialAddressesAba(TypedDict):
            requested: bool

        class CreateParamsFeaturesDepositInsurance(TypedDict):
            requested: bool

        class CreateParamsFeaturesCardIssuing(TypedDict):
            requested: bool

        class ListParams(RequestOptions):
            created: NotRequired["FinancialAccount.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            features: NotRequired["FinancialAccount.ModifyParamsFeatures|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            platform_restrictions: NotRequired[
                "FinancialAccount.ModifyParamsPlatformRestrictions|None"
            ]

        class ModifyParamsPlatformRestrictions(TypedDict):
            inbound_flows: NotRequired[
                "Literal['restricted', 'unrestricted']|None"
            ]
            outbound_flows: NotRequired[
                "Literal['restricted', 'unrestricted']|None"
            ]

        class ModifyParamsFeatures(TypedDict):
            card_issuing: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesCardIssuing|None"
            ]
            deposit_insurance: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesDepositInsurance|None"
            ]
            financial_addresses: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesFinancialAddresses|None"
            ]
            inbound_transfers: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesInboundTransfers|None"
            ]
            intra_stripe_flows: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesIntraStripeFlows|None"
            ]
            outbound_payments: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesOutboundPayments|None"
            ]
            outbound_transfers: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesOutboundTransfers|None"
            ]

        class ModifyParamsFeaturesOutboundTransfers(TypedDict):
            ach: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesOutboundTransfersAch|None"
            ]
            us_domestic_wire: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesOutboundTransfersUsDomesticWire|None"
            ]

        class ModifyParamsFeaturesOutboundTransfersUsDomesticWire(TypedDict):
            requested: bool

        class ModifyParamsFeaturesOutboundTransfersAch(TypedDict):
            requested: bool

        class ModifyParamsFeaturesOutboundPayments(TypedDict):
            ach: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesOutboundPaymentsAch|None"
            ]
            us_domestic_wire: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesOutboundPaymentsUsDomesticWire|None"
            ]

        class ModifyParamsFeaturesOutboundPaymentsUsDomesticWire(TypedDict):
            requested: bool

        class ModifyParamsFeaturesOutboundPaymentsAch(TypedDict):
            requested: bool

        class ModifyParamsFeaturesIntraStripeFlows(TypedDict):
            requested: bool

        class ModifyParamsFeaturesInboundTransfers(TypedDict):
            ach: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesInboundTransfersAch|None"
            ]

        class ModifyParamsFeaturesInboundTransfersAch(TypedDict):
            requested: bool

        class ModifyParamsFeaturesFinancialAddresses(TypedDict):
            aba: NotRequired[
                "FinancialAccount.ModifyParamsFeaturesFinancialAddressesAba|None"
            ]

        class ModifyParamsFeaturesFinancialAddressesAba(TypedDict):
            requested: bool

        class ModifyParamsFeaturesDepositInsurance(TypedDict):
            requested: bool

        class ModifyParamsFeaturesCardIssuing(TypedDict):
            requested: bool

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class RetrieveFeaturesParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class UpdateFeaturesParams(RequestOptions):
            card_issuing: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsCardIssuing|None"
            ]
            deposit_insurance: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsDepositInsurance|None"
            ]
            expand: NotRequired["List[str]|None"]
            financial_addresses: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsFinancialAddresses|None"
            ]
            inbound_transfers: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsInboundTransfers|None"
            ]
            intra_stripe_flows: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsIntraStripeFlows|None"
            ]
            outbound_payments: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsOutboundPayments|None"
            ]
            outbound_transfers: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsOutboundTransfers|None"
            ]

        class UpdateFeaturesParamsOutboundTransfers(TypedDict):
            ach: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsOutboundTransfersAch|None"
            ]
            us_domestic_wire: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsOutboundTransfersUsDomesticWire|None"
            ]

        class UpdateFeaturesParamsOutboundTransfersUsDomesticWire(TypedDict):
            requested: bool

        class UpdateFeaturesParamsOutboundTransfersAch(TypedDict):
            requested: bool

        class UpdateFeaturesParamsOutboundPayments(TypedDict):
            ach: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsOutboundPaymentsAch|None"
            ]
            us_domestic_wire: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsOutboundPaymentsUsDomesticWire|None"
            ]

        class UpdateFeaturesParamsOutboundPaymentsUsDomesticWire(TypedDict):
            requested: bool

        class UpdateFeaturesParamsOutboundPaymentsAch(TypedDict):
            requested: bool

        class UpdateFeaturesParamsIntraStripeFlows(TypedDict):
            requested: bool

        class UpdateFeaturesParamsInboundTransfers(TypedDict):
            ach: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsInboundTransfersAch|None"
            ]

        class UpdateFeaturesParamsInboundTransfersAch(TypedDict):
            requested: bool

        class UpdateFeaturesParamsFinancialAddresses(TypedDict):
            aba: NotRequired[
                "FinancialAccount.UpdateFeaturesParamsFinancialAddressesAba|None"
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
