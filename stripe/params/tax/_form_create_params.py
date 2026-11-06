# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired, TypedDict


class FormCreateParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    payee_details: NotRequired["FormCreateParamsPayeeDetails"]
    """
    Replacement payee details. Cannot be combined with numerical correction fields. Omitted fields remain unchanged.
    """
    second_tin_notice: NotRequired[bool]
    """
    Whether a second TIN notice was received. Supported for K and MISC forms only; cannot be supplied without a substantive correction.
    """
    us_1099_k: NotRequired["FormCreateParamsUs1099K"]
    """
    Replacement numerical values for a 1099-K. Supply only the group matching the original form. Omitted fields remain unchanged.
    """
    us_1099_misc: NotRequired["FormCreateParamsUs1099Misc"]
    """
    Replacement numerical values for a 1099-MISC. Supply only the group matching the original form. Omitted fields remain unchanged.
    """
    us_1099_nec: NotRequired["FormCreateParamsUs1099Nec"]
    """
    Replacement numerical values for a 1099-NEC. Supply only the group matching the original form. Omitted fields remain unchanged.
    """


class FormCreateParamsPayeeDetails(TypedDict):
    address: NotRequired["FormCreateParamsPayeeDetailsAddress"]
    """
    The payee's replacement address fields. Omitted fields remain unchanged.
    """
    merchant_category_code: NotRequired[str]
    """
    The payee's merchant category code.
    """
    name_line_1: NotRequired[str]
    """
    The first line of the payee's name.
    """
    name_line_2: NotRequired[str]
    """
    The second line of the payee's name. An empty string clears this field.
    """
    tax_id_number: NotRequired[str]
    """
    The payee's US taxpayer identification number.
    """
    treasury_tipped_occupation_code: NotRequired[str]
    """
    The payee's Treasury tipped occupation code, where supported by the reporting year and form type.
    """


class FormCreateParamsPayeeDetailsAddress(TypedDict):
    city: NotRequired[str]
    """
    The city of the payee's address.
    """
    country: NotRequired[str]
    """
    The two-letter country code of the payee's address.
    """
    line1: NotRequired[str]
    """
    The first line of the payee's address.
    """
    line2: NotRequired[str]
    """
    The second line of the payee's address. An empty string clears this field.
    """
    postal_code: NotRequired[str]
    """
    The postal code of the payee's address.
    """
    state: NotRequired[str]
    """
    The state of the payee's address.
    """


class FormCreateParamsUs1099K(TypedDict):
    card_not_present_transactions: NotRequired[
        "FormCreateParamsUs1099KCardNotPresentTransactions"
    ]
    """
    Replacement card-not-present transaction amount.
    """
    cash_tips: NotRequired["FormCreateParamsUs1099KCashTips"]
    """
    Replacement cash tips, where supported by the reporting year.
    """
    federal_income_tax_withheld: NotRequired[
        "FormCreateParamsUs1099KFederalIncomeTaxWithheld"
    ]
    """
    Replacement federal income tax withheld.
    """
    monthly_volumes: NotRequired[List["FormCreateParamsUs1099KMonthlyVolume"]]
    """
    Replacement amounts for all twelve months, from January through December.
    """
    payment_transactions_count: NotRequired[
        "FormCreateParamsUs1099KPaymentTransactionsCount"
    ]
    """
    Replacement payment transaction count.
    """
    state_income_tax_withheld: NotRequired[
        "FormCreateParamsUs1099KStateIncomeTaxWithheld"
    ]
    """
    Replacement state income tax withheld.
    """


