# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._deletable_api_resource import DeletableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe._test_helpers import APIResourceTestHelpers
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, List, Optional, Union, cast, overload
from typing_extensions import Literal, Type, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._account import Account
    from stripe._bank_account import BankAccount
    from stripe._card import Card
    from stripe._charge import Charge
    from stripe._payment_intent import PaymentIntent
    from stripe._payment_method import PaymentMethod
    from stripe._refund import Refund
    from stripe._setup_intent import SetupIntent
    from stripe._source import Source
    from stripe.params.terminal._reader_cancel_action_params import (
        ReaderCancelActionParams,
    )
    from stripe.params.terminal._reader_collect_inputs_params import (
        ReaderCollectInputsParams,
    )
    from stripe.params.terminal._reader_collect_payment_method_params import (
        ReaderCollectPaymentMethodParams,
    )
    from stripe.params.terminal._reader_confirm_payment_intent_params import (
        ReaderConfirmPaymentIntentParams,
    )
    from stripe.params.terminal._reader_create_params import ReaderCreateParams
    from stripe.params.terminal._reader_delete_params import ReaderDeleteParams
    from stripe.params.terminal._reader_list_params import ReaderListParams
    from stripe.params.terminal._reader_modify_params import ReaderModifyParams
    from stripe.params.terminal._reader_present_payment_method_params import (
        ReaderPresentPaymentMethodParams,
    )
    from stripe.params.terminal._reader_process_payment_intent_params import (
        ReaderProcessPaymentIntentParams,
    )
    from stripe.params.terminal._reader_process_setup_intent_params import (
        ReaderProcessSetupIntentParams,
    )
    from stripe.params.terminal._reader_refund_payment_params import (
        ReaderRefundPaymentParams,
    )
    from stripe.params.terminal._reader_retrieve_params import (
        ReaderRetrieveParams,
    )
    from stripe.params.terminal._reader_set_reader_display_params import (
        ReaderSetReaderDisplayParams,
    )
    from stripe.params.terminal._reader_succeed_input_collection_params import (
        ReaderSucceedInputCollectionParams,
    )
    from stripe.params.terminal._reader_timeout_input_collection_params import (
        ReaderTimeoutInputCollectionParams,
    )
    from stripe.terminal._location import Location


