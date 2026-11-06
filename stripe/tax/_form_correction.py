# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class FormCorrection(StripeObject):
    """
    Corrections to filed tax forms.
    """

    OBJECT_NAME: ClassVar[Literal["tax.form_correction"]] = (
        "tax.form_correction"
    )

    class CorrectionForm(StripeObject):
        correction_type: Optional[Literal["payee_changed", "totals_changed"]]
        """
        The kind of information changed by this correction.
        """
        form: Optional[str]
        """
        The corrected tax form.
        """

    correction_forms: Optional[List[CorrectionForm]]
    """
    The tax forms created by the correction.
    """
    object: Literal["tax.form_correction"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    original_form: Optional[str]
    """
    The original tax form that was corrected.
    """
    _inner_class_types = {"correction_forms": CorrectionForm}
