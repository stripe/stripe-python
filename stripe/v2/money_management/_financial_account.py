# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class FinancialAccount(StripeObject):
    """
    A FinancialAccount represents a balance and can be the source or destination of money movement.
    """

    OBJECT_NAME: ClassVar[Literal["v2.money_management.financial_account"]] = (
        "v2.money_management.financial_account"
    )

    class Balance(StripeObject):
        available: UntypedStripeObject[Amount]
        """
        Balance available for money movement.
        """
        inbound_pending: UntypedStripeObject[Amount]
        """
        Balance of inbound funds that aren't yet available for money movement and will later move to the `available` balance.
        """
        outbound_pending: UntypedStripeObject[Amount]
        """
        Balance of funds being used for pending outbound money movements.
        """

    class Other(StripeObject):
        type: str
        """
        The FinancialAccount's actual type, represented as a string.
        Upgrade your API version to see this value in `financial_account.type`.
        """

    class StatusDetails(StripeObject):
        class Closed(StripeObject):
            class ForwardingSettings(StripeObject):
                payment_method: Optional[str]
                """
                ID of the FinancialAccount that supplies funds to cover negative balances
                during or after this FinancialAccount's closure.
                """
                payout_method: Optional[str]
                """
                ID of the FinancialAccount that receives funds forwarded from this FinancialAccount when it closes.
                """

            forwarding_settings: Optional[ForwardingSettings]
            """
            When configured, the forwarding settings for the closed FinancialAccount.
            """
            reason: Literal["account_closed", "closed_by_platform", "other"]
            """
            Closed Enum. The reason the FinancialAccount was closed.
            """
            _inner_class_types = {"forwarding_settings": ForwardingSettings}

        closed: Optional[Closed]
        """
        Details about the FinancialAccount's closure. Only populated when `status` is `closed`.
        """
        _inner_class_types = {"closed": Closed}

    class Storage(StripeObject):
        class DepositInsuranceEligibility(StripeObject):
            bank_name: Union[Literal["fifth_third"], str]
            """
            The bank where funds are stored.
            """
            currencies: List[str]
            """
            Currencies eligible for deposit insurance at this bank under this scheme.
            """
            type: Union[Literal["fdic", "fdic_passthrough"], str]
            """
            The deposit insurance scheme.
            """

        deposit_insurance_eligibility: Optional[
            List[DepositInsuranceEligibility]
        ]
        """
        Array of eligibility objects, segmented by bank name and deposit insurance scheme.
        """
        holds_currencies: List[str]
        """
        The currencies that this FinancialAccount can hold.
        """
        _inner_class_types = {
            "deposit_insurance_eligibility": DepositInsuranceEligibility,
        }

    balance: Balance
    """
    The FinancialAccount's balance, split into `available`, `inbound_pending`, and `outbound_pending` balances.
    Each balance is a hash keyed by lowercase currency codes, with an amount for each currency.
    """
    country: str
    """
    Open Enum. The country where the LegalEntity associated with the FinancialAccount is based, represented as a two-letter country code.
    """
    created: str
    """
    Time at which the object was created. Represented as an RFC 3339 timestamp in UTC with millisecond precision, for example `2022-09-18T13:22:18.123Z`.
    """
    display_name: Optional[str]
    """
    A descriptive name for the FinancialAccount, up to 50 characters long. This name appears in the Stripe Dashboard and embedded components.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of key-value pairs that you can attach to an object. This can be useful for storing additional information
    about the object in a structured format.
    """
    object: Literal["v2.money_management.financial_account"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    other: Optional[Other]
    """
    If the FinancialAccount's `type` is `other`, this hash identifies its actual type.
    Upgrade your API version to see that type in `type`.
    """
    status: Literal["closed", "open", "pending"]
    """
    Closed Enum. An enum representing the status of the FinancialAccount. This indicates whether or not the FinancialAccount can be used for any money movement flows.
    """
    status_details: Optional[StatusDetails]
    """
    Additional details related to the status of the FinancialAccount.
    """
    storage: Optional[Storage]
    """
    If the FinancialAccount's `type` is `storage`, this hash contains details specific to that type.
    """
    type: Literal["other", "storage"]
    """
    Closed Enum. The type of the FinancialAccount. Details specific to the type appear in the matching hash.
    For example, a `storage` FinancialAccount includes a `storage` hash.
    """
    _inner_class_types = {
        "balance": Balance,
        "other": Other,
        "status_details": StatusDetails,
        "storage": Storage,
    }
