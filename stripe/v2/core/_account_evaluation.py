# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class AccountEvaluation(StripeObject):
    """
    Account Evaluation resource.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.account_evaluation"]] = (
        "v2.core.account_evaluation"
    )

    class AccountData(StripeObject):
        class Defaults(StripeObject):
            class Profile(StripeObject):
                business_url: str
                """
                The business URL.
                """
                doing_business_as: Optional[str]
                """
                Doing business as (DBA) name.
                """
                product_description: Optional[str]
                """
                Description of the account's product or service.
                """

            profile: Profile
            """
            Account profile data.
            """
            _inner_class_types = {"profile": Profile}

        class Identity(StripeObject):
            class BusinessDetails(StripeObject):
                registered_name: Optional[str]
                """
                Registered business name.
                """

            business_details: BusinessDetails
            """
            Business details for identity data.
            """
            _inner_class_types = {"business_details": BusinessDetails}

        defaults: Optional[Defaults]
        """
        Default account settings.
        """
        identity: Optional[Identity]
        """
        Identity data.
        """
        _inner_class_types = {"defaults": Defaults, "identity": Identity}

    account: Optional[str]
    """
    The account ID if this evaluation is for an existing account.
    """
    account_data: Optional[AccountData]
    """
    Account data if this evaluation is for an account without an existing Stripe entity.
    """
    created: str
    """
    Timestamp at which the evaluation was created.
    """
    evaluations_triggered: List[Literal["fraudulent_website"]]
    """
    List of signals that were triggered for evaluation.
    """
    id: str
    """
    Unique identifier for the account evaluation.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.core.account_evaluation"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    _inner_class_types = {"account_data": AccountData}
