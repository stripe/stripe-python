from stripe.api_resources.abstract.api_resource import APIResource
from typing import TypeVar, cast
from stripe.stripe_object import StripeObject

T = TypeVar("T", bound=StripeObject)


class CreateableAPIResource(APIResource[T]):
    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ) -> T:
        return cast(
            T,
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )
