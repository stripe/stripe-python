# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING


class CountrySpec(ListableAPIResource["CountrySpec"]):
    """
    Stripe needs to collect certain pieces of information about each account
    created. These requirements can differ depending on the account's country. The
    Country Specs API makes these rules available to your integration.

    You can also view the information from this API call as [an online
    guide](https://stripe.com/docs/connect/required-verification-information).
    """

    OBJECT_NAME: ClassVar[Literal["country_spec"]] = "country_spec"

    class VerificationFields(StripeObject):
        class Company(StripeObject):
            additional: List[str]
            """
            Additional fields which are only required for some users.
            """
            minimum: List[str]
            """
            Fields which every account must eventually provide.
            """

        class Individual(StripeObject):
            additional: List[str]
            """
            Additional fields which are only required for some users.
            """
            minimum: List[str]
            """
            Fields which every account must eventually provide.
            """

        company: Company
        individual: Individual
        _inner_class_types = {"company": Company, "individual": Individual}

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

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    default_currency: str
    """
    The default currency for this country. This applies to both payment methods and bank accounts.
    """
    id: str
    """
    Unique identifier for the object. Represented as the ISO country code for this country.
    """
    object: Literal["country_spec"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    supported_bank_account_currencies: Dict[str, List[str]]
    """
    Currencies that can be accepted in the specific country (for transfers).
    """
    supported_payment_currencies: List[str]
    """
    Currencies that can be accepted in the specified country (for payments).
    """
    supported_payment_methods: List[str]
    """
    Payment methods available in the specified country. You may need to enable some payment methods (e.g., [ACH](https://stripe.com/docs/ach)) on your account before they appear in this list. The `stripe` payment method refers to [charging through your platform](https://stripe.com/docs/connect/destination-charges).
    """
    supported_transfer_countries: List[str]
    """
    Countries that can accept transfers from the specified country.
    """
    verification_fields: VerificationFields

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["CountrySpec.ListParams"]
    ) -> ListObject["CountrySpec"]:
        """
        Lists all Country Spec objects available in the API.
        """
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
        cls, id: str, **params: Unpack["CountrySpec.RetrieveParams"]
    ) -> "CountrySpec":
        """
        Returns a Country Spec for a given Country code.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    _inner_class_types = {"verification_fields": VerificationFields}
