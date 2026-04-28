# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2._billing_service import BillingService
    from stripe.v2._commerce_service import CommerceService
    from stripe.v2._core_service import CoreService
    from stripe.v2._data_service import DataService
    from stripe.v2._extend_service import ExtendService
    from stripe.v2._iam_service import IamService
    from stripe.v2._money_management_service import MoneyManagementService
    from stripe.v2._network_service import NetworkService
    from stripe.v2._orchestrated_commerce_service import (
        OrchestratedCommerceService,
    )
    from stripe.v2._payment_service import PaymentService
    from stripe.v2._reporting_service import ReportingService
    from stripe.v2._tax_service import TaxService
    from stripe.v2._test_helper_service import TestHelperService

_subservices = {
    "billing": ["stripe.v2._billing_service", "BillingService"],
    "commerce": ["stripe.v2._commerce_service", "CommerceService"],
    "core": ["stripe.v2._core_service", "CoreService"],
    "data": ["stripe.v2._data_service", "DataService"],
    "extend": ["stripe.v2._extend_service", "ExtendService"],
    "iam": ["stripe.v2._iam_service", "IamService"],
    "money_management": [
        "stripe.v2._money_management_service",
        "MoneyManagementService",
    ],
    "network": ["stripe.v2._network_service", "NetworkService"],
    "orchestrated_commerce": [
        "stripe.v2._orchestrated_commerce_service",
        "OrchestratedCommerceService",
    ],
    "payments": ["stripe.v2._payment_service", "PaymentService"],
    "reporting": ["stripe.v2._reporting_service", "ReportingService"],
    "tax": ["stripe.v2._tax_service", "TaxService"],
    "test_helpers": ["stripe.v2._test_helper_service", "TestHelperService"],
}


class V2Services(StripeService):
    billing: "BillingService"
    commerce: "CommerceService"
    core: "CoreService"
    data: "DataService"
    extend: "ExtendService"
    iam: "IamService"
    money_management: "MoneyManagementService"
    network: "NetworkService"
    orchestrated_commerce: "OrchestratedCommerceService"
    payments: "PaymentService"
    reporting: "ReportingService"
    tax: "TaxService"
    test_helpers: "TestHelperService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()
