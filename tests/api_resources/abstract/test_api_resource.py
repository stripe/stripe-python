import pytest

import stripe


class TestAPIResource(object):
    class MyResource(stripe.api_resources.abstract.APIResource):
        OBJECT_NAME = "myresource"

    def test_retrieve_and_refresh(self, http_client_mock):
        path = "/v1/myresources/foo%2A"
        query_string = "myparam=5"
        http_client_mock.stub_request(
            "get",
            path,
            query_string,
            '{"id": "foo2", "bobble": "scrobble"}',
            rheaders={"request-id": "req_id"},
        )

        res = self.MyResource.retrieve("foo*", myparam=5)

        http_client_mock.assert_requested(
            "get", path=path, query_string=query_string
        )
        assert res.bobble == "scrobble"
        assert res.id == "foo2"
        assert res.api_key == "sk_test_123"

        assert res.last_response is not None
        assert res.last_response.request_id == "req_id"

        path = "/v1/myresources/foo2"
        query_string = "myparam=5"
        http_client_mock.stub_request(
            "get", path, query_string, '{"frobble": 5}'
        )

        res = res.refresh()

        http_client_mock.assert_requested(
            "get", path=path, query_string=query_string
        )
        assert res.frobble == 5
        with pytest.raises(KeyError):
            res["bobble"]

    def test_request_with_special_fields_prefers_explicit(self, http_client_mock):
        path = "/v1/myresources/foo"
        http_client_mock.stub_request(
            "get",
            path=path,
            query_string="bobble=scrobble",
            rbody='{"id": "foo2", "bobble": "scrobble"}',
        )

        self.MyResource._static_request(
            "get",
            "/v1/myresources/foo",
            idempotency_key="explicit",
            params={"idempotency_key": "params", "bobble": "scrobble"},
        )

        http_client_mock.assert_requested(
            "get", path=path, query_string="bobble=scrobble", idempotency_key="explicit"
        )

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
