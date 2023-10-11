from stripe.api_resources.abstract.api_resource import APIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import TypeVar

T = TypeVar("T", bound=StripeObject)


class ListableAPIResource(APIResource[T]):
    @classmethod
    def auto_paging_iter(cls, *args, **params):
        return cls.list(*args, **params).auto_paging_iter()

    @classmethod
    def list(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ) -> ListObject[T]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__,)
            )

        return result
