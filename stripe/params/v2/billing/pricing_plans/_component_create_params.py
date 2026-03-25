# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict
from typing_extensions import Literal, NotRequired, TypedDict


class ComponentCreateParams(TypedDict):
    lookup_key: NotRequired[str]
    """
    An identifier that can be used to find this component.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    type: Literal["license_fee", "rate_card", "service_action"]
    """
    The type of the PricingPlanComponent.
    """
    license_fee: NotRequired["ComponentCreateParamsLicenseFee"]
    """
    Details if this component is a License Fee.
    """
    rate_card: NotRequired["ComponentCreateParamsRateCard"]
    """
    Details if this component is a Rate Card.
    """
    service_action: NotRequired["ComponentCreateParamsServiceAction"]
    """
    Details if this component is a Service Action.
    """


class ComponentCreateParamsLicenseFee(TypedDict):
    id: str
    """
    The ID of the License Fee.
    """
    version: NotRequired[str]
    """
    The ID of the License Fee Version. If not specified, defaults to 'latest'.
    """


class ComponentCreateParamsRateCard(TypedDict):
    id: str
    """
    The ID of the Rate Card.
    """
    version: NotRequired[str]
    """
    The ID of the Rate Card Version. If not specified, defaults to 'latest'.
    """


class ComponentCreateParamsServiceAction(TypedDict):
    id: str
    """
    The ID of the service action.
    """
