# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.climate._order_service import OrderService
from stripe.climate._product_service import ProductService
from stripe.climate._supplier_service import SupplierService
from importlib import import_module

_subservices = {
    "orders": ["stripe._account_service", "AccountService"],
    "products": ["stripe._account_service", "AccountService"],
    "suppliers": ["stripe._account_service", "AccountService"],
}


class ClimateService(StripeService):
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
