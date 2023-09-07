# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal


class Application(StripeObject):
    OBJECT_NAME = "application"
    id: str
    name: Optional[str]
    object: Literal["application"]
