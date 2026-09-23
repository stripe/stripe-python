# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management.financial_accounts._wallet_export_export_credentials_params import (
        WalletExportExportCredentialsParams,
    )
    from stripe.params.v2.money_management.financial_accounts._wallet_export_retrieve_params import (
        WalletExportRetrieveParams,
    )
    from stripe.v2.money_management._financial_account_wallet_export import (
        FinancialAccountWalletExport,
    )
    from stripe.v2.money_management._financial_account_wallet_export_credentials import (
        FinancialAccountWalletExportCredentials,
    )


class WalletExportService(StripeService):
    def retrieve(
        self,
        id: str,
        /,
        params: Optional["WalletExportRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAccountWalletExport":
        """
        Retrieves the wallet export metadata for a closed FinancialAccount. Credentials are returned only by the export_credentials action.
        """
        return cast(
            "FinancialAccountWalletExport",
            self._request(
                "get",
                "/v2/money_management/financial_accounts/{id}/wallet_export".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["WalletExportRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAccountWalletExport":
        """
        Retrieves the wallet export metadata for a closed FinancialAccount. Credentials are returned only by the export_credentials action.
        """
        return cast(
            "FinancialAccountWalletExport",
            await self._request_async(
                "get",
                "/v2/money_management/financial_accounts/{id}/wallet_export".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def export_credentials(
        self,
        id: str,
        /,
        params: "WalletExportExportCredentialsParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAccountWalletExportCredentials":
        """
        Exports wallet credentials encrypted to the supplied recipient key. The first successful request starts one fixed one-hour retrieval window; later requests may use a different recipient key without extending it.
        """
        return cast(
            "FinancialAccountWalletExportCredentials",
            self._request(
                "post",
                "/v2/money_management/financial_accounts/{id}/wallet_export/export_credentials".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def export_credentials_async(
        self,
        id: str,
        /,
        params: "WalletExportExportCredentialsParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAccountWalletExportCredentials":
        """
        Exports wallet credentials encrypted to the supplied recipient key. The first successful request starts one fixed one-hour retrieval window; later requests may use a different recipient key without extending it.
        """
        return cast(
            "FinancialAccountWalletExportCredentials",
            await self._request_async(
                "post",
                "/v2/money_management/financial_accounts/{id}/wallet_export/export_credentials".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
