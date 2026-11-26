import json
import pickle
import stripe
from typing import Any, Callable, Dict, Optional, Union
from typing_extensions import assert_type

import pytest
from stripe.billing._meter import Meter
from tests.http_client_mock import HTTPClientMock


from stripe import DEFAULT_API_BASE
from stripe._error import SignatureVerificationError
from stripe._stripe_client import StripeClient
from stripe.events._v1_billing_meter_error_report_triggered_event import (
    V1BillingMeterErrorReportTriggeredEventNotification,
    V1BillingMeterErrorReportTriggeredEvent,
)
from stripe.events._v1_product_updated_event import (
    V1ProductUpdatedEvent,
    V1ProductUpdatedEventNotification,
)
from stripe.events._v2_core_account_person_updated_event import (
    V2CoreAccountPersonUpdatedEvent,
)
from stripe.v2.core._event import (
    EventNotification,
    RelatedSingletonObject,
    UnknownEventNotification,
)
from stripe.events._event_classes import ALL_EVENT_NOTIFICATIONS
from stripe._webhook import WebhookPayload, WebhookSignature
from tests.test_webhook import (
    ASCII_WHITESPACE_WEBHOOK_SECRETS,
    DUMMY_WEBHOOK_SECRET,
)

EventParser = Callable[[str], ALL_EVENT_NOTIFICATIONS]

BINARY_ENCODERS = [
    lambda p: p.encode("utf-8"),
    lambda p: bytearray(p, "utf-8"),
]


def _require_stripe_object(value: object) -> stripe.StripeObject:
    assert isinstance(value, stripe.StripeObject)
    return value


