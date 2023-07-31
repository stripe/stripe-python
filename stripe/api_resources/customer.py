# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import APIResourceTestHelpers
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import SearchableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods(
    "balance_transaction",
    operations=["create", "retrieve", "update", "list"],
)
@nested_resource_class_methods(
    "cash_balance_transaction",
    operations=["retrieve", "list"],
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
    """
    This object represents a customer of your business. It lets you create recurring charges and track payments that belong to the same customer.

    Related guide: [Save a card during payment](https://stripe.com/docs/payments/save-during-payment)
    """

    OBJECT_NAME = "customer"

    @classmethod
    def _cls_create_funding_instructions(
        cls,
        customer,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/customers/{customer}/funding_instructions".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_create_funding_instructions")
    def create_funding_instructions(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/customers/{customer}/funding_instructions".format(
                customer=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_delete_discount(
        cls,
        customer,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "delete",
            "/v1/customers/{customer}/discount".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_delete_discount")
    def delete_discount(self, idempotency_key=None, **params):
        return self._request(
            "delete",
            "/v1/customers/{customer}/discount".format(
                customer=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_list_payment_methods(
        cls,
        customer,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/payment_methods".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_payment_methods")
    def list_payment_methods(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/customers/{customer}/payment_methods".format(
                customer=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

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
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/payment_methods/{payment_method}".format(
                customer=util.sanitize_id(customer),
                payment_method=util.sanitize_id(payment_method),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_retrieve_payment_method")
    def retrieve_payment_method(
        self, payment_method, idempotency_key=None, **params
    ):
        return self._request(
            "get",
            "/v1/customers/{customer}/payment_methods/{payment_method}".format(
                customer=util.sanitize_id(self.get("id")),
                payment_method=util.sanitize_id(payment_method),
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def search(cls, *args, **kwargs):
        return cls._search(search_url="/v1/customers/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()

    @classmethod
    def retrieve_cash_balance(
        cls,
        customer,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/cash_balance".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def modify_cash_balance(
        cls,
        customer,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/customers/{customer}/cash_balance".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

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
            return cls._static_request(
                "post",
                "/v1/test_helpers/customers/{customer}/fund_cash_balance".format(
                    customer=util.sanitize_id(customer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_fund_cash_balance")
        def fund_cash_balance(self, idempotency_key=None, **params):
            return self.resource._request(
                "post",
                "/v1/test_helpers/customers/{customer}/fund_cash_balance".format(
                    customer=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)


Customer.TestHelpers._resource_cls = Customer
