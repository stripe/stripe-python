import json

import pytest

import stripe
from stripe._webhook import Webhook
from stripe.v2.core._event import EventNotification

BINARY_ENCODERS = [
    lambda p: p.encode("utf-8"),
    lambda p: bytearray(p, "utf-8"),
]


@pytest.fixture
def client():
    return stripe.StripeClient("sk_test_fake")


@pytest.fixture
def eventbridge_payload():
    return json.dumps(
        {
            "version": "0",
            "id": "17e8dff5-d6cd-3770-ace9-aeac02b6ac3f",
            "detail-type": "customer.created",
            "source": "aws.partner/stripe.com/ed_123",
            "account": "506417113029",
            "time": "2024-03-07T18:27:56Z",
            "region": "us-west-2",
            "resources": [],
            "detail": {
                "id": "evt_test_123",
                "object": "event",
                "api_version": "2023-10-16",
                "created": 1709836076,
                "data": {"object": {"id": "cus_123", "object": "customer"}},
                "livemode": True,
                "pending_webhooks": 0,
                "request": {"id": "req_123", "idempotency_key": None},
                "type": "customer.created",
            },
        }
    )


@pytest.fixture
def eventgrid_payload():
    return json.dumps(
        {
            "specversion": "1.0",
            "type": "customer.created",
            "source": "/providers/stripe/ed_test_123",
            "id": "9aeb0fdf-c01e-0131-0922-9eb54906e209",
            "time": "2025-07-11T14:30:00Z",
            "subject": None,
            "dataContentType": "application/cloudevents+json",
            "data": {
                "id": "evt_test_456",
                "object": "event",
                "api_version": "2023-10-16",
                "created": 1709836076,
                "data": {"object": {"id": "cus_456", "object": "customer"}},
                "livemode": False,
                "pending_webhooks": 0,
                "request": {"id": "req_456", "idempotency_key": None},
                "type": "customer.created",
            },
        }
    )


@pytest.fixture
def eventbridge_notification_payload():
    return json.dumps(
        {
            "version": "0",
            "id": "17e8dff5-d6cd-3770-ace9-aeac02b6ac3f",
            "detail-type": "v2.core.event_destination.ping",
            "source": "aws.partner/stripe.com/ed_123",
            "account": "506417113029",
            "time": "2024-03-07T18:27:56Z",
            "region": "us-west-2",
            "resources": [],
            "detail": {
                "id": "evt_test_789",
                "object": "v2.core.event",
                "type": "v2.core.event_destination.ping",
                "created": "2024-03-07T18:27:56.000Z",
                "context": "acct_123",
                "livemode": True,
                "related_object": {
                    "id": "ed_123",
                    "type": "v2.core.event_destination",
                    "url": "/v2/core/event_destinations/ed_123",
                },
            },
        }
    )


@pytest.fixture
def eventgrid_notification_payload():
    return json.dumps(
        {
            "specversion": "1.0",
            "type": "v2.core.event_destination.ping",
            "source": "/providers/stripe/ed_test_123",
            "id": "9aeb0fdf-c01e-0131-0922-9eb54906e209",
            "time": "2025-07-11T14:30:00Z",
            "data": {
                "id": "evt_test_790",
                "object": "v2.core.event",
                "type": "v2.core.event_destination.ping",
                "created": "2024-03-07T18:27:56.000Z",
                "context": "acct_123",
                "livemode": True,
                "related_object": {
                    "id": "ed_test_123",
                    "type": "v2.core.event_destination",
                    "url": "/v2/core/event_destinations/ed_test_123",
                },
            },
        }
    )


class TestConstructEventWithoutVerification:
    def test_eventbridge(self, client, eventbridge_payload):
        result = client.construct_event_without_verification(
            eventbridge_payload
        )
        assert isinstance(result, stripe.Event)
        assert result.id == "evt_test_123"
        assert result.type == "customer.created"

    def test_eventgrid(self, client, eventgrid_payload):
        result = client.construct_event_without_verification(eventgrid_payload)
        assert isinstance(result, stripe.Event)
        assert result.id == "evt_test_456"
        assert result.type == "customer.created"

    def test_raw_event_passthrough(self, client):
        raw_event = json.dumps(
            {
                "id": "evt_test_123",
                "object": "event",
                "type": "customer.created",
            }
        )
        result = client.construct_event_without_verification(raw_event)
        assert isinstance(result, stripe.Event)
        assert result.id == "evt_test_123"
        assert result.type == "customer.created"

    def test_invalid_json(self, client):
        with pytest.raises(json.JSONDecodeError):
            client.construct_event_without_verification("not valid json")

    def test_thin_event_suggests_parse_event_notification_without_verification(
        self, client, eventbridge_notification_payload
    ):
        with pytest.raises(ValueError, match="parse_event_notification"):
            client.construct_event_without_verification(
                eventbridge_notification_payload
            )

    def test_unrecognized_format(self, client):
        with pytest.raises(ValueError, match="Unrecognized event format"):
            client.construct_event_without_verification(
                json.dumps({"foo": "bar"})
            )

    def test_azure_envelope_missing_data_field(self, client):
        payload = json.dumps(
            {
                "specversion": "1.0",
                "type": "customer.created",
                "source": "/providers/stripe/ed_test_123",
                "id": "test-missing-data",
            }
        )
        with pytest.raises(ValueError, match="Unrecognized event format"):
            client.construct_event_without_verification(payload)

    @pytest.mark.parametrize(
        "payload_fixture", ["eventbridge_payload", "eventgrid_payload"]
    )
    @pytest.mark.parametrize(
        "encode", BINARY_ENCODERS, ids=["bytes", "bytearray"]
    )
    def test_binary_envelope(self, request, client, payload_fixture, encode):
        """An envelope can arrive as bytes or a bytearray, which is how many frameworks expose it"""
        payload = request.getfixturevalue(payload_fixture)

        result = client.construct_event_without_verification(encode(payload))

        assert isinstance(result, stripe.Event)
        assert result.type == "customer.created"

    def test_webhook_static_method_eventbridge(self, eventbridge_payload):
        result = Webhook.construct_event_without_verification(
            eventbridge_payload
        )
        assert isinstance(result, stripe.Event)
        assert result.id == "evt_test_123"
        assert result.type == "customer.created"


