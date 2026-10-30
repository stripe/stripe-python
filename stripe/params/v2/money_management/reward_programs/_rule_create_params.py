# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from typing import List
from typing_extensions import NotRequired, TypedDict


class RuleCreateParams(TypedDict):
    condition: NotRequired["RuleCreateParamsCondition"]
    """
    Conditions that must be true for this rule to match a card transaction. Omitting this field, or
    providing an empty condition, means the rule matches all transactions.
    """
    name: str
    """
    Human-readable name for this rule. Max 250 characters.
    """
    reward: "RuleCreateParamsReward"
    """
    The reward to grant when this rule matches.
    """


class RuleCreateParamsCondition(TypedDict):
    card_spend: NotRequired["RuleCreateParamsConditionCardSpend"]
    """
    Card-spend specific matching condition.
    """


class RuleCreateParamsConditionCardSpend(TypedDict):
    merchant_category_codes: NotRequired[
        "RuleCreateParamsConditionCardSpendMerchantCategoryCodes"
    ]
    """
    Merchant Category Code include/exclude configuration. Omitted means the rule matches all MCCs.
    """


class RuleCreateParamsConditionCardSpendMerchantCategoryCodes(TypedDict):
    excluded: List[str]
    """
    Four-digit Merchant Category Codes to explicitly exclude. Takes precedence over `included`.
    """
    included: List[str]
    """
    Four-digit Merchant Category Codes to include. An empty list matches all MCCs.
    """


class RuleCreateParamsReward(TypedDict):
    cashback: "RuleCreateParamsRewardCashback"
    """
    Cashback reward configuration.
    """


class RuleCreateParamsRewardCashback(TypedDict):
    rate: Decimal
    """
    Cashback rate as a percentage, represented as a decimal string. For example, `"2"` represents 2% and
    `"1.5"` represents 1.5%. Must be greater than `"0"` and less than or equal to `"100"`.
    """
