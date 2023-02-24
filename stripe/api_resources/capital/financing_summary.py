# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import SingletonAPIResource


class FinancingSummary(SingletonAPIResource):
    """
    A financing object describes an account's current financing state. Used by Connect
    platforms to read the state of Capital offered to their connected accounts.
    """

    OBJECT_NAME = "capital.financing_summary"

    @classmethod
    def class_url(cls):
        return "/v1/capital/financing_summary"
