import json
import sys
from typing import Callable

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
from stripe.v2._event import UnknownEventNotification
from stripe.events._event_classes import ALL_EVENT_NOTIFICATIONS
from tests.test_webhook import DUMMY_WEBHOOK_SECRET, generate_header

EventParser = Callable[[str], ALL_EVENT_NOTIFICATIONS]


class TestV2Event(object):
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
        return StripeClient(
            api_key="sk_test_1234",
            http_client=http_client_mock.get_mock_http_client(),
        )

    @pytest.fixture(scope="function")
    def parse_thin_event(self, stripe_client: StripeClient) -> EventParser:
        """
        helper to simplify parsing and validating events given a payload
        returns a function that has the client pre-bound
        """

        def _parse_thin_event(payload: str):
            return stripe_client.parse_event_notification(
                payload, generate_header(payload=payload), DUMMY_WEBHOOK_SECRET
            )

        return _parse_thin_event

    def test_parses_thin_event(
        self, parse_thin_event: EventParser, v2_payload_no_data: str
    ):
        event = parse_thin_event(v2_payload_no_data)

        assert isinstance(
            event, V1BillingMeterErrorReportTriggeredEventNotification
        )
        assert event.id == "evt_234"

        assert event.related_object
        assert event.related_object.id == "mtr_123"

        assert event.reason
        assert event.reason.id == "foo"

    def test_parses_thin_event_with_data(
        self, parse_thin_event: EventParser, v2_payload_with_data: str
    ):
        event = parse_thin_event(v2_payload_with_data)

        assert isinstance(
            event, V1BillingMeterErrorReportTriggeredEventNotification
        )
        # this isn't for constructing events, it's for parsing thin ones
        assert not hasattr(event, "data")
        assert event.reason is None

    def test_parses_unknown_thin_event(self, parse_thin_event: EventParser):
        event = parse_thin_event(
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
                    "reason": {
                        "id": "foo",
                        "idempotency_key": "bar",
                    },
                }
            )
        )

        assert type(event) is UnknownEventNotification
        assert event.related_object

    def test_validates_signature(
        self, stripe_client: StripeClient, v2_payload_no_data
    ):
        with pytest.raises(SignatureVerificationError):
            stripe_client.parse_event_notification(
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
        parse_thin_event: EventParser,
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

        thin_event = parse_thin_event(v2_payload_no_data)
        assert thin_event.type == "v1.billing.meter.error_report_triggered"

        event = thin_event.fetch_event()
        meter = thin_event.fetch_related_object()

        if sys.version_info >= (3, 7):
            from typing_extensions import assert_type  # noqa: SPY103 - this is only available on 3.6 pythons because of typing_extensions version restrictions

            # these are purely type-level checks to ensure our narrowing works for users
            assert_type(
                thin_event, V1BillingMeterErrorReportTriggeredEventNotification
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
        )
        http_client_mock.assert_requested(
            method,
            api_base=DEFAULT_API_BASE,
            path=meter_path,
            api_key="sk_test_1234",
            # context read from event
            stripe_context="acct_123",
        )

        assert isinstance(
            event.data,
            V1BillingMeterErrorReportTriggeredEvent.V1BillingMeterErrorReportTriggeredEventData,
        )
        assert event.data.reason.error_count == 1

        assert isinstance(meter, Meter)
        assert meter.event_name == "cool event"
