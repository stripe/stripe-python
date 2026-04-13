# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Any, Dict
from typing_extensions import TypedDict


class WorkflowInvokeParams(TypedDict):
    input_parameters: "Dict[str, Any]|UntypedStripeObject[Any]"
    """
    Parameters used to invoke the Workflow Run.
    """
