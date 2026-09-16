# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class NetworkTokenCreateFromCredentialParams(TypedDict):
    card: NotRequired["NetworkTokenCreateFromCredentialParamsCard"]
    """
    The existing Stripe card reference to provision or resolve.
    """
    type: Literal["card"]
    """
    Private preview supports card only.
    """


class NetworkTokenCreateFromCredentialParamsCard(TypedDict):
    origin: NotRequired[Literal["card_on_file"]]
    """
    The optional origin attestation for the referenced card.
    """
    reference: str
    """
    A supported v2 Card ID or v1 PaymentMethod ID of type card.
    """
