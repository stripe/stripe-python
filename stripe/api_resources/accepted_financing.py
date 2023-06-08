# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import SingletonAPIResource


class AcceptedFinancing(SingletonAPIResource):
    """
    This is an object representing financing that has been accepted by a merchant.
    """

    OBJECT_NAME = "accepted_financing"

    @classmethod
    def class_url(cls):
        return "/v1/capital/financing/accepted"
