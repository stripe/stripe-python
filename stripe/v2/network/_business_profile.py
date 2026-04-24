# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class BusinessProfile(StripeObject):
    """
    The Stripe profile represents a business' public identity on the Stripe network.
    """

    OBJECT_NAME: ClassVar[Literal["v2.network.business_profile"]] = (
        "v2.network.business_profile"
    )

    class Branding(StripeObject):
        class Icon(StripeObject):
            original: str
            """
            The URL of the image in its original size.
            """

        class Logo(StripeObject):
            original: str
            """
            The URL of the image in its original size.
            """

        icon: Optional[Icon]
        """
        URL of the icon for the business. The image will be square and at least 128px x 128px.
        """
        logo: Optional[Logo]
        """
        URL of the logo for the business. The image will be at least 128px x 128px.
        """
        primary_color: Optional[str]
        """
        A CSS hex color value representing the primary branding color for this business.
        """
        secondary_color: Optional[str]
        """
        A CSS hex color value representing the secondary branding color for this business.
        """
        _inner_class_types = {"icon": Icon, "logo": Logo}

    branding: Optional[Branding]
    """
    Branding data for the business.
    """
    description: Optional[str]
    """
    The description of the business.
    """
    display_name: str
    """
    The display name of the Stripe profile.
    """
    id: str
    """
    The ID of the Stripe business profile; also known as the Network ID. This is the ID used to identify the business on the Stripe network.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.network.business_profile"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    url: Optional[str]
    """
    The URL of the business.
    """
    username: str
    """
    The username of the Stripe profile.
    """
    _inner_class_types = {"branding": Branding}
