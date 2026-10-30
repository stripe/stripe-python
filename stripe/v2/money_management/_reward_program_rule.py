# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class RewardProgramRule(StripeObject):
    """
    A RewardProgramRule defines the matching conditions and cashback reward outcome shared across all
    active enrollments in a RewardProgram. At most one RewardProgramRule may be active per RewardProgram
    at a time.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.reward_program_rule"]
    ] = "v2.money_management.reward_program_rule"

    class Condition(StripeObject):
        class CardSpend(StripeObject):
            class MerchantCategoryCodes(StripeObject):
                excluded: List[str]
                """
                Four-digit Merchant Category Codes to explicitly exclude. Takes precedence over `included`.
                """
                included: List[str]
                """
                Four-digit Merchant Category Codes to include. An empty list matches all MCCs.
                """

            merchant_category_codes: Optional[MerchantCategoryCodes]
            """
            Merchant Category Code include/exclude configuration. Omitted means the rule matches all MCCs.
            """
            _inner_class_types = {
                "merchant_category_codes": MerchantCategoryCodes,
            }

        card_spend: Optional[CardSpend]
        """
        Card-spend specific matching condition.
        """
        _inner_class_types = {"card_spend": CardSpend}

    class Reward(StripeObject):
        class Cashback(StripeObject):
            rate: Decimal
            """
            Cashback rate as a percentage, represented as a decimal string. For example, `"2"` represents 2% and
            `"1.5"` represents 1.5%. Must be greater than `"0"` and less than or equal to `"100"`.
            """
            _field_encodings = {"rate": "decimal_string"}

        cashback: Cashback
        """
        Cashback reward configuration.
        """
        _inner_class_types = {"cashback": Cashback}

    condition: Condition
    """
    Conditions that must be true for this rule to match a card transaction. Empty means the rule matches
    all transactions.
    """
    created: str
    """
    Time at which the RewardProgramRule was created.
    """
    id: str
    """
    Unique identifier for the RewardProgramRule.
    """
    livemode: bool
    """
    Whether this object exists in livemode or testmode.
    """
    name: str
    """
    Human-readable name for this rule. Max 250 characters.
    """
    object: Literal["v2.money_management.reward_program_rule"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    reward: Reward
    """
    The reward to grant when this rule matches.
    """
    reward_program: str
    """
    The ID of the RewardProgram this rule belongs to. Immutable after creation.
    """
    status: Union[Literal["active", "inactive"], str]
    """
    The status of the RewardProgramRule. Inactive by default on creation; use activate/deactivate to
    change.
    """
    _inner_class_types = {"condition": Condition, "reward": Reward}
