# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import sanitize_id
from typing import ClassVar, Dict, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params._account_notice_list_params import (
        AccountNoticeListParams,
    )
    from stripe.params._account_notice_modify_params import (
        AccountNoticeModifyParams,
    )
    from stripe.params._account_notice_retrieve_params import (
        AccountNoticeRetrieveParams,
    )


class AccountNotice(
    ListableAPIResource["AccountNotice"],
    UpdateableAPIResource["AccountNotice"],
):
    """
    A notice to a Connected account. Notice can be sent by Stripe on your behalf or you can opt to send the notices yourself.

    See the [guide to send notices](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices) to your connected accounts.
    """

    OBJECT_NAME: ClassVar[Literal["account_notice"]] = "account_notice"

    class Email(StripeObject):
        plain_text: str
        """
        Content of the email in plain text. The copy must match exactly the language that Stripe Compliance has approved for use.
        """
        recipient: str
        """
        Email address of the recipient.
        """
        subject: str
        """
        Subject of the email.
        """

    class LinkedObjects(StripeObject):
        capability: Optional[str]
        """
        Associated [Capability](https://docs.stripe.com/api/capabilities)
        """
        issuing_credit_underwriting_record: Optional[str]
        """
        Associated [Credit Underwriting Record](https://docs.stripe.com/api/issuing/credit_underwriting_record)
        """
        issuing_dispute: Optional[str]
        """
        Associated [Issuing Dispute](https://docs.stripe.com/api/issuing/disputes)
        """

    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    deadline: Optional[int]
    """
    When present, the deadline for sending the notice to meet the relevant regulations.
    """
    email: Optional[Email]
    """
    Information about the email when sent.
    """
    id: str
    """
    Unique identifier for the object.
    """
    linked_objects: Optional[LinkedObjects]
    """
    Information about objects related to the notice.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["account_notice"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    reason: Literal[
        "issuing.account_closed_for_inactivity",
        "issuing.account_closed_for_not_providing_business_model_clarification",
        "issuing.account_closed_for_not_providing_url_clarification",
        "issuing.account_closed_for_not_providing_use_case_clarification",
        "issuing.account_closed_for_terms_of_service_violation",
        "issuing.application_rejected_for_failure_to_verify",
        "issuing.credit_application_rejected",
        "issuing.credit_increase_application_rejected",
        "issuing.credit_limit_decreased",
        "issuing.credit_line_closed",
        "issuing.dispute_lost",
        "issuing.dispute_submitted",
        "issuing.dispute_won",
    ]
    """
    Reason the notice is being sent. The reason determines what copy the notice must contain. See the [regulated customer notices](https://docs.stripe.com/issuing/compliance-us/issuing-regulated-customer-notices) guide. All reasons might not apply to your integration, and Stripe might add new reasons in the future, so we recommend an internal warning when you receive an unknown reason.
    """
    sent_at: Optional[int]
    """
    Date when the notice was sent. When absent, you must send the notice, update the content of the email and date when it was sent.
    """

    @classmethod
    def list(
        cls, **params: Unpack["AccountNoticeListParams"]
    ) -> ListObject["AccountNotice"]:
        """
        Retrieves a list of AccountNotice objects. The objects are sorted in descending order by creation date, with the most-recently-created object appearing first.
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
        cls, **params: Unpack["AccountNoticeListParams"]
    ) -> ListObject["AccountNotice"]:
        """
        Retrieves a list of AccountNotice objects. The objects are sorted in descending order by creation date, with the most-recently-created object appearing first.
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
        cls, id: str, **params: Unpack["AccountNoticeModifyParams"]
    ) -> "AccountNotice":
        """
        Updates an AccountNotice object.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "AccountNotice",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["AccountNoticeModifyParams"]
    ) -> "AccountNotice":
        """
        Updates an AccountNotice object.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "AccountNotice",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["AccountNoticeRetrieveParams"]
    ) -> "AccountNotice":
        """
        Retrieves an AccountNotice object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["AccountNoticeRetrieveParams"]
    ) -> "AccountNotice":
        """
        Retrieves an AccountNotice object.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {"email": Email, "linked_objects": LinkedObjects}
