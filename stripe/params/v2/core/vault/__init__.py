# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.core.vault._gb_bank_account_acknowledge_confirmation_of_payee_params import (
        GbBankAccountAcknowledgeConfirmationOfPayeeParams as GbBankAccountAcknowledgeConfirmationOfPayeeParams,
    )
    from stripe.params.v2.core.vault._gb_bank_account_archive_params import (
        GbBankAccountArchiveParams as GbBankAccountArchiveParams,
    )
    from stripe.params.v2.core.vault._gb_bank_account_create_params import (
        GbBankAccountCreateParams as GbBankAccountCreateParams,
        GbBankAccountCreateParamsConfirmationOfPayee as GbBankAccountCreateParamsConfirmationOfPayee,
    )
    from stripe.params.v2.core.vault._gb_bank_account_initiate_confirmation_of_payee_params import (
        GbBankAccountInitiateConfirmationOfPayeeParams as GbBankAccountInitiateConfirmationOfPayeeParams,
    )
    from stripe.params.v2.core.vault._gb_bank_account_list_params import (
        GbBankAccountListParams as GbBankAccountListParams,
    )
    from stripe.params.v2.core.vault._gb_bank_account_retrieve_params import (
        GbBankAccountRetrieveParams as GbBankAccountRetrieveParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_archive_params import (
        UsBankAccountArchiveParams as UsBankAccountArchiveParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_confirm_microdeposits_params import (
        UsBankAccountConfirmMicrodepositsParams as UsBankAccountConfirmMicrodepositsParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_create_params import (
        UsBankAccountCreateParams as UsBankAccountCreateParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_list_params import (
        UsBankAccountListParams as UsBankAccountListParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_retrieve_params import (
        UsBankAccountRetrieveParams as UsBankAccountRetrieveParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_send_microdeposits_params import (
        UsBankAccountSendMicrodepositsParams as UsBankAccountSendMicrodepositsParams,
    )
    from stripe.params.v2.core.vault._us_bank_account_update_params import (
        UsBankAccountUpdateParams as UsBankAccountUpdateParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "GbBankAccountAcknowledgeConfirmationOfPayeeParams": (
        "stripe.params.v2.core.vault._gb_bank_account_acknowledge_confirmation_of_payee_params",
        False,
    ),
    "GbBankAccountArchiveParams": (
        "stripe.params.v2.core.vault._gb_bank_account_archive_params",
        False,
    ),
    "GbBankAccountCreateParams": (
        "stripe.params.v2.core.vault._gb_bank_account_create_params",
        False,
    ),
    "GbBankAccountCreateParamsConfirmationOfPayee": (
        "stripe.params.v2.core.vault._gb_bank_account_create_params",
        False,
    ),
    "GbBankAccountInitiateConfirmationOfPayeeParams": (
        "stripe.params.v2.core.vault._gb_bank_account_initiate_confirmation_of_payee_params",
        False,
    ),
    "GbBankAccountListParams": (
        "stripe.params.v2.core.vault._gb_bank_account_list_params",
        False,
    ),
    "GbBankAccountRetrieveParams": (
        "stripe.params.v2.core.vault._gb_bank_account_retrieve_params",
        False,
    ),
    "UsBankAccountArchiveParams": (
        "stripe.params.v2.core.vault._us_bank_account_archive_params",
        False,
    ),
    "UsBankAccountConfirmMicrodepositsParams": (
        "stripe.params.v2.core.vault._us_bank_account_confirm_microdeposits_params",
        False,
    ),
    "UsBankAccountCreateParams": (
        "stripe.params.v2.core.vault._us_bank_account_create_params",
        False,
    ),
    "UsBankAccountListParams": (
        "stripe.params.v2.core.vault._us_bank_account_list_params",
        False,
    ),
    "UsBankAccountRetrieveParams": (
        "stripe.params.v2.core.vault._us_bank_account_retrieve_params",
        False,
    ),
    "UsBankAccountSendMicrodepositsParams": (
        "stripe.params.v2.core.vault._us_bank_account_send_microdeposits_params",
        False,
    ),
    "UsBankAccountUpdateParams": (
        "stripe.params.v2.core.vault._us_bank_account_update_params",
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
