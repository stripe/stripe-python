import json
from typing import Callable

import pytest

import stripe
from stripe._stripe_object import StripeObject
from stripe import ThinEvent
from tests.test_webhook import DUMMY_WEBHOOK_SECRET, generate_header

EventParser = Callable[[str], ThinEvent]


class TestV2Event(object):
    @pytest.fixture(scope="function")
    def v2_payload_no_data(self):
        return json.dumps(
            {
                "id": "evt_234",
                "object": "event",
                "type": "financial_account.balance.opened",
                "created": "2022-02-15T00:27:45.330Z",
                "related_object": {
                    "id": "fa_123",
                    "type": "financial_account",
                    "url": "/v2/financial_accounts/fa_123",
                    "stripe_context": "acct_123",
                },
            }
        )

    @pytest.fixture(scope="function")
    def v2_payload_with_data(self):
        return json.dumps(
            {
                "id": "evt_234",
                "object": "event",
                "type": "financial_account.balance.opened",
                "created": "2022-02-15T00:27:45.330Z",
                "related_object": {
                    "id": "fa_123",
                    "type": "financial_account",
                    "url": "/v2/financial_accounts/fa_123",
                    "stripe_context": "acct_123",
                },
                "data": {
                    "containing_compartment_id": "compid",
                    "id": "foo",
                    "type": "bufo",
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

    def test_parses_v2_event(
        self, parse_thin_event: EventParser, v2_payload_no_data: str
    ):
        event = parse_thin_event(v2_payload_no_data)

        # parse event returns a plain dict
        assert not isinstance(event, StripeObject)
        assert event == json.loads(v2_payload_no_data)

    def test_validates_signature(
        self, stripe_client: stripe.StripeClient, v2_payload_no_data
    ):
        with pytest.raises(stripe.error.SignatureVerificationError):
            stripe_client.parse_thin_event(
                v2_payload_no_data, "bad header", DUMMY_WEBHOOK_SECRET
            )
