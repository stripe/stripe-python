import stripe
import json


TEST_RESOURCE_ID = "acct_123"
TEST_CAPABILITY_ID = "acap_123"
TEST_EXTERNALACCOUNT_ID = "ba_123"
TEST_PERSON_ID = "person_123"


class TestAccount(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Account.list()
        http_client_mock.assert_requested("get", path="/v1/accounts")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Account)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Account.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/accounts/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Account)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Account.create(country="US", type="custom")
        http_client_mock.assert_requested("post", path="/v1/accounts")
        assert isinstance(resource, stripe.Account)

    def test_is_saveable(self, http_client_mock):
        account = stripe.Account.retrieve(TEST_RESOURCE_ID)
        account.metadata["key"] = "value"
        resource = account.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Account)
        assert resource is account

    def test_is_saveable_with_individual(self, http_client_mock):
        individual = stripe.Person.construct_from(
            {"id": "person_123", "object": "person", "first_name": "Jenny"},
            stripe.api_key,
        )
        account = stripe.Account.construct_from(
            {"id": "acct_123", "object": "account", "individual": individual},
            stripe.api_key,
        )

        account.individual.first_name = "Jane"

        http_client_mock.stub_request(
            "post",
            path="/v1/accounts/%s" % TEST_RESOURCE_ID,
            rbody=json.dumps(account.to_dict_recursive()),
        )
        resource = account.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/%s" % TEST_RESOURCE_ID,
            post_data="individual[first_name]=Jane",
        )
        assert isinstance(resource, stripe.Account)
        assert resource is account

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Account.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post", path="/v1/accounts/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Account)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.Account.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/accounts/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, http_client_mock):
        resource = stripe.Account.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/accounts/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_retrieve_no_id(self, http_client_mock):
        resource = stripe.Account.retrieve()
        http_client_mock.assert_requested("get", path="/v1/account")
        assert isinstance(resource, stripe.Account)

    def test_can_reject(self, http_client_mock):
        account = stripe.Account.retrieve(TEST_RESOURCE_ID)
        resource = account.reject(reason="fraud")
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/%s/reject" % TEST_RESOURCE_ID,
            post_data="reason=fraud",
        )
        assert isinstance(resource, stripe.Account)
        assert resource is account

    def test_can_reject_classmethod(self, http_client_mock):
        resource = stripe.Account.reject(TEST_RESOURCE_ID, reason="fraud")
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/%s/reject" % TEST_RESOURCE_ID,
            post_data="reason=fraud",
        )
        assert isinstance(resource, stripe.Account)

    def test_is_deauthorizable(self, http_client_mock):
        account = stripe.Account.retrieve(TEST_RESOURCE_ID)
        http_client_mock.stub_request(
            "post",
            path="/oauth/deauthorize",
            rbody='{"stripe_user_id": "%s"}' % account.id,
        )
        account.deauthorize()
        http_client_mock.assert_requested(
            "post",
            path="/oauth/deauthorize",
            post_data="client_id=%s&stripe_user_id=%s"
            % (
                stripe.client_id,
                account.id,
            ),
        )

    def test_can_call_persons(self, http_client_mock):
        account = stripe.Account.retrieve(TEST_RESOURCE_ID)
        resources = account.persons()
        http_client_mock.assert_requested(
            "get", path="/v1/accounts/%s/persons" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Person)


class TestAccountCapabilities(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Account.list_capabilities(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/accounts/%s/capabilities" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Capability)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Account.modify_capability(
            TEST_RESOURCE_ID, TEST_CAPABILITY_ID, requested=True
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/%s/capabilities/%s"
            % (TEST_RESOURCE_ID, TEST_CAPABILITY_ID),
        )
        assert isinstance(resource, stripe.Capability)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Account.retrieve_capability(
            TEST_RESOURCE_ID, TEST_CAPABILITY_ID
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/accounts/%s/capabilities/%s"
            % (TEST_RESOURCE_ID, TEST_CAPABILITY_ID),
        )
        assert isinstance(resource, stripe.Capability)


class TestAccountExternalAccounts(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Account.list_external_accounts(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/accounts/%s/external_accounts" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Account.retrieve_external_account(
            TEST_RESOURCE_ID, TEST_EXTERNALACCOUNT_ID
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/accounts/%s/external_accounts/%s"
            % (TEST_RESOURCE_ID, TEST_EXTERNALACCOUNT_ID),
        )
        assert isinstance(resource, stripe.BankAccount)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Account.create_external_account(
            TEST_RESOURCE_ID, external_account="btok_123"
        )
        http_client_mock.assert_requested(
            "post", path="/v1/accounts/%s/external_accounts" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.BankAccount)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Account.modify_external_account(
            TEST_RESOURCE_ID, TEST_EXTERNALACCOUNT_ID, metadata={"foo": "bar"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/%s/external_accounts/%s"
            % (TEST_RESOURCE_ID, TEST_EXTERNALACCOUNT_ID),
        )
        assert isinstance(resource, stripe.BankAccount)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.Account.delete_external_account(
            TEST_RESOURCE_ID, TEST_EXTERNALACCOUNT_ID
        )
        http_client_mock.assert_requested(
            "delete",
            path="/v1/accounts/%s/external_accounts/%s"
            % (TEST_RESOURCE_ID, TEST_EXTERNALACCOUNT_ID),
        )
        assert resource.deleted is True


class TestAccountLoginLinks(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.Account.create_login_link(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/accounts/%s/login_links" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.LoginLink)


class TestAccountPersons(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.Account.create_person(
            TEST_RESOURCE_ID, dob={"day": 1, "month": 1, "year": 1980}
        )
        http_client_mock.assert_requested(
            "post", path="/v1/accounts/%s/persons" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Person)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.Account.delete_person(
            TEST_RESOURCE_ID, TEST_PERSON_ID
        )
        http_client_mock.assert_requested(
            "delete",
            path="/v1/accounts/%s/persons/%s"
            % (TEST_RESOURCE_ID, TEST_PERSON_ID),
        )
        assert resource.deleted is True

    def test_is_listable(self, http_client_mock):
        resources = stripe.Account.list_persons(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/accounts/%s/persons" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Person)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Account.modify_person(
            TEST_RESOURCE_ID, TEST_PERSON_ID, metadata={"foo": "bar"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/%s/persons/%s"
            % (TEST_RESOURCE_ID, TEST_PERSON_ID),
        )
        assert isinstance(resource, stripe.Person)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Account.retrieve_person(
            TEST_RESOURCE_ID, TEST_PERSON_ID
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/accounts/%s/persons/%s"
            % (TEST_RESOURCE_ID, TEST_PERSON_ID),
        )
        assert isinstance(resource, stripe.Person)
