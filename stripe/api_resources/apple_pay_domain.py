# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from typing_extensions import Literal


class ApplePayDomain(
    CreateableAPIResource["ApplePayDomain"],
    DeletableAPIResource["ApplePayDomain"],
    ListableAPIResource["ApplePayDomain"],
):
    OBJECT_NAME = "apple_pay_domain"
    created: str
    domain_name: str
    id: str
    livemode: bool
    object: Literal["apple_pay_domain"]

    @classmethod
    def class_url(cls):
        return "/v1/apple_pay/domains"
