# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Optional, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.billing._feedback_option_create_params import (
        FeedbackOptionCreateParams,
    )
    from stripe.params.billing._feedback_option_deactivate_params import (
        FeedbackOptionDeactivateParams,
    )
    from stripe.params.billing._feedback_option_list_params import (
        FeedbackOptionListParams,
    )
    from stripe.params.billing._feedback_option_modify_params import (
        FeedbackOptionModifyParams,
    )
    from stripe.params.billing._feedback_option_retrieve_params import (
        FeedbackOptionRetrieveParams,
    )


class FeedbackOption(
    CreateableAPIResource["FeedbackOption"],
    ListableAPIResource["FeedbackOption"],
    UpdateableAPIResource["FeedbackOption"],
):
    """
    A resource for the feedback options model (for custom cancellation reasons)
    """

    OBJECT_NAME: ClassVar[Literal["billing.feedback_option"]] = (
        "billing.feedback_option"
    )

    class StatusTransitions(StripeObject):
        deactivated_at: Optional[int]
        """
        The time the feedback option was deactivated, if any. Measured in seconds since Unix epoch.
        """

    description: str
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["billing.feedback_option"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: Literal["active", "inactive"]
    """
    The feedback option's status.
    """
    status_transitions: StatusTransitions

    @classmethod
    def create(
        cls, **params: Unpack["FeedbackOptionCreateParams"]
    ) -> "FeedbackOption":
        """
        Creates a new feedback option.
        """
        return cast(
            "FeedbackOption",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["FeedbackOptionCreateParams"]
    ) -> "FeedbackOption":
        """
        Creates a new feedback option.
        """
        return cast(
            "FeedbackOption",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def _cls_deactivate(
        cls, id: str, **params: Unpack["FeedbackOptionDeactivateParams"]
    ) -> "FeedbackOption":
        """
        Deactivates a feedback option. Deactivated feedback options cannot be used in portal configurations.
        """
        return cast(
            "FeedbackOption",
            cls._static_request(
                "post",
                "/v1/billing/feedback_options/{id}/deactivate".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def deactivate(
        id: str, **params: Unpack["FeedbackOptionDeactivateParams"]
    ) -> "FeedbackOption":
        """
        Deactivates a feedback option. Deactivated feedback options cannot be used in portal configurations.
        """
        ...

    @overload
    def deactivate(
        self, **params: Unpack["FeedbackOptionDeactivateParams"]
    ) -> "FeedbackOption":
        """
        Deactivates a feedback option. Deactivated feedback options cannot be used in portal configurations.
        """
        ...

    @class_method_variant("_cls_deactivate")
    def deactivate(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["FeedbackOptionDeactivateParams"]
    ) -> "FeedbackOption":
        """
        Deactivates a feedback option. Deactivated feedback options cannot be used in portal configurations.
        """
        return cast(
            "FeedbackOption",
            self._request(
                "post",
                "/v1/billing/feedback_options/{id}/deactivate".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_deactivate_async(
        cls, id: str, **params: Unpack["FeedbackOptionDeactivateParams"]
    ) -> "FeedbackOption":
        """
        Deactivates a feedback option. Deactivated feedback options cannot be used in portal configurations.
        """
        return cast(
            "FeedbackOption",
            await cls._static_request_async(
                "post",
                "/v1/billing/feedback_options/{id}/deactivate".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def deactivate_async(
        id: str, **params: Unpack["FeedbackOptionDeactivateParams"]
    ) -> "FeedbackOption":
        """
        Deactivates a feedback option. Deactivated feedback options cannot be used in portal configurations.
        """
        ...

    @overload
    async def deactivate_async(
        self, **params: Unpack["FeedbackOptionDeactivateParams"]
    ) -> "FeedbackOption":
        """
        Deactivates a feedback option. Deactivated feedback options cannot be used in portal configurations.
        """
        ...

    @class_method_variant("_cls_deactivate_async")
    async def deactivate_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["FeedbackOptionDeactivateParams"]
    ) -> "FeedbackOption":
        """
        Deactivates a feedback option. Deactivated feedback options cannot be used in portal configurations.
        """
        return cast(
            "FeedbackOption",
            await self._request_async(
                "post",
                "/v1/billing/feedback_options/{id}/deactivate".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["FeedbackOptionListParams"]
    ) -> ListObject["FeedbackOption"]:
        """
        An API method for listing the feedback options model
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
        cls, **params: Unpack["FeedbackOptionListParams"]
    ) -> ListObject["FeedbackOption"]:
        """
        An API method for listing the feedback options model
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
        cls, id: str, **params: Unpack["FeedbackOptionModifyParams"]
    ) -> "FeedbackOption":
        """
        Updates the description of an existing feedback option.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "FeedbackOption",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["FeedbackOptionModifyParams"]
    ) -> "FeedbackOption":
        """
        Updates the description of an existing feedback option.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "FeedbackOption",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["FeedbackOptionRetrieveParams"]
    ) -> "FeedbackOption":
        """
        Retrieves a feedback options object given an ID.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["FeedbackOptionRetrieveParams"]
    ) -> "FeedbackOption":
        """
        Retrieves a feedback options object given an ID.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {"status_transitions": StatusTransitions}
