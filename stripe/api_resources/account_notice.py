# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus


class AccountNotice(
    ListableAPIResource["AccountNotice"],
    UpdateableAPIResource["AccountNotice"],
):
    """
    A notice to a Connected account. Notice can be sent by Stripe on your behalf or you can opt to send the notices yourself.

    See the [guide to send notices](https://stripe.com/docs/issuing/compliance-us/issuing-regulated-customer-notices) to your connected accounts.
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
        Associated [Capability](https://stripe.com/docs/api/capabilities)
        """
        issuing_credit_underwriting_record: Optional[str]
        """
        Associated [Credit Underwriting Record](https://stripe.com/docs/api/issuing/credit_underwriting_record)
        """
        issuing_dispute: Optional[str]
        """
        Associated [Issuing Dispute](https://stripe.com/docs/api/issuing/disputes)
        """

    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            sent: NotRequired["bool|None"]
            """
            Set to false to only return unsent AccountNotices.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class ModifyParams(RequestOptions):
            email: "AccountNotice.ModifyParamsEmail"
            """
            Information about the email you sent.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            sent_at: int
            """
            Date when you sent the notice.
            """

        class ModifyParamsEmail(TypedDict):
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

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
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
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["account_notice"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    reason: Literal[
        "issuing.account_closed_for_inactivity",
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
    Reason the notice is being sent. The reason determines what copy the notice must contain. See the [regulated customer notices](https://stripe.com/docs/issuing/compliance-us/issuing-regulated-customer-notices) guide. All reasons might not apply to your integration, and Stripe might add new reasons in the future, so we recommend an internal warning when you receive an unknown reason.
    """
    sent_at: Optional[int]
    """
    Date when the notice was sent. When absent, you must send the notice, update the content of the email and date when it was sent.
    """

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["AccountNotice.ListParams"]
    ) -> ListObject["AccountNotice"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
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
        cls, id: str, **params: Unpack["AccountNotice.ModifyParams"]
    ) -> "AccountNotice":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "AccountNotice",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["AccountNotice.RetrieveParams"]
    ) -> "AccountNotice":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {"email": Email, "linked_objects": LinkedObjects}
