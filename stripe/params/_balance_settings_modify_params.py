# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class BalanceSettingsModifyParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    payments: NotRequired["BalanceSettingsModifyParamsPayments"]
    """
    Settings that apply to the [Payments Balance](https://docs.stripe.com/api/balance).
    """


class BalanceSettingsModifyParamsPayments(TypedDict):
    debit_negative_balances: NotRequired[bool]
    """
    A Boolean indicating whether Stripe should try to reclaim negative balances from an attached bank account. For details, see [Understanding Connect Account Balances](https://docs.stripe.com/connect/account-balances).
    """
    payouts: NotRequired["BalanceSettingsModifyParamsPaymentsPayouts"]
    """
    Settings specific to the account's payouts.
    """
    settlement_timing: NotRequired[
        "BalanceSettingsModifyParamsPaymentsSettlementTiming"
    ]
    """
    Settings related to the account's balance settlement timing.
    """


class BalanceSettingsModifyParamsPaymentsPayouts(TypedDict):
    automatic_transfer_rules_by_currency: NotRequired[
        "Literal['']|Dict[str, Union[Literal[''], List[BalanceSettingsModifyParamsPaymentsPayoutsAutomaticTransferRulesByCurrency]]]|UntypedStripeObject[Union[Literal[''], List[BalanceSettingsModifyParamsPaymentsPayoutsAutomaticTransferRulesByCurrency]]]"
    ]
    """
    Configures per-currency rules for automatically transferring funds from the payments balance to a FinancialAccount.
    """
    minimum_balance_by_currency: NotRequired[
        "Literal['']|Dict[str, Union[Literal[''], int]]|UntypedStripeObject[Union[Literal[''], int]]"
    ]
    """
    The minimum balance amount to retain per currency after automatic payouts. Only funds that exceed these amounts are paid out. Learn more about the [minimum balances for automatic payouts](https://docs.stripe.com/payouts/minimum-balances-for-automatic-payouts).
    """
    schedule: NotRequired["BalanceSettingsModifyParamsPaymentsPayoutsSchedule"]
    """
    Details on when funds from charges are available, and when they are paid out to an external account. For details, see our [Setting Bank and Debit Card Payouts](https://docs.stripe.com/connect/bank-transfers#payout-information) documentation.
    """
    statement_descriptor: NotRequired[str]
    """
    The text that appears on the bank account statement for payouts. If not set, this defaults to the platform's bank descriptor as set in the Dashboard.
    """


class BalanceSettingsModifyParamsPaymentsPayoutsAutomaticTransferRulesByCurrency(
    TypedDict,
):
    payout_method: str
    """
    The ID of the FinancialAccount that funds will be transferred to during automatic transfers.
    """
    transfer_up_to_amount: NotRequired[int]
    """
    The maximum amount in minor units to transfer to the FinancialAccount. Required and only applicable when `type` is `transfer_up_to_amount`.
    """
    type: Literal["transfer_all", "transfer_up_to_amount"]
    """
    The type of automatic transfer rule.
    """


class BalanceSettingsModifyParamsPaymentsPayoutsSchedule(TypedDict):
    interval: NotRequired[Literal["daily", "manual", "monthly", "weekly"]]
    """
    How frequently available funds are paid out. One of: `daily`, `manual`, `weekly`, or `monthly`. Default is `daily`.
    """
    monthly_payout_days: NotRequired[List[int]]
    """
    The days of the month when available funds are paid out, specified as an array of numbers between 1--31. Payouts nominally scheduled between the 29th and 31st of the month are instead sent on the last day of a shorter month. Required and applicable only if `interval` is `monthly`.
    """
    weekly_payout_days: NotRequired[
        List[Literal["friday", "monday", "thursday", "tuesday", "wednesday"]]
    ]
    """
    The days of the week when available funds are paid out, specified as an array, e.g., [`monday`, `tuesday`]. Required and applicable only if `interval` is `weekly`.
    """


class BalanceSettingsModifyParamsPaymentsSettlementTiming(TypedDict):
    delay_days_override: NotRequired["Literal['']|int"]
    """
    Change `delay_days` for this account, which determines the number of days charge funds are held before becoming available. The maximum value is 31. Passing an empty string to `delay_days_override` will return `delay_days` to the default, which is the lowest available value for the account. [Learn more about controlling delay days](https://docs.stripe.com/connect/manage-payout-schedule).
    """
    start_of_day: NotRequired[
        "Literal['']|BalanceSettingsModifyParamsPaymentsSettlementTimingStartOfDay"
    ]
    """
    Customized start of day configuration for automatic payouts to group and send payments in local timezones with a customized day starting time. For details, see our [Customized start of day](https://docs.stripe.com/connect/customized-start-of-day) documentation.
    """


class BalanceSettingsModifyParamsPaymentsSettlementTimingStartOfDay(TypedDict):
    hour: NotRequired[int]
    """
    Hour at which the customized start of day begins according to the given timezone. Must be a [supported customized start of day hour](https://docs.stripe.com/connect/customized-start-of-day#available-timezones-and-cutoffs).
    """
    minutes: NotRequired[int]
    """
    Minutes at which the customized start of day begins according to the given timezone. Must be either 0 or 30.
    """
    timezone: NotRequired[str]
    """
    Timezone for the customized start of day. Must be a [supported customized start of day timezone](https://docs.stripe.com/connect/customized-start-of-day#available-timezones-and-cutoffs).
    """
