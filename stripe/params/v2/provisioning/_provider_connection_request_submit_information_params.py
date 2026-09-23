# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Any, Dict
from typing_extensions import NotRequired, TypedDict


class ProviderConnectionRequestSubmitInformationParams(TypedDict):
    confirmation_secret: NotRequired[str]
    """
    Secret used to confirm the request when submitting on behalf of a resource without
    an authenticated session.
    """
    information: "Dict[str, Any]|UntypedStripeObject[Any]"
    """
    Information requested by the provider, matching the connection's needs_information_schema.
    """
