import pytest

import stripe


class TestAPIResource(object):
    class MyResource(stripe.APIResource):
        OBJECT_NAME = "myresource"

    class MyDeletableResource(stripe.DeletableAPIResource):
        OBJECT_NAME = "myresource"

        @classmethod
        def my_method(cls, **params):
            return cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            )

        @classmethod
        async def my_method_async(cls, **params):
            return cls.construct_from(
                await cls._static_request_async(
                    "post",
                    cls.class_url(),
                    params=params,
                ),
                stripe.api_key,
            )

    def test_retrieve_and_refresh(self, http_client_mock):
        path = "/v1/myresources/foo%2A"
        query_string = "myparam=5"
        key = "sk_test_123"
        stripe_version = "2018-02-28"
        stripe_account = "acct_foo"
        http_client_mock.stub_request(
            "get",
            path,
            query_string,
            '{"id": "foo2", "bobble": "scrobble"}',
            rheaders={"request-id": "req_id"},
        )

        res = self.MyResource.retrieve(
            "foo*",
            myparam=5,
            stripe_version="2018-02-28",
            stripe_account="acct_foo",
        )

        http_client_mock.assert_requested(
            "get",
            path=path,
            query_string=query_string,
            api_key=key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
        )
        assert res.bobble == "scrobble"
        assert res.id == "foo2"
        assert res.api_key == key
        assert res.stripe_version == stripe_version
        assert res.stripe_account == stripe_account

        assert res.last_response is not None
        assert res.last_response.request_id == "req_id"

        path = "/v1/myresources/foo2"
        query_string = "myparam=5"
        http_client_mock.stub_request(
            "get", path, query_string, '{"frobble": 5}'
        )

        res = res.refresh()

        http_client_mock.assert_requested(
            "get",
            path=path,
            query_string=query_string,
            api_key=key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
        )
        assert res.frobble == 5
        with pytest.raises(KeyError):
            res["bobble"]

    def test_convert_to_stripe_object(self):
        sample = {
            "foo": "bar",
            "adict": {"object": "charge", "id": 42, "amount": 7},
            "alist": [{"object": "customer", "name": "chilango"}],
        }

        converted = stripe.util.convert_to_stripe_object(
            sample, "akey", None, None
        )

        # Types
        assert isinstance(converted, stripe.stripe_object.StripeObject)
        assert isinstance(converted.adict, stripe.Charge)
        assert len(converted.alist) == 1
        assert isinstance(converted.alist[0], stripe.Customer)

        # Values
        assert converted.foo == "bar"
        assert converted.adict.id == 42
        assert converted.alist[0].name == "chilango"

        # Stripping
        # TODO: We should probably be stripping out this property
        # self.assertRaises(AttributeError, getattr, converted.adict, 'object')

    def test_raise_on_incorrect_id_type(self):
        for obj in [None, 1, 3.14, dict(), list(), set(), tuple(), object()]:
            with pytest.raises(stripe.error.InvalidRequestError):
                self.MyResource.retrieve(obj)

    def test_class_methods_use_global_options(self, http_client_mock):
        key = "newkey"
        stripe_version = "2023-01-01"
        stripe_account = "acct_foo"

        resource = self.MyDeletableResource.construct_from(
            {"id": "foo"},
            key=key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
        )

        http_client_mock.stub_request(
            "get",
            "/v1/myresources/foo",
            rbody='{"id": "foo"}',
        )

        resource.retrieve("foo")

        http_client_mock.assert_requested(
            "get",
            path="/v1/myresources/foo",
            api_key=stripe.api_key,
            stripe_version=stripe.api_version,
            extra_headers={"Stripe-Account": None},
        )

        http_client_mock.stub_request(
            "post",
            "/v1/myresources",
            rbody='{"id": "foo", "object": "myresource"}',
        )

        self.MyDeletableResource.my_method()

        http_client_mock.assert_requested(
            "post",
            path="/v1/myresources",
            api_key=stripe.api_key,
            stripe_version=stripe.api_version,
            extra_headers={"Stripe-Account": None},
        )

    def test_class_method_prefers_method_arguments(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            "/v1/myresources/foo",
            rbody='{"id": "foo"}',
        )

        resource = self.MyResource.construct_from(
            {"id": "foo"},
            key="oldkey",
            stripe_version="2000-01-01",
            stripe_account="acct_foo",
        )

        resource.retrieve(
            "foo",
            api_key="newkey",
            stripe_version="2023-01-01",
            stripe_account="acct_bar",
        )

        http_client_mock.assert_requested(
            "get",
            path="/v1/myresources/foo",
            api_key="newkey",
            stripe_version="2023-01-01",
            stripe_account="acct_bar",
        )

    def test_retrieve_forwards_options(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            "/v1/myresources/foo",
            rbody='{"id": "foo"}',
        )

        res = self.MyDeletableResource.retrieve(
            "foo",
            api_key="newkey",
            stripe_version="2023-01-01",
            stripe_account="foo",
        )

        http_client_mock.assert_requested(
            "get",
            path="/v1/myresources/foo",
            api_key="newkey",
            stripe_version="2023-01-01",
            stripe_account="foo",
        )

        http_client_mock.stub_request(
            "delete",
            "/v1/myresources/foo",
        )

        res.delete()

        http_client_mock.assert_requested(
            "delete",
            path="/v1/myresources/foo",
            api_key="newkey",
            stripe_version="2023-01-01",
            stripe_account="foo",
        )

    def test_class_method_forwards_options(self, http_client_mock):
        from stripe._object_classes import OBJECT_CLASSES

        OBJECT_CLASSES["myresource"] = self.MyDeletableResource

        http_client_mock.stub_request(
            "post",
            "/v1/myresources",
            rbody='{"id": "foo", "object": "myresource"}',
        )

        res = self.MyDeletableResource.my_method(
            api_key="newkey", stripe_version="2023-01-01", stripe_account="foo"
        )

        http_client_mock.assert_requested(
            "post",
            path="/v1/myresources",
            api_key="newkey",
            stripe_version="2023-01-01",
            stripe_account="foo",
        )

        http_client_mock.stub_request(
            "delete",
            "/v1/myresources/foo",
        )

        res.delete()

        http_client_mock.assert_requested(
            "delete",
            path="/v1/myresources/foo",
            api_key="newkey",
            stripe_version="2023-01-01",
            stripe_account="foo",
        )

        del OBJECT_CLASSES["myresource"]

    def test_instance_method_forwards_options(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            "/v1/myresources/foo",
            rbody='{"id": "foo"}',
        )

        key = "newkey"
        stripe_version = "2023-01-01"
        stripe_account = "acct_foo"

        resource = self.MyResource.construct_from(
            {"id": "foo"},
            key=key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
        )

        resource.refresh()

        http_client_mock.assert_requested(
            "get",
            path="/v1/myresources/foo",
            api_key=key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
        )

    def test_instance_method_prefers_method_arguments(self, http_client_mock):
        class MyDeletableResource(stripe.DeletableAPIResource):
            OBJECT_NAME = "mydeletableresource"

        http_client_mock.stub_request(
            "delete",
            "/v1/mydeletableresources/foo",
            rbody='{"id": "foo"}',
        )

        resource = MyDeletableResource.construct_from(
            {"id": "foo"},
            key="oldkey",
            stripe_version="2000-01-01",
            stripe_account="acct_foo",
        )

        resource.delete(
            api_key="newkey",
            stripe_version="2023-01-01",
            stripe_account="acct_bar",
        )

        http_client_mock.assert_requested(
            "delete",
            path="/v1/mydeletableresources/foo",
            api_key="newkey",
            stripe_version="2023-01-01",
            stripe_account="acct_bar",
        )

    @pytest.mark.anyio
    async def test_async_methods_succeed(self, http_client_mock_async):
        http_client_mock_async.stub_request(
            "post",
            "/v1/myresources",
            rbody='{"id": "foo", "object": "myresource"}',
        )
        resource = await self.MyDeletableResource.my_method_async()
        http_client_mock_async.assert_requested(
            "post",
            path="/v1/myresources",
        )

        http_client_mock_async.stub_request(
            "get",
            "/v1/myresources/foo",
            rbody='{"id": "foo", "object": "myresource"}',
        )
        await resource.refresh_async()
        http_client_mock_async.assert_requested(
            "get",
            path="/v1/myresources/foo",
        )
