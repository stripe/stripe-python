# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class AlertHistoryEntry(StripeObject):
    """
    An alert history entry representing a state transition of a health alert.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.health.alert_history_entry"]] = (
        "v2.core.health.alert_history_entry"
    )

    class ApiError(StripeObject):
        class TopImpactedAccount(StripeObject):
            account: str
            """
            The account ID of the impacted connected account.
            """
            impacted_requests: int
            """
            The number of impacted requests.
            """
            impacted_requests_percentage: Optional[Decimal]
            """
            The percentage of impacted requests.
            """
            _field_encodings = {
                "impacted_requests_percentage": "decimal_string",
            }

        canonical_path: str
        """
        The canonical path.
        """
        error_code: Optional[str]
        """
        The error code.
        """
        http_method: Union[Literal["DELETE", "GET", "POST", "PUT"], str]
        """
        The HTTP method.
        """
        http_status: str
        """
        The HTTP status.
        """
        impacted_requests: int
        """
        The number of impacted requests.
        """
        impacted_requests_percentage: Optional[Decimal]
        """
        The percentage of impacted requests.
        """
        top_impacted_accounts: Optional[List[TopImpactedAccount]]
        """
        The top impacted connected accounts (only for platforms).
        """
        _inner_class_types = {"top_impacted_accounts": TopImpactedAccount}
        _field_encodings = {"impacted_requests_percentage": "decimal_string"}

    class ApiLatency(StripeObject):
        class TopImpactedAccount(StripeObject):
            account: str
            """
            The account ID of the impacted connected account.
            """
            impacted_requests: int
            """
            The number of impacted requests.
            """
            impacted_requests_percentage: Optional[Decimal]
            """
            The percentage of impacted requests.
            """
            _field_encodings = {
                "impacted_requests_percentage": "decimal_string",
            }

        canonical_path: str
        """
        The canonical path.
        """
        http_method: Union[Literal["DELETE", "GET", "POST", "PUT"], str]
        """
        The HTTP method.
        """
        http_status: str
        """
        The HTTP status.
        """
        impacted_requests: int
        """
        The number of impacted requests.
        """
        impacted_requests_percentage: Optional[Decimal]
        """
        The percentage of impacted requests.
        """
        top_impacted_accounts: Optional[List[TopImpactedAccount]]
        """
        The top impacted connected accounts (only for platforms).
        """
        _inner_class_types = {"top_impacted_accounts": TopImpactedAccount}
        _field_encodings = {"impacted_requests_percentage": "decimal_string"}

    class AuthorizationRateDrop(StripeObject):
        class Dimension(StripeObject):
            issuer: Optional[str]
            """
            Populated when type is issuer.
            """
            type: Literal["issuer"]
            """
            The type of the dimension. Determines which field in dimension_details is populated.
            """

        charge_type: Union[Literal["money_moving", "validation"], str]
        """
        The type of the charge.
        """
        current_percentage: Decimal
        """
        The current authorization rate percentage.
        """
        dimensions: Optional[List[Dimension]]
        """
        Dimensions that describe what subset of payments are impacted.
        """
        payment_method_type: Union[
            Literal[
                "acss_debit",
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "alma",
                "amazon_pay",
                "apple_pay",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "billie",
                "blik",
                "boleto",
                "card",
                "card_present",
                "cartes_bancaires",
                "cashapp",
                "crypto",
                "dummy_passthrough_card",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "interac_present",
                "kakao_pay",
                "klarna",
                "konbini",
                "kriya",
                "kr_card",
                "link",
                "mb_way",
                "mobilepay",
                "mondu",
                "multibanco",
                "naver_pay",
                "ng_bank",
                "ng_bank_transfer",
                "ng_card",
                "ng_market",
                "ng_ussd",
                "ng_wallet",
                "oxxo",
                "p24",
                "paper_check",
                "payco",
                "paynow",
                "paypal",
                "paypay",
                "payto",
                "pay_by_bank",
                "pix",
                "promptpay",
                "rechnung",
                "revolut_pay",
                "samsung_pay",
                "satispay",
                "scalapay",
                "sepa_debit",
                "sequra",
                "sofort",
                "sunbit",
                "swish",
                "twint",
                "upi",
                "us_bank_account",
                "vipps",
                "wechat_pay",
                "zip",
            ],
            str,
        ]
        """
        The type of the payment method.
        """
        previous_percentage: Decimal
        """
        The previous authorization rate percentage.
        """
        _inner_class_types = {"dimensions": Dimension}
        _field_encodings = {
            "current_percentage": "decimal_string",
            "previous_percentage": "decimal_string",
        }

    class ElementsError(StripeObject):
        element_type: Optional[
            Union[Literal["expressCheckout", "payment"], str]
        ]
        """
        The type of the element.
        """
        impacted_sessions: int
        """
        The number of impacted sessions.
        """

    class EventGenerationFailure(StripeObject):
        class RelatedObject(StripeObject):
            id: str
            """
            The ID of the related object (e.g., "pi_...").
            """
            type: str
            """
            The type of the related object (e.g., "payment_intent").
            """
            url: str
            """
            The API URL for the related object (e.g., "/v1/payment_intents/pi_...").
            """

        context: Optional[str]
        """
        The context the event should have been generated for. Only present when the account is a connected account.
        """
        event_type: str
        """
        The type of event that Stripe failed to generate.
        """
        related_object: RelatedObject
        """
        The related object details.
        """
        _inner_class_types = {"related_object": RelatedObject}

    class FraudRate(StripeObject):
        attack_type: Union[Literal["spike", "sustained_attack"], str]
        """
        Fraud attack type.
        """
        impacted_requests: int
        """
        The number of impacted requests which are detected.
        """
        realized_fraud_amount: Amount
        """
        Estimated aggregated amount for the impacted requests.
        """

    class InvoiceCountDropped(StripeObject):
        observed_count: Decimal
        """
        The observed number of invoices within the time window.
        """
        threshold_count: Decimal
        """
        The expected threshold number of invoices within the time window.
        """
        time_window: str
        """
        The size of the observation time window.
        """
        _field_encodings = {
            "observed_count": "decimal_string",
            "threshold_count": "decimal_string",
        }

    class IssuingAuthorizationRequestErrors(StripeObject):
        approved_amount: Optional[Amount]
        """
        Estimated aggregated amount for the approved requests.
        """
        approved_impacted_requests: Optional[int]
        """
        The number of approved requests which are impacted.
        """
        declined_amount: Optional[Amount]
        """
        Estimated aggregated amount for the declined requests.
        """
        declined_impacted_requests: Optional[int]
        """
        The number of declined requests which are impacted.
        """

    class IssuingAuthorizationRequestTimeout(StripeObject):
        approved_amount: Optional[Amount]
        """
        Estimated aggregated amount for the approved requests.
        """
        approved_impacted_requests: Optional[int]
        """
        The number of approved requests which are impacted.
        """
        declined_amount: Optional[Amount]
        """
        Estimated aggregated amount for the declined requests.
        """
        declined_impacted_requests: Optional[int]
        """
        The number of declined requests which are impacted.
        """

    class MeterEventSummariesDelayed(StripeObject):
        ingestion_method: Optional[Literal["import_sets"]]
        """
        The ingestion method.
        """

    class MetronomeNotificationLatency(StripeObject):
        pipeline: Union[
            Literal[
                "configuration_triggered",
                "high_cardinality_usage_triggered",
                "standard_usage_triggered",
                "time_triggered",
            ],
            str,
        ]
        """
        The impacted Metronome billing pipeline.
        """

    class PaymentMethodError(StripeObject):
        class TopImpactedAccount(StripeObject):
            account: str
            """
            The account ID of the impacted connected account.
            """
            impacted_requests: int
            """
            The number of impacted requests.
            """
            impacted_requests_percentage: Optional[Decimal]
            """
            The percentage of impacted requests.
            """
            _field_encodings = {
                "impacted_requests_percentage": "decimal_string",
            }

        error_code: Optional[str]
        """
        The returned error code.
        """
        impacted_requests: int
        """
        The number of impacted requests.
        """
        impacted_requests_percentage: Optional[Decimal]
        """
        The percentage of impacted requests.
        """
        payment_method_type: Union[
            Literal[
                "acss_debit",
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "alma",
                "amazon_pay",
                "apple_pay",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "billie",
                "blik",
                "boleto",
                "card",
                "card_present",
                "cartes_bancaires",
                "cashapp",
                "crypto",
                "dummy_passthrough_card",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "interac_present",
                "kakao_pay",
                "klarna",
                "konbini",
                "kriya",
                "kr_card",
                "link",
                "mb_way",
                "mobilepay",
                "mondu",
                "multibanco",
                "naver_pay",
                "ng_bank",
                "ng_bank_transfer",
                "ng_card",
                "ng_market",
                "ng_ussd",
                "ng_wallet",
                "oxxo",
                "p24",
                "paper_check",
                "payco",
                "paynow",
                "paypal",
                "paypay",
                "payto",
                "pay_by_bank",
                "pix",
                "promptpay",
                "rechnung",
                "revolut_pay",
                "samsung_pay",
                "satispay",
                "scalapay",
                "sepa_debit",
                "sequra",
                "sofort",
                "sunbit",
                "swish",
                "twint",
                "upi",
                "us_bank_account",
                "vipps",
                "wechat_pay",
                "zip",
            ],
            str,
        ]
        """
        The type of the payment method.
        """
        top_impacted_accounts: Optional[List[TopImpactedAccount]]
        """
        The top impacted connected accounts (only for platforms).
        """
        _inner_class_types = {"top_impacted_accounts": TopImpactedAccount}
        _field_encodings = {"impacted_requests_percentage": "decimal_string"}

    class SepaDebitDelayed(StripeObject):
        impacted_payments: int
        """
        The number of impacted payments.
        """
        impacted_payments_percentage: Decimal
        """
        The percentage of impacted payments.
        """
        _field_encodings = {"impacted_payments_percentage": "decimal_string"}

    class TrafficVolumeDrop(StripeObject):
        actual_traffic: int
        """
        The total volume of payment requests within the latest observation time window.
        """
        canonical_path: Optional[str]
        """
        The canonical path.
        """
        expected_traffic: Optional[int]
        """
        The expected volume of payment requests within the latest observation time window.
        """
        time_window: str
        """
        The size of the observation time window.
        """

    class WebhookLatency(StripeObject):
        impacted_requests: int
        """
        The number of impacted requests.
        """

    api_error: Optional[ApiError]
    """
    Populated when type is api_error.
    """
    api_latency: Optional[ApiLatency]
    """
    Populated when type is api_latency.
    """
    at: str
    """
    The time at which this transition occurred.
    """
    authorization_rate_drop: Optional[AuthorizationRateDrop]
    """
    Populated when type is authorization_rate_drop.
    """
    elements_error: Optional[ElementsError]
    """
    Populated when type is elements_error.
    """
    event_generation_failure: Optional[EventGenerationFailure]
    """
    Populated when type is event_generation_failure.
    """
    fraud_rate: Optional[FraudRate]
    """
    Populated when type is fraud_rate.
    """
    id: str
    """
    Unique identifier for the alert history entry.
    """
    invoice_count_dropped: Optional[InvoiceCountDropped]
    """
    Populated when type is invoice_count_dropped.
    """
    issuing_authorization_request_errors: Optional[
        IssuingAuthorizationRequestErrors
    ]
    """
    Populated when type is issuing_authorization_request_errors.
    """
    issuing_authorization_request_timeout: Optional[
        IssuingAuthorizationRequestTimeout
    ]
    """
    Populated when type is issuing_authorization_request_timeout.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    meter_event_summaries_delayed: Optional[MeterEventSummariesDelayed]
    """
    Populated when type is meter_event_summaries_delayed.
    """
    metronome_notification_latency: Optional[MetronomeNotificationLatency]
    """
    Populated when type is metronome_notification_latency.
    """
    object: Literal["v2.core.health.alert_history_entry"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    payment_method_error: Optional[PaymentMethodError]
    """
    Populated when type is payment_method_error.
    """
    sepa_debit_delayed: Optional[SepaDebitDelayed]
    """
    Populated when type is sepa_debit_delayed.
    """
    traffic_volume_drop: Optional[TrafficVolumeDrop]
    """
    Populated when type is traffic_volume_drop.
    """
    transition: Union[Literal["impact_updated", "opened", "resolved"], str]
    """
    The type of transition that occurred.
    """
    type: Union[
        Literal[
            "api_error",
            "api_latency",
            "authorization_rate_drop",
            "elements_error",
            "event_generation_failure",
            "fraud_rate",
            "invoice_count_dropped",
            "issuing_authorization_request_errors",
            "issuing_authorization_request_timeout",
            "meter_event_summaries_delayed",
            "metronome_notification_latency",
            "payment_method_error",
            "sepa_debit_delayed",
            "traffic_volume_drop",
            "webhook_latency",
        ],
        str,
    ]
    """
    The type of the alert. Determines which sub-hash field is populated.
    """
    webhook_latency: Optional[WebhookLatency]
    """
    Populated when type is webhook_latency.
    """
    _inner_class_types = {
        "api_error": ApiError,
        "api_latency": ApiLatency,
        "authorization_rate_drop": AuthorizationRateDrop,
        "elements_error": ElementsError,
        "event_generation_failure": EventGenerationFailure,
        "fraud_rate": FraudRate,
        "invoice_count_dropped": InvoiceCountDropped,
        "issuing_authorization_request_errors": IssuingAuthorizationRequestErrors,
        "issuing_authorization_request_timeout": IssuingAuthorizationRequestTimeout,
        "meter_event_summaries_delayed": MeterEventSummariesDelayed,
        "metronome_notification_latency": MetronomeNotificationLatency,
        "payment_method_error": PaymentMethodError,
        "sepa_debit_delayed": SepaDebitDelayed,
        "traffic_volume_drop": TrafficVolumeDrop,
        "webhook_latency": WebhookLatency,
    }