class TestParseEventNotificationWithoutVerification:
    def test_eventbridge(self, client, eventbridge_notification_payload):
        result = client.parse_event_notification_without_verification(
            eventbridge_notification_payload
        )
        assert result.id == "evt_test_789"
        assert result.type == "v2.core.event_destination.ping"

    def test_eventgrid(self, client, eventgrid_notification_payload):
        result = client.parse_event_notification_without_verification(
            eventgrid_notification_payload
        )
        assert result.id == "evt_test_790"
        assert result.type == "v2.core.event_destination.ping"

    @pytest.mark.parametrize(
        "payload_fixture",
        [
            "eventbridge_notification_payload",
            "eventgrid_notification_payload",
        ],
    )
    @pytest.mark.parametrize(
        "encode", BINARY_ENCODERS, ids=["bytes", "bytearray"]
    )
    def test_binary_envelope(self, request, client, payload_fixture, encode):
        """An envelope can arrive as bytes or a bytearray, which is how many frameworks expose it"""
        payload = request.getfixturevalue(payload_fixture)

        result = client.parse_event_notification_without_verification(
            encode(payload)
        )

        assert isinstance(result, EventNotification)
        assert result.type == "v2.core.event_destination.ping"

    def test_v1_event_suggests_construct_event_without_verification(
        self, client, eventbridge_payload
    ):
        with pytest.raises(ValueError, match="construct_event"):
            client.parse_event_notification_without_verification(
                eventbridge_payload
            )

    def test_invalid_json(self, client):
        with pytest.raises(json.JSONDecodeError):
            client.parse_event_notification_without_verification(
                "not valid json"
            )

    def test_unrecognized_format(self, client):
        with pytest.raises(ValueError, match="Unrecognized event format"):
            client.parse_event_notification_without_verification(
                json.dumps({"foo": "bar"})
            )

    def test_azure_envelope_missing_data_field(self, client):
        payload = json.dumps(
            {
                "specversion": "1.0",
                "type": "v2.core.event_destination.ping",
                "source": "/providers/stripe/ed_test_123",
                "id": "test-missing-data",
            }
        )
        with pytest.raises(ValueError, match="Unrecognized event format"):
            client.parse_event_notification_without_verification(payload)

    def test_unexpected_object_type_in_event_notification(self, client):
        # Wrap in an EventBridge envelope so envelope extraction succeeds,
        # letting the object-type guard inside from_json fire.
        payload = json.dumps(
            {
                "version": "0",
                "id": "17e8dff5-d6cd-3770-ace9-aeac02b6ac3f",
                "detail-type": "customer.created",
                "source": "aws.partner/stripe.com/ed_123",
                "account": "506417113029",
                "time": "2024-03-07T18:27:56Z",
                "region": "us-west-2",
                "resources": [],
                "detail": {
                    "object": "customer",
                    "type": "customer.created",
                    "id": "cus_123",
                },
            }
        )
        with pytest.raises(ValueError, match="Unexpected object type"):
            client.parse_event_notification_without_verification(payload)

    def test_raw_event_notification_passthrough(self, client):
        raw_notification = json.dumps(
            {
                "id": "evt_234",
                "object": "v2.core.event",
                "type": "v2.core.event_destination.ping",
                "created": "2022-02-15T00:27:45.330Z",
                "livemode": True,
                "context": "acct_123",
                "related_object": {
                    "id": "ed_123",
                    "type": "v2.core.event_destination",
                    "url": "/v2/core/event_destinations/ed_123",
                },
            }
        )
        result = client.parse_event_notification_without_verification(
            raw_notification
        )
        assert isinstance(result, EventNotification)
        assert result.id == "evt_234"
        assert result.type == "v2.core.event_destination.ping"
