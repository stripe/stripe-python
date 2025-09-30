# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, List, Optional
from typing_extensions import Literal, NotRequired, TypedDict


class CadenceUpdateParams(TypedDict):
    include: NotRequired[
        List[Literal["invoice_discount_rules", "settings_data"]]
    ]
    """
    Additional resource to include in the response.
    """
    lookup_key: NotRequired[str]
    """
    A lookup key used to retrieve cadences dynamically from a static string. Maximum length of 200 characters.
    """
    metadata: NotRequired[Dict[str, Optional[str]]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    payer: NotRequired["CadenceUpdateParamsPayer"]
    """
    The payer determines the entity financially responsible for the bill.
    """
    settings: NotRequired["CadenceUpdateParamsSettings"]
    """
    The settings associated with the cadence.
    """


class CadenceUpdateParamsPayer(TypedDict):
    billing_profile: NotRequired[str]
    """
    The ID of the Billing Profile object which determines how a bill will be paid.
    """


class CadenceUpdateParamsSettings(TypedDict):
    bill: NotRequired["CadenceUpdateParamsSettingsBill"]
    """
    Settings that configure bills generation, which includes calculating totals, tax, and presenting invoices. If null is provided, the current bill settings will be removed from the billing cadence.
    """
    collection: NotRequired["CadenceUpdateParamsSettingsCollection"]
    """
    Settings that configure and manage the behavior of collecting payments. If null is provided, the current collection settings will be removed from the billing cadence.
    """


class CadenceUpdateParamsSettingsBill(TypedDict):
    id: str
    """
    The ID of the referenced settings object.
    """
    version: NotRequired[str]
    """
    An optional field to specify the version of Settings to use.
    If not provided, this will always default to the `live_version` specified on the setting, any time the settings are used.
    Using a specific version here will prevent the settings from updating, and is discouraged for cadences.
    To clear a pinned version, set the version to null.
    """


class CadenceUpdateParamsSettingsCollection(TypedDict):
    id: str
    """
    The ID of the referenced settings object.
    """
    version: NotRequired[str]
    """
    An optional field to specify the version of Settings to use.
    If not provided, this will always default to the `live_version` specified on the setting, any time the settings are used.
    Using a specific version here will prevent the settings from updating, and is discouraged for cadences.
    To clear a pinned version, set the version to null.
    """
