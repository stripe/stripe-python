# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.list_object import ListObject
from typing import Dict
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.radar.value_list_item import ValueListItem


class ValueList(
    CreateableAPIResource["ValueList"],
    DeletableAPIResource["ValueList"],
    ListableAPIResource["ValueList"],
    UpdateableAPIResource["ValueList"],
):
    """
    Value lists allow you to group values together which can then be referenced in rules.

    Related guide: [Default Stripe lists](https://stripe.com/docs/radar/lists#managing-list-items)
    """

    OBJECT_NAME = "radar.value_list"
    alias: str
    created: str
    created_by: str
    id: str
    item_type: str
    list_items: ListObject["ValueListItem"]
    livemode: bool
    metadata: Dict[str, str]
    name: str
    object: Literal["radar.value_list"]
