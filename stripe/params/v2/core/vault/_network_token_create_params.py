# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class NetworkTokenCreateParams(TypedDict):
    card: NotRequired["NetworkTokenCreateParamsCard"]
    """
    Raw card values used to provision the network token.
    """
    type: Literal["card"]
    """
    Private preview supports card only.
    """


class NetworkTokenCreateParamsCard(TypedDict):
    exp_month: str
    """
    The two-digit number representing the card's expiration month.
    """
    exp_year: str
    """
    The four-digit number representing the card's expiration year.
    """
    number: str
    """
    The card number.
    """
    origin: NotRequired[Literal["card_on_file"]]
    """
    The optional origin attestation for the card.
    """
    owner_details: NotRequired["NetworkTokenCreateParamsCardOwnerDetails"]
    """
    Optional owner contact details used only when a network requires them for raw-card tokenization.
    """


class NetworkTokenCreateParamsCardOwnerDetails(TypedDict):
    email: NotRequired[str]
    """
    Cardholder email address.
    """
    phone: NotRequired[str]
    """
    Cardholder phone number in international format, for example +15555550123.
    """
