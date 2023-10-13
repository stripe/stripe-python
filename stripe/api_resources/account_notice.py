# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
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

    OBJECT_NAME = "account_notice"

    class Email(StripeObject):
        plain_text: str
        recipient: str
        subject: str

    class LinkedObjects(StripeObject):
        capability: Optional[str]
        issuing_credit_underwriting_record: Optional[str]
        issuing_dispute: Optional[str]

    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            sent: NotRequired["bool|None"]
            starting_after: NotRequired["str|None"]

        class ModifyParams(RequestOptions):
            email: "AccountNotice.ModifyParamsEmail"
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            sent_at: int

        class ModifyParamsEmail(TypedDict):
            plain_text: str
            recipient: str
            subject: str

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    created: int
    deadline: Optional[int]
    email: Optional[Email]
    id: str
    linked_objects: Optional[LinkedObjects]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["account_notice"]
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
    sent_at: Optional[int]

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
        cls, id, **params: Unpack["AccountNotice.ModifyParams"]
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
