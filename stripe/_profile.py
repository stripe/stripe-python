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
            """
            The original image.
            """

        class Logo(StripeObject):
            original: str
            """
            The original image.
            """

        icon: Optional[Icon]
        """
        Profile icon image.
        """
        logo: Optional[Logo]
        """
        Profile logo image.
        """
        primary_color: Optional[str]
        """
        The primary brand color for the profile.
        """
        secondary_color: Optional[str]
        """
        The secondary brand color for the profile.
        """
        _inner_class_types = {"icon": Icon, "logo": Logo}

    branding: Optional[Branding]
    """
    Branding information for the Stripe profile.
    """
    description: Optional[str]
    """
    A description of the business or entity represented by the Stripe profile.
    """
    display_name: str
    """
    The display name shown for the Stripe profile.
    """
    id: str
    """
    Unique identifier for the Stripe profile.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["profile"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    url: Optional[str]
    """
    The external website URL associated with the Stripe profile.
    """
    username: str
    """
    The unique username for the Stripe profile.
    """
    _inner_class_types = {"branding": Branding}
