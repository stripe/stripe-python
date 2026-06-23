import json
import pytest

from stripe._stripe_client import StripeClient
from stripe.billing._meter import Meter
from stripe.v2._ref import Ref
from tests.http_client_mock import HTTPClientMock


class TestRef(object):
    def test_construction(self):
        parsed = {
            "type": "billing.meter",
            "id": "mtr_123",
            "url": "/v1/billing/meters/mtr_123",
        }
        ref: Ref[Meter] = Ref(parsed, requestor=None)

        assert ref.type == "billing.meter"
        assert ref.id == "mtr_123"
        assert ref.url == "/v1/billing/meters/mtr_123"

    def test_repr(self):
        parsed = {
            "type": "billing.meter",
            "id": "mtr_123",
            "url": "/v1/billing/meters/mtr_123",
        }
        ref: Ref[Meter] = Ref(parsed, requestor=None)
        assert repr(ref) == "<Ref type=billing.meter id=mtr_123 url=/v1/billing/meters/mtr_123>"

    def test_fetch_raises_without_requestor(self):
        parsed = {
            "type": "billing.meter",
            "id": "mtr_123",
            "url": "/v1/billing/meters/mtr_123",
        }
        ref: Ref[Meter] = Ref(parsed, requestor=None)

        with pytest.raises(RuntimeError, match="no associated requestor"):
            ref.fetch()

    def test_fetch_async_raises_without_requestor(self):
        parsed = {
            "type": "billing.meter",
            "id": "mtr_123",
            "url": "/v1/billing/meters/mtr_123",
        }
        ref: Ref[Meter] = Ref(parsed, requestor=None)

        with pytest.raises(RuntimeError, match="no associated requestor"):
            import asyncio
            asyncio.get_event_loop().run_until_complete(ref.fetch_async())

    def test_fetch_v1_resource(self, http_client_mock: HTTPClientMock):
        client = StripeClient(
            api_key="sk_test_1234",
            http_client=http_client_mock.get_mock_http_client(),
        )

        meter_path = "/v1/billing/meters/mtr_123"
        http_client_mock.stub_request(
            "get",
            path=meter_path,
            rbody=json.dumps(
                {
                    "id": "mtr_123",
                    "object": "billing.meter",
                    "event_name": "api_calls",
                }
            ),
            rcode=200,
            rheaders={},
        )

        parsed = {
            "type": "billing.meter",
            "id": "mtr_123",
            "url": meter_path,
        }
        ref: Ref[Meter] = Ref(parsed, requestor=client._requestor)
        result = ref.fetch()

        http_client_mock.assert_requested(
            "get",
            path=meter_path,
            api_key="sk_test_1234",
        )
        assert isinstance(result, Meter)
        assert result.id == "mtr_123"

    def test_fetch_v2_resource(self, http_client_mock: HTTPClientMock):
        from stripe.v2.core._event import Event

        client = StripeClient(
            api_key="sk_test_1234",
            http_client=http_client_mock.get_mock_http_client(),
        )

        event_path = "/v2/core/events/evt_123"
        http_client_mock.stub_request(
            "get",
            path=event_path,
            rbody=json.dumps(
                {
                    "id": "evt_123",
                    "object": "v2.core.event",
                    "type": "unknown.event.type",
                    "livemode": False,
                    "created": "2024-01-01T00:00:00.000Z",
                    "context": None,
                    "reason": None,
                }
            ),
            rcode=200,
            rheaders={},
        )

        parsed = {
            "type": "v2.core.event",
            "id": "evt_123",
            "url": event_path,
        }
        ref: Ref[Event] = Ref(parsed, requestor=client._requestor)
        result = ref.fetch()

        http_client_mock.assert_requested(
            "get",
            path=event_path,
            api_key="sk_test_1234",
        )
        assert isinstance(result, Event)
        assert result.id == "evt_123"
