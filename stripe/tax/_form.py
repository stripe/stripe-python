# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
import stripe
from stripe import _util
from stripe._api_requestor import APIRequestor
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from typing import Any, ClassVar, List, Optional, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe._account import Account


class Form(ListableAPIResource["Form"]):
    """
    Tax forms are legal documents which are delivered to one or more tax authorities for information reporting purposes.

    Related guide: [US tax reporting for Connect platforms](https://stripe.com/docs/connect/tax-reporting)
    """

    OBJECT_NAME: ClassVar[Literal["tax.form"]] = "tax.form"

    class FilingStatus(StripeObject):
        class Jurisdiction(StripeObject):
            country: str
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)). Always `US`.
            """
            level: Literal["country", "state"]
            """
            Indicates the level of the jurisdiction where the form was filed.
            """
            state: Optional[str]
            """
            [ISO 3166-2 U.S. state code](https://en.wikipedia.org/wiki/ISO_3166-2:US), without country prefix, if any. For example, "NY" for New York, United States.
            """

        effective_at: int
        """
        Time when the filing status was updated.
        """
        jurisdiction: Jurisdiction
        value: Literal["accepted", "filed", "rejected"]
        """
        The current status of the filed form.
        """
        _inner_class_types = {"jurisdiction": Jurisdiction}

    class Payee(StripeObject):
        account: Optional[ExpandableField["Account"]]
        """
        The ID of the payee's Stripe account.
        """
        type: Literal["account"]
        """
        Always `account`.
        """

    class Us1099K(StripeObject):
        reporting_year: int
        """
        Year represented by the information reported on the tax form.
        """

    class Us1099Misc(StripeObject):
        reporting_year: int
        """
        Year represented by the information reported on the tax form.
        """

    class Us1099Nec(StripeObject):
        reporting_year: int
        """
        Year represented by the information reported on the tax form.
        """

    class ListParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        payee: "Form.ListParamsPayee"
        """
        The payee whose volume is represented on the tax form.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        type: NotRequired[
            "Literal['us_1099_k', 'us_1099_misc', 'us_1099_nec']"
        ]
        """
        An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future tax form types. If your integration expects only one type of tax form in the response, make sure to provide a type value in the request.
        """

    class ListParamsPayee(TypedDict):
        account: NotRequired["str"]
        """
        The ID of the Stripe account whose forms will be retrieved.
        """
        type: NotRequired["Literal['account']"]
        """
        Specifies the payee type. Always `account`.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    corrected_by: Optional[ExpandableField["Form"]]
    """
    The form that corrects this form, if any.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    filing_statuses: List[FilingStatus]
    """
    A list of tax filing statuses. Note that a filing status will only be included if the form has been filed directly with the jurisdiction's tax authority.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["tax.form"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payee: Payee
    type: Literal["us_1099_k", "us_1099_misc", "us_1099_nec"]
    """
    The type of the tax form. An additional hash is included on the tax form with a name matching this value. It contains additional information specific to the tax form type.
    """
    us_1099_k: Optional[Us1099K]
    us_1099_misc: Optional[Us1099Misc]
    us_1099_nec: Optional[Us1099Nec]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "Form.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["Form"]:
        """
        Returns a list of tax forms which were previously created. The tax forms are returned in sorted order, with the oldest tax forms appearing first.
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
        cls, id: str, **params: Unpack["Form.RetrieveParams"]
    ) -> "Form":
        """
        Retrieves the details of a tax form that has previously been created. Supply the unique tax form ID that was returned from your previous request, and Stripe will return the corresponding tax form information.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_pdf(
        cls,
        sid,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        url = "%s/%s/%s" % (
            cls.class_url(),
            quote_plus(sid),
            "pdf",
        )
        requestor = APIRequestor(
            api_key,
            api_base=stripe.upload_api_base,
            api_version=stripe_version,
            account=stripe_account,
        )
        headers = _util.populate_headers(idempotency_key)
        response, _ = requestor.request_stream("get", url, params, headers)
        return response

    @overload
    @staticmethod
    def pdf(
        sid: str,
        api_key: Optional[str] = None,
        idempotency_key=None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        ...

    @overload
    def pdf(
        self,
        api_key: Optional[str] = None,
        api_version: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        ...

    @_util.class_method_variant("_cls_pdf")
    def pdf(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        api_key: Optional[str] = None,
        api_version: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        version = api_version or stripe_version
        requestor = APIRequestor(
            api_key,
            api_base=stripe.upload_api_base,
            api_version=version,
            account=stripe_account,
        )
        url = self.instance_url() + "/pdf"
        return requestor.request_stream("get", url, params=params)

    _inner_class_types = {
        "filing_statuses": FilingStatus,
        "payee": Payee,
        "us_1099_k": Us1099K,
        "us_1099_misc": Us1099Misc,
        "us_1099_nec": Us1099Nec,
    }
