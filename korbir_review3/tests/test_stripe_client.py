from __future__ import absolute_import, division, print_function
import stripe
import pytest

from stripe.v2._event import Event
from stripe._http_client import new_default_http_client
from stripe.events._v1_billing_meter_error_report_triggered_event import (
    V1BillingMeterErrorReportTriggeredEvent,
)


class TestStripeClient(object):
    def test_constructor_with_posargs(self):
        client = stripe.StripeClient("sk_test_456")
        assert client._requestor.api_key == "sk_test_456"

    def test_v1_customers_retrieve(
        self, stripe_mock_stripe_client, http_client_mock
    ):
        method = "get"
        path = "/v1/customers/cus_xxxxxxxxxxxxx"
        http_client_mock.stub_request(
            method,
            path=path,
            rbody='{"id": "cus_xxxxxxxxxxxxx","object": "customer"}',
            rcode=200,
            rheaders={},
        )
        customer = stripe_mock_stripe_client.customers.retrieve(
            "cus_xxxxxxxxxxxxx"
        )
        http_client_mock.assert_requested(method, path=path)
        assert customer.id is not None

    def test_v2_events_retrieve(self, http_client_mock):
        method = "get"
        path = "/v2/core/events/evt_123"
        http_client_mock.stub_request(
            method,
            path=path,
            rbody='{"id": "evt_123","object": "v2.core.event", "type": "v1.billing.meter.error_report_triggered"}',
            rcode=200,
            rheaders={},
        )
        client = stripe.StripeClient(
            api_key="keyinfo_test_123",
            http_client=http_client_mock.get_mock_http_client(),
        )
        event = client.v2.core.events.retrieve("evt_123")

        http_client_mock.assert_requested(
            method,
            api_base=stripe.DEFAULT_API_BASE,
            path=path,
            api_key="keyinfo_test_123",
        )
        assert event.id is not None
        assert isinstance(event, Event)
        assert isinstance(event, V1BillingMeterErrorReportTriggeredEvent)

    def test_no_api_key(self):
        with pytest.raises(stripe.error.AuthenticationError):
            stripe.StripeClient(None)  # type: ignore

    def test_http_client_and_options_overlap(self):
        with pytest.raises(ValueError):
            stripe.StripeClient(
                api_key="sk_test_123",
                http_client=new_default_http_client(),
                proxy="http://localhost:8080",
            )

        with pytest.raises(ValueError):
            stripe.StripeClient(
                api_key="sk_test_123",
                http_client=new_default_http_client(),
                verify_ssl_certs=False,
            )

    def test_client_level_options(self, http_client_mock):
        method = "get"
        path = "/v1/customers/cus_xxxxxxxxxxxxx"
        http_client_mock.stub_request(
            method,
            path=path,
            rbody='{"id": "cus_xxxxxxxxxxxxx","object": "customer"}',
            rcode=200,
            rheaders={},
        )

        api_base = "https://example.com"
        api_key = "sk_test_456"
        stripe_account = "acct_123"
        stripe_context = "wksp_123"

        stripe_client = stripe.StripeClient(
            api_key=api_key,
            http_client=http_client_mock.get_mock_http_client(),
            base_addresses={"api": api_base},
            stripe_account=stripe_account,
            stripe_context=stripe_context,
        )

        stripe_client.customers.retrieve("cus_xxxxxxxxxxxxx")

        http_client_mock.assert_requested(
            method,
            api_base=api_base,
            path=path,
            api_key=api_key,
            stripe_account=stripe_account,
            stripe_context=stripe_context,
            stripe_version=stripe.api_version,
        )

    def test_uses_default_api_base_if_none_specified(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            "/v1/customers/cus_xxxxxxxxxxxxx",
        )
        stripe.StripeClient(
            api_key="sk_test_123",
            http_client=http_client_mock.get_mock_http_client(),
        ).customers.retrieve("cus_xxxxxxxxxxxxx")

        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            api_key="sk_test_123",
            api_base=stripe.DEFAULT_API_BASE,
        )

    def test_request_level_options(self, http_client_mock):
        method = "get"
        path = "/v1/customers/cus_xxxxxxxxxxxxx"
        http_client_mock.stub_request(
            method,
            path=path,
            rbody='{"id": "cus_xxxxxxxxxxxxx","object": "customer"}',
            rcode=200,
            rheaders={},
        )

        client_api_base = "https://example.com"
        client_api_key = "sk_test_456"
        client_stripe_account = "acct_123"
        client_stripe_context = "wksp_123"

        request_api_key = "sk_test_789"
        request_stripe_account = "acct_456"
        request_stripe_context = "wksp_456"

        stripe_client = stripe.StripeClient(
            api_key=client_api_key,
            http_client=http_client_mock.get_mock_http_client(),
            base_addresses={"api": client_api_base},
            stripe_account=client_stripe_account,
            stripe_context=client_stripe_context,
        )

        stripe_client.customers.retrieve(
            "cus_xxxxxxxxxxxxx",
            options={
                "api_key": request_api_key,
                "stripe_account": request_stripe_account,
                "stripe_context": request_stripe_context,
            },
        )

        http_client_mock.assert_requested(
            method,
            api_base=client_api_base,
            path=path,
            api_key=request_api_key,
            stripe_account=request_stripe_account,
            stripe_context=request_stripe_context,
            stripe_version=stripe.api_version,
        )

    def test_separate_clients_have_separate_options(self, http_client_mock):
        method = "get"
        path = "/v1/customers/cus_xxxxxxxxxxxxx"
        http_client_mock.stub_request(
            method,
            path=path,
            rbody='{"id": "cus_xxxxxxxxxxxxx","object": "customer"}',
            rcode=200,
            rheaders={},
        )

        stripe_client_1 = stripe.StripeClient(
            api_key="sk_test_123",
            base_addresses={"api": "https://example.com"},
            http_client=http_client_mock.get_mock_http_client(),
        )
        stripe_client_2 = stripe.StripeClient(
            api_key="sk_test_456",
            base_addresses={"api": "https://example2.com"},
            http_client=http_client_mock.get_mock_http_client(),
        )

        stripe_client_1.customers.retrieve("cus_xxxxxxxxxxxxx")
        stripe_client_2.customers.retrieve("cus_xxxxxxxxxxxxx")

        http_client_mock.assert_requested(
            method,
            api_base="https://example.com",
            path=path,
            api_key="sk_test_123",
            stripe_version=stripe.api_version,
        )
        http_client_mock.assert_requested(
            method,
            api_base="https://example2.com",
            path=path,
            api_key="sk_test_456",
            stripe_version=stripe.api_version,
        )

    def test_v2_encodes_none_as_null(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/v2/billing/meter_events",
            rbody='{"event_name": "cool", "payload": {}, "identifier": null}',
            rcode=200,
            rheaders={},
        )

        client = stripe.StripeClient(
            api_key="sk_test_123",
            http_client=http_client_mock.get_mock_http_client(),
        )

        client.v2.billing.meter_events.create(
            {"event_name": "cool", "payload": {}, "identifier": None}  # type: ignore - None is not valid for `identifier`
        )

        http_client_mock.assert_requested(
            "post",
            content_type="application/json",
            post_data='{"event_name": "cool", "payload": {}, "identifier": null}',
            is_json=True,
        )

    def test_carries_over_requestor_options_to_resource(
        self, http_client_mock
    ):
        client = stripe.StripeClient(
            api_key="sk_test_123",
            stripe_account="acct_123",
            base_addresses={
                "api": "https://example.com",
            },
            http_client=http_client_mock.get_mock_http_client(),
        )
        http_client_mock.stub_request(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            rbody='{"id": "cus_xxxxxxxxxxxxx","object": "customer"}',
            rcode=200,
            rheaders={},
        )
        cus = client.customers.retrieve("cus_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            api_key="sk_test_123",
            stripe_account="acct_123",
            api_base="https://example.com",
        )

        http_client_mock.stub_request(
            "delete",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            rbody='{"id": "cus_xxxxxxxxxxxxx","object": "customer"}',
            rcode=200,
            rheaders={},
        )
        cus.delete()
        http_client_mock.assert_requested(
            "delete",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            api_key="sk_test_123",
            stripe_account="acct_123",
            api_base="https://example.com",
        )

    def test_user_options_are_not_mutated(self, http_client_mock):
        client = stripe.StripeClient(
            http_client=http_client_mock.get_mock_http_client(),
            api_key="sk_test_abc",
        )

        http_client_mock.stub_request(
            "get",
            path="/v2/core/events",
            query_string="object_id=obj_123",
            rbody='{"data": [{"id": "x"}], "next_page": "page_2"}',
            rcode=200,
            rheaders={},
        )

        my_options: stripe.RequestOptions = {"api_key": "sk_test_xyz"}

        client.v2.core.events.list(
            {"object_id": "obj_123"}, options=my_options
        )

        assert my_options == {"api_key": "sk_test_xyz"}

    def test_carries_over_request_options_to_resource(self, http_client_mock):
        client = stripe.StripeClient(
            api_key="sk_test_123",
            stripe_account="acct_123",
            stripe_version="2019-12-03",
            http_client=http_client_mock.get_mock_http_client(),
        )
        http_client_mock.stub_request(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            rbody='{"id": "cus_xxxxxxxxxxxxx","object": "customer"}',
            rcode=200,
            rheaders={},
        )
        cus = client.customers.retrieve(
            "cus_xxxxxxxxxxxxx",
            {},
            {
                "api_key": "sk_test_456",
                "stripe_version": "2023-12-03",
                "stripe_account": "acct_456",
            },
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            api_key="sk_test_456",
            stripe_account="acct_456",
            stripe_version="2023-12-03",
        )

        http_client_mock.stub_request(
            "delete",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            rbody='{"id": "cus_xxxxxxxxxxxxx","object": "customer"}',
            rcode=200,
            rheaders={},
        )

        cus.delete()
        assert cus._requestor is not client._requestor
        http_client_mock.assert_requested(
            "delete",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            api_key="sk_test_456",
            stripe_account="acct_456",
            stripe_version="2023-12-03",
        )

    def test_respects_max_network_retries_in_request_options(
        self, http_client_mock
    ):
        client = stripe.StripeClient(
            api_key="sk_test_123",
            http_client=http_client_mock.get_mock_http_client(),
        )
        http_client_mock.stub_request(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            rbody='{"id": "cus_xxxxxxxxxxxxx","object": "customer"}',
            rcode=200,
            rheaders={},
        )

        client.customers.retrieve(
            "cus_xxxxxxxxxxxxx",
            {},
            {
                "max_network_retries": 2,
            },
        )

        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            api_key="sk_test_123",
            max_network_retries=2,
        )

    def test_respects_max_network_retries_in_client_options(
        self, http_client_mock
    ):
        client = stripe.StripeClient(
            api_key="sk_test_123",
            http_client=http_client_mock.get_mock_http_client(),
            max_network_retries=2,
        )
        http_client_mock.stub_request(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            rbody='{"id": "cus_xxxxxxxxxxxxx","object": "customer"}',
            rcode=200,
            rheaders={},
        )

        client.customers.retrieve("cus_xxxxxxxxxxxxx")

        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            api_key="sk_test_123",
            max_network_retries=2,
        )

    def test_prefers_max_network_retries_in_request_options(
        self, http_client_mock
    ):
        client = stripe.StripeClient(
            api_key="sk_test_123",
            http_client=http_client_mock.get_mock_http_client(),
            max_network_retries=2,
        )
        http_client_mock.stub_request(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            rbody='{"id": "cus_xxxxxxxxxxxxx","object": "customer"}',
            rcode=200,
            rheaders={},
        )

        client.customers.retrieve(
            "cus_xxxxxxxxxxxxx", options={"max_network_retries": 0}
        )

        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            api_key="sk_test_123",
            max_network_retries=0,
        )

    def test_stripe_client_sends_usage(
        self, stripe_mock_stripe_client, http_client_mock
    ):
        path = "/v1/customers/cus_xxxxxxxxxxxxx"
        http_client_mock.stub_request(
            "get",
            path=path,
            rbody='{"id": "cus_xxxxxxxxxxxxx","object": "customer"}',
            rcode=200,
            rheaders={},
        )

        customer = stripe_mock_stripe_client.customers.retrieve(
            "cus_xxxxxxxxxxxxx"
        )

        http_client_mock.assert_requested(
            "get", path=path, usage=["stripe_client"]
        )

        http_client_mock.stub_request(
            "delete",
            path=path,
            rbody='{"id": "cus_xxxxxxxxxxxxx","object": "customer", "deleted": true}',
            rcode=200,
            rheaders={},
        )

        customer.delete()
        http_client_mock.assert_requested("delete", path=path, usage=None)
