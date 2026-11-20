# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.risk._form_retrieve_params import FormRetrieveParams
    from stripe.params.risk._form_update_params import FormUpdateParams
    from stripe.risk._form import Form


class FormService(StripeService):
    def retrieve(
        self,
        id: str,
        /,
        params: Optional["FormRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Form":
        """
        Retrieves a risk Form by ID.

        Error Codes

        | Code | HTTP status | Description |
        | — | — | — |
        | form_not_found | 400 | No Form matches the supplied ID. |
        """
        return cast(
            "Form",
            self._request(
                "get",
                "/v1/risk/forms/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["FormRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Form":
        """
        Retrieves a risk Form by ID.

        Error Codes

        | Code | HTTP status | Description |
        | — | — | — |
        | form_not_found | 400 | No Form matches the supplied ID. |
        """
        return cast(
            "Form",
            await self._request_async(
                "get",
                "/v1/risk/forms/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        /,
        params: Optional["FormUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Form":
        """
        Updates a risk Form with the connected account's response.

        Error Codes

        | Code | HTTP status | Description |
        | — | — | — |
        | form_not_found | 400 | No Form matches the supplied ID. |
        | form_closed | 400 | The Form is closed and cannot accept updates. |
        | invalid_field_for_form_type | 400 | Submitted fields contain invalid values. |
        | form_field_already_submitted | 400 | A submitted field has already been submitted. |
        | form_insufficient_fields | 400 | Required fields are missing for this Form type. |
        | resource_missing | 404 | A submitted file does not exist or is not accessible to the requesting account. |

        Validation errors include a summary in message. Missing required properties use
        form_insufficient_fields and include missing_fields, an array of public dotted paths.
        Missing required properties take precedence over value violations.

        Invalid values use invalid_field_for_form_type and include violations. Each violation
        has a public dotted field path and a reason of missing_value or invalid_value.
        Reviewed-field violations include a corrective message; corrective messages for other
        Form types are omitted. For an array member, target identifies the member's field path.
        For a scalar value, target is explicitly null.

        For example, a reviewed-fields submission with an out-of-date timestamp and an omitted
        requested member returns both violations:

        json
        {
         "error": {
         "type": "invalid_request_error",
         "code": "invalid_field_for_form_type",
         "message": "Submitted fields are invalid for Form type reviewed_fields. See violations for details and corrective actions for these fields: 'reviewed_fields.attestation.attested_at', 'reviewed_fields.attestation.fields'.",
         "violations": [
         {
         "field": "reviewed_fields.attestation.attested_at",
         "reason": "invalid_value",
         "message": "The attestation timestamp is out of date. Review and attest the requested information again, then provide the new attestation timestamp.",
         "target": null
         },
         {
         "field": "reviewed_fields.attestation.fields",
         "reason": "missing_value",
         "message": "'defaults.profile.product_description' is required by subject.fields_to_review but is missing from reviewed_fields.attestation.fields. Review this information, then include its path in the attestation.",
         "target": "defaults.profile.product_description"
         }
         ]
         }
        }


        A v1 request with no extracted field submissions is rejected before the Form is loaded,
        including for reviewed-fields Forms. This early error uses form_insufficient_fields
        and omits missing_fields,
        violations, and param. Partially populated reviewed-fields requests use structured
        missing-property validation.
        """
        return cast(
            "Form",
            self._request(
                "post",
                "/v1/risk/forms/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        /,
        params: Optional["FormUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Form":
        """
        Updates a risk Form with the connected account's response.

        Error Codes

        | Code | HTTP status | Description |
        | — | — | — |
        | form_not_found | 400 | No Form matches the supplied ID. |
        | form_closed | 400 | The Form is closed and cannot accept updates. |
        | invalid_field_for_form_type | 400 | Submitted fields contain invalid values. |
        | form_field_already_submitted | 400 | A submitted field has already been submitted. |
        | form_insufficient_fields | 400 | Required fields are missing for this Form type. |
        | resource_missing | 404 | A submitted file does not exist or is not accessible to the requesting account. |

        Validation errors include a summary in message. Missing required properties use
        form_insufficient_fields and include missing_fields, an array of public dotted paths.
        Missing required properties take precedence over value violations.

        Invalid values use invalid_field_for_form_type and include violations. Each violation
        has a public dotted field path and a reason of missing_value or invalid_value.
        Reviewed-field violations include a corrective message; corrective messages for other
        Form types are omitted. For an array member, target identifies the member's field path.
        For a scalar value, target is explicitly null.

        For example, a reviewed-fields submission with an out-of-date timestamp and an omitted
        requested member returns both violations:

        json
        {
         "error": {
         "type": "invalid_request_error",
         "code": "invalid_field_for_form_type",
         "message": "Submitted fields are invalid for Form type reviewed_fields. See violations for details and corrective actions for these fields: 'reviewed_fields.attestation.attested_at', 'reviewed_fields.attestation.fields'.",
         "violations": [
         {
         "field": "reviewed_fields.attestation.attested_at",
         "reason": "invalid_value",
         "message": "The attestation timestamp is out of date. Review and attest the requested information again, then provide the new attestation timestamp.",
         "target": null
         },
         {
         "field": "reviewed_fields.attestation.fields",
         "reason": "missing_value",
         "message": "'defaults.profile.product_description' is required by subject.fields_to_review but is missing from reviewed_fields.attestation.fields. Review this information, then include its path in the attestation.",
         "target": "defaults.profile.product_description"
         }
         ]
         }
        }


        A v1 request with no extracted field submissions is rejected before the Form is loaded,
        including for reviewed-fields Forms. This early error uses form_insufficient_fields
        and omits missing_fields,
        violations, and param. Partially populated reviewed-fields requests use structured
        missing-property validation.
        """
        return cast(
            "Form",
            await self._request_async(
                "post",
                "/v1/risk/forms/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