class TestV2Event(object):
    def test_pickled_event_requires_reattachment(
        self, http_client_mock, v2_payload_no_data
    ):
        event = V1BillingMeterErrorReportTriggeredEvent.construct_from(
            json.loads(v2_payload_no_data),
            "producer-key-sentinel",
            stripe_account="acct_retrieving",
        )
        restored = pickle.loads(pickle.dumps(event))
        with pytest.raises(
            stripe.AuthenticationError, match="reattach_api_key"
        ):
            restored.fetch_related_object()
        http_client_mock.assert_no_request()
        restored.reattach_api_key("worker-key-sentinel")
        assert restored.stripe_account is None
        assert restored._requestor._options.stripe_context == "acct_123"
        assert restored.reason.request.stripe_account is None
        assert (
            restored.reason.request._requestor._options.stripe_context
            == "acct_123"
        )
        http_client_mock.stub_request(
            "get",
            path="/v1/billing/meters/mtr_123",
            rbody='{"id": "mtr_123", "object": "billing.meter"}',
        )
        restored.fetch_related_object()
        http_client_mock.assert_requested(
            "get",
            path="/v1/billing/meters/mtr_123",
            api_key="worker-key-sentinel",
            stripe_context="acct_123",
        )

    @pytest.mark.parametrize("retrieve", [True, False])
    def test_full_event_scopes_children_before_hydration(
        self, http_client_mock: HTTPClientMock, retrieve
    ):
        data = {
            "id": "evt_123",
            "object": "v2.core.event",
            "type": "v2.core.account_person.updated",
            "context": "acct_event",
            "data": {"account_id": "acct_event"},
            "reason": {
                "type": "request",
                "request": {"id": "req_123", "idempotency_key": "key_123"},
            },
        }
        if retrieve:
            http_client_mock.stub_request(
                "get",
                path="/v2/core/events/evt_123",
                rbody=json.dumps(data),
            )
            client = StripeClient(
                api_key="sk_test_1234",
                stripe_account="acct_retrieving",
                stripe_context="acct_previous_context",
                http_client=http_client_mock.get_mock_http_client(),
            )
            event = client.v2.core.events.retrieve("evt_123")
        else:
            event = V2CoreAccountPersonUpdatedEvent.construct_from(
                data,
                "sk_test_1234",
                stripe_account="acct_retrieving",
                api_mode="V2",
            )

        assert isinstance(event, V2CoreAccountPersonUpdatedEvent)
        assert isinstance(
            event.data,
            V2CoreAccountPersonUpdatedEvent.V2CoreAccountPersonUpdatedEventData,
        )
        assert event.reason is not None
        request = _require_stripe_object(event.reason.request)
        for child in (event, event.data, request):
            assert child.stripe_account is None
            assert child._requestor._options.stripe_context == "acct_event"

    @pytest.mark.parametrize(
        ("partial", "context_fields", "expected_context"),
        [
            (True, {}, "acct_123"),
            (True, {"context": "acct_new"}, "acct_new"),
            (True, {"context": None}, None),
            (False, {}, None),
        ],
    )
    def test_full_event_refresh_inherits_only_an_omitted_partial_context(
        self, v2_payload_no_data, partial, context_fields, expected_context
    ):
        event = V1BillingMeterErrorReportTriggeredEvent.construct_from(
            json.loads(v2_payload_no_data),
            "sk_test_1234",
            stripe_account="acct_retrieving",
            api_mode="V2",
        )
        original_related_object = event.related_object
        event.refresh_from(
            {
                "reason": {
                    "type": "request",
                    "request": {"id": "req_456", "idempotency_key": "key_456"},
                },
                **context_fields,
            },
            partial=partial,
            stripe_account="acct_stale",
            api_mode="V2",
        )
        assert event.reason is not None
        expected = [event, _require_stripe_object(event.reason.request)]
        if partial:
            assert event.related_object is original_related_object
            expected.append(event.related_object)
        for child in expected:
            assert child.stripe_account is None
            assert child._requestor._options.stripe_context == expected_context

    def test_full_event_partial_refresh_keeps_independently_scoped_child(
        self, v2_payload_no_data
    ):
        event = V1BillingMeterErrorReportTriggeredEvent.construct_from(
            json.loads(v2_payload_no_data), "sk_test_1234", api_mode="V2"
        )
        assert event.reason is not None
        request = _require_stripe_object(event.reason.request)
        request._requestor = request._requestor.with_stripe_context(
            "acct_independent"
        )

        event.refresh_from(
            {"context": "acct_new"}, partial=True, api_mode="V2"
        )

        reason = _require_stripe_object(event.reason)
        assert reason._requestor._options.stripe_context == "acct_new"
        assert request._requestor._options.stripe_context == "acct_independent"

    @pytest.fixture(scope="function")
    def v2_payload_no_data(self):
        return json.dumps(
            {
                "id": "evt_234",
                "object": "v2.core.event",
                "type": "v1.billing.meter.error_report_triggered",
                "livemode": True,
                "context": "acct_123",
                "created": "2022-02-15T00:27:45.330Z",
                "related_object": {
                    "id": "mtr_123",
                    "type": "billing.meter",
                    "url": "/v1/billing/meters/mtr_123",
                },
                "reason": {
                    "type": "request",
                    "request": {"id": "foo", "idempotency_key": "bar"},
                },
            }
        )

    @pytest.fixture(scope="function")
    def v2_payload_with_data(self):
        return json.dumps(
            {
                "id": "evt_234",
                "object": "v2.core.event",
                "type": "v1.billing.meter.error_report_triggered",
                "livemode": False,
                "created": "2022-02-15T00:27:45.330Z",
                "context": "acct_123",
                "related_object": {
                    "id": "mtr_123",
                    "type": "billing.meter",
                    "url": "/v1/billing/meters/mtr_123",
                },
                "data": {
                    "reason": {
                        "error_count": 1,
                    }
                },
            }
        )

    @pytest.fixture(scope="function")
    def stripe_client(self, http_client_mock):
        return StripeClient(
            api_key="sk_test_1234",
            http_client=http_client_mock.get_mock_http_client(),
        )

    @pytest.fixture(scope="function")
    def parse_event_notif(self, stripe_client: StripeClient) -> EventParser:
        """
        helper to simplify parsing and validating events given a payload
        returns a function that has the client pre-bound
        """

        def _parse_event_notif(payload: str):
            return stripe_client.parse_event_notification(
                payload,
                WebhookSignature.generate_signature_header(
                    payload, DUMMY_WEBHOOK_SECRET
                ),
                DUMMY_WEBHOOK_SECRET,
            )

        return _parse_event_notif

    def test_parses_event_notif(
        self, parse_event_notif: EventParser, v2_payload_no_data: str
    ):
        notif = parse_event_notif(v2_payload_no_data)

        assert isinstance(
            notif, V1BillingMeterErrorReportTriggeredEventNotification
        )
        assert notif.id == "evt_234"
        assert notif.object == "v2.core.event"

        assert notif.related_object
        assert notif.related_object.id == "mtr_123"

        assert notif.reason
        assert notif.reason.type == "request"
        assert notif.reason.request
        assert notif.reason.request.id == "foo"
        assert notif.reason.request.idempotency_key == "bar"

    def test_parses_event_notif_with_data(
        self, parse_event_notif: EventParser, v2_payload_with_data: str
    ):
        notif = parse_event_notif(v2_payload_with_data)

        assert isinstance(
            notif, V1BillingMeterErrorReportTriggeredEventNotification
        )
        # this isn't for constructing events, it's for parsing thin ones
        assert not hasattr(notif, "data")
        assert notif.reason is None

    @pytest.mark.parametrize(
        "encode", BINARY_ENCODERS, ids=["bytes", "bytearray"]
    )
    def test_parses_binary_event_notif(
        self,
        stripe_client: StripeClient,
        v2_payload_no_data: str,
        encode: Callable[[str], WebhookPayload],
    ):
        """The body can arrive as bytes or a bytearray, which is how many frameworks expose it"""
        notif = stripe_client.parse_event_notification(
            encode(v2_payload_no_data),
            WebhookSignature.generate_signature_header(
                v2_payload_no_data, DUMMY_WEBHOOK_SECRET
            ),
            DUMMY_WEBHOOK_SECRET,
        )

        assert isinstance(
            notif, V1BillingMeterErrorReportTriggeredEventNotification
        )
        assert notif.id == "evt_234"

    @pytest.mark.parametrize(
        "to_payload",
        [lambda p: p, *BINARY_ENCODERS, json.loads],
        ids=["str", "bytes", "bytearray", "dict"],
    )
    def test_from_json_accepts_every_payload_shape(
        self,
        stripe_client: StripeClient,
        v2_payload_no_data: str,
        to_payload: Callable[[str], Union[WebhookPayload, Dict[str, Any]]],
    ):
        """`from_json` is public (for pre-verified payloads & tests), so it takes the same shapes the parse methods do"""
        notif = EventNotification.from_json(
            to_payload(v2_payload_no_data), stripe_client
        )

        assert isinstance(
            notif, V1BillingMeterErrorReportTriggeredEventNotification
        )
        assert notif.id == "evt_234"
        assert notif.related_object
        assert notif.related_object.id == "mtr_123"

    def test_parses_unknown_event_notif(self, parse_event_notif: EventParser):
        event = parse_event_notif(
            json.dumps(
                {
                    "id": "evt_234",
                    "object": "v2.core.event",
                    "type": "uknown.event.type",
                    "livemode": True,
                    "created": "2022-02-15T00:27:45.330Z",
                    "context": "acct_456",
                    "related_object": {
                        "id": "mtr_123",
                        "type": "billing.meter",
                        "url": "/v1/billing/meters/mtr_123",
                    },
                }
            )
        )

        assert type(event) is UnknownEventNotification
        assert event.related_object

    def test_related_singleton_object_omits_id(self):
        """
        events whose related object is a singleton get a `RelatedSingletonObject`,
        which has no `id` at all (instead of a perpetually-`None` one)
        """
        related_object = RelatedSingletonObject(
            {"type": "balance", "url": "/v1/balance"}
        )

        assert related_object.type == "balance"
        assert related_object.url == "/v1/balance"
        assert not hasattr(related_object, "id")

    def test_raise_on_v1_payload(self, parse_event_notif: EventParser):
        v1_payload = json.dumps(
            {
                "id": "evt_test_webhook",
                "object": "event",
                "data": {
                    "object": {"id": "rdr_123", "object": "terminal.reader"}
                },
            }
        )
        with pytest.raises(ValueError) as e:
            parse_event_notif(v1_payload)
        assert "StripeClient.construct_event" in str(e.value)

    def test_validates_signature(
        self, stripe_client: StripeClient, v2_payload_no_data
    ):
        with pytest.raises(SignatureVerificationError):
            stripe_client.parse_event_notification(
                v2_payload_no_data, "bad header", DUMMY_WEBHOOK_SECRET
            )

    @pytest.mark.parametrize("secret", [None, ""])
    def test_rejects_missing_secret(
        self,
        stripe_client: StripeClient,
        v2_payload_no_data: str,
        secret: Optional[str],
    ):
        """`secret` is typed as optional for web framework ergonomics, but a missing one is still an error"""
        with pytest.raises(
            SignatureVerificationError,
            match="No webhook secret value was provided",
        ):
            stripe_client.parse_event_notification(
                v2_payload_no_data,
                WebhookSignature.generate_signature_header(
                    v2_payload_no_data,
                    DUMMY_WEBHOOK_SECRET,
                ),
                secret,
            )

    @pytest.mark.parametrize("secret", ASCII_WHITESPACE_WEBHOOK_SECRETS)
    def test_rejects_ascii_whitespace_secret(
        self,
        stripe_client: StripeClient,
        v2_payload_no_data: str,
        secret: str,
    ):
        with pytest.raises(
            SignatureVerificationError,
            match="No webhook secret value was provided",
        ):
            stripe_client.parse_event_notification(
                v2_payload_no_data,
                WebhookSignature.generate_signature_header(
                    v2_payload_no_data,
                    secret,
                ),
                secret,
            )

    def test_v2_events_data_type(self, http_client_mock, v2_payload_with_data):
        method = "get"
        path = "/v2/core/events/evt_123"
        http_client_mock.stub_request(
            method,
            path=path,
            rbody=v2_payload_with_data,
            rcode=200,
            rheaders={},
        )
        client = StripeClient(
            api_key="sk_test_1234",
            stripe_context="org_456",
            http_client=http_client_mock.get_mock_http_client(),
        )
        event = client.v2.core.events.retrieve("evt_123")

        http_client_mock.assert_requested(
            method,
            api_base=DEFAULT_API_BASE,
            path=path,
            api_key="sk_test_1234",
            stripe_context="org_456",
        )
        assert event.id is not None
        assert isinstance(event, V1BillingMeterErrorReportTriggeredEvent)
        assert event.data is not None
        assert isinstance(
            event.data,
            V1BillingMeterErrorReportTriggeredEvent.V1BillingMeterErrorReportTriggeredEventData,
        )
        assert event.data.reason.error_count == 1

    # an "integration" shaped test with all the bells and whistles
    def test_v2_events_integration(
        self,
        http_client_mock: HTTPClientMock,
        v2_payload_no_data,
        v2_payload_with_data,
        # use the real client so we get the real types
        stripe_client: StripeClient,
    ):
        method = "get"
        path = "/v2/core/events/evt_234"
        meter_path = "/v1/billing/meters/mtr_123"

        http_client_mock.stub_request(
            method,
            path=path,
            rbody=v2_payload_with_data,
            rcode=200,
            rheaders={},
        )
        http_client_mock.stub_request(
            method,
            path=meter_path,
            rbody=json.dumps(
                {
                    "id": "mtr_123",
                    "object": "billing.meter",
                    "event_name": "cool event",
                }
            ),
            rcode=200,
            rheaders={},
        )

        event_notif = stripe_client.parse_event_notification(
            v2_payload_no_data,
            WebhookSignature.generate_signature_header(
                v2_payload_no_data, DUMMY_WEBHOOK_SECRET
            ),
            DUMMY_WEBHOOK_SECRET,
        )
        assert event_notif.type == "v1.billing.meter.error_report_triggered"

        event = event_notif.fetch_event()
        meter = event_notif.fetch_related_object()

        # these are purely type-level checks to ensure our narrowing works for users
        assert_type(
            event_notif,
            V1BillingMeterErrorReportTriggeredEventNotification,
        )

        assert_type(event, V1BillingMeterErrorReportTriggeredEvent)
        assert_type(meter, Meter)

        assert isinstance(event, V1BillingMeterErrorReportTriggeredEvent)

        http_client_mock.assert_requested(
            method,
            api_base=DEFAULT_API_BASE,
            path=path,
            api_key="sk_test_1234",
            # context read from event
            stripe_context="acct_123",
            extra_headers={"Stripe-Request-Trigger": "event=evt_234"},
        )
        http_client_mock.assert_requested(
            method,
            api_base=DEFAULT_API_BASE,
            path=meter_path,
            api_key="sk_test_1234",
            # context read from event
            stripe_context="acct_123",
            extra_headers={"Stripe-Request-Trigger": "event=evt_234"},
        )

        assert isinstance(
            event.data,
            V1BillingMeterErrorReportTriggeredEvent.V1BillingMeterErrorReportTriggeredEventData,
        )
        assert event.data.reason.error_count == 1

        assert isinstance(meter, Meter)
        assert meter.event_name == "cool event"

    def test_related_object_retains_event_context(
        self, http_client_mock: HTTPClientMock
    ):
        payload = json.dumps(
            {
                "id": "evt_123",
                "object": "v2.core.event",
                "type": "v1.product.updated",
                "created": "2022-02-15T00:27:45.330Z",
                "livemode": False,
                "context": "acct_child",
                "related_object": {
                    "id": "prod_shared",
                    "type": "product",
                    "url": "/v1/products/prod_shared",
                },
            }
        )
        path = "/v1/products/prod_shared"
        http_client_mock.stub_request(
            "get",
            path=path,
            rbody=json.dumps({"id": "prod_shared", "object": "product"}),
        )
        http_client_mock.stub_request(
            "delete",
            path=path,
            rbody=json.dumps(
                {"id": "prod_shared", "object": "product", "deleted": True}
            ),
        )
        client = StripeClient(
            api_key="sk_test_1234",
            stripe_context="acct_platform",
            http_client=http_client_mock.get_mock_http_client(),
        )

        notification = client.parse_event_notification(
            payload,
            WebhookSignature.generate_signature_header(
                payload, DUMMY_WEBHOOK_SECRET
            ),
            DUMMY_WEBHOOK_SECRET,
        )
        assert isinstance(notification, V1ProductUpdatedEventNotification)

        product = notification.fetch_related_object()
        product.delete()

        http_client_mock.assert_requested(
            "get", path=path, stripe_context="acct_child"
        )
        http_client_mock.assert_requested(
            "delete", path=path, stripe_context="acct_child"
        )

    @pytest.mark.anyio
    async def test_related_object_retains_event_context_async(
        self, http_client_mock: HTTPClientMock
    ):
        payload = json.dumps(
            {
                "id": "evt_123",
                "object": "v2.core.event",
                "type": "v1.product.updated",
                "created": "2022-02-15T00:27:45.330Z",
                "livemode": False,
                "context": "acct_child",
                "related_object": {
                    "id": "prod_shared",
                    "type": "product",
                    "url": "/v1/products/prod_shared",
                },
            }
        )
        path = "/v1/products/prod_shared"
        http_client_mock.stub_request(
            "get",
            path=path,
            query_string="usage[0]=fetch_related_object",
            rbody=json.dumps({"id": "prod_shared", "object": "product"}),
        )
        http_client_mock.stub_request(
            "delete",
            path=path,
            rbody=json.dumps(
                {"id": "prod_shared", "object": "product", "deleted": True}
            ),
        )
        client = StripeClient(
            api_key="sk_test_1234",
            stripe_context="acct_platform",
            http_client=http_client_mock.get_mock_http_client(),
        )

        notification = client.parse_event_notification(
            payload,
            WebhookSignature.generate_signature_header(
                payload, DUMMY_WEBHOOK_SECRET
            ),
            DUMMY_WEBHOOK_SECRET,
        )
        assert isinstance(notification, V1ProductUpdatedEventNotification)

        product = await notification.fetch_related_object_async()
        await product.delete_async()

        http_client_mock.assert_requested(
            "get", path=path, stripe_context="acct_child"
        )
        http_client_mock.assert_requested(
            "delete", path=path, stripe_context="acct_child"
        )

    def test_direct_retrieve_related_object_retains_event_context(
        self, http_client_mock: HTTPClientMock
    ):
        """
        Unlike EventNotification (built from a webhook), a directly-retrieved
        Event doesn't go through StripeClient.with_stripe_context in its own
        construction, so historically it kept whatever stripe_account retrieved
        it. Make sure fetch_related_object() only ever uses the event's own
        context, with no stale account from the retrieving client leaking in.
        """
        event_path = "/v2/core/events/evt_123"
        related_path = "/v1/products/prod_shared"

        http_client_mock.stub_request(
            "get",
            path=event_path,
            rbody=json.dumps(
                {
                    "id": "evt_123",
                    "object": "v2.core.event",
                    "type": "v1.product.updated",
                    "created": "2022-02-15T00:27:45.330Z",
                    "livemode": False,
                    "context": "acct_child",
                    "related_object": {
                        "id": "prod_shared",
                        "type": "product",
                        "url": related_path,
                    },
                }
            ),
        )
        http_client_mock.stub_request(
            "get",
            path=related_path,
            rbody=json.dumps({"id": "prod_shared", "object": "product"}),
        )

        client = StripeClient(
            api_key="sk_test_1234",
            stripe_account="acct_platform",
            http_client=http_client_mock.get_mock_http_client(),
        )

        event = client.v2.core.events.retrieve("evt_123")
        assert isinstance(event, V1ProductUpdatedEvent)

        product = event.fetch_related_object()
        assert product.id == "prod_shared"

        http_client_mock.assert_requested(
            "get", path=related_path, stripe_context="acct_child"
        )

        assert len(http_client_mock.get_all_calls()) == 2
        related_call = http_client_mock.get_last_call()
        assert related_call.headers is not None
        assert "Stripe-Account" not in related_call.headers
