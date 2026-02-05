# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._fr_meal_vouchers_onboarding import FrMealVouchersOnboarding
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params._fr_meal_vouchers_onboarding_create_params import (
        FrMealVouchersOnboardingCreateParams,
    )
    from stripe.params._fr_meal_vouchers_onboarding_list_params import (
        FrMealVouchersOnboardingListParams,
    )
    from stripe.params._fr_meal_vouchers_onboarding_retrieve_params import (
        FrMealVouchersOnboardingRetrieveParams,
    )
    from stripe.params._fr_meal_vouchers_onboarding_update_params import (
        FrMealVouchersOnboardingUpdateParams,
    )


class FrMealVouchersOnboardingService(StripeService):
    def list(
        self,
        params: Optional["FrMealVouchersOnboardingListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FrMealVouchersOnboarding]":
        """
        Lists French Meal Vouchers Onboarding objects. The objects are returned in sorted order, with the most recently created objects appearing first.
        """
        return cast(
            "ListObject[FrMealVouchersOnboarding]",
            self._request(
                "get",
                "/v1/fr_meal_vouchers_onboardings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["FrMealVouchersOnboardingListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FrMealVouchersOnboarding]":
        """
        Lists French Meal Vouchers Onboarding objects. The objects are returned in sorted order, with the most recently created objects appearing first.
        """
        return cast(
            "ListObject[FrMealVouchersOnboarding]",
            await self._request_async(
                "get",
                "/v1/fr_meal_vouchers_onboardings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "FrMealVouchersOnboardingCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FrMealVouchersOnboarding":
        """
        Creates a French Meal Vouchers Onboarding object that represents a restaurant's onboarding status and starts the onboarding process.
        """
        return cast(
            "FrMealVouchersOnboarding",
            self._request(
                "post",
                "/v1/fr_meal_vouchers_onboardings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "FrMealVouchersOnboardingCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FrMealVouchersOnboarding":
        """
        Creates a French Meal Vouchers Onboarding object that represents a restaurant's onboarding status and starts the onboarding process.
        """
        return cast(
            "FrMealVouchersOnboarding",
            await self._request_async(
                "post",
                "/v1/fr_meal_vouchers_onboardings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["FrMealVouchersOnboardingRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FrMealVouchersOnboarding":
        """
        Retrieves the details of a previously created French Meal Vouchers Onboarding object.

        Supply the unique French Meal Vouchers Onboarding ID that was returned from your previous request,
        and Stripe returns the corresponding onboarding information.
        """
        return cast(
            "FrMealVouchersOnboarding",
            self._request(
                "get",
                "/v1/fr_meal_vouchers_onboardings/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["FrMealVouchersOnboardingRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FrMealVouchersOnboarding":
        """
        Retrieves the details of a previously created French Meal Vouchers Onboarding object.

        Supply the unique French Meal Vouchers Onboarding ID that was returned from your previous request,
        and Stripe returns the corresponding onboarding information.
        """
        return cast(
            "FrMealVouchersOnboarding",
            await self._request_async(
                "get",
                "/v1/fr_meal_vouchers_onboardings/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "FrMealVouchersOnboardingUpdateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FrMealVouchersOnboarding":
        """
        Updates the details of a restaurant's French Meal Vouchers Onboarding object by
        setting the values of the parameters passed. Any parameters not provided are left unchanged.
        After you update the object, the onboarding process automatically restarts.

        You can only update French Meal Vouchers Onboarding objects with the postal_code field requirement in past_due.
        """
        return cast(
            "FrMealVouchersOnboarding",
            self._request(
                "post",
                "/v1/fr_meal_vouchers_onboardings/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "FrMealVouchersOnboardingUpdateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FrMealVouchersOnboarding":
        """
        Updates the details of a restaurant's French Meal Vouchers Onboarding object by
        setting the values of the parameters passed. Any parameters not provided are left unchanged.
        After you update the object, the onboarding process automatically restarts.

        You can only update French Meal Vouchers Onboarding objects with the postal_code field requirement in past_due.
        """
        return cast(
            "FrMealVouchersOnboarding",
            await self._request_async(
                "post",
                "/v1/fr_meal_vouchers_onboardings/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
