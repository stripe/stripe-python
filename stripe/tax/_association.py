# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_resource import APIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, NotRequired, Unpack


class Association(APIResource["Association"]):
    """
    A Tax Association exposes the Tax Transactions that Stripe attempted to create on your behalf based on the PaymentIntent input
    """

    OBJECT_NAME: ClassVar[Literal["tax.association"]] = "tax.association"

    class TaxTransactionAttempt(StripeObject):
        class Committed(StripeObject):
            transaction: str
            """
            The [Tax Transaction](https://stripe.com/docs/api/tax/transaction/object)
            """

        class Errored(StripeObject):
            reason: Literal[
                "another_payment_associated_with_calculation",
                "calculation_expired",
                "currency_mismatch",
                "original_transaction_voided",
                "unique_reference_violation",
            ]
            """
            Details on why we couldn't commit the tax transaction.
            """

        committed: Optional[Committed]
        errored: Optional[Errored]
        source: str
        """
        The source of the tax transaction attempt. This is either a refund or a payment intent.
        """
        status: str
        """
        The status of the transaction attempt. This can be `errored` or `committed`.
        """
        _inner_class_types = {"committed": Committed, "errored": Errored}

    class FindParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        payment_intent: str
        """
        Valid [PaymentIntent](https://stripe.com/docs/api/payment_intents/object) id
        """

    calculation: str
    """
    The [Tax Calculation](https://stripe.com/docs/api/tax/calculations/object) that was included in PaymentIntent.
    """
    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["tax.association"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_intent: str
    """
    The [PaymentIntent](https://stripe.com/docs/api/payment_intents/object) that this Tax Association is tracking.
    """
    tax_transaction_attempts: Optional[List[TaxTransactionAttempt]]
    """
    Information about the tax transactions linked to this payment intent
    """

    @classmethod
    def find(cls, **params: Unpack["Association.FindParams"]) -> "Association":
        """
        Finds a tax association object by PaymentIntent id.
        """
        return cast(
            "Association",
            cls._static_request(
                "get",
                "/v1/tax/associations/find",
                params=params,
            ),
        )

    @classmethod
    async def find_async(
        cls, **params: Unpack["Association.FindParams"]
    ) -> "Association":
        """
        Finds a tax association object by PaymentIntent id.
        """
        return cast(
            "Association",
            await cls._static_request_async(
                "get",
                "/v1/tax/associations/find",
                params=params,
            ),
        )

    _inner_class_types = {"tax_transaction_attempts": TaxTransactionAttempt}
