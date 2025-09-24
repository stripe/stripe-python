# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._balance_settings import BalanceSettings
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict


class BalanceSettingsService(StripeService):
    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        payments: NotRequired["BalanceSettingsService.UpdateParamsPayments"]
        """
        Settings that apply to the [Payments Balance](https://docs.stripe.com/api/balance).
        """

    class UpdateParamsPayments(TypedDict):
        debit_negative_balances: NotRequired[bool]
        """
        A Boolean indicating whether Stripe should try to reclaim negative balances from an attached bank account. For details, see [Understanding Connect Account Balances](https://docs.stripe.com/connect/account-balances).
        """
        payouts: NotRequired[
            "BalanceSettingsService.UpdateParamsPaymentsPayouts"
        ]
        """
        Settings specific to the account's payouts.
        """
        settlement_timing: NotRequired[
            "BalanceSettingsService.UpdateParamsPaymentsSettlementTiming"
        ]
        """
        Settings related to the account's balance settlement timing.
        """

    class UpdateParamsPaymentsPayouts(TypedDict):
        minimum_balance_by_currency: NotRequired[
            "Literal['']|Dict[str, Union[Literal[''], int]]"
        ]
        """
        The minimum balance amount to retain per currency after automatic payouts. Only funds that exceed these amounts are paid out. Learn more about the [minimum balances for automatic payouts](https://docs.stripe.com/payouts/minimum-balances-for-automatic-payouts).
        """
        schedule: NotRequired[
            "BalanceSettingsService.UpdateParamsPaymentsPayoutsSchedule"
        ]
        """
        Details on when funds from charges are available, and when they are paid out to an external account. For details, see our [Setting Bank and Debit Card Payouts](https://docs.stripe.com/connect/bank-transfers#payout-information) documentation.
        """
        statement_descriptor: NotRequired[str]
        """
        The text that appears on the bank account statement for payouts. If not set, this defaults to the platform's bank descriptor as set in the Dashboard.
        """

    class UpdateParamsPaymentsPayoutsSchedule(TypedDict):
        interval: NotRequired[Literal["daily", "manual", "monthly", "weekly"]]
        """
        How frequently available funds are paid out. One of: `daily`, `manual`, `weekly`, or `monthly`. Default is `daily`.
        """
        monthly_payout_days: NotRequired[List[int]]
        """
        The days of the month when available funds are paid out, specified as an array of numbers between 1--31. Payouts nominally scheduled between the 29th and 31st of the month are instead sent on the last day of a shorter month. Required and applicable only if `interval` is `monthly`.
        """
        weekly_payout_days: NotRequired[
            List[
                Literal["friday", "monday", "thursday", "tuesday", "wednesday"]
            ]
        ]
        """
        The days of the week when available funds are paid out, specified as an array, e.g., [`monday`, `tuesday`]. Required and applicable only if `interval` is `weekly`.
        """

    class UpdateParamsPaymentsSettlementTiming(TypedDict):
        delay_days_override: NotRequired["Literal['']|int"]
        """
        Change `delay_days` for this account, which determines the number of days charge funds are held before becoming available. The maximum value is 31. Passing an empty string to `delay_days_override` will return `delay_days` to the default, which is the lowest available value for the account. [Learn more about controlling delay days](https://docs.stripe.com/connect/manage-payout-schedule).
        """

    def retrieve(
        self,
        params: Optional["BalanceSettingsService.RetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
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
        params: Optional["BalanceSettingsService.RetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
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
        params: Optional["BalanceSettingsService.UpdateParams"] = None,
        options: Optional[RequestOptions] = None,
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
        params: Optional["BalanceSettingsService.UpdateParams"] = None,
        options: Optional[RequestOptions] = None,
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
