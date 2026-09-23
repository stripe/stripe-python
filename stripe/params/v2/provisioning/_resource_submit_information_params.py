# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Any, Dict
from typing_extensions import TypedDict


class ResourceSubmitInformationParams(TypedDict):
    submitted_information: "Dict[str, Any]|UntypedStripeObject[Any]"
    """
    Additional information being submitted for the resource.
    """
