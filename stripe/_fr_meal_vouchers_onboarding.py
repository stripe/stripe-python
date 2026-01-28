# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import sanitize_id
from typing import ClassVar, Dict, List, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params._fr_meal_vouchers_onboarding_create_params import (
        FrMealVouchersOnboardingCreateParams,
    )
    from stripe.params._fr_meal_vouchers_onboarding_list_params import (
        FrMealVouchersOnboardingListParams,
    )
    from stripe.params._fr_meal_vouchers_onboarding_modify_params import (
        FrMealVouchersOnboardingModifyParams,
    )
    from stripe.params._fr_meal_vouchers_onboarding_retrieve_params import (
        FrMealVouchersOnboardingRetrieveParams,
    )


class FrMealVouchersOnboarding(
    CreateableAPIResource["FrMealVouchersOnboarding"],
    ListableAPIResource["FrMealVouchersOnboarding"],
    UpdateableAPIResource["FrMealVouchersOnboarding"],
):
    """
    The French Meal Vouchers Onboarding resource encapsulates the onboarding status and other related information
    for a single restaurant (SIRET number) in the context of the French Meal Vouchers program.
    """

    OBJECT_NAME: ClassVar[Literal["fr_meal_vouchers_onboarding"]] = (
        "fr_meal_vouchers_onboarding"
    )

    class Providers(StripeObject):
        class Conecs(StripeObject):
            class Issuers(StripeObject):
                available: List[Literal["bimpli", "edenred", "pluxee", "up"]]
                """
                Issuers are available to this restaurant via Conecs, will be blank if the onboarding to Conecs is not complete or unsuccessful
                """

            class Requirements(StripeObject):
                class Error(StripeObject):
                    code: Literal["postal_code_invalid", "siret_invalid"]
                    """
                    The code for the type of error.
                    """
                    message: str
                    """
                    An informative message that provides additional details about the error.
                    """
                    requirement: Optional[Literal["postal_code", "siret"]]
                    """
                    The specific onboarding requirement field (in the requirements hash) that needs to be resolved.
                    """

                errors: List[Error]
                """
                Information any errors that are preventing the onboarding to Conecs from being completed.
                """
                past_due: List[Literal["postal_code", "siret"]]
                """
                Fields that need to be provided to complete the onboarding to Conecs.
                """
                _inner_class_types = {"errors": Error}

            issuers: Issuers
            """
            This represents information which issuers are available to this restaurant via Conecs
            """
            requirements: Requirements
            """
            This represents information about outstanding requirements for this restaurant to onboard to Conecs
            """
            status: Literal[
                "action_required", "active", "disentitled", "pending"
            ]
            """
            Status of the restaurant's onboarding to Conecs
            """
            _inner_class_types = {
                "issuers": Issuers,
                "requirements": Requirements,
            }

        conecs: Conecs
        """
        This represents the onboarding state of the restaurant on Conecs.
        """
        _inner_class_types = {"conecs": Conecs}

    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: str
    """
    Name of the restaurant.
    """
    object: Literal["fr_meal_vouchers_onboarding"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    postal_code: str
    """
    Postal code of the restaurant.
    """
    providers: Providers
    """
    This represents the onboarding state of the restaurant on different providers.
    """
    siret: str
    """
    SIRET number associated with the restaurant.
    """

    @classmethod
    def create(
        cls, **params: Unpack["FrMealVouchersOnboardingCreateParams"]
    ) -> "FrMealVouchersOnboarding":
        """
        Creates a French Meal Vouchers Onboarding object that represents a restaurant's onboarding status and starts the onboarding process.
        """
        return cast(
            "FrMealVouchersOnboarding",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["FrMealVouchersOnboardingCreateParams"]
    ) -> "FrMealVouchersOnboarding":
        """
        Creates a French Meal Vouchers Onboarding object that represents a restaurant's onboarding status and starts the onboarding process.
        """
        return cast(
            "FrMealVouchersOnboarding",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["FrMealVouchersOnboardingListParams"]
    ) -> ListObject["FrMealVouchersOnboarding"]:
        """
        Lists French Meal Vouchers Onboarding objects
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["FrMealVouchersOnboardingListParams"]
    ) -> ListObject["FrMealVouchersOnboarding"]:
        """
        Lists French Meal Vouchers Onboarding objects
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["FrMealVouchersOnboardingModifyParams"]
    ) -> "FrMealVouchersOnboarding":
        """
        Updates the details of a restaurant's French Meal Vouchers Onboarding object
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "FrMealVouchersOnboarding",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["FrMealVouchersOnboardingModifyParams"]
    ) -> "FrMealVouchersOnboarding":
        """
        Updates the details of a restaurant's French Meal Vouchers Onboarding object
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "FrMealVouchersOnboarding",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls,
        id: str,
        **params: Unpack["FrMealVouchersOnboardingRetrieveParams"],
    ) -> "FrMealVouchersOnboarding":
        """
        Retrieves the details of a French Meal Vouchers Onboarding object
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls,
        id: str,
        **params: Unpack["FrMealVouchersOnboardingRetrieveParams"],
    ) -> "FrMealVouchersOnboarding":
        """
        Retrieves the details of a French Meal Vouchers Onboarding object
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {"providers": Providers}
