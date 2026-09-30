# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from typing_extensions import Literal, NotRequired, TypedDict


class NetworkTokenCreateFromCredentialParams(TypedDict):
    card: NotRequired["NetworkTokenCreateFromCredentialParamsCard"]
    """
    The existing Stripe card reference to provision or resolve.
    """
    type: Union[Literal["card"], str]
    """
    Private preview supports card only.
    """


class NetworkTokenCreateFromCredentialParamsCard(TypedDict):
    origin: NotRequired["Literal['card_on_file', 'wallet']|str"]
    """
    The optional origin attestation for the referenced card.
    """
    reference: str
    """
    A supported v2 Card ID or v1 PaymentMethod ID of type card.
    """
