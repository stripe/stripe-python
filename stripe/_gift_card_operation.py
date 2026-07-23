# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_resource import APIResource
from stripe._expandable_field import ExpandableField
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, Union
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._gift_card import GiftCard
    from stripe.params._gift_card_operation_retrieve_params import (
        GiftCardOperationRetrieveParams,
    )


class GiftCardOperation(APIResource["GiftCardOperation"]):
    """
    A GiftCardOperation represents an operation performed on a third-party gift card,
    such as activation, reload, cashout, balance check, or void.
    """

    OBJECT_NAME: ClassVar[Literal["gift_card_operation"]] = (
        "gift_card_operation"
    )

    class Activation(StripeObject):
        class Balance(StripeObject):
            amount: int
            """
            The balance amount.
            """
            currency: str
            """
            The currency of the balance.
            """

        balance: Balance
        """
        The balance amount of a gift card, including currency and amount.
        """
        _inner_class_types = {"balance": Balance}

    class ActivationVoid(StripeObject):
        voided_operation: str
        """
        The operation that was voided.
        """

    class BalanceCheck(StripeObject):
        class Balance(StripeObject):
            amount: int
            """
            The balance amount.
            """
            currency: str
            """
            The currency of the balance.
            """

        balance: Balance
        """
        The balance amount of a gift card, including currency and amount.
        """
        _inner_class_types = {"balance": Balance}

    class Cashout(StripeObject):
        class Balance(StripeObject):
            amount: int
            """
            The balance amount.
            """
            currency: str
            """
            The currency of the balance.
            """

        class PreviousBalance(StripeObject):
            amount: int
            """
            The balance amount.
            """
            currency: str
            """
            The currency of the balance.
            """

        balance: Balance
        """
        The balance amount of a gift card, including currency and amount.
        """
        previous_balance: Optional[PreviousBalance]
        """
        The balance before the operation.
        """
        _inner_class_types = {
            "balance": Balance,
            "previous_balance": PreviousBalance,
        }

    class CashoutVoid(StripeObject):
        class Balance(StripeObject):
            amount: int
            """
            The balance amount.
            """
            currency: str
            """
            The currency of the balance.
            """

        balance: Balance
        """
        The balance amount of a gift card, including currency and amount.
        """
        voided_operation: str
        """
        The operation that was voided.
        """
        _inner_class_types = {"balance": Balance}

    class Reload(StripeObject):
        class Balance(StripeObject):
            amount: int
            """
            The balance amount.
            """
            currency: str
            """
            The currency of the balance.
            """

        class PreviousBalance(StripeObject):
            amount: int
            """
            The balance amount.
            """
            currency: str
            """
            The currency of the balance.
            """

        balance: Balance
        """
        The balance amount of a gift card, including currency and amount.
        """
        previous_balance: Optional[PreviousBalance]
        """
        The balance before the operation.
        """
        _inner_class_types = {
            "balance": Balance,
            "previous_balance": PreviousBalance,
        }

    class ReloadVoid(StripeObject):
        class Balance(StripeObject):
            amount: int
            """
            The balance amount.
            """
            currency: str
            """
            The currency of the balance.
            """

        balance: Balance
        """
        The balance amount of a gift card, including currency and amount.
        """
        voided_operation: str
        """
        The operation that was voided.
        """
        _inner_class_types = {"balance": Balance}

    activation: Optional[Activation]
    """
    Details about a gift card activation operation.
    """
    activation_void: Optional[ActivationVoid]
    """
    Details about a gift card activation void operation.
    """
    balance_check: Optional[BalanceCheck]
    """
    Details about a gift card balance check operation.
    """
    cashout: Optional[Cashout]
    """
    Details about a gift card cashout operation.
    """
    cashout_void: Optional[CashoutVoid]
    """
    Details about a gift card cashout void operation.
    """
    completed_at: int
    """
    The timestamp of when this operation was completed.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    failure_code: Optional[
        Union[
            Literal[
                "action_not_supported",
                "card_already_activated",
                "card_expired",
                "card_not_activated",
                "do_not_honor",
                "generic_failure",
                "insufficient_balance",
                "invalid_amount",
                "invalid_currency",
                "invalid_number",
                "invalid_pin",
                "invalid_track_data",
                "lost_card",
                "lost_or_stolen_card",
                "pin_required",
                "pin_tries_exceeded",
                "processing_error",
                "provider_unavailable",
                "stolen_card",
                "suspected_fraud",
                "timeout",
            ],
            str,
        ]
    ]
    """
    The failure code of the operation. Only present if the status is failed.
    """
    gift_card: ExpandableField["GiftCard"]
    """
    The gift card this operation was performed on.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    location: Optional[str]
    """
    ID of the location that this transaction's reader is assigned to.
    """
    object: Literal["gift_card_operation"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: Optional[str]
    """
    The connected account whose credentials were used to perform this operation.
    """
    reader: Optional[str]
    """
    ID of the reader this transaction was made on.
    """
    reload: Optional[Reload]
    """
    Details about a gift card reload operation.
    """
    reload_void: Optional[ReloadVoid]
    """
    Details about a gift card reload void operation.
    """
    status: Literal["failed", "succeeded"]
    """
    The status of the operation.
    """
    type: Literal[
        "activation",
        "activation_void",
        "balance_check",
        "cashout",
        "cashout_void",
        "reload",
        "reload_void",
    ]
    """
    The type of operation performed.
    """

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["GiftCardOperationRetrieveParams"]
    ) -> "GiftCardOperation":
        """
        Retrieves a third-party gift card operation object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["GiftCardOperationRetrieveParams"]
    ) -> "GiftCardOperation":
        """
        Retrieves a third-party gift card operation object.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "activation": Activation,
        "activation_void": ActivationVoid,
        "balance_check": BalanceCheck,
        "cashout": Cashout,
        "cashout_void": CashoutVoid,
        "reload": Reload,
        "reload_void": ReloadVoid,
    }
