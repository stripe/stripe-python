# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class FileLink(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    To share the contents of a `File` object with non-Stripe users, you can
    create a `FileLink`. `FileLink`s contain a URL that can be used to
    retrieve the contents of the file without authentication.
    """

    OBJECT_NAME = "file_link"
