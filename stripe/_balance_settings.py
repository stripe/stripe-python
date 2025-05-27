# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._singleton_api_resource import SingletonAPIResource
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack


class BalanceSettings(
    SingletonAPIResource["BalanceSettings"],
    UpdateableAPIResource["BalanceSettings"],
):
    """
    Options for customizing account balances and payout settings for a Stripe platform's connected accounts.

    This API is only available for users enrolled in the public preview for Accounts v2 on Stripe Connect.
    If you are not in this preview, please use the [Accounts v1 API](https://docs.stripe.com/api/accounts?api-version=2025-03-31.basil)
    to manage your connected accounts' balance settings instead.
    """

    OBJECT_NAME: ClassVar[Literal["balance_settings"]] = "balance_settings"

    class Payouts(StripeObject):
        class Schedule(StripeObject):
            interval: Optional[Literal["daily", "manual", "monthly", "weekly"]]
            """
            How frequently funds will be paid out. One of `manual` (payouts only created via API call), `daily`, `weekly`, or `monthly`.
            """
            monthly_anchor: Optional[int]
            """
            The day of the month funds will be paid out. Only shown if `interval` is monthly. Payouts scheduled between the 29th and 31st of the month are sent on the last day of shorter months.
            """
            weekly_anchor: Optional[
                Literal["friday", "monday", "thursday", "tuesday", "wednesday"]
            ]
            """
            The day of the week funds will be paid out, of the style 'monday', 'tuesday', etc. Only shown if `interval` is weekly.
            """

        schedule: Optional[Schedule]
        """
        Details on when funds from charges are available, and when they are paid out to an external account. See our [Setting Bank and Debit Card Payouts](https://stripe.com/docs/connect/bank-transfers#payout-information) documentation for details.
        """
        statement_descriptor: Optional[str]
        """
        The text that appears on the bank account statement for payouts. If not set, this defaults to the platform's bank descriptor as set in the Dashboard.
        """
        status: Literal["disabled", "enabled"]
        """
        Whether the funds in this account can be paid out.
        """
        _inner_class_types = {"schedule": Schedule}

    class SettlementTiming(StripeObject):
        delay_days: int
        """
        The number of days charge funds are held before becoming available.
        """

    class ModifyParams(RequestOptions):
        debit_negative_balances: NotRequired[bool]
        """
        A Boolean indicating whether Stripe should try to reclaim negative balances from an attached bank account. For details, see [Understanding Connect Account Balances](https://docs.stripe.com/connect/account-balances).
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        payouts: NotRequired["BalanceSettings.ModifyParamsPayouts"]
        """
        Settings specific to the account's payouts.
        """
        settlement_timing: NotRequired[
            "BalanceSettings.ModifyParamsSettlementTiming"
        ]
        """
        Settings related to the account's balance settlement timing.
        """

    class ModifyParamsPayouts(TypedDict):
        schedule: NotRequired["BalanceSettings.ModifyParamsPayoutsSchedule"]
        """
        Details on when funds from charges are available, and when they are paid out to an external account. For details, see our [Setting Bank and Debit Card Payouts](https://docs.stripe.com/connect/bank-transfers#payout-information) documentation.
        """
        statement_descriptor: NotRequired[str]
        """
        The text that appears on the bank account statement for payouts. If not set, this defaults to the platform's bank descriptor as set in the Dashboard.
        """

    class ModifyParamsPayoutsSchedule(TypedDict):
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

    class ModifyParamsSettlementTiming(TypedDict):
        delay_days: NotRequired[int]
        """
        The number of days charge funds are held before becoming available. May also be set to `minimum`, representing the lowest available value for the account country. Default is `minimum`. The `delay_days` parameter remains at the last configured value if `payouts.schedule.interval` is `manual`. [Learn more about controlling payout delay days](https://docs.stripe.com/connect/manage-payout-schedule).
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    debit_negative_balances: Optional[bool]
    """
    A Boolean indicating if Stripe should try to reclaim negative balances from an attached bank account. See [Understanding Connect account balances](https://docs.stripe.com/connect/account-balances) for details. The default value is `false` when [controller.requirement_collection](https://docs.stripe.com/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts, otherwise `true`.
    """
    object: Literal["balance_settings"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payouts: Optional[Payouts]
    """
    Settings specific to the account's payouts.
    """
    settlement_timing: SettlementTiming

    @classmethod
    def modify(
        cls, **params: Unpack["BalanceSettings.ModifyParams"]
    ) -> "BalanceSettings":
        """
        Updates balance settings for a given connected account.
         Related guide: [Making API calls for connected accounts](https://docs.stripe.com/connect/authentication)
        """
        return cast(
            "BalanceSettings",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, **params: Unpack["BalanceSettings.ModifyParams"]
    ) -> "BalanceSettings":
        """
        Updates balance settings for a given connected account.
         Related guide: [Making API calls for connected accounts](https://docs.stripe.com/connect/authentication)
        """
        return cast(
            "BalanceSettings",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, **params: Unpack["BalanceSettings.RetrieveParams"]
    ) -> "BalanceSettings":
        """
        Retrieves balance settings for a given connected account.
         Related guide: [Making API calls for connected accounts](https://docs.stripe.com/connect/authentication)
        """
        instance = cls(None, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, **params: Unpack["BalanceSettings.RetrieveParams"]
    ) -> "BalanceSettings":
        """
        Retrieves balance settings for a given connected account.
         Related guide: [Making API calls for connected accounts](https://docs.stripe.com/connect/authentication)
        """
        instance = cls(None, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/balance_settings"

    _inner_class_types = {
        "payouts": Payouts,
        "settlement_timing": SettlementTiming,
    }
