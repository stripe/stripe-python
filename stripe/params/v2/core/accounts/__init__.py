# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.core.accounts._person_create_params import (
        PersonCreateParams as PersonCreateParams,
        PersonCreateParamsAdditionalAddress as PersonCreateParamsAdditionalAddress,
        PersonCreateParamsAdditionalName as PersonCreateParamsAdditionalName,
        PersonCreateParamsAdditionalTermsOfService as PersonCreateParamsAdditionalTermsOfService,
        PersonCreateParamsAdditionalTermsOfServiceAccount as PersonCreateParamsAdditionalTermsOfServiceAccount,
        PersonCreateParamsAddress as PersonCreateParamsAddress,
        PersonCreateParamsDateOfBirth as PersonCreateParamsDateOfBirth,
        PersonCreateParamsDocuments as PersonCreateParamsDocuments,
        PersonCreateParamsDocumentsCompanyAuthorization as PersonCreateParamsDocumentsCompanyAuthorization,
        PersonCreateParamsDocumentsPassport as PersonCreateParamsDocumentsPassport,
        PersonCreateParamsDocumentsPrimaryVerification as PersonCreateParamsDocumentsPrimaryVerification,
        PersonCreateParamsDocumentsPrimaryVerificationFrontBack as PersonCreateParamsDocumentsPrimaryVerificationFrontBack,
        PersonCreateParamsDocumentsSecondaryVerification as PersonCreateParamsDocumentsSecondaryVerification,
        PersonCreateParamsDocumentsSecondaryVerificationFrontBack as PersonCreateParamsDocumentsSecondaryVerificationFrontBack,
        PersonCreateParamsDocumentsVisa as PersonCreateParamsDocumentsVisa,
        PersonCreateParamsIdNumber as PersonCreateParamsIdNumber,
        PersonCreateParamsRelationship as PersonCreateParamsRelationship,
        PersonCreateParamsScriptAddresses as PersonCreateParamsScriptAddresses,
        PersonCreateParamsScriptAddressesKana as PersonCreateParamsScriptAddressesKana,
        PersonCreateParamsScriptAddressesKanji as PersonCreateParamsScriptAddressesKanji,
        PersonCreateParamsScriptNames as PersonCreateParamsScriptNames,
        PersonCreateParamsScriptNamesKana as PersonCreateParamsScriptNamesKana,
        PersonCreateParamsScriptNamesKanji as PersonCreateParamsScriptNamesKanji,
    )
    from stripe.params.v2.core.accounts._person_delete_params import (
        PersonDeleteParams as PersonDeleteParams,
    )
    from stripe.params.v2.core.accounts._person_list_params import (
        PersonListParams as PersonListParams,
    )
    from stripe.params.v2.core.accounts._person_retrieve_params import (
        PersonRetrieveParams as PersonRetrieveParams,
    )
    from stripe.params.v2.core.accounts._person_update_params import (
        PersonUpdateParams as PersonUpdateParams,
        PersonUpdateParamsAdditionalAddress as PersonUpdateParamsAdditionalAddress,
        PersonUpdateParamsAdditionalName as PersonUpdateParamsAdditionalName,
        PersonUpdateParamsAdditionalTermsOfService as PersonUpdateParamsAdditionalTermsOfService,
        PersonUpdateParamsAdditionalTermsOfServiceAccount as PersonUpdateParamsAdditionalTermsOfServiceAccount,
        PersonUpdateParamsAddress as PersonUpdateParamsAddress,
        PersonUpdateParamsDateOfBirth as PersonUpdateParamsDateOfBirth,
        PersonUpdateParamsDocuments as PersonUpdateParamsDocuments,
        PersonUpdateParamsDocumentsCompanyAuthorization as PersonUpdateParamsDocumentsCompanyAuthorization,
        PersonUpdateParamsDocumentsPassport as PersonUpdateParamsDocumentsPassport,
        PersonUpdateParamsDocumentsPrimaryVerification as PersonUpdateParamsDocumentsPrimaryVerification,
        PersonUpdateParamsDocumentsPrimaryVerificationFrontBack as PersonUpdateParamsDocumentsPrimaryVerificationFrontBack,
        PersonUpdateParamsDocumentsSecondaryVerification as PersonUpdateParamsDocumentsSecondaryVerification,
        PersonUpdateParamsDocumentsSecondaryVerificationFrontBack as PersonUpdateParamsDocumentsSecondaryVerificationFrontBack,
        PersonUpdateParamsDocumentsVisa as PersonUpdateParamsDocumentsVisa,
        PersonUpdateParamsIdNumber as PersonUpdateParamsIdNumber,
        PersonUpdateParamsRelationship as PersonUpdateParamsRelationship,
        PersonUpdateParamsScriptAddresses as PersonUpdateParamsScriptAddresses,
        PersonUpdateParamsScriptAddressesKana as PersonUpdateParamsScriptAddressesKana,
        PersonUpdateParamsScriptAddressesKanji as PersonUpdateParamsScriptAddressesKanji,
        PersonUpdateParamsScriptNames as PersonUpdateParamsScriptNames,
        PersonUpdateParamsScriptNamesKana as PersonUpdateParamsScriptNamesKana,
        PersonUpdateParamsScriptNamesKanji as PersonUpdateParamsScriptNamesKanji,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "PersonCreateParams": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsAdditionalAddress": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsAdditionalName": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsAdditionalTermsOfService": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsAdditionalTermsOfServiceAccount": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsAddress": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsDateOfBirth": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsDocuments": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsDocumentsCompanyAuthorization": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsDocumentsPassport": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsDocumentsPrimaryVerification": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsDocumentsPrimaryVerificationFrontBack": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsDocumentsSecondaryVerification": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsDocumentsSecondaryVerificationFrontBack": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsDocumentsVisa": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsIdNumber": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsRelationship": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsScriptAddresses": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsScriptAddressesKana": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsScriptAddressesKanji": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsScriptNames": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsScriptNamesKana": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonCreateParamsScriptNamesKanji": (
        "stripe.params.v2.core.accounts._person_create_params",
        False,
    ),
    "PersonDeleteParams": (
        "stripe.params.v2.core.accounts._person_delete_params",
        False,
    ),
    "PersonListParams": (
        "stripe.params.v2.core.accounts._person_list_params",
        False,
    ),
    "PersonRetrieveParams": (
        "stripe.params.v2.core.accounts._person_retrieve_params",
        False,
    ),
    "PersonUpdateParams": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsAdditionalAddress": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsAdditionalName": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsAdditionalTermsOfService": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsAdditionalTermsOfServiceAccount": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsAddress": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsDateOfBirth": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsDocuments": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsDocumentsCompanyAuthorization": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsDocumentsPassport": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsDocumentsPrimaryVerification": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsDocumentsPrimaryVerificationFrontBack": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsDocumentsSecondaryVerification": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsDocumentsSecondaryVerificationFrontBack": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsDocumentsVisa": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsIdNumber": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsRelationship": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsScriptAddresses": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsScriptAddressesKana": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsScriptAddressesKanji": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsScriptNames": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsScriptNamesKana": (
        "stripe.params.v2.core.accounts._person_update_params",
        False,
    ),
    "PersonUpdateParamsScriptNamesKanji": (
        "stripe.params.v2.core.accounts._person_update_params",
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
