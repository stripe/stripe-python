# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.capital._financing_offer_create_params import (
        FinancingOfferCreateParams as FinancingOfferCreateParams,
    )
    from stripe.params.capital._financing_offer_list_params import (
        FinancingOfferListParams as FinancingOfferListParams,
        FinancingOfferListParamsCreated as FinancingOfferListParamsCreated,
    )
    from stripe.params.capital._financing_offer_mark_delivered_params import (
        FinancingOfferMarkDeliveredParams as FinancingOfferMarkDeliveredParams,
    )
    from stripe.params.capital._financing_offer_refill_params import (
        FinancingOfferRefillParams as FinancingOfferRefillParams,
    )
    from stripe.params.capital._financing_offer_retrieve_params import (
        FinancingOfferRetrieveParams as FinancingOfferRetrieveParams,
    )
    from stripe.params.capital._financing_summary_retrieve_params import (
        FinancingSummaryRetrieveParams as FinancingSummaryRetrieveParams,
    )
    from stripe.params.capital._financing_transaction_list_params import (
        FinancingTransactionListParams as FinancingTransactionListParams,
    )
    from stripe.params.capital._financing_transaction_retrieve_params import (
        FinancingTransactionRetrieveParams as FinancingTransactionRetrieveParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "FinancingOfferCreateParams": (
        "stripe.params.capital._financing_offer_create_params",
        False,
    ),
    "FinancingOfferListParams": (
        "stripe.params.capital._financing_offer_list_params",
        False,
    ),
    "FinancingOfferListParamsCreated": (
        "stripe.params.capital._financing_offer_list_params",
        False,
    ),
    "FinancingOfferMarkDeliveredParams": (
        "stripe.params.capital._financing_offer_mark_delivered_params",
        False,
    ),
    "FinancingOfferRefillParams": (
        "stripe.params.capital._financing_offer_refill_params",
        False,
    ),
    "FinancingOfferRetrieveParams": (
        "stripe.params.capital._financing_offer_retrieve_params",
        False,
    ),
    "FinancingSummaryRetrieveParams": (
        "stripe.params.capital._financing_summary_retrieve_params",
        False,
    ),
    "FinancingTransactionListParams": (
        "stripe.params.capital._financing_transaction_list_params",
        False,
    ),
    "FinancingTransactionRetrieveParams": (
        "stripe.params.capital._financing_transaction_retrieve_params",
        False,
    ),
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
