from typing_extensions import TYPE_CHECKING
from stripe.v2._list_object import ListObject as ListObject
from stripe.v2._amount import Amount as Amount, AmountParam as AmountParam


# The beginning of the section generated from our OpenAPI spec
from importlib import import_module

if TYPE_CHECKING:
    from stripe.v2 import (
        billing as billing,
        core as core,
        iam as iam,
        money_management as money_management,
        payments as payments,
        reporting as reporting,
        tax as tax,
        test_helpers as test_helpers,
    )
    from stripe.v2._billing_service import BillingService as BillingService
    from stripe.v2._core_service import CoreService as CoreService
    from stripe.v2._deleted_object import DeletedObject as DeletedObject
    from stripe.v2._financial_address_credit_simulation import (
        FinancialAddressCreditSimulation as FinancialAddressCreditSimulation,
    )
    from stripe.v2._financial_address_generated_microdeposits import (
        FinancialAddressGeneratedMicrodeposits as FinancialAddressGeneratedMicrodeposits,
    )
    from stripe.v2._iam_service import IamService as IamService
    from stripe.v2._money_management_service import (
        MoneyManagementService as MoneyManagementService,
    )
    from stripe.v2._payment_service import PaymentService as PaymentService
    from stripe.v2._reporting_service import (
        ReportingService as ReportingService,
    )
    from stripe.v2._tax_service import TaxService as TaxService
    from stripe.v2._test_helper_service import (
        TestHelperService as TestHelperService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "billing": ("stripe.v2.billing", True),
    "core": ("stripe.v2.core", True),
    "iam": ("stripe.v2.iam", True),
    "money_management": ("stripe.v2.money_management", True),
    "payments": ("stripe.v2.payments", True),
    "reporting": ("stripe.v2.reporting", True),
    "tax": ("stripe.v2.tax", True),
    "test_helpers": ("stripe.v2.test_helpers", True),
    "BillingService": ("stripe.v2._billing_service", False),
    "CoreService": ("stripe.v2._core_service", False),
    "DeletedObject": ("stripe.v2._deleted_object", False),
    "FinancialAddressCreditSimulation": (
        "stripe.v2._financial_address_credit_simulation",
        False,
    ),
    "FinancialAddressGeneratedMicrodeposits": (
        "stripe.v2._financial_address_generated_microdeposits",
        False,
    ),
    "IamService": ("stripe.v2._iam_service", False),
    "MoneyManagementService": ("stripe.v2._money_management_service", False),
    "PaymentService": ("stripe.v2._payment_service", False),
    "ReportingService": ("stripe.v2._reporting_service", False),
    "TaxService": ("stripe.v2._tax_service", False),
    "TestHelperService": ("stripe.v2._test_helper_service", False),
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            target, is_submodule = _import_map[name]
            module = import_module(target)
            if is_submodule:
                return module

            return getattr(
                module,
                name,
            )
        except KeyError:
            raise AttributeError()

# The end of the section generated from our OpenAPI spec
