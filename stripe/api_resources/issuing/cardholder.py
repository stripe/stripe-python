# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing_extensions import Literal


class Cardholder(
    CreateableAPIResource["Cardholder"],
    ListableAPIResource["Cardholder"],
    UpdateableAPIResource["Cardholder"],
):
    """
    An Issuing `Cardholder` object represents an individual or business entity who is [issued](https://stripe.com/docs/issuing) cards.

    Related guide: [How to create a cardholder](https://stripe.com/docs/issuing/cards#create-cardholder)
    """

    OBJECT_NAME = "issuing.cardholder"
    billing: Any
    company: Optional[Any]
    created: str
    email: Optional[str]
    id: str
    individual: Optional[Any]
    livemode: bool
    metadata: Dict[str, str]
    name: str
    object: Literal["issuing.cardholder"]
    phone_number: Optional[str]
    preferred_locales: Optional[List[str]]
    requirements: Any
    spending_controls: Optional[Any]
    status: str
    type: str
