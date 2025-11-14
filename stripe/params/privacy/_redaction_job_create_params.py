# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class RedactionJobCreateParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    objects: "RedactionJobCreateParamsObjects"
    """
    The objects to redact. These root objects and their related ones will be validated for redaction.
    """
    validation_behavior: NotRequired[Literal["error", "fix"]]
    """
    Determines the validation behavior of the job. Default is `error`.
    """


class RedactionJobCreateParamsObjects(TypedDict):
    charges: NotRequired[List[str]]
    checkout_sessions: NotRequired[List[str]]
    customers: NotRequired[List[str]]
    identity_verification_sessions: NotRequired[List[str]]
    invoices: NotRequired[List[str]]
    issuing_cardholders: NotRequired[List[str]]
    issuing_cards: NotRequired[List[str]]
    payment_intents: NotRequired[List[str]]
    radar_value_list_items: NotRequired[List[str]]
    setup_intents: NotRequired[List[str]]
