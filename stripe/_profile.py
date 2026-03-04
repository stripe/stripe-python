# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class Profile(StripeObject):
    """
    A Stripe profile
    """

    OBJECT_NAME: ClassVar[Literal["profile"]] = "profile"

    class Branding(StripeObject):
        class Icon(StripeObject):
            original: str

        class Logo(StripeObject):
            original: str

        icon: Optional[Icon]
        logo: Optional[Logo]
        primary_color: Optional[str]
        secondary_color: Optional[str]
        _inner_class_types = {"icon": Icon, "logo": Logo}

    branding: Optional[Branding]
    description: Optional[str]
    display_name: str
    id: str
    livemode: bool
    object: Literal["profile"]
    url: Optional[str]
    username: str
    _inner_class_types = {"branding": Branding}
