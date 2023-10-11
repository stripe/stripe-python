# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
import stripe
from stripe import api_requestor, util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, List, Optional
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account


class Form(ListableAPIResource["Form"]):
    """
    Tax forms are legal documents which are delivered to one or more tax authorities for information reporting purposes.

    Related guide: [US tax reporting for Connect platforms](https://stripe.com/docs/connect/tax-reporting)
    """

    OBJECT_NAME = "tax.form"

    class FilingStatus(StripeObject):
        class Jurisdiction(StripeObject):
            country: str
            level: Literal["country", "state"]
            state: Optional[str]

        effective_at: int
        jurisdiction: Jurisdiction
        value: Literal["accepted", "filed", "rejected"]
        _inner_class_types = {"jurisdiction": Jurisdiction}

    class Payee(StripeObject):
        account: Optional[ExpandableField["Account"]]
        type: Literal["account"]

    class Us1099K(StripeObject):
        reporting_year: int

    class Us1099Misc(StripeObject):
        reporting_year: int

    class Us1099Nec(StripeObject):
        reporting_year: int

    corrected_by: Optional[ExpandableField["Form"]]
    created: int
    filing_statuses: List[FilingStatus]
    id: str
    livemode: bool
    object: Literal["tax.form"]
    payee: Payee
    type: Literal["us_1099_k", "us_1099_misc", "us_1099_nec"]
    us_1099_k: Optional[Us1099K]
    us_1099_misc: Optional[Us1099Misc]
    us_1099_nec: Optional[Us1099Nec]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["Form"]:
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
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Form":
        instance = cls(id, api_key, **params)
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
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=stripe.upload_api_base,
            api_version=stripe_version,
            account=stripe_account,
        )
        headers = util.populate_headers(idempotency_key)
        response, _ = requestor.request_stream("get", url, params, headers)
        return response

    @util.class_method_variant("_cls_pdf")
    def pdf(
        self,
        api_key=None,
        api_version=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        version = api_version or stripe_version
        requestor = api_requestor.APIRequestor(
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
