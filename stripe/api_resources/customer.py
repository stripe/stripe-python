# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    APIResourceTestHelpers,
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal, Type
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.cash_balance import CashBalance
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.tax_id import TaxId
    from stripe.api_resources.test_helpers.test_clock import TestClock


@nested_resource_class_methods("balance_transaction")
@nested_resource_class_methods("cash_balance_transaction")
@nested_resource_class_methods("source")
@nested_resource_class_methods("tax_id")
class Customer(
    CreateableAPIResource["Customer"],
    DeletableAPIResource["Customer"],
    ListableAPIResource["Customer"],
    SearchableAPIResource["Customer"],
    UpdateableAPIResource["Customer"],
):
    """
    This object represents a customer of your business. Use it to create recurring charges and track payments that belong to the same customer.

    Related guide: [Save a card during payment](https://stripe.com/docs/payments/save-during-payment)
    """

    OBJECT_NAME = "customer"
    address: Optional[StripeObject]
    balance: Optional[int]
    cash_balance: Optional["CashBalance"]
    created: int
    currency: Optional[str]
    default_source: Optional[ExpandableField[Any]]
    delinquent: Optional[bool]
    description: Optional[str]
    discount: Optional["Discount"]
    email: Optional[str]
    id: str
    invoice_credit_balance: Optional[Dict[str, int]]
    invoice_prefix: Optional[str]
    invoice_settings: Optional[StripeObject]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    name: Optional[str]
    next_invoice_sequence: Optional[int]
    object: Literal["customer"]
    phone: Optional[str]
    preferred_locales: Optional[List[str]]
    shipping: Optional[StripeObject]
    sources: Optional[ListObject[Any]]
    subscriptions: Optional[ListObject["Subscription"]]
    tax: Optional[StripeObject]
    tax_exempt: Optional[Literal["exempt", "none", "reverse"]]
    tax_ids: Optional[ListObject["TaxId"]]
    test_clock: Optional[ExpandableField["TestClock"]]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Customer":
        return cast(
            "Customer",
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

    @classmethod
    def _cls_create_funding_instructions(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def create_funding_instructions(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/customers/{customer}/funding_instructions".format(
                customer=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_delete(cls, sid: str, **params: Any) -> "Customer":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Customer",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Any) -> "Customer":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def _cls_delete_discount(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def delete_discount(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "delete",
            "/v1/customers/{customer}/discount".format(
                customer=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["Customer"]:
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
    def _cls_list_payment_methods(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def list_payment_methods(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "get",
            "/v1/customers/{customer}/payment_methods".format(
                customer=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def modify(cls, id, **params: Any) -> "Customer":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Customer",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Customer":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_retrieve_payment_method(
        cls,
        customer: str,
        payment_method: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
        self,
        payment_method: str,
        idempotency_key: Optional[str] = None,
        **params: Any
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
    def search(cls, *args, **kwargs) -> Any:
        return cls._search(search_url="/v1/customers/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs) -> Any:
        return cls.search(*args, **kwargs).auto_paging_iter()

    @classmethod
    def create_balance_transaction(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/customers/{customer}/balance_transactions".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_balance_transaction(
        cls,
        customer: str,
        transaction: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/balance_transactions/{transaction}".format(
                customer=util.sanitize_id(customer),
                transaction=util.sanitize_id(transaction),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def modify_balance_transaction(
        cls,
        customer: str,
        transaction: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/customers/{customer}/balance_transactions/{transaction}".format(
                customer=util.sanitize_id(customer),
                transaction=util.sanitize_id(transaction),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_balance_transactions(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/balance_transactions".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_cash_balance_transaction(
        cls,
        customer: str,
        transaction: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/cash_balance_transactions/{transaction}".format(
                customer=util.sanitize_id(customer),
                transaction=util.sanitize_id(transaction),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_cash_balance_transactions(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/cash_balance_transactions".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def create_source(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/customers/{customer}/sources".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_source(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/sources/{id}".format(
                customer=util.sanitize_id(customer), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def modify_source(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/customers/{customer}/sources/{id}".format(
                customer=util.sanitize_id(customer), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def delete_source(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "delete",
            "/v1/customers/{customer}/sources/{id}".format(
                customer=util.sanitize_id(customer), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_sources(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/sources".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def create_tax_id(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/customers/{customer}/tax_ids".format(
                customer=util.sanitize_id(customer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_tax_id(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/tax_ids/{id}".format(
                customer=util.sanitize_id(customer), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def delete_tax_id(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "delete",
            "/v1/customers/{customer}/tax_ids/{id}".format(
                customer=util.sanitize_id(customer), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_tax_ids(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/customers/{customer}/tax_ids".format(
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
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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

    @classmethod
    def retrieve_cash_balance(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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

    class TestHelpers(APIResourceTestHelpers["Customer"]):
        _resource_cls: Type["Customer"]

        @classmethod
        def _cls_fund_cash_balance(
            cls,
            customer: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
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
        def fund_cash_balance(
            self, idempotency_key: Optional[str] = None, **params: Any
        ):
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
