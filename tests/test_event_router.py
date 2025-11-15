import json
import pytest
from typing import Optional
from unittest.mock import Mock

from stripe import StripeClient
from stripe._event_router import EventRouter, UnhandledNotificationDetails
from stripe._stripe_context import StripeContext
from stripe.events._v1_billing_meter_error_report_triggered_event import (
    V1BillingMeterErrorReportTriggeredEventNotification,
)
from stripe.events._v2_core_account_created_event import (
    V2CoreAccountCreatedEventNotification,
)
from stripe.v2.core._event import EventNotification, UnknownEventNotification
from tests.http_client_mock import HTTPClientMock
from tests.test_webhook import DUMMY_WEBHOOK_SECRET, generate_header


class TestEventRouter:
    @pytest.fixture(scope="function")
    def stripe_client(self, http_client_mock: HTTPClientMock) -> StripeClient:
        return StripeClient(
            api_key="sk_test_1234",
            stripe_context=StripeContext.parse("original_context_123"),
            http_client=http_client_mock.get_mock_http_client(),
        )

    @pytest.fixture(scope="function")
    def on_unhandled_handler(self) -> Mock:
        """Mock handler for unhandled events"""
        return Mock()

    @pytest.fixture(scope="function")
    def event_router(
        self, stripe_client: StripeClient, on_unhandled_handler: Mock
    ) -> EventRouter:
        return EventRouter(
            client=stripe_client,
            webhook_secret=DUMMY_WEBHOOK_SECRET,
            on_unhandled_handler=on_unhandled_handler,
        )

    @pytest.fixture(scope="function")
    def v1_billing_meter_payload(self) -> str:
        """A payload for v1.billing.meter.error_report_triggered event"""
        return json.dumps(
            {
                "id": "evt_123",
                "object": "v2.core.event",
                "type": "v1.billing.meter.error_report_triggered",
                "livemode": False,
                "created": "2022-02-15T00:27:45.330Z",
                "context": "event_context_456",
                "related_object": {
                    "id": "mtr_123",
                    "type": "billing.meter",
                    "url": "/v1/billing/meters/mtr_123",
                },
            }
        )

    @pytest.fixture(scope="function")
    def v2_account_created_payload(self) -> str:
        """A payload for v2.core.account.created event with None context"""
        return json.dumps(
            {
                "id": "evt_789",
                "object": "v2.core.event",
                "type": "v2.core.account.created",
                "livemode": False,
                "created": "2022-02-15T00:27:45.330Z",
                "context": None,
                "related_object": {
                    "id": "acct_abc",
                    "type": "account",
                    "url": "/v2/core/accounts/acct_abc",
                },
            }
        )

    @pytest.fixture(scope="function")
    def unknown_event_payload(self) -> str:
        """A payload for an unknown event type (llama.created)"""
        return json.dumps(
            {
                "id": "evt_unknown",
                "object": "v2.core.event",
                "type": "llama.created",
                "livemode": False,
                "created": "2022-02-15T00:27:45.330Z",
                "context": "event_context_unknown",
                "related_object": {
                    "id": "llama_123",
                    "type": "llama",
                    "url": "/v1/llamas/llama_123",
                },
            }
        )

    def test_routes_event_to_registered_handler(
        self,
        event_router: EventRouter,
        v1_billing_meter_payload: str,
        on_unhandled_handler: Mock,
    ) -> None:
        """Test that a registered event type is routed to the correct handler"""
        handler = Mock()
        event_router.on_V1BillingMeterErrorReportTriggeredEventNotification(
            handler
        )

        sig_header = generate_header(payload=v1_billing_meter_payload)
        event_router.handle(v1_billing_meter_payload, sig_header)

        handler.assert_called_once()

        call_args = handler.call_args[0]
        assert isinstance(
            call_args[0], V1BillingMeterErrorReportTriggeredEventNotification
        )

        on_unhandled_handler.assert_not_called()

    def test_routes_different_events_to_correct_handlers(
        self,
        event_router: EventRouter,
        v1_billing_meter_payload: str,
        v2_account_created_payload: str,
        on_unhandled_handler: Mock,
    ) -> None:
        """Test that different event types route to their respective handlers"""
        billing_handler = Mock()
        account_handler = Mock()

        event_router.on_V1BillingMeterErrorReportTriggeredEventNotification(
            billing_handler
        )
        event_router.on_V2CoreAccountCreatedEventNotification(account_handler)

        sig_header1 = generate_header(payload=v1_billing_meter_payload)
        event_router.handle(v1_billing_meter_payload, sig_header1)

        sig_header2 = generate_header(payload=v2_account_created_payload)
        event_router.handle(v2_account_created_payload, sig_header2)

        billing_handler.assert_called_once()
        account_handler.assert_called_once()

        assert isinstance(
            billing_handler.call_args[0][0],
            V1BillingMeterErrorReportTriggeredEventNotification,
        )
        assert isinstance(
            account_handler.call_args[0][0],
            V2CoreAccountCreatedEventNotification,
        )

        on_unhandled_handler.assert_not_called()

    def test_handler_receives_correct_runtime_type(
        self, event_router: EventRouter, v1_billing_meter_payload: str
    ) -> None:
        """Test that handlers receive the correctly typed event notification"""
        received_event: Optional[EventNotification] = None
        received_client: Optional[StripeClient] = None

        def handler(
            event: V1BillingMeterErrorReportTriggeredEventNotification,
            client: StripeClient,
        ) -> None:
            nonlocal received_event, received_client
            received_event = event
            received_client = client

        event_router.on_V1BillingMeterErrorReportTriggeredEventNotification(
            handler
        )

        sig_header = generate_header(payload=v1_billing_meter_payload)
        event_router.handle(v1_billing_meter_payload, sig_header)

        assert isinstance(
            received_event, V1BillingMeterErrorReportTriggeredEventNotification
        )
        assert received_event.type == "v1.billing.meter.error_report_triggered"
        assert received_event.id == "evt_123"
        assert received_event.related_object.id == "mtr_123"
        assert isinstance(received_client, StripeClient)

    def test_cannot_register_handler_after_handling(
        self, event_router: EventRouter, v1_billing_meter_payload: str
    ) -> None:
        """Test that registering handlers after handle() raises RuntimeError"""
        handler = Mock()
        event_router.on_V1BillingMeterErrorReportTriggeredEventNotification(
            handler
        )

        sig_header = generate_header(payload=v1_billing_meter_payload)
        event_router.handle(v1_billing_meter_payload, sig_header)

        with pytest.raises(
            RuntimeError,
            match="Cannot register new event handlers after .handle\\(\\) has been called",
        ):
            event_router.on_V2CoreAccountCreatedEventNotification(Mock())

    def test_cannot_register_duplicate_handler(
        self, event_router: EventRouter
    ) -> None:
        """Test that registering the same event type twice raises ValueError"""
        handler1 = Mock()
        handler2 = Mock()

        event_router.on_V1BillingMeterErrorReportTriggeredEventNotification(
            handler1
        )

        with pytest.raises(
            ValueError,
            match='Handler for event type "v1.billing.meter.error_report_triggered" already registered',
        ):
            event_router.on_V1BillingMeterErrorReportTriggeredEventNotification(
                handler2
            )

    def test_handler_uses_event_stripe_context(
        self,
        event_router: EventRouter,
        v1_billing_meter_payload: str,
        stripe_client: StripeClient,
    ) -> None:
        """Test that the handler receives a client with stripe_context from the event"""
        received_context: Optional[StripeContext | str] = None

        def handler(
            event: V1BillingMeterErrorReportTriggeredEventNotification,
            client: StripeClient,
        ) -> None:
            nonlocal received_context
            received_context = client._requestor._options.stripe_context

        event_router.on_V1BillingMeterErrorReportTriggeredEventNotification(
            handler
        )

        assert (
            str(stripe_client._requestor._options.stripe_context)
            == "original_context_123"
        )

        sig_header = generate_header(payload=v1_billing_meter_payload)
        event_router.handle(v1_billing_meter_payload, sig_header)

        assert str(received_context) == "event_context_456"

    def test_stripe_context_restored_after_handler_success(
        self,
        event_router: EventRouter,
        v1_billing_meter_payload: str,
        stripe_client: StripeClient,
    ) -> None:
        """Test that the original stripe_context is restored after successful handler execution"""

        def handler(
            event: V1BillingMeterErrorReportTriggeredEventNotification,
            client: StripeClient,
        ) -> None:
            assert (
                str(client._requestor._options.stripe_context)
                == "event_context_456"
            )

        event_router.on_V1BillingMeterErrorReportTriggeredEventNotification(
            handler
        )

        assert (
            str(stripe_client._requestor._options.stripe_context)
            == "original_context_123"
        )

        sig_header = generate_header(payload=v1_billing_meter_payload)
        event_router.handle(v1_billing_meter_payload, sig_header)

        assert (
            str(stripe_client._requestor._options.stripe_context)
            == "original_context_123"
        )

    def test_stripe_context_restored_after_handler_error(
        self,
        event_router: EventRouter,
        v1_billing_meter_payload: str,
        stripe_client: StripeClient,
    ) -> None:
        """Test that the original stripe_context is restored even when handler raises an exception"""

        def handler(
            event: V1BillingMeterErrorReportTriggeredEventNotification,
            client: StripeClient,
        ) -> None:
            assert (
                str(client._requestor._options.stripe_context)
                == "event_context_456"
            )
            raise RuntimeError("Handler error!")

        event_router.on_V1BillingMeterErrorReportTriggeredEventNotification(
            handler
        )

        assert (
            str(stripe_client._requestor._options.stripe_context)
            == "original_context_123"
        )

        sig_header = generate_header(payload=v1_billing_meter_payload)

        with pytest.raises(RuntimeError, match="Handler error!"):
            event_router.handle(v1_billing_meter_payload, sig_header)

        assert (
            str(stripe_client._requestor._options.stripe_context)
            == "original_context_123"
        )

    def test_stripe_context_set_to_none_when_event_has_no_context(
        self,
        event_router: EventRouter,
        v2_account_created_payload: str,
        stripe_client: StripeClient,
    ) -> None:
        """Test that stripe_context is set to None when event context is None"""
        received_context: Optional[StripeContext | str] = None

        def handler(
            event: V2CoreAccountCreatedEventNotification, client: StripeClient
        ) -> None:
            nonlocal received_context
            received_context = client._requestor._options.stripe_context

        event_router.on_V2CoreAccountCreatedEventNotification(handler)

        # Verify we're working with StripeContext instances
        assert isinstance(
            stripe_client._requestor._options.stripe_context, StripeContext
        )
        assert (
            str(stripe_client._requestor._options.stripe_context)
            == "original_context_123"
        )

        sig_header = generate_header(payload=v2_account_created_payload)
        event_router.handle(v2_account_created_payload, sig_header)

        assert received_context is None

        assert (
            str(stripe_client._requestor._options.stripe_context)
            == "original_context_123"
        )

    def test_unknown_event_routes_to_on_unhandled(
        self,
        event_router: EventRouter,
        unknown_event_payload: str,
        on_unhandled_handler: Mock,
    ) -> None:
        """Test that events without SDK types route to on_unhandled handler"""
        sig_header = generate_header(payload=unknown_event_payload)

        event_router.handle(unknown_event_payload, sig_header)

        on_unhandled_handler.assert_called_once()

        call_args = on_unhandled_handler.call_args[0]
        event_notif = call_args[0]
        client = call_args[1]
        info = call_args[2]

        assert isinstance(event_notif, UnknownEventNotification)
        assert event_notif.type == "llama.created"
        assert isinstance(client, StripeClient)
        assert isinstance(info, UnhandledNotificationDetails)
        assert info.is_known_event_type is False

    def test_known_unregistered_event_routes_to_on_unhandled(
        self,
        event_router: EventRouter,
        v1_billing_meter_payload: str,
        on_unhandled_handler: Mock,
    ) -> None:
        """Test that known event types without a registered handler route to on_unhandled"""
        sig_header = generate_header(payload=v1_billing_meter_payload)

        event_router.handle(v1_billing_meter_payload, sig_header)

        on_unhandled_handler.assert_called_once()

        call_args = on_unhandled_handler.call_args[0]
        event_notif = call_args[0]
        client = call_args[1]
        info = call_args[2]

        assert isinstance(
            event_notif, V1BillingMeterErrorReportTriggeredEventNotification
        )
        assert event_notif.type == "v1.billing.meter.error_report_triggered"
        assert isinstance(client, StripeClient)
        assert isinstance(info, UnhandledNotificationDetails)
        assert info.is_known_event_type is True

    def test_registered_event_does_not_call_on_unhandled(
        self,
        event_router: EventRouter,
        v1_billing_meter_payload: str,
        on_unhandled_handler: Mock,
    ) -> None:
        """Test that registered events don't trigger on_unhandled"""
        handler = Mock()
        event_router.on_V1BillingMeterErrorReportTriggeredEventNotification(
            handler
        )

        sig_header = generate_header(payload=v1_billing_meter_payload)
        event_router.handle(v1_billing_meter_payload, sig_header)

        handler.assert_called_once()
        on_unhandled_handler.assert_not_called()

    def test_handler_client_retains_configuration(
        self,
        http_client_mock: HTTPClientMock,
        on_unhandled_handler: Mock,
        v1_billing_meter_payload: str,
    ) -> None:
        """Test that the client passed to handlers retains all configuration except stripe_context"""
        api_key = "sk_test_custom_key"
        original_context = "original_context_xyz"

        client = StripeClient(
            api_key=api_key,
            stripe_context=StripeContext.parse(original_context),
            http_client=http_client_mock.get_mock_http_client(),
        )

        router = EventRouter(
            client=client,
            webhook_secret=DUMMY_WEBHOOK_SECRET,
            on_unhandled_handler=on_unhandled_handler,
        )

        received_api_key: Optional[str] = None
        received_context: Optional[StripeContext | str] = None

        def handler(
            event: V1BillingMeterErrorReportTriggeredEventNotification,
            client: StripeClient,
        ) -> None:
            nonlocal received_api_key, received_context
            received_api_key = client._requestor.api_key
            received_context = client._requestor._options.stripe_context

        router.on_V1BillingMeterErrorReportTriggeredEventNotification(handler)

        sig_header = generate_header(payload=v1_billing_meter_payload)
        router.handle(v1_billing_meter_payload, sig_header)

        assert received_api_key == api_key
        assert str(received_context) == "event_context_456"
        assert (
            str(client._requestor._options.stripe_context) == original_context
        )

    def test_on_unhandled_receives_correct_info_for_unknown(
        self,
        event_router: EventRouter,
        unknown_event_payload: str,
        on_unhandled_handler: Mock,
    ) -> None:
        """Test that on_unhandled receives correct UnhandledNotificationDetails for unknown events"""
        sig_header = generate_header(payload=unknown_event_payload)

        event_router.handle(unknown_event_payload, sig_header)

        on_unhandled_handler.assert_called_once()
        info = on_unhandled_handler.call_args[0][2]

        assert isinstance(info, UnhandledNotificationDetails)
        assert info.is_known_event_type is False

    def test_on_unhandled_receives_correct_info_for_known_unregistered(
        self,
        event_router: EventRouter,
        v1_billing_meter_payload: str,
        on_unhandled_handler: Mock,
    ) -> None:
        """Test that on_unhandled receives correct UnhandledNotificationDetails for known unregistered events"""
        sig_header = generate_header(payload=v1_billing_meter_payload)

        event_router.handle(v1_billing_meter_payload, sig_header)

        on_unhandled_handler.assert_called_once()
        info = on_unhandled_handler.call_args[0][2]

        assert isinstance(info, UnhandledNotificationDetails)
        assert info.is_known_event_type is True

    def test_validates_webhook_signature(
        self, event_router: EventRouter, v1_billing_meter_payload: str
    ) -> None:
        """Test that invalid webhook signatures are rejected"""
        from stripe._error import SignatureVerificationError

        with pytest.raises(SignatureVerificationError):
            event_router.handle(v1_billing_meter_payload, "invalid_signature")

    def test_registered_event_types_empty(
        self, event_router: EventRouter
    ) -> None:
        """Test that registered_event_types returns empty list when no handlers are registered"""
        assert event_router.registered_event_types == []

    def test_registered_event_types_single(
        self, event_router: EventRouter
    ) -> None:
        """Test that registered_event_types returns a single event type"""
        handler = Mock()
        event_router.on_V1BillingMeterErrorReportTriggeredEventNotification(
            handler
        )

        assert event_router.registered_event_types == [
            "v1.billing.meter.error_report_triggered"
        ]

    def test_registered_event_types_multiple_alphabetized(
        self, event_router: EventRouter
    ) -> None:
        """Test that registered_event_types returns multiple event types in alphabetical order"""
        handler = Mock()

        # Register in non-alphabetical order
        event_router.on_V2CoreAccountUpdatedEventNotification(handler)
        event_router.on_V1BillingMeterErrorReportTriggeredEventNotification(
            handler
        )
        event_router.on_V2CoreAccountCreatedEventNotification(handler)

        expected = [
            "v1.billing.meter.error_report_triggered",
            "v2.core.account.created",
            "v2.core.account.updated",
        ]

        assert event_router.registered_event_types == expected
