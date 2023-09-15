# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal


class VerificationReport(ListableAPIResource["VerificationReport"]):
    """
    A VerificationReport is the result of an attempt to collect and verify data from a user.
    The collection of verification checks performed is determined from the `type` and `options`
    parameters used. You can find the result of each verification check performed in the
    appropriate sub-resource: `document`, `id_number`, `selfie`.

    Each VerificationReport contains a copy of any data collected by the user as well as
    reference IDs which can be used to access collected images through the [FileUpload](https://stripe.com/docs/api/files)
    API. To configure and create VerificationReports, use the
    [VerificationSession](https://stripe.com/docs/api/identity/verification_sessions) API.

    Related guides: [Accessing verification results](https://stripe.com/docs/identity/verification-sessions#results).
    """

    OBJECT_NAME = "identity.verification_report"
    created: int
    document: StripeObject
    id: str
    id_number: StripeObject
    livemode: bool
    object: Literal["identity.verification_report"]
    options: StripeObject
    selfie: StripeObject
    type: Literal["document", "id_number"]
    verification_session: Optional[str]

    @classmethod
    def list(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ) -> ListObject["VerificationReport"]:
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
    def retrieve(cls, id, api_key=None, **params) -> "VerificationReport":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
