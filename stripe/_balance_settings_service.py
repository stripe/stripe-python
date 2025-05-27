# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._balance_settings import BalanceSettings
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class BalanceSettingsService(StripeService):
    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
        debit_negative_balances: NotRequired[bool]
        """
        A Boolean indicating whether Stripe should try to reclaim negative balances from an attached bank account. For details, see [Understanding Connect Account Balances](https://docs.stripe.com/connect/account-balances).
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        payouts: NotRequired["BalanceSettingsService.UpdateParamsPayouts"]
        """
        Settings specific to the account's payouts.
        """
        settlement_timing: NotRequired[
            "BalanceSettingsService.UpdateParamsSettlementTiming"
        ]
        """
        Settings related to the account's balance settlement timing.
        """

    class UpdateParamsPayouts(TypedDict):
        schedule: NotRequired[
            "BalanceSettingsService.UpdateParamsPayoutsSchedule"
        ]
        """
        Details on when funds from charges are available, and when they are paid out to an external account. For details, see our [Setting Bank and Debit Card Payouts](https://docs.stripe.com/connect/bank-transfers#payout-information) documentation.
        """
        statement_descriptor: NotRequired[str]
        """
        The text that appears on the bank account statement for payouts. If not set, this defaults to the platform's bank descriptor as set in the Dashboard.
        """

    class UpdateParamsPayoutsSchedule(TypedDict):
        interval: NotRequired[Literal["daily", "manual", "monthly", "weekly"]]
        """
        How frequently available funds are paid out. One of: `daily`, `manual`, `weekly`, or `monthly`. Default is `daily`.
        """
        monthly_anchor: NotRequired[int]
        """
        The day of the month when available funds are paid out, specified as a number between 1--31. Payouts nominally scheduled between the 29th and 31st of the month are instead sent on the last day of a shorter month. Required and applicable only if `interval` is `monthly`.
        """
        weekly_anchor: NotRequired[
            Literal["friday", "monday", "thursday", "tuesday", "wednesday"]
        ]
        """
        The day of the week when available funds are paid out (required and applicable only if `interval` is `weekly`.)
        """

    class UpdateParamsSettlementTiming(TypedDict):
        delay_days: NotRequired[int]
        """
        The number of days charge funds are held before becoming available. May also be set to `minimum`, representing the lowest available value for the account country. Default is `minimum`. The `delay_days` parameter remains at the last configured value if `payouts.schedule.interval` is `manual`. [Learn more about controlling payout delay days](https://docs.stripe.com/connect/manage-payout-schedule).
        """

    def retrieve(
        self,
        params: "BalanceSettingsService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> BalanceSettings:
        """
        Retrieves balance settings for a given connected account.
         Related guide: [Making API calls for connected accounts](https://docs.stripe.com/connect/authentication)
        """
        return cast(
            BalanceSettings,
            self._request(
                "get",
                "/v1/balance_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        params: "BalanceSettingsService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> BalanceSettings:
        """
        Retrieves balance settings for a given connected account.
         Related guide: [Making API calls for connected accounts](https://docs.stripe.com/connect/authentication)
        """
        return cast(
            BalanceSettings,
            await self._request_async(
                "get",
                "/v1/balance_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        params: "BalanceSettingsService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> BalanceSettings:
        """
        Updates balance settings for a given connected account.
         Related guide: [Making API calls for connected accounts](https://docs.stripe.com/connect/authentication)
        """
        return cast(
            BalanceSettings,
            self._request(
                "post",
                "/v1/balance_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        params: "BalanceSettingsService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> BalanceSettings:
        """
        Updates balance settings for a given connected account.
         Related guide: [Making API calls for connected accounts](https://docs.stripe.com/connect/authentication)
        """
        return cast(
            BalanceSettings,
            await self._request_async(
                "post",
                "/v1/balance_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )
