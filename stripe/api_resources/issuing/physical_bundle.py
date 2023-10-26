# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING


class PhysicalBundle(ListableAPIResource["PhysicalBundle"]):
    """
    A Physical Bundle represents the bundle of physical items - card stock, carrier letter, and envelope - that is shipped to a cardholder when you create a physical card.
    """

    OBJECT_NAME: ClassVar[
        Literal["issuing.physical_bundle"]
    ] = "issuing.physical_bundle"

    class Features(StripeObject):
        card_logo: Literal["optional", "required", "unsupported"]
        """
        The policy for how to use card logo images in a card design with this physical bundle.
        """
        carrier_text: Literal["optional", "required", "unsupported"]
        """
        The policy for how to use carrier letter text in a card design with this physical bundle.
        """

    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            status: NotRequired["Literal['active', 'inactive', 'review']|None"]
            """
            Only return physical bundles with the given status.
            """
            type: NotRequired["Literal['custom', 'standard']|None"]
            """
            Only return physical bundles with the given type.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    features: Optional[Features]
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    name: str
    """
    Friendly display name.
    """
    object: Literal["issuing.physical_bundle"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: Literal["active", "inactive", "review"]
    """
    Whether this physical bundle can be used to create cards.
    """
    type: Literal["custom", "standard"]
    """
    Whether this physical bundle is a standard Stripe offering or custom-made for you.
    """

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PhysicalBundle.ListParams"]
    ) -> ListObject["PhysicalBundle"]:
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
                % (type(result).__name__)
            )

        return result

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PhysicalBundle.RetrieveParams"]
    ) -> "PhysicalBundle":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {"features": Features}
