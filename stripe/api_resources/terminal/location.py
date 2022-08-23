# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Location(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    A Location represents a grouping of readers.

    Related guide: [Fleet Management](https://stripe.com/docs/terminal/fleet/locations).
    """

    OBJECT_NAME = "terminal.location"
