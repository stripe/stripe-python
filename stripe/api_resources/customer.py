# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import APIResourceTestHelpers
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import SearchableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method
from stripe.api_resources.abstract import nested_resource_class_methods
from stripe.api_resources.abstract import test_helpers


@custom_method("delete_discount", http_verb="delete", http_path="discount")
@test_helpers
@custom_method(
    "create_funding_instructions",
    http_verb="post",
    http_path="funding_instructions",
)
@custom_method(
    "list_payment_methods",
    http_verb="get",
    http_path="payment_methods",
)
@nested_resource_class_methods(
    "balance_transaction",
    operations=["create", "retrieve", "update", "list"],
)
@nested_resource_class_methods(
    "source",
    operations=["create", "retrieve", "update", "delete", "list"],
)
@nested_resource_class_methods(
    "tax_id",
    operations=["create", "retrieve", "delete", "list"],
)
class Customer(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
):
    OBJECT_NAME = "customer"

    def create_funding_instructions(self, idempotency_key=None, **params):
        url = "/v1/customers/{customer}/funding_instructions".format(
            customer=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        resp = self.request("post", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        return stripe_object

    def list_payment_methods(self, idempotency_key=None, **params):
        url = "/v1/customers/{customer}/payment_methods".format(
            customer=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        resp = self.request("get", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        stripe_object._retrieve_params = params
        return stripe_object

    @classmethod
    def _cls_retrieve_payment_method(
        cls,
        customer,
        payment_method,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = (
            "/v1/customers/{customer}/payment_methods/{payment_method}".format(
                customer=util.sanitize_id(customer),
                payment_method=util.sanitize_id(payment_method),
            )
        )
        response, api_key = requestor.request("get", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @util.class_method_variant("_cls_retrieve_payment_method")
    def retrieve_payment_method(
        self, payment_method, idempotency_key=None, **params
    ):
        url = (
            "/v1/customers/{customer}/payment_methods/{payment_method}".format(
                customer=util.sanitize_id(self.get("id")),
                payment_method=util.sanitize_id(payment_method),
            )
        )
        headers = util.populate_headers(idempotency_key)
        resp = self.request("get", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        return stripe_object

    @classmethod
    def search(cls, *args, **kwargs):
        return cls._search(search_url="/v1/customers/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()

    def delete_discount(self, **params):
        requestor = api_requestor.APIRequestor(
            self.api_key,
            api_version=self.stripe_version,
            account=self.stripe_account,
        )
        url = self.instance_url() + "/discount"
        _, api_key = requestor.request("delete", url, params)
        self.refresh_from({"discount": None}, api_key, True)

    @classmethod
    def retrieve_cash_balance(
        cls,
        customer,
        nested_id=None,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        # The nested_id parameter is required for backwards compatibility purposes and is ignored.
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/customers/{customer}/cash_balance".format(
            customer=util.sanitize_id(customer)
        )
        response, api_key = requestor.request("get", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    @classmethod
    def modify_cash_balance(
        cls,
        customer,
        nested_id=None,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        # The nested_id parameter is required for backwards compatibility purposes and is ignored.
        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        url = "/v1/customers/{customer}/cash_balance".format(
            customer=util.sanitize_id(customer)
        )
        response, api_key = requestor.request("post", url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object

    class TestHelpers(APIResourceTestHelpers):
        @classmethod
        def _cls_fund_cash_balance(
            cls,
            customer,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            requestor = api_requestor.APIRequestor(
                api_key, api_version=stripe_version, account=stripe_account
            )
            url = "/v1/test_helpers/customers/{customer}/fund_cash_balance".format(
                customer=util.sanitize_id(customer)
            )
            response, api_key = requestor.request("post", url, params)
            stripe_object = util.convert_to_stripe_object(
                response, api_key, stripe_version, stripe_account
            )
            return stripe_object

        @util.class_method_variant("_cls_fund_cash_balance")
        def fund_cash_balance(self, idempotency_key=None, **params):
            url = "/v1/test_helpers/customers/{customer}/fund_cash_balance".format(
                customer=util.sanitize_id(self.get("id"))
            )
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource
