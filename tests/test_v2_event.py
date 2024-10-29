import json
from typing import Callable

import pytest

import stripe
from stripe import ThinEvent
from stripe.events._v1_billing_meter_error_report_triggered_event import (
    V1BillingMeterErrorReportTriggeredEvent,
)
from tests.test_webhook import DUMMY_WEBHOOK_SECRET, generate_header

EventParser = Callable[[str], ThinEvent]


class TestV2Event(object):
    @pytest.fixture(scope="function")
    def v2_payload_no_data(self):
        return json.dumps(
            {
                "id": "evt_234",
                "object": "v2.core.event",
                "type": "v1.billing.meter.error_report_triggered",
                "livemode": True,
                "created": "2022-02-15T00:27:45.330Z",
                "related_object": {
                    "id": "mtr_123",
                    "type": "billing.meter",
                    "url": "/v1/billing/meters/mtr_123",
                    "stripe_context": "acct_123",
                },
                "reason": {
                    "id": "foo",
                    "idempotency_key": "bar",
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
        return stripe.StripeClient(
            api_key="keyinfo_test_123",
            stripe_context="wksp_123",
            http_client=http_client_mock.get_mock_http_client(),
        )

    @pytest.fixture(scope="function")
    def parse_thin_event(
        self, stripe_client: stripe.StripeClient
    ) -> EventParser:
        """
        helper to simplify parsing and validating events given a payload
        returns a function that has the client pre-bound
        """

        def _parse_thin_event(payload: str):
            return stripe_client.parse_thin_event(
                payload, generate_header(payload=payload), DUMMY_WEBHOOK_SECRET
            )

        return _parse_thin_event

    def test_parses_thin_event(
        self, parse_thin_event: EventParser, v2_payload_no_data: str
    ):
        event = parse_thin_event(v2_payload_no_data)

        assert isinstance(event, ThinEvent)
        assert event.id == "evt_234"

        assert event.related_object
        assert event.related_object.id == "mtr_123"

        assert event.reason
        assert event.reason.id == "foo"

    def test_parses_thin_event_with_data(
        self, parse_thin_event: EventParser, v2_payload_with_data: str
    ):
        event = parse_thin_event(v2_payload_with_data)

        assert isinstance(event, ThinEvent)
        assert not hasattr(event, "data")
        assert event.reason is None

    def test_validates_signature(
        self, stripe_client: stripe.StripeClient, v2_payload_no_data
    ):
        with pytest.raises(stripe.error.SignatureVerificationError):
            stripe_client.parse_thin_event(
                v2_payload_no_data, "bad header", DUMMY_WEBHOOK_SECRET
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
        assert isinstance(event, V1BillingMeterErrorReportTriggeredEvent)
        assert event.data is not None
        assert isinstance(
            event.data,
            V1BillingMeterErrorReportTriggeredEvent.V1BillingMeterErrorReportTriggeredEventData,
        )
        assert event.data.reason.error_count == 1
