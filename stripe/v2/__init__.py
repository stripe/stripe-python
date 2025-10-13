from typing_extensions import TYPE_CHECKING
from stripe.v2._list_object import ListObject as ListObject
from stripe.v2._amount import Amount as Amount, AmountParam as AmountParam


# The beginning of the section generated from our OpenAPI spec
from importlib import import_module

if TYPE_CHECKING:
    from stripe.v2 import billing as billing, core as core
    from stripe.v2._billing_service import BillingService as BillingService
    from stripe.v2._core_service import CoreService as CoreService
    from stripe.v2._deleted_object import DeletedObject as DeletedObject

_submodules = {
    "billing": "stripe.v2",
    "core": "stripe.v2",
    "BillingService": "stripe.v2._billing_service",
    "CoreService": "stripe.v2._core_service",
    "DeletedObject": "stripe.v2._deleted_object",
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            return getattr(
                import_module(_submodules[name]),
                name,
            )
        except KeyError:
            raise AttributeError(f"cannot import '{name}' from '{__name__}'")

# The end of the section generated from our OpenAPI spec
