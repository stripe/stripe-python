# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.treasury._financial_account_features import (
    FinancialAccountFeatures,
)
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class FinancialAccountFeaturesService(StripeService):
    class CreateParams(TypedDict):
        card_issuing: NotRequired[
            "FinancialAccountFeaturesService.CreateParamsCardIssuing"
        ]
        """
        Encodes the FinancialAccount's ability to be used with the Issuing product, including attaching cards to and drawing funds from the FinancialAccount.
        """
        deposit_insurance: NotRequired[
            "FinancialAccountFeaturesService.CreateParamsDepositInsurance"
        ]
        """
        Represents whether this FinancialAccount is eligible for deposit insurance. Various factors determine the insurance amount.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        financial_addresses: NotRequired[
            "FinancialAccountFeaturesService.CreateParamsFinancialAddresses"
        ]
        """
        Contains Features that add FinancialAddresses to the FinancialAccount.
        """
        inbound_transfers: NotRequired[
            "FinancialAccountFeaturesService.CreateParamsInboundTransfers"
        ]
        """
        Contains settings related to adding funds to a FinancialAccount from another Account with the same owner.
        """
        intra_stripe_flows: NotRequired[
            "FinancialAccountFeaturesService.CreateParamsIntraStripeFlows"
        ]
        """
        Represents the ability for the FinancialAccount to send money to, or receive money from other FinancialAccounts (for example, via OutboundPayment).
        """
        outbound_payments: NotRequired[
            "FinancialAccountFeaturesService.CreateParamsOutboundPayments"
        ]
        """
        Includes Features related to initiating money movement out of the FinancialAccount to someone else's bucket of money.
        """
        outbound_transfers: NotRequired[
            "FinancialAccountFeaturesService.CreateParamsOutboundTransfers"
        ]
        """
        Contains a Feature and settings related to moving money out of the FinancialAccount into another Account with the same owner.
        """

    class CreateParamsCardIssuing(TypedDict):
        requested: bool
        """
        Whether the FinancialAccount should have the Feature.
        """

    class CreateParamsDepositInsurance(TypedDict):
        requested: bool
        """
        Whether the FinancialAccount should have the Feature.
        """

    class CreateParamsFinancialAddresses(TypedDict):
        aba: NotRequired[
            "FinancialAccountFeaturesService.CreateParamsFinancialAddressesAba"
        ]
        """
        Adds an ABA FinancialAddress to the FinancialAccount.
        """

    class CreateParamsFinancialAddressesAba(TypedDict):
        requested: bool
        """
        Whether the FinancialAccount should have the Feature.
        """

    class CreateParamsInboundTransfers(TypedDict):
        ach: NotRequired[
            "FinancialAccountFeaturesService.CreateParamsInboundTransfersAch"
        ]
        """
        Enables ACH Debits via the InboundTransfers API.
        """

    class CreateParamsInboundTransfersAch(TypedDict):
        requested: bool
        """
        Whether the FinancialAccount should have the Feature.
        """

    class CreateParamsIntraStripeFlows(TypedDict):
        requested: bool
        """
        Whether the FinancialAccount should have the Feature.
        """

    class CreateParamsOutboundPayments(TypedDict):
        ach: NotRequired[
            "FinancialAccountFeaturesService.CreateParamsOutboundPaymentsAch"
        ]
        """
        Enables ACH transfers via the OutboundPayments API.
        """
        us_domestic_wire: NotRequired[
            "FinancialAccountFeaturesService.CreateParamsOutboundPaymentsUsDomesticWire"
        ]
        """
        Enables US domestic wire transfers via the OutboundPayments API.
        """

    class CreateParamsOutboundPaymentsAch(TypedDict):
        requested: bool
        """
        Whether the FinancialAccount should have the Feature.
        """

    class CreateParamsOutboundPaymentsUsDomesticWire(TypedDict):
        requested: bool
        """
        Whether the FinancialAccount should have the Feature.
        """

    class CreateParamsOutboundTransfers(TypedDict):
        ach: NotRequired[
            "FinancialAccountFeaturesService.CreateParamsOutboundTransfersAch"
        ]
        """
        Enables ACH transfers via the OutboundTransfers API.
        """
        us_domestic_wire: NotRequired[
            "FinancialAccountFeaturesService.CreateParamsOutboundTransfersUsDomesticWire"
        ]
        """
        Enables US domestic wire transfers via the OutboundTransfers API.
        """

    class CreateParamsOutboundTransfersAch(TypedDict):
        requested: bool
        """
        Whether the FinancialAccount should have the Feature.
        """

    class CreateParamsOutboundTransfersUsDomesticWire(TypedDict):
        requested: bool
        """
        Whether the FinancialAccount should have the Feature.
        """

    class ListParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    def create(
        self,
        financial_account: str,
        params: "FinancialAccountFeaturesService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> FinancialAccountFeatures:
        """
        Updates the Features associated with a FinancialAccount.
        """
        return cast(
            FinancialAccountFeatures,
            self._request(
                "post",
                "/v1/treasury/financial_accounts/{financial_account}/features".format(
                    financial_account=sanitize_id(financial_account),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def list(
        self,
        financial_account: str,
        params: "FinancialAccountFeaturesService.ListParams" = {},
        options: RequestOptions = {},
    ) -> FinancialAccountFeatures:
        """
        Retrieves Features information associated with the FinancialAccount.
        """
        return cast(
            FinancialAccountFeatures,
            self._request(
                "get",
                "/v1/treasury/financial_accounts/{financial_account}/features".format(
                    financial_account=sanitize_id(financial_account),
                ),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
