from typing import Optional
from typing_extensions import TYPE_CHECKING
from stripe._util import merge_dicts
from stripe._stripe_object import StripeObject
from stripe._api_mode import ApiMode

if TYPE_CHECKING:
    # errorImports: The beginning of the section generated from our OpenAPI spec
    from stripe._payment_intent import PaymentIntent
    from stripe._payment_method import PaymentMethod
    from stripe._setup_intent import SetupIntent
    from stripe._source import Source
    # errorImports: The end of the section generated from our OpenAPI spec


class ErrorObject(StripeObject):
    # errorAnnotations: The beginning of the section generated from our OpenAPI spec
    advice_code: Optional[str]
    """
    For card errors resulting from a card issuer decline, a short string indicating [how to proceed with an error](https://docs.stripe.com/declines#retrying-issuer-declines) if they provide one.
    """
    charge: Optional[str]
    """
    For card errors, the ID of the failed charge.
    """
    code: Optional[str]
    """
    For some errors that could be handled programmatically, a short string indicating the [error code](https://docs.stripe.com/error-codes) reported.
    """
    decline_code: Optional[str]
    """
    For card errors resulting from a card issuer decline, a short string indicating the [card issuer's reason for the decline](https://docs.stripe.com/declines#issuer-declines) if they provide one.
    """
    doc_url: Optional[str]
    """
    A URL to more information about the [error code](https://docs.stripe.com/error-codes) reported.
    """
    message: Optional[str]
    """
    A human-readable message providing more details about the error. For card errors, these messages can be shown to your users.
    """
    network_advice_code: Optional[str]
    """
    For card errors resulting from a card issuer decline, a 2 digit code which indicates the advice given to merchant by the card network on how to proceed with an error.
    """
    network_decline_code: Optional[str]
    """
    For payments declined by the network, an alphanumeric code which indicates the reason the payment failed.
    """
    param: Optional[str]
    """
    If the error is parameter-specific, the parameter related to the error. For example, you can use this to display a message near the correct form field.
    """
    payment_intent: Optional["PaymentIntent"]
    """
    The PaymentIntent object for errors returned on a request involving a PaymentIntent.
    """
    payment_method: Optional["PaymentMethod"]
    """
    The PaymentMethod object for errors returned on a request involving a PaymentMethod.
    """
    payment_method_type: Optional[str]
    """
    If the error is specific to the type of payment method, the payment method type that had a problem. This field is only populated for invoice-related errors.
    """
    request_log_url: Optional[str]
    """
    A URL to the request log entry in your dashboard.
    """
    setup_intent: Optional["SetupIntent"]
    """
    The SetupIntent object for errors returned on a request involving a SetupIntent.
    """
    source: Optional["Source"]
    """
    The PaymentSource object for errors returned on a request involving a PaymentSource.
    """
    type: str
    """
    The type of error returned. One of `api_error`, `card_error`, `idempotency_error`, or `invalid_request_error`
    """
    user_message: Optional[str]
    """
    The user message associated with the error.
    """
    # errorAnnotations: The end of the section generated from our OpenAPI spec

    def refresh_from(
        self,
        values,
        api_key=None,
        partial=False,
        stripe_version=None,
        stripe_account=None,
        last_response=None,
        *,
        api_mode: ApiMode = "V1",
    ):
        return self._refresh_from(
            values=values,
            partial=partial,
            last_response=last_response,
            requestor=self._requestor._new_requestor_with_options(
                {
                    "api_key": api_key,
                    "stripe_version": stripe_version,
                    "stripe_account": stripe_account,
                }
            ),
            api_mode=api_mode,
        )

    def _refresh_from(
        self,
        *,
        values,
        partial=False,
        last_response=None,
        requestor,
        api_mode: ApiMode,
    ) -> None:
        # Unlike most other API resources, the API will omit attributes in
        # error objects when they have a null value. We manually set default
        # values here to facilitate generic error handling.
        values = merge_dicts(
            {
                # errorDefaults: The beginning of the section generated from our OpenAPI spec
                "advice_code": None,
                "charge": None,
                "code": None,
                "decline_code": None,
                "doc_url": None,
                "message": None,
                "network_advice_code": None,
                "network_decline_code": None,
                "param": None,
                "payment_intent": None,
                "payment_method": None,
                "payment_method_type": None,
                "request_log_url": None,
                "setup_intent": None,
                "source": None,
                "type": None,
                "user_message": None,
                # errorDefaults: The end of the section generated from our OpenAPI spec
            },
            values,
        )
        return super(ErrorObject, self)._refresh_from(
            values=values,
            partial=partial,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )


class OAuthErrorObject(StripeObject):
    def refresh_from(
        self,
        values,
        api_key=None,
        partial=False,
        stripe_version=None,
        stripe_account=None,
        last_response=None,
        *,
        api_mode: ApiMode = "V1",
    ):
        return self._refresh_from(
            values=values,
            partial=partial,
            last_response=last_response,
            requestor=self._requestor._new_requestor_with_options(
                {
                    "api_key": api_key,
                    "stripe_version": stripe_version,
                    "stripe_account": stripe_account,
                }
            ),
            api_mode=api_mode,
        )

    def _refresh_from(
        self,
        *,
        values,
        partial=False,
        last_response=None,
        requestor,
        api_mode: ApiMode,
    ) -> None:
        # Unlike most other API resources, the API will omit attributes in
        # error objects when they have a null value. We manually set default
        # values here to facilitate generic error handling.
        values = merge_dicts(
            {"error": None, "error_description": None}, values
        )
        return super(OAuthErrorObject, self)._refresh_from(
            values=values,
            partial=partial,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
