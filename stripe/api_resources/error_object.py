from typing import Optional
from typing_extensions import TYPE_CHECKING
from stripe.util import merge_dicts
from stripe.stripe_object import StripeObject

if TYPE_CHECKING:
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.setup_intent import SetupIntent
    from stripe.api_resources.source import Source
    from stripe.api_resources.payment_method import PaymentMethod


class ErrorObject(StripeObject):
    charge: Optional[str]
    code: int
    decline_code: Optional[str]
    doc_url: Optional[str]
    message: Optional[str]
    param: Optional[str]
    payment_intent: Optional["PaymentIntent"]
    payment_method: Optional["PaymentMethod"]
    setup_intent: Optional["SetupIntent"]
    source: Optional["Source"]
    type: str

    def refresh_from(
        self,
        values,
        api_key=None,
        partial=False,
        stripe_version=None,
        stripe_account=None,
        last_response=None,
    ):
        # Unlike most other API resources, the API will omit attributes in
        # error objects when they have a null value. We manually set default
        # values here to facilitate generic error handling.
        values = merge_dicts(
            {
                "charge": None,
                "code": None,
                "decline_code": None,
                "doc_url": None,
                "message": None,
                "param": None,
                "payment_intent": None,
                "payment_method": None,
                "setup_intent": None,
                "source": None,
                "type": None,
            },
            values,
        )
        return super(ErrorObject, self).refresh_from(
            values,
            api_key,
            partial,
            stripe_version,
            stripe_account,
            last_response,
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
    ):
        # Unlike most other API resources, the API will omit attributes in
        # error objects when they have a null value. We manually set default
        # values here to facilitate generic error handling.
        values = merge_dicts(
            {"error": None, "error_description": None}, values
        )
        return super(OAuthErrorObject, self).refresh_from(
            values,
            api_key,
            partial,
            stripe_version,
            stripe_account,
            last_response,
        )
