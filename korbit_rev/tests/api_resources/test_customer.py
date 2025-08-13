import stripe


TEST_RESOURCE_ID = "cus_123"
TEST_SUB_ID = "sub_123"
TEST_SOURCE_ID = "ba_123"
TEST_TAX_ID_ID = "txi_123"
TEST_TRANSACTION_ID = "cbtxn_123"


class TestCustomer(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Customer.list()
        http_client_mock.assert_requested("get", path="/v1/customers")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Customer)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/customers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Customer)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Customer.create()
        http_client_mock.assert_requested("post", path="/v1/customers")
        assert isinstance(resource, stripe.Customer)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Customer.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Customer)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/customers/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, http_client_mock):
        resource = stripe.Customer.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/customers/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete_discount(self, http_client_mock):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        resource.delete_discount()
        http_client_mock.assert_requested(
            "delete", path="/v1/customers/%s/discount" % TEST_RESOURCE_ID
        )

    def test_can_delete_discount_class_method(self, http_client_mock):
        stripe.Customer.delete_discount(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/customers/%s/discount" % TEST_RESOURCE_ID
        )


class TestCustomerSources(object):
    def test_is_creatable(self, http_client_mock):
        stripe.Customer.create_source(TEST_RESOURCE_ID, source="btok_123")
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/%s/sources" % TEST_RESOURCE_ID,
            post_data="source=btok_123",
        )

    def test_is_retrievable(self, http_client_mock):
        stripe.Customer.retrieve_source(TEST_RESOURCE_ID, TEST_SOURCE_ID)
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/%s/sources/%s"
            % (TEST_RESOURCE_ID, TEST_SOURCE_ID),
        )

    def test_is_modifiable(self, http_client_mock):
        stripe.Customer.modify_source(
            TEST_RESOURCE_ID, TEST_SOURCE_ID, metadata={"foo": "bar"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/%s/sources/%s"
            % (TEST_RESOURCE_ID, TEST_SOURCE_ID),
            post_data="metadata[foo]=bar",
        )

    def test_is_deletable(self, http_client_mock):
        stripe.Customer.delete_source(TEST_RESOURCE_ID, TEST_SOURCE_ID)
        http_client_mock.assert_requested(
            "delete",
            path="/v1/customers/%s/sources/%s"
            % (TEST_RESOURCE_ID, TEST_SOURCE_ID),
        )

    def test_is_listable(self, http_client_mock):
        resources = stripe.Customer.list_sources(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/customers/%s/sources" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)


class TestCustomerTaxIds(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.Customer.create_tax_id(
            TEST_RESOURCE_ID, type="eu_vat", value="11111"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/%s/tax_ids" % TEST_RESOURCE_ID,
            post_data="type=eu_vat&value=11111",
        )
        assert isinstance(resource, stripe.TaxId)

    def test_is_retrievable(self, http_client_mock):
        stripe.Customer.retrieve_tax_id(TEST_RESOURCE_ID, TEST_TAX_ID_ID)
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/%s/tax_ids/%s"
            % (TEST_RESOURCE_ID, TEST_TAX_ID_ID),
        )

    def test_is_deletable(self, http_client_mock):
        stripe.Customer.delete_tax_id(TEST_RESOURCE_ID, TEST_TAX_ID_ID)
        http_client_mock.assert_requested(
            "delete",
            path="/v1/customers/%s/tax_ids/%s"
            % (TEST_RESOURCE_ID, TEST_TAX_ID_ID),
        )

    def test_is_listable(self, http_client_mock):
        resources = stripe.Customer.list_tax_ids(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/customers/%s/tax_ids" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)


class TestCustomerTransactions(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.Customer.create_balance_transaction(
            TEST_RESOURCE_ID, amount=1234, currency="usd"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/%s/balance_transactions" % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, stripe.CustomerBalanceTransaction)

    def test_is_retrievable(self, http_client_mock):
        stripe.Customer.retrieve_balance_transaction(
            TEST_RESOURCE_ID, TEST_TRANSACTION_ID
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/%s/balance_transactions/%s"
            % (TEST_RESOURCE_ID, TEST_TRANSACTION_ID),
        )

    def test_is_listable(self, http_client_mock):
        resources = stripe.Customer.list_balance_transactions(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/%s/balance_transactions" % TEST_RESOURCE_ID,
        )
        assert isinstance(resources.data, list)


class TestCustomerPaymentMethods(object):
    def test_is_listable(self, http_client_mock):
        stripe.Customer.list_payment_methods(TEST_RESOURCE_ID, type="card")
        http_client_mock.assert_requested(
            "get", path="/v1/customers/%s/payment_methods" % TEST_RESOURCE_ID
        )

    def test_is_listable_on_object(self, http_client_mock):
        resource = stripe.Customer.retrieve(
            TEST_RESOURCE_ID
        ).list_payment_methods(type="card")
        http_client_mock.assert_requested(
            "get", path="/v1/customers/%s/payment_methods" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.ListObject)


class TestCustomerCashBalanceMethods(object):
    # These tests are present for compatibility purposes. Previously the cash
    # balance methods required None as a second nested_id parameter. The method
    # has been patched to no longer require this, but we want to preserve
    # compatibility for existing users.
    def test_customer_cashbalance_retrieve_legacy_call_pattern(
        self, http_client_mock
    ):
        stripe.Customer.retrieve_cash_balance("cus_123")
        http_client_mock.assert_requested(
            "get", path="/v1/customers/cus_123/cash_balance"
        )

    def test_customer_cashbalance_modify_legacy_call_pattern(
        self, http_client_mock
    ):
        stripe.Customer.modify_cash_balance(
            "cus_123",
            settings={"reconciliation_mode": "manual"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/cus_123/cash_balance",
            post_data="settings[reconciliation_mode]=manual",
        )

    def test_customer_cashbalance_modify_fixed_pattern(self, http_client_mock):
        stripe.Customer.modify_cash_balance(
            "cus_123",
            settings={"reconciliation_mode": "manual"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/cus_123/cash_balance",
            post_data="settings[reconciliation_mode]=manual",
        )
