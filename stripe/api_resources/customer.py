# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import SearchableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method
from stripe.api_resources.abstract import nested_resource_class_methods


@custom_method("delete_discount", http_verb="delete", http_path="discount")
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
        url = self.instance_url() + "/funding_instructions"
        headers = util.populate_headers(idempotency_key)
        resp = self.request("post", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        return stripe_object

    def list_payment_methods(self, idempotency_key=None, **params):
        url = self.instance_url() + "/payment_methods"
        headers = util.populate_headers(idempotency_key)
        resp = self.request("get", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        stripe_object._retrieve_params = params
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
