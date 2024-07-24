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

    class StatusDetails(StripeObject):
        class Committed(StripeObject):
            class Reversal(StripeObject):
                class StatusDetails(StripeObject):
                    class Committed(StripeObject):
                        transaction: str
                        """
                        The [Tax Transaction](https://stripe.com/docs/api/tax/transaction/object)
                        """

                    class Errored(StripeObject):
                        reason: Literal[
                            "original_transaction_voided",
                            "unique_reference_violation",
                        ]
                        """
                        Details on why we could not commit the reversal Tax Transaction
                        """
                        refund_id: str
                        """
                        The [Refund](https://stripe.com/docs/api/refunds/object) ID that should have created a tax reversal.
                        """

                    committed: Optional[Committed]
                    errored: Optional[Errored]
                    _inner_class_types = {
                        "committed": Committed,
                        "errored": Errored,
                    }

                status: Literal["committed", "errored"]
                """
                Status of the attempted Tax Transaction reversal.
                """
                status_details: StatusDetails
                _inner_class_types = {"status_details": StatusDetails}

            reversals: List[Reversal]
            """
            Attempts to create Tax Transaction reversals
            """
            transaction: str
            """
            The [Tax Transaction](https://stripe.com/docs/api/tax/transaction/object)
            """
            _inner_class_types = {"reversals": Reversal}

        class Errored(StripeObject):
            reason: Literal[
                "another_payment_associated_with_calculation",
                "calculation_expired",
                "currency_mismatch",
                "unique_reference_violation",
            ]
            """
            Details on why we could not commit the Tax Transaction
            """

        committed: Optional[Committed]
        errored: Optional[Errored]
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
    status: Literal["committed", "errored"]
    """
    Status of the Tax Association.
    """
    status_details: StatusDetails

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

    _inner_class_types = {"status_details": StatusDetails}
