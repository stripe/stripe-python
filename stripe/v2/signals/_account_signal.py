# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class AccountSignal(StripeObject):
    """
    An automatically evaluated signal on an account. Each Account Signal object corresponds to
    exactly one signal type, indicated by type. Only the type-specific field is populated; other
    type-specific payload fields are null. If an account has multiple signals, Stripe creates
    separate account signal objects.
    """

    OBJECT_NAME: ClassVar[Literal["v2.signals.account_signal"]] = (
        "v2.signals.account_signal"
    )

    class AccountDetails(StripeObject):
        account: Optional[str]
        """
        The v2 account ID of the account.
        """
        customer: Optional[str]
        """
        The v1 customer ID of the account, for users not yet migrated to v2/accounts.
        """

    class UserAccountSharing(StripeObject):
        risk_level: Literal["elevated", "highest", "low", "normal", "unknown"]
        """
        Categorical assessment of the account-sharing risk.
        """
        score: Optional[Decimal]
        """
        The specific risk score for the account, between 0.00 and 100.00. Absent when risk level is
        not_assessed or unknown, or when the user is not on a product tier that includes numeric scores.
        """
        _field_encodings = {"score": "decimal_string"}

    class UserMultiAccounting(StripeObject):
        risk_level: Literal["elevated", "highest", "low", "normal", "unknown"]
        """
        Categorical assessment of the multi-accounting risk.
        """
        score: Optional[Decimal]
        """
        The specific risk score for the account, between 0.00 and 100.00. Absent when risk level is
        not_assessed or unknown, or when the user is not on a product tier that includes numeric scores.
        """
        _field_encodings = {"score": "decimal_string"}

    account_details: Optional[AccountDetails]
    """
    The account or customer this signal is associated with.
    """
    account_evaluation: Optional[str]
    """
    The account evaluation that produced this signal, if applicable.
    """
    created: str
    """
    Timestamp at which the signal was created.
    """
    id: str
    """
    Unique identifier for the account signal.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.signals.account_signal"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    type: Union[Literal["user_account_sharing", "user_multi_accounting"], str]
    """
    The type of signal.
    """
    user_account_sharing: Optional[UserAccountSharing]
    """
    Data for the user account-sharing signal. Present only when type is user_account_sharing.
    """
    user_multi_accounting: Optional[UserMultiAccounting]
    """
    Data for the user multi-accounting signal. Present only when type is user_multi_accounting.
    """
    _inner_class_types = {
        "account_details": AccountDetails,
        "user_account_sharing": UserAccountSharing,
        "user_multi_accounting": UserMultiAccounting,
    }
