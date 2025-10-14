# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.radar._early_fraud_warning_service import EarlyFraudWarningService
from stripe.radar._value_list_item_service import ValueListItemService
from stripe.radar._value_list_service import ValueListService
from importlib import import_module

_subservices = {
    "early_fraud_warnings": ["stripe._account_service", "AccountService"],
    "value_lists": ["stripe._account_service", "AccountService"],
    "value_list_items": ["stripe._account_service", "AccountService"],
}


class RadarService(StripeService):
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