class FormCreateParamsUs1099KCardNotPresentTransactions(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099KCashTips(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099KFederalIncomeTaxWithheld(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099KMonthlyVolume(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099KPaymentTransactionsCount(TypedDict):
    count: int
    """
    The replacement non-negative transaction count.
    """


class FormCreateParamsUs1099KStateIncomeTaxWithheld(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099Misc(TypedDict):
    cash_tips: NotRequired["FormCreateParamsUs1099MiscCashTips"]
    """
    Replacement cash tips, where supported by the reporting year.
    """
    crop_insurance_proceeds: NotRequired[
        "FormCreateParamsUs1099MiscCropInsuranceProceeds"
    ]
    """
    Replacement crop insurance proceeds.
    """
    direct_sales_for_resale: NotRequired[bool]
    """
    Replacement direct-sales-for-resale indicator.
    """
    excess_golden_parachute_payments: NotRequired[
        "FormCreateParamsUs1099MiscExcessGoldenParachutePayments"
    ]
    """
    Replacement excess golden parachute payments, where supported by the reporting year.
    """
    fatca_filing_required: NotRequired[bool]
    """
    Replacement FATCA filing requirement; cannot be supplied without a substantive correction.
    """
    federal_income_tax_withheld: NotRequired[
        "FormCreateParamsUs1099MiscFederalIncomeTaxWithheld"
    ]
    """
    Replacement federal income tax withheld.
    """
    fish_purchased_for_resale: NotRequired[
        "FormCreateParamsUs1099MiscFishPurchasedForResale"
    ]
    """
    Replacement fish purchased for resale.
    """
    fishing_boat_proceeds: NotRequired[
        "FormCreateParamsUs1099MiscFishingBoatProceeds"
    ]
    """
    Replacement fishing boat proceeds.
    """
    gross_proceeds_paid_to_an_attorney: NotRequired[
        "FormCreateParamsUs1099MiscGrossProceedsPaidToAnAttorney"
    ]
    """
    Replacement gross proceeds paid to an attorney.
    """
    medical_and_health_care_payments: NotRequired[
        "FormCreateParamsUs1099MiscMedicalAndHealthCarePayments"
    ]
    """
    Replacement medical and health care payments.
    """
    nonqualified_deferred_compensation: NotRequired[
        "FormCreateParamsUs1099MiscNonqualifiedDeferredCompensation"
    ]
    """
    Replacement nonqualified deferred compensation.
    """
    other_income: NotRequired["FormCreateParamsUs1099MiscOtherIncome"]
    """
    Replacement other income.
    """
    overtime_compensation: NotRequired[
        "FormCreateParamsUs1099MiscOvertimeCompensation"
    ]
    """
    Replacement overtime compensation, where supported by the reporting year.
    """
    rents: NotRequired["FormCreateParamsUs1099MiscRents"]
    """
    Replacement rents.
    """
    royalties: NotRequired["FormCreateParamsUs1099MiscRoyalties"]
    """
    Replacement royalties.
    """
    section_409a_deferrals: NotRequired[
        "FormCreateParamsUs1099MiscSection409aDeferrals"
    ]
    """
    Replacement section 409A deferrals.
    """
    state_income: NotRequired["FormCreateParamsUs1099MiscStateIncome"]
    """
    Replacement state income.
    """
    state_tax_withheld: NotRequired[
        "FormCreateParamsUs1099MiscStateTaxWithheld"
    ]
    """
    Replacement state tax withheld.
    """
    substitute_payments: NotRequired[
        "FormCreateParamsUs1099MiscSubstitutePayments"
    ]
    """
    Replacement substitute payments.
    """


class FormCreateParamsUs1099MiscCashTips(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscCropInsuranceProceeds(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscExcessGoldenParachutePayments(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscFederalIncomeTaxWithheld(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscFishPurchasedForResale(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscFishingBoatProceeds(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscGrossProceedsPaidToAnAttorney(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscMedicalAndHealthCarePayments(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscNonqualifiedDeferredCompensation(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscOtherIncome(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscOvertimeCompensation(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscRents(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscRoyalties(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscSection409aDeferrals(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscStateIncome(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscStateTaxWithheld(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099MiscSubstitutePayments(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099Nec(TypedDict):
    cash_tips: NotRequired["FormCreateParamsUs1099NecCashTips"]
    """
    Replacement cash tips, where supported by the reporting year.
    """
    direct_sales_indicator: NotRequired[bool]
    """
    Replacement direct-sales indicator.
    """
    federal_income_tax_withheld: NotRequired[
        "FormCreateParamsUs1099NecFederalIncomeTaxWithheld"
    ]
    """
    Replacement federal income tax withheld.
    """
    nonemployee_compensation: NotRequired[
        "FormCreateParamsUs1099NecNonemployeeCompensation"
    ]
    """
    Replacement nonemployee compensation.
    """
    overtime_compensation: NotRequired[
        "FormCreateParamsUs1099NecOvertimeCompensation"
    ]
    """
    Replacement overtime compensation, where supported by the reporting year.
    """
    state_income: NotRequired["FormCreateParamsUs1099NecStateIncome"]
    """
    Replacement state income.
    """
    state_tax_withheld: NotRequired[
        "FormCreateParamsUs1099NecStateTaxWithheld"
    ]
    """
    Replacement state tax withheld.
    """


class FormCreateParamsUs1099NecCashTips(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099NecFederalIncomeTaxWithheld(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099NecNonemployeeCompensation(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099NecOvertimeCompensation(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099NecStateIncome(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """


class FormCreateParamsUs1099NecStateTaxWithheld(TypedDict):
    volume_decimal: str
    """
    The replacement amount in major currency units, with at most two decimal places. Must be non-negative.
    """
