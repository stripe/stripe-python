# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from typing import List
from typing_extensions import NotRequired, TypedDict


class RuleUpdateParams(TypedDict):
    condition: NotRequired["RuleUpdateParamsCondition"]
    """
    Conditions that must be true for this rule to match a card transaction.
    """
    name: NotRequired[str]
    """
    Human-readable name for this rule. Max 250 characters.
    """
    reward: NotRequired["RuleUpdateParamsReward"]
    """
    The reward to grant when this rule matches.
    """


class RuleUpdateParamsCondition(TypedDict):
    card_spend: NotRequired["RuleUpdateParamsConditionCardSpend"]
    """
    Card-spend specific matching condition.
    """


class RuleUpdateParamsConditionCardSpend(TypedDict):
    merchant_category_codes: NotRequired[
        "RuleUpdateParamsConditionCardSpendMerchantCategoryCodes"
    ]
    """
    Merchant Category Code include/exclude configuration. Omitted means the rule matches all MCCs.
    """


class RuleUpdateParamsConditionCardSpendMerchantCategoryCodes(TypedDict):
    excluded: List[str]
    """
    Four-digit Merchant Category Codes to explicitly exclude. Takes precedence over `included`.
    """
    included: List[str]
    """
    Four-digit Merchant Category Codes to include. An empty list matches all MCCs.
    """


class RuleUpdateParamsReward(TypedDict):
    cashback: "RuleUpdateParamsRewardCashback"
    """
    Cashback reward configuration.
    """


class RuleUpdateParamsRewardCashback(TypedDict):
    rate: Decimal
    """
    Cashback rate as a percentage, represented as a decimal string. For example, `"2"` represents 2% and
    `"1.5"` represents 1.5%. Must be greater than `"0"` and less than or equal to `"100"`.
    """
