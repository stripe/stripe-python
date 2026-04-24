from typing_extensions import TYPE_CHECKING
from stripe.v2._list_object import ListObject as ListObject
from stripe.v2._amount import Amount as Amount, AmountParam as AmountParam


# The beginning of the section generated from our OpenAPI spec
from importlib import import_module

if TYPE_CHECKING:
    from stripe.v2 import (
        billing as billing,
        commerce as commerce,
        core as core,
        data as data,
        extend as extend,
        iam as iam,
        money_management as money_management,
        network as network,
        orchestrated_commerce as orchestrated_commerce,
        test_helpers as test_helpers,
    )
    from stripe.v2._billing_service import BillingService as BillingService
    from stripe.v2._commerce_service import CommerceService as CommerceService
    from stripe.v2._core_service import CoreService as CoreService
    from stripe.v2._datum_service import DatumService as DatumService
    from stripe.v2._deleted_object import DeletedObject as DeletedObject
    from stripe.v2._extend_service import ExtendService as ExtendService
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
    from stripe.v2._network_service import NetworkService as NetworkService
    from stripe.v2._orchestrated_commerce_service import (
        OrchestratedCommerceService as OrchestratedCommerceService,
    )
    from stripe.v2._test_helper_service import (
        TestHelperService as TestHelperService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "billing": ("stripe.v2.billing", True),
    "commerce": ("stripe.v2.commerce", True),
    "core": ("stripe.v2.core", True),
    "data": ("stripe.v2.data", True),
    "extend": ("stripe.v2.extend", True),
    "iam": ("stripe.v2.iam", True),
    "money_management": ("stripe.v2.money_management", True),
    "network": ("stripe.v2.network", True),
    "orchestrated_commerce": ("stripe.v2.orchestrated_commerce", True),
    "test_helpers": ("stripe.v2.test_helpers", True),
    "BillingService": ("stripe.v2._billing_service", False),
    "CommerceService": ("stripe.v2._commerce_service", False),
    "CoreService": ("stripe.v2._core_service", False),
    "DatumService": ("stripe.v2._datum_service", False),
    "DeletedObject": ("stripe.v2._deleted_object", False),
    "ExtendService": ("stripe.v2._extend_service", False),
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
    "NetworkService": ("stripe.v2._network_service", False),
    "OrchestratedCommerceService": (
        "stripe.v2._orchestrated_commerce_service",
        False,
    ),
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
