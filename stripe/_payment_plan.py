# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import sanitize_id
from typing import ClassVar, List, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params._payment_plan_create_params import (
        PaymentPlanCreateParams,
    )
    from stripe.params._payment_plan_list_params import PaymentPlanListParams
    from stripe.params._payment_plan_modify_params import (
        PaymentPlanModifyParams,
    )
    from stripe.params._payment_plan_retrieve_params import (
        PaymentPlanRetrieveParams,
    )


class PaymentPlan(
    CreateableAPIResource["PaymentPlan"],
    ListableAPIResource["PaymentPlan"],
    UpdateableAPIResource["PaymentPlan"],
):
    """
    A Payment Plan splits a single invoice obligation into multiple installments,
    each with its own due date and amount. Payment Plans are associated with a
    finalized or draft invoice and track how much has been collected against
    each installment.
    """

    OBJECT_NAME: ClassVar[Literal["payment_plan"]] = "payment_plan"

    class CollectsOn(StripeObject):
        class InvoiceDetails(StripeObject):
            invoice: str
            """
            The ID of the invoice this plan collects against.
            """

        invoice_details: InvoiceDetails
        type: str
        """
        The type of object this plan collects against. Currently always `invoice_details`.
        """
        _inner_class_types = {"invoice_details": InvoiceDetails}

    class Installment(StripeObject):
        amount_due: int
        """
        Amount owed for this installment, in the smallest currency unit.
        """
        amount_forgiven: int
        """
        Amount forgiven for this installment, in the smallest currency unit.
        """
        amount_paid: int
        """
        Amount already paid toward this installment, in the smallest currency unit.
        """
        currency: str
        """
        Three-letter ISO currency code.
        """
        description: str
        """
        A description of this installment.
        """
        due_date: Optional[int]
        """
        Unix timestamp when this installment is due. Omitted for installments with no due date.
        """
        id: Optional[str]
        """
        Unique identifier for the installment.
        """
        paid_at: Optional[int]
        """
        Unix timestamp when this installment was paid.
        """
        status: str
        """
        The status of this installment. One of `open`, `paid`, `past_due`, or `canceled`.
        """

    class Schedule(StripeObject):
        class AmountsDue(StripeObject):
            class Amount(StripeObject):
                class DueDate(StripeObject):
                    class Relative(StripeObject):
                        count: int
                        """
                        The number of intervals after the invoice is finalized that this entry is due.
                        """
                        interval: str
                        """
                        The interval unit: `day`, `week`, `month`, or `year`.
                        """

                    absolute: Optional[int]
                    """
                    Unix timestamp of the due date. Present when type is `absolute`.
                    """
                    relative: Optional[Relative]
                    type: str
                    """
                    The type of due date. Either `absolute` or `relative`.
                    """
                    _inner_class_types = {"relative": Relative}

                class FixedAmount(StripeObject):
                    amount: int
                    """
                    Fixed amount for this entry, in the smallest currency unit.
                    """
                    currency: str
                    """
                    Three-letter ISO currency code.
                    """

                description: str
                """
                A description of this schedule entry.
                """
                due_date: Optional[DueDate]
                fixed_amount: Optional[FixedAmount]
                id: Optional[str]
                """
                Unique identifier for this schedule entry.
                """
                percentage: Optional[float]
                """
                Percentage of the invoice total for this entry (0–100). Present when type is `percentage`.
                """
                type: str
                """
                The type of this schedule entry. Either `fixed_amount` or `percentage`.
                """
                _inner_class_types = {
                    "due_date": DueDate,
                    "fixed_amount": FixedAmount,
                }

            amounts: List[Amount]
            """
            The list of installment schedule entries.
            """
            _inner_class_types = {"amounts": Amount}

        amounts_due: AmountsDue
        type: str
        """
        The type of schedule. Currently always `amounts_due`.
        """
        _inner_class_types = {"amounts_due": AmountsDue}

    collects_on: List[CollectsOn]
    """
    The list of objects this payment plan collects against.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    id: str
    """
    Unique identifier for the object.
    """
    installments: List[Installment]
    """
    The list of installments derived from the schedule. Each installment tracks an individual payment obligation.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["payment_plan"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    schedule: Schedule

    @classmethod
    def create(
        cls, **params: Unpack["PaymentPlanCreateParams"]
    ) -> "PaymentPlan":
        """
        Creates a payment plan that splits a single invoice obligation into installments with their own due dates and amounts.
        """
        return cast(
            "PaymentPlan",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["PaymentPlanCreateParams"]
    ) -> "PaymentPlan":
        """
        Creates a payment plan that splits a single invoice obligation into installments with their own due dates and amounts.
        """
        return cast(
            "PaymentPlan",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["PaymentPlanListParams"]
    ) -> ListObject["PaymentPlan"]:
        """
        Returns a list of payment plans.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["PaymentPlanListParams"]
    ) -> ListObject["PaymentPlan"]:
        """
        Returns a list of payment plans.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["PaymentPlanModifyParams"]
    ) -> "PaymentPlan":
        """
        Updates the schedule or metadata of an existing payment plan. Only unpaid installments can be updated.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "PaymentPlan",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["PaymentPlanModifyParams"]
    ) -> "PaymentPlan":
        """
        Updates the schedule or metadata of an existing payment plan. Only unpaid installments can be updated.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "PaymentPlan",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PaymentPlanRetrieveParams"]
    ) -> "PaymentPlan":
        """
        Retrieves the payment plan with the given ID.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["PaymentPlanRetrieveParams"]
    ) -> "PaymentPlan":
        """
        Retrieves the payment plan with the given ID.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "collects_on": CollectsOn,
        "installments": Installment,
        "schedule": Schedule,
    }
