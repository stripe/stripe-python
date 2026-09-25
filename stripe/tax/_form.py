# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from stripe._util import class_method_variant, sanitize_id
from typing import Any, ClassVar, List, Optional, Union, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._account import Account
    from stripe.params.tax._form_list_params import FormListParams
    from stripe.params.tax._form_pdf_params import FormPdfParams
    from stripe.params.tax._form_retrieve_params import FormRetrieveParams


class Form(ListableAPIResource["Form"]):
    """
    Tax forms are legal documents which are delivered to one or more tax authorities for information reporting purposes.

    Related guide: [US tax reporting for Connect platforms](https://stripe.com/docs/connect/tax-reporting)
    """

    OBJECT_NAME: ClassVar[Literal["tax.form"]] = "tax.form"

    class AuSerr(StripeObject):
        reporting_period_end_date: str
        """
        End date of the period represented by the information reported on the tax form.
        """
        reporting_period_start_date: str
        """
        Start date of the period represented by the information reported on the tax form.
        """

    class CaMrdp(StripeObject):
        reporting_period_end_date: str
        """
        End date of the period represented by the information reported on the tax form.
        """
        reporting_period_start_date: str
        """
        Start date of the period represented by the information reported on the tax form.
        """

    class EuDac7(StripeObject):
        reporting_period_end_date: str
        """
        End date of the period represented by the information reported on the tax form.
        """
        reporting_period_start_date: str
        """
        Start date of the period represented by the information reported on the tax form.
        """

    class FilingStatus(StripeObject):
        class Jurisdiction(StripeObject):
            country: str
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            level: Union[Literal["country", "state"], str]
            """
            Indicates the level of the jurisdiction where the form was filed.
            """
            state: Optional[str]
            """
            [ISO 3166-2 U.S. state code](https://en.wikipedia.org/wiki/ISO_3166-2:US), without country prefix, if any. For example, "NY" for New York, United States. Null for non-U.S. forms.
            """

        effective_at: int
        """
        Time when the filing status was updated.
        """
        jurisdiction: Jurisdiction
        value: Union[Literal["accepted", "filed", "rejected"], str]
        """
        The current status of the filed form.
        """
        _inner_class_types = {"jurisdiction": Jurisdiction}

    class GbMrdp(StripeObject):
        reporting_period_end_date: str
        """
        End date of the period represented by the information reported on the tax form.
        """
        reporting_period_start_date: str
        """
        Start date of the period represented by the information reported on the tax form.
        """

    class NzMrdp(StripeObject):
        reporting_period_end_date: str
        """
        End date of the period represented by the information reported on the tax form.
        """
        reporting_period_start_date: str
        """
        Start date of the period represented by the information reported on the tax form.
        """

    class Payee(StripeObject):
        account: Optional[ExpandableField["Account"]]
        """
        The ID of the payee's Stripe account.
        """
        external_reference: Optional[str]
        """
        The external reference to this payee.
        """
        type: Union[Literal["account", "external_reference"], str]
        """
        Specifies the payee type.
        """

    class Us1099K(StripeObject):
        class CardNotPresentTransactions(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class CashTips(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class FederalIncomeTaxWithheld(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class MonthlyVolume(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class PaymentTransactionsCount(StripeObject):
            count: Optional[int]
            """
            The effective number of transactions.
            """
            delta: Optional[int]
            """
            The signed adjustment included in the effective count. Only present for drafts.
            """

        class StateIncomeTaxWithheld(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        card_not_present_transactions: Optional[CardNotPresentTransactions]
        cash_tips: Optional[CashTips]
        currency: Optional[str]
        """
        The currency of the amounts on the form. Always `usd`.
        """
        federal_income_tax_withheld: Optional[FederalIncomeTaxWithheld]
        gross_amount_of_transactions_decimal: Optional[str]
        """
        The gross amount of payment transactions, as a decimal string in USD.
        """
        monthly_volumes: Optional[List[MonthlyVolume]]
        """
        The gross amounts for each month, ordered from January through December.
        """
        payment_transactions_count: Optional[PaymentTransactionsCount]
        reporting_year: int
        """
        Year represented by the information reported on the tax form.
        """
        state_income_tax_withheld: Optional[StateIncomeTaxWithheld]
        _inner_class_types = {
            "card_not_present_transactions": CardNotPresentTransactions,
            "cash_tips": CashTips,
            "federal_income_tax_withheld": FederalIncomeTaxWithheld,
            "monthly_volumes": MonthlyVolume,
            "payment_transactions_count": PaymentTransactionsCount,
            "state_income_tax_withheld": StateIncomeTaxWithheld,
        }

    class Us1099Misc(StripeObject):
        class CashTips(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class CropInsuranceProceeds(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class ExcessGoldenParachutePayments(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class FederalIncomeTaxWithheld(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class FishPurchasedForResale(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class FishingBoatProceeds(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class GrossProceedsPaidToAnAttorney(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class MedicalAndHealthCarePayments(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class NonqualifiedDeferredCompensation(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class OtherIncome(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class OvertimeCompensation(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class Rents(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class Royalties(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class Section409aDeferrals(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class StateIncome(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class StateTaxWithheld(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class SubstitutePayments(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        cash_tips: Optional[CashTips]
        crop_insurance_proceeds: Optional[CropInsuranceProceeds]
        currency: Optional[str]
        """
        The currency of the amounts on the form. Always `usd`.
        """
        direct_sales_for_resale: Optional[bool]
        """
        Whether direct sales of at least $5,000 of consumer products were made for resale.
        """
        excess_golden_parachute_payments: Optional[
            ExcessGoldenParachutePayments
        ]
        fatca_filing_required: Optional[bool]
        """
        Whether the FATCA filing requirement applies.
        """
        federal_income_tax_withheld: Optional[FederalIncomeTaxWithheld]
        fish_purchased_for_resale: Optional[FishPurchasedForResale]
        fishing_boat_proceeds: Optional[FishingBoatProceeds]
        gross_proceeds_paid_to_an_attorney: Optional[
            GrossProceedsPaidToAnAttorney
        ]
        medical_and_health_care_payments: Optional[
            MedicalAndHealthCarePayments
        ]
        nonqualified_deferred_compensation: Optional[
            NonqualifiedDeferredCompensation
        ]
        other_income: Optional[OtherIncome]
        overtime_compensation: Optional[OvertimeCompensation]
        rents: Optional[Rents]
        reporting_year: int
        """
        Year represented by the information reported on the tax form.
        """
        royalties: Optional[Royalties]
        section_409a_deferrals: Optional[Section409aDeferrals]
        state_income: Optional[StateIncome]
        state_tax_withheld: Optional[StateTaxWithheld]
        substitute_payments: Optional[SubstitutePayments]
        _inner_class_types = {
            "cash_tips": CashTips,
            "crop_insurance_proceeds": CropInsuranceProceeds,
            "excess_golden_parachute_payments": ExcessGoldenParachutePayments,
            "federal_income_tax_withheld": FederalIncomeTaxWithheld,
            "fish_purchased_for_resale": FishPurchasedForResale,
            "fishing_boat_proceeds": FishingBoatProceeds,
            "gross_proceeds_paid_to_an_attorney": GrossProceedsPaidToAnAttorney,
            "medical_and_health_care_payments": MedicalAndHealthCarePayments,
            "nonqualified_deferred_compensation": NonqualifiedDeferredCompensation,
            "other_income": OtherIncome,
            "overtime_compensation": OvertimeCompensation,
            "rents": Rents,
            "royalties": Royalties,
            "section_409a_deferrals": Section409aDeferrals,
            "state_income": StateIncome,
            "state_tax_withheld": StateTaxWithheld,
            "substitute_payments": SubstitutePayments,
        }

    class Us1099Nec(StripeObject):
        class CashTips(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class FederalIncomeTaxWithheld(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class NonemployeeCompensation(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class OvertimeCompensation(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class StateIncome(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        class StateTaxWithheld(StripeObject):
            delta_decimal: Optional[str]
            """
            The signed adjustment included in the effective amount, as a decimal string. Only present for drafts.
            """
            volume_decimal: Optional[str]
            """
            The effective amount in the form's currency, as a decimal string.
            """

        cash_tips: Optional[CashTips]
        currency: Optional[str]
        """
        The currency of the amounts on the form. Always `usd`.
        """
        direct_sales_indicator: Optional[bool]
        """
        Whether direct sales of at least $5,000 of consumer products were made for resale.
        """
        fatca_filing_requirement: Optional[bool]
        """
        Whether the FATCA filing requirement applies.
        """
        federal_income_tax_withheld: Optional[FederalIncomeTaxWithheld]
        nonemployee_compensation: Optional[NonemployeeCompensation]
        overtime_compensation: Optional[OvertimeCompensation]
        reporting_year: int
        """
        Year represented by the information reported on the tax form.
        """
        state_income: Optional[StateIncome]
        state_tax_withheld: Optional[StateTaxWithheld]
        _inner_class_types = {
            "cash_tips": CashTips,
            "federal_income_tax_withheld": FederalIncomeTaxWithheld,
            "nonemployee_compensation": NonemployeeCompensation,
            "overtime_compensation": OvertimeCompensation,
            "state_income": StateIncome,
            "state_tax_withheld": StateTaxWithheld,
        }

    au_serr: Optional[AuSerr]
    ca_mrdp: Optional[CaMrdp]
    corrected_by: Optional[ExpandableField["Form"]]
    """
    The form that corrects this form, if any.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    eu_dac7: Optional[EuDac7]
    filing_statuses: List[FilingStatus]
    """
    A list of tax filing statuses. Note that a filing status will only be included if the form has been filed directly with the jurisdiction's tax authority.
    """
    gb_mrdp: Optional[GbMrdp]
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    nz_mrdp: Optional[NzMrdp]
    object: Literal["tax.form"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payee: Payee
    status: Optional[Literal["draft", "finalized"]]
    """
    Whether the tax form is a mutable draft or a finalized form.
    """
    type: Union[
        Literal[
            "au_serr",
            "ca_mrdp",
            "eu_dac7",
            "gb_mrdp",
            "nz_mrdp",
            "us_1099_k",
            "us_1099_misc",
            "us_1099_nec",
        ],
        str,
    ]
    """
    The type of the tax form. An additional hash is included on the tax form with a name matching this value. It contains additional information specific to the tax form type.
    """
    us_1099_k: Optional[Us1099K]
    us_1099_misc: Optional[Us1099Misc]
    us_1099_nec: Optional[Us1099Nec]

    @classmethod
    def list(cls, **params: Unpack["FormListParams"]) -> ListObject["Form"]:
        """
        Returns a list of tax forms which were previously created. The tax forms are returned in sorted order, with the oldest tax forms appearing first.
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
        cls, **params: Unpack["FormListParams"]
    ) -> ListObject["Form"]:
        """
        Returns a list of tax forms which were previously created. The tax forms are returned in sorted order, with the oldest tax forms appearing first.
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
    def _cls_pdf(cls, id: str, /, **params: Unpack["FormPdfParams"]) -> Any:
        """
        Download the PDF for a tax form.
        """
        return cast(
            Any,
            cls._static_request_stream(
                "get",
                "/v1/tax/forms/{id}/pdf".format(id=sanitize_id(id)),
                params=params,
                base_address="files",
            ),
        )

    @overload
    @staticmethod
    def pdf(id: str, /, **params: Unpack["FormPdfParams"]) -> Any:
        """
        Download the PDF for a tax form.
        """
        ...

    @overload
    def pdf(self, **params: Unpack["FormPdfParams"]) -> Any:
        """
        Download the PDF for a tax form.
        """
        ...

    @class_method_variant("_cls_pdf")
    def pdf(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["FormPdfParams"]
    ) -> Any:
        """
        Download the PDF for a tax form.
        """
        return cast(
            Any,
            self._request_stream(
                "get",
                "/v1/tax/forms/{id}/pdf".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
                base_address="files",
            ),
        )

    @classmethod
    async def _cls_pdf_async(
        cls, id: str, /, **params: Unpack["FormPdfParams"]
    ) -> Any:
        """
        Download the PDF for a tax form.
        """
        return cast(
            Any,
            await cls._static_request_stream_async(
                "get",
                "/v1/tax/forms/{id}/pdf".format(id=sanitize_id(id)),
                params=params,
                base_address="files",
            ),
        )

    @overload
    @staticmethod
    async def pdf_async(id: str, /, **params: Unpack["FormPdfParams"]) -> Any:
        """
        Download the PDF for a tax form.
        """
        ...

    @overload
    async def pdf_async(self, **params: Unpack["FormPdfParams"]) -> Any:
        """
        Download the PDF for a tax form.
        """
        ...

    @class_method_variant("_cls_pdf_async")
    async def pdf_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["FormPdfParams"]
    ) -> Any:
        """
        Download the PDF for a tax form.
        """
        return cast(
            Any,
            await self._request_stream_async(
                "get",
                "/v1/tax/forms/{id}/pdf".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
                base_address="files",
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["FormRetrieveParams"]
    ) -> "Form":
        """
        Retrieves the details of a tax form that has previously been created. Supply the unique tax form ID that was returned from your previous request, and Stripe will return the corresponding tax form information.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["FormRetrieveParams"]
    ) -> "Form":
        """
        Retrieves the details of a tax form that has previously been created. Supply the unique tax form ID that was returned from your previous request, and Stripe will return the corresponding tax form information.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "au_serr": AuSerr,
        "ca_mrdp": CaMrdp,
        "eu_dac7": EuDac7,
        "filing_statuses": FilingStatus,
        "gb_mrdp": GbMrdp,
        "nz_mrdp": NzMrdp,
        "payee": Payee,
        "us_1099_k": Us1099K,
        "us_1099_misc": Us1099Misc,
        "us_1099_nec": Us1099Nec,
    }
