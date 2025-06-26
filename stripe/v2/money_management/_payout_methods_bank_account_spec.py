# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List
from typing_extensions import Literal


class PayoutMethodsBankAccountSpec(StripeObject):
    """
    The PayoutMethodsBankAccountSpec object.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.payout_methods_bank_account_spec"]
    ] = "v2.money_management.payout_methods_bank_account_spec"

    class Countries(StripeObject):
        class Field(StripeObject):
            class LocalNameHuman(StripeObject):
                content: str
                localization_key: str

            local_name: str
            """
            The local name of the field.
            """
            local_name_human: LocalNameHuman
            """
            The human readable local name of the field.
            """
            max_length: int
            """
            The maximum length of the field.
            """
            min_length: int
            """
            THe minimum length of the field.
            """
            placeholder: str
            """
            The placeholder value of the field.
            """
            stripe_name: str
            """
            The stripe name of the field.
            """
            validation_regex: str
            """
            The validation regex of the field.
            """
            _inner_class_types = {"local_name_human": LocalNameHuman}

        fields: List[Field]
        """
        The list of fields for a country, along with associated information.
        """
        _inner_class_types = {"fields": Field}

    countries: Dict[str, Countries]
    """
    The list of specs by country.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.payout_methods_bank_account_spec"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    _inner_class_types = {"countries": Countries}