class Reader(
    CreateableAPIResource["Reader"],
    DeletableAPIResource["Reader"],
    ListableAPIResource["Reader"],
    UpdateableAPIResource["Reader"],
):
    """
    A Reader represents a physical device for accepting payment details.

    Related guide: [Connecting to a reader](https://docs.stripe.com/terminal/payments/connect-reader)
    """

    OBJECT_NAME: ClassVar[Literal["terminal.reader"]] = "terminal.reader"

    class Action(StripeObject):
        class ApiError(StripeObject):
            advice_code: Optional[str]
            """
            For card errors resulting from a card issuer decline, a short string indicating [how to proceed with an error](https://docs.stripe.com/declines#retrying-issuer-declines) if they provide one.
            """
            charge: Optional[str]
            """
            For card errors, the ID of the failed charge.
            """
            code: Optional[
                Literal[
                    "account_closed",
                    "account_country_invalid_address",
                    "account_error_country_change_requires_additional_steps",
                    "account_information_mismatch",
                    "account_invalid",
                    "account_number_invalid",
                    "account_token_required_for_v2_account",
                    "acss_debit_session_incomplete",
                    "action_blocked",
                    "alipay_upgrade_required",
                    "amount_too_large",
                    "amount_too_small",
                    "api_key_expired",
                    "application_fees_not_allowed",
                    "approval_required",
                    "authentication_required",
                    "balance_insufficient",
                    "balance_invalid_parameter",
                    "bank_account_bad_routing_numbers",
                    "bank_account_declined",
                    "bank_account_exists",
                    "bank_account_restricted",
                    "bank_account_unusable",
                    "bank_account_unverified",
                    "bank_account_verification_failed",
                    "billing_invalid_mandate",
                    "bitcoin_upgrade_required",
                    "capture_charge_authorization_expired",
                    "capture_unauthorized_payment",
                    "card_decline_rate_limit_exceeded",
                    "card_declined",
                    "cardholder_phone_number_required",
                    "charge_already_captured",
                    "charge_already_refunded",
                    "charge_disputed",
                    "charge_exceeds_source_limit",
                    "charge_exceeds_transaction_limit",
                    "charge_expired_for_capture",
                    "charge_invalid_parameter",
                    "charge_not_refundable",
                    "clearing_code_unsupported",
                    "country_code_invalid",
                    "country_unsupported",
                    "coupon_expired",
                    "customer_max_payment_methods",
                    "customer_max_subscriptions",
                    "customer_session_expired",
                    "customer_tax_location_invalid",
                    "debit_not_authorized",
                    "email_invalid",
                    "expired_card",
                    "financial_connections_account_inactive",
                    "financial_connections_account_pending_account_numbers",
                    "financial_connections_account_unavailable_account_numbers",
                    "financial_connections_no_successful_transaction_refresh",
                    "forwarding_api_inactive",
                    "forwarding_api_invalid_parameter",
                    "forwarding_api_retryable_upstream_error",
                    "forwarding_api_upstream_connection_error",
                    "forwarding_api_upstream_connection_timeout",
                    "forwarding_api_upstream_error",
                    "idempotency_key_in_use",
                    "incorrect_address",
                    "incorrect_cvc",
                    "incorrect_number",
                    "incorrect_zip",
                    "india_recurring_payment_mandate_canceled",
                    "instant_payouts_config_disabled",
                    "instant_payouts_currency_disabled",
                    "instant_payouts_limit_exceeded",
                    "instant_payouts_unsupported",
                    "insufficient_funds",
                    "intent_invalid_state",
                    "intent_verification_method_missing",
                    "invalid_card_type",
                    "invalid_characters",
                    "invalid_charge_amount",
                    "invalid_cvc",
                    "invalid_expiry_month",
                    "invalid_expiry_year",
                    "invalid_mandate_reference_prefix_format",
                    "invalid_number",
                    "invalid_source_usage",
                    "invalid_tax_location",
                    "invoice_no_customer_line_items",
                    "invoice_no_payment_method_types",
                    "invoice_no_subscription_line_items",
                    "invoice_not_editable",
                    "invoice_on_behalf_of_not_editable",
                    "invoice_payment_intent_requires_action",
                    "invoice_upcoming_none",
                    "livemode_mismatch",
                    "lock_timeout",
                    "missing",
                    "no_account",
                    "not_allowed_on_standard_account",
                    "out_of_inventory",
                    "ownership_declaration_not_allowed",
                    "parameter_invalid_empty",
                    "parameter_invalid_integer",
                    "parameter_invalid_string_blank",
                    "parameter_invalid_string_empty",
                    "parameter_missing",
                    "parameter_unknown",
                    "parameters_exclusive",
                    "payment_intent_action_required",
                    "payment_intent_authentication_failure",
                    "payment_intent_incompatible_payment_method",
                    "payment_intent_invalid_parameter",
                    "payment_intent_konbini_rejected_confirmation_number",
                    "payment_intent_mandate_invalid",
                    "payment_intent_payment_attempt_expired",
                    "payment_intent_payment_attempt_failed",
                    "payment_intent_rate_limit_exceeded",
                    "payment_intent_unexpected_state",
                    "payment_method_bank_account_already_verified",
                    "payment_method_bank_account_blocked",
                    "payment_method_billing_details_address_missing",
                    "payment_method_configuration_failures",
                    "payment_method_currency_mismatch",
                    "payment_method_customer_decline",
                    "payment_method_invalid_parameter",
                    "payment_method_invalid_parameter_testmode",
                    "payment_method_microdeposit_failed",
                    "payment_method_microdeposit_processing_error",
                    "payment_method_microdeposit_verification_amounts_invalid",
                    "payment_method_microdeposit_verification_amounts_mismatch",
                    "payment_method_microdeposit_verification_attempts_exceeded",
                    "payment_method_microdeposit_verification_descriptor_code_mismatch",
                    "payment_method_microdeposit_verification_timeout",
                    "payment_method_not_available",
                    "payment_method_provider_decline",
                    "payment_method_provider_timeout",
                    "payment_method_unactivated",
                    "payment_method_unexpected_state",
                    "payment_method_unsupported_type",
                    "payout_reconciliation_not_ready",
                    "payouts_limit_exceeded",
                    "payouts_not_allowed",
                    "platform_account_required",
                    "platform_api_key_expired",
                    "postal_code_invalid",
                    "processing_error",
                    "product_inactive",
                    "progressive_onboarding_limit_exceeded",
                    "rate_limit",
                    "refer_to_customer",
                    "refund_disputed_payment",
                    "request_blocked",
                    "resource_already_exists",
                    "resource_missing",
                    "return_intent_already_processed",
                    "routing_number_invalid",
                    "secret_key_required",
                    "sepa_unsupported_account",
                    "service_period_coupon_with_metered_tiered_item_unsupported",
                    "setup_attempt_failed",
                    "setup_intent_authentication_failure",
                    "setup_intent_invalid_parameter",
                    "setup_intent_mandate_invalid",
                    "setup_intent_mobile_wallet_unsupported",
                    "setup_intent_setup_attempt_expired",
                    "setup_intent_unexpected_state",
                    "shipping_address_invalid",
                    "shipping_calculation_failed",
                    "siret_invalid",
                    "sku_inactive",
                    "state_unsupported",
                    "status_transition_invalid",
                    "storer_capability_missing",
                    "storer_capability_not_active",
                    "stripe_tax_inactive",
                    "tax_id_invalid",
                    "tax_id_prohibited",
                    "taxes_calculation_failed",
                    "terminal_location_country_unsupported",
                    "terminal_reader_busy",
                    "terminal_reader_hardware_fault",
                    "terminal_reader_invalid_location_for_activation",
                    "terminal_reader_invalid_location_for_payment",
                    "terminal_reader_offline",
                    "terminal_reader_timeout",
                    "testmode_charges_only",
                    "tls_version_unsupported",
                    "token_already_used",
                    "token_card_network_invalid",
                    "token_in_use",
                    "transfer_source_balance_parameters_mismatch",
                    "transfers_not_allowed",
                    "url_invalid",
                ]
            ]
            """
            For some errors that could be handled programmatically, a short string indicating the [error code](https://docs.stripe.com/error-codes) reported.
            """
            decline_code: Optional[str]
            """
            For card errors resulting from a card issuer decline, a short string indicating the [card issuer's reason for the decline](https://docs.stripe.com/declines#issuer-declines) if they provide one.
            """
            doc_url: Optional[str]
            """
            A URL to more information about the [error code](https://docs.stripe.com/error-codes) reported.
            """
            message: Optional[str]
            """
            A human-readable message providing more details about the error. For card errors, these messages can be shown to your users.
            """
            network_advice_code: Optional[str]
            """
            For card errors resulting from a card issuer decline, a 2 digit code which indicates the advice given to merchant by the card network on how to proceed with an error.
            """
            network_decline_code: Optional[str]
            """
            For payments declined by the network, an alphanumeric code which indicates the reason the payment failed.
            """
            param: Optional[str]
            """
            If the error is parameter-specific, the parameter related to the error. For example, you can use this to display a message near the correct form field.
            """
            payment_intent: Optional["PaymentIntent"]
            """
            A PaymentIntent guides you through the process of collecting a payment from your customer.
            We recommend that you create exactly one PaymentIntent for each order or
            customer session in your system. You can reference the PaymentIntent later to
            see the history of payment attempts for a particular session.

            A PaymentIntent transitions through
            [multiple statuses](https://docs.stripe.com/payments/paymentintents/lifecycle)
            throughout its lifetime as it interfaces with Stripe.js to perform
            authentication flows and ultimately creates at most one successful charge.

            Related guide: [Payment Intents API](https://docs.stripe.com/payments/payment-intents)
            """
            payment_method: Optional["PaymentMethod"]
            """
            PaymentMethod objects represent your customer's payment instruments.
            You can use them with [PaymentIntents](https://docs.stripe.com/payments/payment-intents) to collect payments or save them to
            Customer objects to store instrument details for future payments.

            Related guides: [Payment Methods](https://docs.stripe.com/payments/payment-methods) and [More Payment Scenarios](https://docs.stripe.com/payments/more-payment-scenarios).
            """
            payment_method_type: Optional[str]
            """
            If the error is specific to the type of payment method, the payment method type that had a problem. This field is only populated for invoice-related errors.
            """
            request_log_url: Optional[str]
            """
            A URL to the request log entry in your dashboard.
            """
            setup_intent: Optional["SetupIntent"]
            """
            A SetupIntent guides you through the process of setting up and saving a customer's payment credentials for future payments.
            For example, you can use a SetupIntent to set up and save your customer's card without immediately collecting a payment.
            Later, you can use [PaymentIntents](https://api.stripe.com#payment_intents) to drive the payment flow.

            Create a SetupIntent when you're ready to collect your customer's payment credentials.
            Don't maintain long-lived, unconfirmed SetupIntents because they might not be valid.
            The SetupIntent transitions through multiple [statuses](https://docs.stripe.com/payments/intents#intent-statuses) as it guides
            you through the setup process.

            Successful SetupIntents result in payment credentials that are optimized for future payments.
            For example, cardholders in [certain regions](https://stripe.com/guides/strong-customer-authentication) might need to be run through
            [Strong Customer Authentication](https://docs.stripe.com/strong-customer-authentication) during payment method collection
            to streamline later [off-session payments](https://docs.stripe.com/payments/setup-intents).
            If you use the SetupIntent with a [Customer](https://api.stripe.com#setup_intent_object-customer),
            it automatically attaches the resulting payment method to that Customer after successful setup.
            We recommend using SetupIntents or [setup_future_usage](https://api.stripe.com#payment_intent_object-setup_future_usage) on
            PaymentIntents to save payment methods to prevent saving invalid or unoptimized payment methods.

            By using SetupIntents, you can reduce friction for your customers, even as regulations change over time.

            Related guide: [Setup Intents API](https://docs.stripe.com/payments/setup-intents)
            """
            source: Optional[Union["Account", "BankAccount", "Card", "Source"]]
            type: Literal[
                "api_error",
                "card_error",
                "idempotency_error",
                "invalid_request_error",
            ]
            """
            The type of error returned. One of `api_error`, `card_error`, `idempotency_error`, or `invalid_request_error`
            """

        class CollectInputs(StripeObject):
            class Input(StripeObject):
                class CustomText(StripeObject):
                    description: Optional[str]
                    """
                    Customize the default description for this input
                    """
                    skip_button: Optional[str]
                    """
                    Customize the default label for this input's skip button
                    """
                    submit_button: Optional[str]
                    """
                    Customize the default label for this input's submit button
                    """
                    title: Optional[str]
                    """
                    Customize the default title for this input
                    """

                class Email(StripeObject):
                    value: Optional[str]
                    """
                    The collected email address
                    """

                class Numeric(StripeObject):
                    value: Optional[str]
                    """
                    The collected number
                    """

                class Phone(StripeObject):
                    value: Optional[str]
                    """
                    The collected phone number
                    """

                class Selection(StripeObject):
                    class Choice(StripeObject):
                        id: Optional[str]
                        """
                        The identifier for the selected choice. Maximum 50 characters.
                        """
                        style: Optional[Literal["primary", "secondary"]]
                        """
                        The button style for the choice. Can be `primary` or `secondary`.
                        """
                        text: str
                        """
                        The text to be selected. Maximum 30 characters.
                        """

                    choices: List[Choice]
                    """
                    List of possible choices to be selected
                    """
                    id: Optional[str]
                    """
                    The id of the selected choice
                    """
                    text: Optional[str]
                    """
                    The text of the selected choice
                    """
                    _inner_class_types = {"choices": Choice}

                class Signature(StripeObject):
                    value: Optional[str]
                    """
                    The File ID of a collected signature image
                    """

                class Text(StripeObject):
                    value: Optional[str]
                    """
                    The collected text value
                    """

                class Toggle(StripeObject):
                    default_value: Optional[Literal["disabled", "enabled"]]
                    """
                    The toggle's default value. Can be `enabled` or `disabled`.
                    """
                    description: Optional[str]
                    """
                    The toggle's description text. Maximum 50 characters.
                    """
                    title: Optional[str]
                    """
                    The toggle's title text. Maximum 50 characters.
                    """
                    value: Optional[Literal["disabled", "enabled"]]
                    """
                    The toggle's collected value. Can be `enabled` or `disabled`.
                    """

                custom_text: Optional[CustomText]
                """
                Default text of input being collected.
                """
                email: Optional[Email]
                """
                Information about a email being collected using a reader
                """
                numeric: Optional[Numeric]
                """
                Information about a number being collected using a reader
                """
                phone: Optional[Phone]
                """
                Information about a phone number being collected using a reader
                """
                required: Optional[bool]
                """
                Indicate that this input is required, disabling the skip button.
                """
                selection: Optional[Selection]
                """
                Information about a selection being collected using a reader
                """
                signature: Optional[Signature]
                """
                Information about a signature being collected using a reader
                """
                skipped: Optional[bool]
                """
                Indicate that this input was skipped by the user.
                """
                text: Optional[Text]
                """
                Information about text being collected using a reader
                """
                toggles: Optional[List[Toggle]]
                """
                List of toggles being collected. Values are present if collection is complete.
                """
                type: Literal[
                    "email",
                    "numeric",
                    "phone",
                    "selection",
                    "signature",
                    "text",
                ]
                """
                Type of input being collected.
                """
                _inner_class_types = {
                    "custom_text": CustomText,
                    "email": Email,
                    "numeric": Numeric,
                    "phone": Phone,
                    "selection": Selection,
                    "signature": Signature,
                    "text": Text,
                    "toggles": Toggle,
                }

            inputs: List[Input]
            """
            List of inputs to be collected.
            """
            metadata: Optional[UntypedStripeObject[str]]
            """
            Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
            """
            _inner_class_types = {"inputs": Input}

        class CollectPaymentMethod(StripeObject):
            class CollectConfig(StripeObject):
                class Tipping(StripeObject):
                    amount_eligible: Optional[int]
                    """
                    Amount used to calculate tip suggestions on tipping selection screen for this transaction. Must be a positive integer in the smallest currency unit (e.g., 100 cents to represent $1.00 or 100 to represent ¥100, a zero-decimal currency).
                    """

                enable_customer_cancellation: Optional[bool]
                """
                Enable customer-initiated cancellation when processing this payment.
                """
                skip_tipping: Optional[bool]
                """
                Override showing a tipping selection screen on this transaction.
                """
                tipping: Optional[Tipping]
                """
                Represents a per-transaction tipping configuration
                """
                _inner_class_types = {"tipping": Tipping}

            collect_config: Optional[CollectConfig]
            """
            Represents a per-transaction override of a reader configuration
            """
            payment_intent: ExpandableField["PaymentIntent"]
            """
            Most recent PaymentIntent processed by the reader.
            """
            payment_method: Optional["PaymentMethod"]
            """
            PaymentMethod objects represent your customer's payment instruments.
            You can use them with [PaymentIntents](https://docs.stripe.com/payments/payment-intents) to collect payments or save them to
            Customer objects to store instrument details for future payments.

            Related guides: [Payment Methods](https://docs.stripe.com/payments/payment-methods) and [More Payment Scenarios](https://docs.stripe.com/payments/more-payment-scenarios).
            """
            _inner_class_types = {"collect_config": CollectConfig}

        class ConfirmPaymentIntent(StripeObject):
            class ConfirmConfig(StripeObject):
                return_url: Optional[str]
                """
                If the customer doesn't abandon authenticating the payment, they're redirected to this URL after completion.
                """

            confirm_config: Optional[ConfirmConfig]
            """
            Represents a per-transaction override of a reader configuration
            """
            payment_intent: ExpandableField["PaymentIntent"]
            """
            Most recent PaymentIntent processed by the reader.
            """
            _inner_class_types = {"confirm_config": ConfirmConfig}

        class PrintContent(StripeObject):
            class Image(StripeObject):
                created_at: int
                """
                Creation time of the object (in seconds since the Unix epoch).
                """
                filename: str
                """
                The original name of the uploaded file (e.g. `receipt.png`).
                """
                size: int
                """
                The size (in bytes) of the uploaded file.
                """
                type: str
                """
                The format of the uploaded file.
                """

            image: Optional[Image]
            """
            Metadata of an uploaded file
            """
            type: Literal["image"]
            """
            The type of content to print. Currently supports `image`.
            """
            _inner_class_types = {"image": Image}

        class ProcessPaymentIntent(StripeObject):
            class ProcessConfig(StripeObject):
                class Tipping(StripeObject):
                    amount_eligible: Optional[int]
                    """
                    Amount used to calculate tip suggestions on tipping selection screen for this transaction. Must be a positive integer in the smallest currency unit (e.g., 100 cents to represent $1.00 or 100 to represent ¥100, a zero-decimal currency).
                    """

                enable_customer_cancellation: Optional[bool]
                """
                Enable customer-initiated cancellation when processing this payment.
                """
                return_url: Optional[str]
                """
                If the customer doesn't abandon authenticating the payment, they're redirected to this URL after completion.
                """
                skip_tipping: Optional[bool]
                """
                Override showing a tipping selection screen on this transaction.
                """
                tipping: Optional[Tipping]
                """
                Represents a per-transaction tipping configuration
                """
                _inner_class_types = {"tipping": Tipping}

            payment_intent: ExpandableField["PaymentIntent"]
            """
            Most recent PaymentIntent processed by the reader.
            """
            process_config: Optional[ProcessConfig]
            """
            Represents a per-transaction override of a reader configuration
            """
            _inner_class_types = {"process_config": ProcessConfig}

        class ProcessSetupIntent(StripeObject):
            class ProcessConfig(StripeObject):
                enable_customer_cancellation: Optional[bool]
                """
                Enable customer-initiated cancellation when processing this SetupIntent.
                """

            generated_card: Optional[str]
            """
            ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod.
            """
            process_config: Optional[ProcessConfig]
            """
            Represents a per-setup override of a reader configuration
            """
            setup_intent: ExpandableField["SetupIntent"]
            """
            Most recent SetupIntent processed by the reader.
            """
            _inner_class_types = {"process_config": ProcessConfig}

        class RefundPayment(StripeObject):
            class RefundPaymentConfig(StripeObject):
                enable_customer_cancellation: Optional[bool]
                """
                Enable customer-initiated cancellation when refunding this payment.
                """

            amount: Optional[int]
            """
            The amount being refunded.
            """
            charge: Optional[ExpandableField["Charge"]]
            """
            Charge that is being refunded.
            """
            metadata: Optional[UntypedStripeObject[str]]
            """
            Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
            """
            payment_intent: Optional[ExpandableField["PaymentIntent"]]
            """
            Payment intent that is being refunded.
            """
            reason: Optional[
                Literal["duplicate", "fraudulent", "requested_by_customer"]
            ]
            """
            The reason for the refund.
            """
            refund: Optional[ExpandableField["Refund"]]
            """
            Unique identifier for the refund object.
            """
            refund_application_fee: Optional[bool]
            """
            Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.
            """
            refund_payment_config: Optional[RefundPaymentConfig]
            """
            Represents a per-transaction override of a reader configuration
            """
            reverse_transfer: Optional[bool]
            """
            Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge.
            """
            _inner_class_types = {"refund_payment_config": RefundPaymentConfig}

        class SetReaderDisplay(StripeObject):
            class Cart(StripeObject):
                class LineItem(StripeObject):
                    amount: int
                    """
                    The amount of the line item. A positive integer in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
                    """
                    description: str
                    """
                    Description of the line item.
                    """
                    quantity: int
                    """
                    The quantity of the line item.
                    """

                currency: str
                """
                Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
                """
                line_items: List[LineItem]
                """
                List of line items in the cart.
                """
                tax: Optional[int]
                """
                Tax amount for the entire cart. A positive integer in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
                """
                total: int
                """
                Total amount for the entire cart, including tax. A positive integer in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
                """
                _inner_class_types = {"line_items": LineItem}

            cart: Optional[Cart]
            """
            Cart object to be displayed by the reader, including line items, amounts, and currency.
            """
            type: Literal["cart"]
            """
            Type of information to be displayed by the reader. Only `cart` is currently supported.
            """
            _inner_class_types = {"cart": Cart}

        api_error: Optional[ApiError]
        """
        The reader action failed due to an [API error](https://docs.stripe.com/api/errors). Only present when `status` is `failed` and the underlying failure was an API error. Avoid parsing the `message` field for programmatic logic; use `type` or `code` instead. The `message` field is for display to humans only and may be updated at anytime. Requires [reader version](https://docs.stripe.com/terminal/readers/stripe-reader-s700-s710#reader-software-version) 2.42 or later. Readers on older versions always return null.
        """
        collect_inputs: Optional[CollectInputs]
        """
        Represents a reader action to collect customer inputs
        """
        collect_payment_method: Optional[CollectPaymentMethod]
        """
        Represents a reader action to collect a payment method
        """
        confirm_payment_intent: Optional[ConfirmPaymentIntent]
        """
        Represents a reader action to confirm a payment
        """
        failure_code: Optional[str]
        """
        Failure code, only set if status is `failed`.
        """
        failure_message: Optional[str]
        """
        Detailed failure message, only set if status is `failed`.
        """
        print_content: Optional[PrintContent]
        """
        Represents a reader action to print content
        """
        process_payment_intent: Optional[ProcessPaymentIntent]
        """
        Represents a reader action to process a payment intent
        """
        process_setup_intent: Optional[ProcessSetupIntent]
        """
        Represents a reader action to process a setup intent
        """
        refund_payment: Optional[RefundPayment]
        """
        Represents a reader action to refund a payment
        """
        set_reader_display: Optional[SetReaderDisplay]
        """
        Represents a reader action to set the reader display
        """
        status: Literal["failed", "in_progress", "succeeded"]
        """
        Status of the action performed by the reader.
        """
        type: Literal[
            "collect_inputs",
            "collect_payment_method",
            "confirm_payment_intent",
            "print_content",
            "process_payment_intent",
            "process_setup_intent",
            "refund_payment",
            "set_reader_display",
        ]
        """
        Type of action performed by the reader.
        """
        _inner_class_types = {
            "api_error": ApiError,
            "collect_inputs": CollectInputs,
            "collect_payment_method": CollectPaymentMethod,
            "confirm_payment_intent": ConfirmPaymentIntent,
            "print_content": PrintContent,
            "process_payment_intent": ProcessPaymentIntent,
            "process_setup_intent": ProcessSetupIntent,
            "refund_payment": RefundPayment,
            "set_reader_display": SetReaderDisplay,
        }

    action: Optional[Action]
    """
    The most recent action performed by the reader.
    """
    deleted: Optional[Literal[True]]
    """
    Always true for a deleted object
    """
    device_sw_version: Optional[str]
    """
    The current software version of the reader.
    """
    device_type: Literal[
        "bbpos_chipper2x",
        "bbpos_wisepad3",
        "bbpos_wisepos_e",
        "mobile_phone_reader",
        "simulated_stripe_s700",
        "simulated_stripe_s710",
        "simulated_verifone_m425",
        "simulated_verifone_p630",
        "simulated_verifone_ux700",
        "simulated_verifone_v660p",
        "simulated_wisepos_e",
        "stripe_m2",
        "stripe_s700",
        "stripe_s710",
        "verifone_P400",
        "verifone_m425",
        "verifone_p630",
        "verifone_ux700",
        "verifone_v660p",
    ]
    """
    Device type of the reader.
    """
    id: str
    """
    Unique identifier for the object.
    """
    ip_address: Optional[str]
    """
    The local IP address of the reader.
    """
    label: str
    """
    Custom label given to the reader for easier identification.
    """
    last_seen_at: Optional[int]
    """
    The last time this reader reported to Stripe backend. Timestamp is measured in milliseconds since the Unix epoch. Unlike most other Stripe timestamp fields which use seconds, this field uses milliseconds.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    location: Optional[ExpandableField["Location"]]
    """
    The location identifier of the reader.
    """
    metadata: UntypedStripeObject[str]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["terminal.reader"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    serial_number: str
    """
    Serial number of the reader.
    """
    status: Optional[Literal["offline", "online"]]
    """
    The networking status of the reader. We do not recommend using this field in flows that may block taking payments.
    """

    @classmethod
    def _cls_cancel_action(
        cls, reader: str, **params: Unpack["ReaderCancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action. See [Programmatic Cancellation](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#programmatic-cancellation) for more details.
        """
        return cast(
            "Reader",
            cls._static_request(
                "post",
                "/v1/terminal/readers/{reader}/cancel_action".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def cancel_action(
        reader: str, **params: Unpack["ReaderCancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action. See [Programmatic Cancellation](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#programmatic-cancellation) for more details.
        """
        ...

    @overload
    def cancel_action(
        self, **params: Unpack["ReaderCancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action. See [Programmatic Cancellation](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#programmatic-cancellation) for more details.
        """
        ...

    @class_method_variant("_cls_cancel_action")
    def cancel_action(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderCancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action. See [Programmatic Cancellation](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#programmatic-cancellation) for more details.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/cancel_action".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_cancel_action_async(
        cls, reader: str, **params: Unpack["ReaderCancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action. See [Programmatic Cancellation](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#programmatic-cancellation) for more details.
        """
        return cast(
            "Reader",
            await cls._static_request_async(
                "post",
                "/v1/terminal/readers/{reader}/cancel_action".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def cancel_action_async(
        reader: str, **params: Unpack["ReaderCancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action. See [Programmatic Cancellation](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#programmatic-cancellation) for more details.
        """
        ...

    @overload
    async def cancel_action_async(
        self, **params: Unpack["ReaderCancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action. See [Programmatic Cancellation](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#programmatic-cancellation) for more details.
        """
        ...

    @class_method_variant("_cls_cancel_action_async")
    async def cancel_action_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderCancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action. See [Programmatic Cancellation](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven#programmatic-cancellation) for more details.
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/cancel_action".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_collect_inputs(
        cls, reader: str, **params: Unpack["ReaderCollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an [input collection flow](https://docs.stripe.com/docs/terminal/features/collect-inputs) on a Reader to display input forms and collect information from your customers.
        """
        return cast(
            "Reader",
            cls._static_request(
                "post",
                "/v1/terminal/readers/{reader}/collect_inputs".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def collect_inputs(
        reader: str, **params: Unpack["ReaderCollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an [input collection flow](https://docs.stripe.com/docs/terminal/features/collect-inputs) on a Reader to display input forms and collect information from your customers.
        """
        ...

    @overload
    def collect_inputs(
        self, **params: Unpack["ReaderCollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an [input collection flow](https://docs.stripe.com/docs/terminal/features/collect-inputs) on a Reader to display input forms and collect information from your customers.
        """
        ...

    @class_method_variant("_cls_collect_inputs")
    def collect_inputs(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderCollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an [input collection flow](https://docs.stripe.com/docs/terminal/features/collect-inputs) on a Reader to display input forms and collect information from your customers.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/collect_inputs".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_collect_inputs_async(
        cls, reader: str, **params: Unpack["ReaderCollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an [input collection flow](https://docs.stripe.com/docs/terminal/features/collect-inputs) on a Reader to display input forms and collect information from your customers.
        """
        return cast(
            "Reader",
            await cls._static_request_async(
                "post",
                "/v1/terminal/readers/{reader}/collect_inputs".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def collect_inputs_async(
        reader: str, **params: Unpack["ReaderCollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an [input collection flow](https://docs.stripe.com/docs/terminal/features/collect-inputs) on a Reader to display input forms and collect information from your customers.
        """
        ...

    @overload
    async def collect_inputs_async(
        self, **params: Unpack["ReaderCollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an [input collection flow](https://docs.stripe.com/docs/terminal/features/collect-inputs) on a Reader to display input forms and collect information from your customers.
        """
        ...

    @class_method_variant("_cls_collect_inputs_async")
    async def collect_inputs_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderCollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an [input collection flow](https://docs.stripe.com/docs/terminal/features/collect-inputs) on a Reader to display input forms and collect information from your customers.
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/collect_inputs".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_collect_payment_method(
        cls, reader: str, **params: Unpack["ReaderCollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation. See [Collecting a Payment method](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#collect-a-paymentmethod) for more details.
        """
        return cast(
            "Reader",
            cls._static_request(
                "post",
                "/v1/terminal/readers/{reader}/collect_payment_method".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def collect_payment_method(
        reader: str, **params: Unpack["ReaderCollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation. See [Collecting a Payment method](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#collect-a-paymentmethod) for more details.
        """
        ...

    @overload
    def collect_payment_method(
        self, **params: Unpack["ReaderCollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation. See [Collecting a Payment method](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#collect-a-paymentmethod) for more details.
        """
        ...

    @class_method_variant("_cls_collect_payment_method")
    def collect_payment_method(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderCollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation. See [Collecting a Payment method](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#collect-a-paymentmethod) for more details.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/collect_payment_method".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_collect_payment_method_async(
        cls, reader: str, **params: Unpack["ReaderCollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation. See [Collecting a Payment method](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#collect-a-paymentmethod) for more details.
        """
        return cast(
            "Reader",
            await cls._static_request_async(
                "post",
                "/v1/terminal/readers/{reader}/collect_payment_method".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def collect_payment_method_async(
        reader: str, **params: Unpack["ReaderCollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation. See [Collecting a Payment method](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#collect-a-paymentmethod) for more details.
        """
        ...

    @overload
    async def collect_payment_method_async(
        self, **params: Unpack["ReaderCollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation. See [Collecting a Payment method](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#collect-a-paymentmethod) for more details.
        """
        ...

    @class_method_variant("_cls_collect_payment_method_async")
    async def collect_payment_method_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderCollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation. See [Collecting a Payment method](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#collect-a-paymentmethod) for more details.
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/collect_payment_method".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_confirm_payment_intent(
        cls, reader: str, **params: Unpack["ReaderConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader. See [Confirming a Payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#confirm-the-paymentintent) for more details.
        """
        return cast(
            "Reader",
            cls._static_request(
                "post",
                "/v1/terminal/readers/{reader}/confirm_payment_intent".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def confirm_payment_intent(
        reader: str, **params: Unpack["ReaderConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader. See [Confirming a Payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#confirm-the-paymentintent) for more details.
        """
        ...

    @overload
    def confirm_payment_intent(
        self, **params: Unpack["ReaderConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader. See [Confirming a Payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#confirm-the-paymentintent) for more details.
        """
        ...

    @class_method_variant("_cls_confirm_payment_intent")
    def confirm_payment_intent(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader. See [Confirming a Payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#confirm-the-paymentintent) for more details.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/confirm_payment_intent".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_confirm_payment_intent_async(
        cls, reader: str, **params: Unpack["ReaderConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader. See [Confirming a Payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#confirm-the-paymentintent) for more details.
        """
        return cast(
            "Reader",
            await cls._static_request_async(
                "post",
                "/v1/terminal/readers/{reader}/confirm_payment_intent".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def confirm_payment_intent_async(
        reader: str, **params: Unpack["ReaderConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader. See [Confirming a Payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#confirm-the-paymentintent) for more details.
        """
        ...

    @overload
    async def confirm_payment_intent_async(
        self, **params: Unpack["ReaderConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader. See [Confirming a Payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#confirm-the-paymentintent) for more details.
        """
        ...

    @class_method_variant("_cls_confirm_payment_intent_async")
    async def confirm_payment_intent_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader. See [Confirming a Payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=inspect#confirm-the-paymentintent) for more details.
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/confirm_payment_intent".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def create(cls, **params: Unpack["ReaderCreateParams"]) -> "Reader":
        """
        Creates a new Reader object.
        """
        return cast(
            "Reader",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["ReaderCreateParams"]
    ) -> "Reader":
        """
        Creates a new Reader object.
        """
        return cast(
            "Reader",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def _cls_delete(
        cls, sid: str, **params: Unpack["ReaderDeleteParams"]
    ) -> "Reader":
        """
        Deletes a Reader object.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(sid))
        return cast(
            "Reader",
            cls._static_request(
                "delete",
                url,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def delete(sid: str, **params: Unpack["ReaderDeleteParams"]) -> "Reader":
        """
        Deletes a Reader object.
        """
        ...

    @overload
    def delete(self, **params: Unpack["ReaderDeleteParams"]) -> "Reader":
        """
        Deletes a Reader object.
        """
        ...

    @class_method_variant("_cls_delete")
    def delete(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderDeleteParams"]
    ) -> "Reader":
        """
        Deletes a Reader object.
        """
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    async def _cls_delete_async(
        cls, sid: str, **params: Unpack["ReaderDeleteParams"]
    ) -> "Reader":
        """
        Deletes a Reader object.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(sid))
        return cast(
            "Reader",
            await cls._static_request_async(
                "delete",
                url,
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def delete_async(
        sid: str, **params: Unpack["ReaderDeleteParams"]
    ) -> "Reader":
        """
        Deletes a Reader object.
        """
        ...

    @overload
    async def delete_async(
        self, **params: Unpack["ReaderDeleteParams"]
    ) -> "Reader":
        """
        Deletes a Reader object.
        """
        ...

    @class_method_variant("_cls_delete_async")
    async def delete_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderDeleteParams"]
    ) -> "Reader":
        """
        Deletes a Reader object.
        """
        return await self._request_and_refresh_async(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls, **params: Unpack["ReaderListParams"]
    ) -> ListObject["Reader"]:
        """
        Returns a list of Reader objects.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["ReaderListParams"]
    ) -> ListObject["Reader"]:
        """
        Returns a list of Reader objects.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["ReaderModifyParams"]
    ) -> "Reader":
        """
        Updates a Reader object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Reader",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["ReaderModifyParams"]
    ) -> "Reader":
        """
        Updates a Reader object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "Reader",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def _cls_process_payment_intent(
        cls, reader: str, **params: Unpack["ReaderProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader. See [process the payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=immediately#process-payment) for more details.
        """
        return cast(
            "Reader",
            cls._static_request(
                "post",
                "/v1/terminal/readers/{reader}/process_payment_intent".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def process_payment_intent(
        reader: str, **params: Unpack["ReaderProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader. See [process the payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=immediately#process-payment) for more details.
        """
        ...

    @overload
    def process_payment_intent(
        self, **params: Unpack["ReaderProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader. See [process the payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=immediately#process-payment) for more details.
        """
        ...

    @class_method_variant("_cls_process_payment_intent")
    def process_payment_intent(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader. See [process the payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=immediately#process-payment) for more details.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/process_payment_intent".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_process_payment_intent_async(
        cls, reader: str, **params: Unpack["ReaderProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader. See [process the payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=immediately#process-payment) for more details.
        """
        return cast(
            "Reader",
            await cls._static_request_async(
                "post",
                "/v1/terminal/readers/{reader}/process_payment_intent".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def process_payment_intent_async(
        reader: str, **params: Unpack["ReaderProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader. See [process the payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=immediately#process-payment) for more details.
        """
        ...

    @overload
    async def process_payment_intent_async(
        self, **params: Unpack["ReaderProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader. See [process the payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=immediately#process-payment) for more details.
        """
        ...

    @class_method_variant("_cls_process_payment_intent_async")
    async def process_payment_intent_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader. See [process the payment](https://docs.stripe.com/docs/terminal/payments/collect-card-payment?terminal-sdk-platform=server-driven&process=immediately#process-payment) for more details.
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/process_payment_intent".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_process_setup_intent(
        cls, reader: str, **params: Unpack["ReaderProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a SetupIntent flow on a Reader. See [Save directly without charging](https://docs.stripe.com/docs/terminal/features/saving-payment-details/save-directly) for more details.
        """
        return cast(
            "Reader",
            cls._static_request(
                "post",
                "/v1/terminal/readers/{reader}/process_setup_intent".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def process_setup_intent(
        reader: str, **params: Unpack["ReaderProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a SetupIntent flow on a Reader. See [Save directly without charging](https://docs.stripe.com/docs/terminal/features/saving-payment-details/save-directly) for more details.
        """
        ...

    @overload
    def process_setup_intent(
        self, **params: Unpack["ReaderProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a SetupIntent flow on a Reader. See [Save directly without charging](https://docs.stripe.com/docs/terminal/features/saving-payment-details/save-directly) for more details.
        """
        ...

    @class_method_variant("_cls_process_setup_intent")
    def process_setup_intent(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a SetupIntent flow on a Reader. See [Save directly without charging](https://docs.stripe.com/docs/terminal/features/saving-payment-details/save-directly) for more details.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/process_setup_intent".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_process_setup_intent_async(
        cls, reader: str, **params: Unpack["ReaderProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a SetupIntent flow on a Reader. See [Save directly without charging](https://docs.stripe.com/docs/terminal/features/saving-payment-details/save-directly) for more details.
        """
        return cast(
            "Reader",
            await cls._static_request_async(
                "post",
                "/v1/terminal/readers/{reader}/process_setup_intent".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def process_setup_intent_async(
        reader: str, **params: Unpack["ReaderProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a SetupIntent flow on a Reader. See [Save directly without charging](https://docs.stripe.com/docs/terminal/features/saving-payment-details/save-directly) for more details.
        """
        ...

    @overload
    async def process_setup_intent_async(
        self, **params: Unpack["ReaderProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a SetupIntent flow on a Reader. See [Save directly without charging](https://docs.stripe.com/docs/terminal/features/saving-payment-details/save-directly) for more details.
        """
        ...

    @class_method_variant("_cls_process_setup_intent_async")
    async def process_setup_intent_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a SetupIntent flow on a Reader. See [Save directly without charging](https://docs.stripe.com/docs/terminal/features/saving-payment-details/save-directly) for more details.
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/process_setup_intent".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_refund_payment(
        cls, reader: str, **params: Unpack["ReaderRefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates an in-person refund on a Reader. See [Refund an Interac Payment](https://docs.stripe.com/docs/terminal/payments/regional?integration-country=CA#refund-an-interac-payment) for more details.
        """
        return cast(
            "Reader",
            cls._static_request(
                "post",
                "/v1/terminal/readers/{reader}/refund_payment".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def refund_payment(
        reader: str, **params: Unpack["ReaderRefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates an in-person refund on a Reader. See [Refund an Interac Payment](https://docs.stripe.com/docs/terminal/payments/regional?integration-country=CA#refund-an-interac-payment) for more details.
        """
        ...

    @overload
    def refund_payment(
        self, **params: Unpack["ReaderRefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates an in-person refund on a Reader. See [Refund an Interac Payment](https://docs.stripe.com/docs/terminal/payments/regional?integration-country=CA#refund-an-interac-payment) for more details.
        """
        ...

    @class_method_variant("_cls_refund_payment")
    def refund_payment(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderRefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates an in-person refund on a Reader. See [Refund an Interac Payment](https://docs.stripe.com/docs/terminal/payments/regional?integration-country=CA#refund-an-interac-payment) for more details.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/refund_payment".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_refund_payment_async(
        cls, reader: str, **params: Unpack["ReaderRefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates an in-person refund on a Reader. See [Refund an Interac Payment](https://docs.stripe.com/docs/terminal/payments/regional?integration-country=CA#refund-an-interac-payment) for more details.
        """
        return cast(
            "Reader",
            await cls._static_request_async(
                "post",
                "/v1/terminal/readers/{reader}/refund_payment".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def refund_payment_async(
        reader: str, **params: Unpack["ReaderRefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates an in-person refund on a Reader. See [Refund an Interac Payment](https://docs.stripe.com/docs/terminal/payments/regional?integration-country=CA#refund-an-interac-payment) for more details.
        """
        ...

    @overload
    async def refund_payment_async(
        self, **params: Unpack["ReaderRefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates an in-person refund on a Reader. See [Refund an Interac Payment](https://docs.stripe.com/docs/terminal/payments/regional?integration-country=CA#refund-an-interac-payment) for more details.
        """
        ...

    @class_method_variant("_cls_refund_payment_async")
    async def refund_payment_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderRefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates an in-person refund on a Reader. See [Refund an Interac Payment](https://docs.stripe.com/docs/terminal/payments/regional?integration-country=CA#refund-an-interac-payment) for more details.
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/refund_payment".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["ReaderRetrieveParams"]
    ) -> "Reader":
        """
        Retrieves a Reader object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["ReaderRetrieveParams"]
    ) -> "Reader":
        """
        Retrieves a Reader object.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def _cls_set_reader_display(
        cls, reader: str, **params: Unpack["ReaderSetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets the reader display to show [cart details](https://docs.stripe.com/docs/terminal/features/display).
        """
        return cast(
            "Reader",
            cls._static_request(
                "post",
                "/v1/terminal/readers/{reader}/set_reader_display".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def set_reader_display(
        reader: str, **params: Unpack["ReaderSetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets the reader display to show [cart details](https://docs.stripe.com/docs/terminal/features/display).
        """
        ...

    @overload
    def set_reader_display(
        self, **params: Unpack["ReaderSetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets the reader display to show [cart details](https://docs.stripe.com/docs/terminal/features/display).
        """
        ...

    @class_method_variant("_cls_set_reader_display")
    def set_reader_display(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderSetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets the reader display to show [cart details](https://docs.stripe.com/docs/terminal/features/display).
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/set_reader_display".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_set_reader_display_async(
        cls, reader: str, **params: Unpack["ReaderSetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets the reader display to show [cart details](https://docs.stripe.com/docs/terminal/features/display).
        """
        return cast(
            "Reader",
            await cls._static_request_async(
                "post",
                "/v1/terminal/readers/{reader}/set_reader_display".format(
                    reader=sanitize_id(reader)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def set_reader_display_async(
        reader: str, **params: Unpack["ReaderSetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets the reader display to show [cart details](https://docs.stripe.com/docs/terminal/features/display).
        """
        ...

    @overload
    async def set_reader_display_async(
        self, **params: Unpack["ReaderSetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets the reader display to show [cart details](https://docs.stripe.com/docs/terminal/features/display).
        """
        ...

    @class_method_variant("_cls_set_reader_display_async")
    async def set_reader_display_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["ReaderSetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets the reader display to show [cart details](https://docs.stripe.com/docs/terminal/features/display).
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/set_reader_display".format(
                    reader=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    class TestHelpers(APIResourceTestHelpers["Reader"]):
        _resource_cls: Type["Reader"]

        @classmethod
        def _cls_present_payment_method(
            cls,
            reader: str,
            **params: Unpack["ReaderPresentPaymentMethodParams"],
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            return cast(
                "Reader",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
                        reader=sanitize_id(reader)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def present_payment_method(
            reader: str, **params: Unpack["ReaderPresentPaymentMethodParams"]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            ...

        @overload
        def present_payment_method(
            self, **params: Unpack["ReaderPresentPaymentMethodParams"]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            ...

        @class_method_variant("_cls_present_payment_method")
        def present_payment_method(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["ReaderPresentPaymentMethodParams"]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            return cast(
                "Reader",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
                        reader=sanitize_id(self.resource._data.get("id"))
                    ),
                    params=params,
                ),
            )

        @classmethod
        async def _cls_present_payment_method_async(
            cls,
            reader: str,
            **params: Unpack["ReaderPresentPaymentMethodParams"],
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            return cast(
                "Reader",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
                        reader=sanitize_id(reader)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        async def present_payment_method_async(
            reader: str, **params: Unpack["ReaderPresentPaymentMethodParams"]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            ...

        @overload
        async def present_payment_method_async(
            self, **params: Unpack["ReaderPresentPaymentMethodParams"]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            ...

        @class_method_variant("_cls_present_payment_method_async")
        async def present_payment_method_async(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["ReaderPresentPaymentMethodParams"]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            return cast(
                "Reader",
                await self.resource._request_async(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
                        reader=sanitize_id(self.resource._data.get("id"))
                    ),
                    params=params,
                ),
            )

        @classmethod
        def _cls_succeed_input_collection(
            cls,
            reader: str,
            **params: Unpack["ReaderSucceedInputCollectionParams"],
        ) -> "Reader":
            """
            Use this endpoint to trigger a successful input collection on a simulated reader.
            """
            return cast(
                "Reader",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/succeed_input_collection".format(
                        reader=sanitize_id(reader)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def succeed_input_collection(
            reader: str, **params: Unpack["ReaderSucceedInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to trigger a successful input collection on a simulated reader.
            """
            ...

        @overload
        def succeed_input_collection(
            self, **params: Unpack["ReaderSucceedInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to trigger a successful input collection on a simulated reader.
            """
            ...

        @class_method_variant("_cls_succeed_input_collection")
        def succeed_input_collection(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["ReaderSucceedInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to trigger a successful input collection on a simulated reader.
            """
            return cast(
                "Reader",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/succeed_input_collection".format(
                        reader=sanitize_id(self.resource._data.get("id"))
                    ),
                    params=params,
                ),
            )

        @classmethod
        async def _cls_succeed_input_collection_async(
            cls,
            reader: str,
            **params: Unpack["ReaderSucceedInputCollectionParams"],
        ) -> "Reader":
            """
            Use this endpoint to trigger a successful input collection on a simulated reader.
            """
            return cast(
                "Reader",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/succeed_input_collection".format(
                        reader=sanitize_id(reader)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        async def succeed_input_collection_async(
            reader: str, **params: Unpack["ReaderSucceedInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to trigger a successful input collection on a simulated reader.
            """
            ...

        @overload
        async def succeed_input_collection_async(
            self, **params: Unpack["ReaderSucceedInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to trigger a successful input collection on a simulated reader.
            """
            ...

        @class_method_variant("_cls_succeed_input_collection_async")
        async def succeed_input_collection_async(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["ReaderSucceedInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to trigger a successful input collection on a simulated reader.
            """
            return cast(
                "Reader",
                await self.resource._request_async(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/succeed_input_collection".format(
                        reader=sanitize_id(self.resource._data.get("id"))
                    ),
                    params=params,
                ),
            )

        @classmethod
        def _cls_timeout_input_collection(
            cls,
            reader: str,
            **params: Unpack["ReaderTimeoutInputCollectionParams"],
        ) -> "Reader":
            """
            Use this endpoint to complete an input collection with a timeout error on a simulated reader.
            """
            return cast(
                "Reader",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/timeout_input_collection".format(
                        reader=sanitize_id(reader)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def timeout_input_collection(
            reader: str, **params: Unpack["ReaderTimeoutInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to complete an input collection with a timeout error on a simulated reader.
            """
            ...

        @overload
        def timeout_input_collection(
            self, **params: Unpack["ReaderTimeoutInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to complete an input collection with a timeout error on a simulated reader.
            """
            ...

        @class_method_variant("_cls_timeout_input_collection")
        def timeout_input_collection(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["ReaderTimeoutInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to complete an input collection with a timeout error on a simulated reader.
            """
            return cast(
                "Reader",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/timeout_input_collection".format(
                        reader=sanitize_id(self.resource._data.get("id"))
                    ),
                    params=params,
                ),
            )

        @classmethod
        async def _cls_timeout_input_collection_async(
            cls,
            reader: str,
            **params: Unpack["ReaderTimeoutInputCollectionParams"],
        ) -> "Reader":
            """
            Use this endpoint to complete an input collection with a timeout error on a simulated reader.
            """
            return cast(
                "Reader",
                await cls._static_request_async(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/timeout_input_collection".format(
                        reader=sanitize_id(reader)
                    ),
                    params=params,
                ),
            )

        @overload
        @staticmethod
        async def timeout_input_collection_async(
            reader: str, **params: Unpack["ReaderTimeoutInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to complete an input collection with a timeout error on a simulated reader.
            """
            ...

        @overload
        async def timeout_input_collection_async(
            self, **params: Unpack["ReaderTimeoutInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to complete an input collection with a timeout error on a simulated reader.
            """
            ...

        @class_method_variant("_cls_timeout_input_collection_async")
        async def timeout_input_collection_async(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["ReaderTimeoutInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to complete an input collection with a timeout error on a simulated reader.
            """
            return cast(
                "Reader",
                await self.resource._request_async(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/timeout_input_collection".format(
                        reader=sanitize_id(self.resource._data.get("id"))
                    ),
                    params=params,
                ),
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {"action": Action}


Reader.TestHelpers._resource_cls = Reader
