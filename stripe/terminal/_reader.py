# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._deletable_api_resource import DeletableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._test_helpers import APIResourceTestHelpers
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    Type,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe._charge import Charge
    from stripe._payment_intent import PaymentIntent
    from stripe._payment_method import PaymentMethod
    from stripe._refund import Refund
    from stripe._setup_intent import SetupIntent
    from stripe.terminal._location import Location


class Reader(
    CreateableAPIResource["Reader"],
    DeletableAPIResource["Reader"],
    ListableAPIResource["Reader"],
    UpdateableAPIResource["Reader"],
):
    """
    A Reader represents a physical device for accepting payment details.

    Related guide: [Connecting to a reader](https://stripe.com/docs/terminal/payments/connect-reader)
    """

    OBJECT_NAME: ClassVar[Literal["terminal.reader"]] = "terminal.reader"

    class Action(StripeObject):
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
                        The id to be selected
                        """
                        style: Optional[Literal["primary", "secondary"]]
                        """
                        The button style for the choice
                        """
                        text: str
                        """
                        The text to be selected
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
                    The toggle's default value
                    """
                    description: Optional[str]
                    """
                    The toggle's description text
                    """
                    title: Optional[str]
                    """
                    The toggle's title text
                    """
                    value: Optional[Literal["disabled", "enabled"]]
                    """
                    The toggle's collected value
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
            metadata: Optional[Dict[str, str]]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
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
            You can use them with [PaymentIntents](https://stripe.com/docs/payments/payment-intents) to collect payments or save them to
            Customer objects to store instrument details for future payments.

            Related guides: [Payment Methods](https://stripe.com/docs/payments/payment-methods) and [More Payment Scenarios](https://stripe.com/docs/payments/more-payment-scenarios).
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
            metadata: Optional[Dict[str, str]]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
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
                    The amount of the line item. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
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
                Tax amount for the entire cart. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
                """
                total: int
                """
                Total amount for the entire cart, including tax. A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
                """
                _inner_class_types = {"line_items": LineItem}

            cart: Optional[Cart]
            """
            Cart object to be displayed by the reader.
            """
            type: Literal["cart"]
            """
            Type of information to be displayed by the reader.
            """
            _inner_class_types = {"cart": Cart}

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
            "process_payment_intent",
            "process_setup_intent",
            "refund_payment",
            "set_reader_display",
        ]
        """
        Type of action performed by the reader.
        """
        _inner_class_types = {
            "collect_inputs": CollectInputs,
            "collect_payment_method": CollectPaymentMethod,
            "confirm_payment_intent": ConfirmPaymentIntent,
            "process_payment_intent": ProcessPaymentIntent,
            "process_setup_intent": ProcessSetupIntent,
            "refund_payment": RefundPayment,
            "set_reader_display": SetReaderDisplay,
        }

    class CancelActionParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class CollectInputsParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        inputs: List["Reader.CollectInputsParamsInput"]
        """
        List of inputs to be collected using the Reader
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """

    class CollectInputsParamsInput(TypedDict):
        custom_text: "Reader.CollectInputsParamsInputCustomText"
        """
        Customize the text which will be displayed while collecting this input
        """
        required: NotRequired[bool]
        """
        Indicate that this input is required, disabling the skip button
        """
        selection: NotRequired["Reader.CollectInputsParamsInputSelection"]
        """
        Options for the `selection` input
        """
        toggles: NotRequired[List["Reader.CollectInputsParamsInputToggle"]]
        """
        List of toggles to be displayed and customization for the toggles
        """
        type: Literal[
            "email", "numeric", "phone", "selection", "signature", "text"
        ]
        """
        The type of input to collect
        """

    class CollectInputsParamsInputCustomText(TypedDict):
        description: NotRequired[str]
        """
        The description which will be displayed when collecting this input
        """
        skip_button: NotRequired[str]
        """
        The skip button text
        """
        submit_button: NotRequired[str]
        """
        The submit button text
        """
        title: str
        """
        The title which will be displayed when collecting this input
        """

    class CollectInputsParamsInputSelection(TypedDict):
        choices: List["Reader.CollectInputsParamsInputSelectionChoice"]
        """
        List of choices for the `selection` input
        """

    class CollectInputsParamsInputSelectionChoice(TypedDict):
        id: str
        """
        The unique identifier for this choice
        """
        style: NotRequired[Literal["primary", "secondary"]]
        """
        The style of the button which will be shown for this choice
        """
        text: str
        """
        The text which will be shown on the button for this choice
        """

    class CollectInputsParamsInputToggle(TypedDict):
        default_value: NotRequired[Literal["disabled", "enabled"]]
        """
        The default value of the toggle
        """
        description: NotRequired[str]
        """
        The description which will be displayed for the toggle
        """
        title: NotRequired[str]
        """
        The title which will be displayed for the toggle
        """

    class CollectPaymentMethodParams(RequestOptions):
        collect_config: NotRequired[
            "Reader.CollectPaymentMethodParamsCollectConfig"
        ]
        """
        Configuration overrides.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        payment_intent: str
        """
        PaymentIntent ID.
        """

    class CollectPaymentMethodParamsCollectConfig(TypedDict):
        allow_redisplay: NotRequired[
            Literal["always", "limited", "unspecified"]
        ]
        """
        This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow.
        """
        enable_customer_cancellation: NotRequired[bool]
        """
        Enables cancel button on transaction screens.
        """
        skip_tipping: NotRequired[bool]
        """
        Override showing a tipping selection screen on this transaction.
        """
        tipping: NotRequired[
            "Reader.CollectPaymentMethodParamsCollectConfigTipping"
        ]
        """
        Tipping configuration for this transaction.
        """

    class CollectPaymentMethodParamsCollectConfigTipping(TypedDict):
        amount_eligible: NotRequired[int]
        """
        Amount used to calculate tip suggestions on tipping selection screen for this transaction. Must be a positive integer in the smallest currency unit (e.g., 100 cents to represent $1.00 or 100 to represent ¥100, a zero-decimal currency).
        """

    class ConfirmPaymentIntentParams(RequestOptions):
        confirm_config: NotRequired[
            "Reader.ConfirmPaymentIntentParamsConfirmConfig"
        ]
        """
        Configuration overrides.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        payment_intent: str
        """
        PaymentIntent ID.
        """

    class ConfirmPaymentIntentParamsConfirmConfig(TypedDict):
        return_url: NotRequired[str]
        """
        The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.
        """

    class CreateParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        label: NotRequired[str]
        """
        Custom label given to the reader for easier identification. If no label is specified, the registration code will be used.
        """
        location: NotRequired[str]
        """
        The location to assign the reader to.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        registration_code: str
        """
        A code generated by the reader used for registering to an account.
        """

    class DeleteParams(RequestOptions):
        pass

    class ListParams(RequestOptions):
        device_type: NotRequired[
            Literal[
                "bbpos_chipper2x",
                "bbpos_wisepad3",
                "bbpos_wisepos_e",
                "mobile_phone_reader",
                "simulated_stripe_s700",
                "simulated_wisepos_e",
                "stripe_m2",
                "stripe_s700",
                "verifone_P400",
            ]
        ]
        """
        Filters readers by device type
        """
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        location: NotRequired[str]
        """
        A location ID to filter the response list to only readers at the specific location
        """
        serial_number: NotRequired[str]
        """
        Filters readers by serial number
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        status: NotRequired[Literal["offline", "online"]]
        """
        A status filter to filter readers to only offline or online readers
        """

    class ModifyParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        label: NotRequired["Literal['']|str"]
        """
        The new label of the reader.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """

    class PresentPaymentMethodParams(RequestOptions):
        amount_tip: NotRequired[int]
        """
        Simulated on-reader tip amount.
        """
        card: NotRequired["Reader.PresentPaymentMethodParamsCard"]
        """
        Simulated data for the card payment method.
        """
        card_present: NotRequired[
            "Reader.PresentPaymentMethodParamsCardPresent"
        ]
        """
        Simulated data for the card_present payment method.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        interac_present: NotRequired[
            "Reader.PresentPaymentMethodParamsInteracPresent"
        ]
        """
        Simulated data for the interac_present payment method.
        """
        type: NotRequired[Literal["card", "card_present", "interac_present"]]
        """
        Simulated payment type.
        """

    class PresentPaymentMethodParamsCard(TypedDict):
        cvc: NotRequired[str]
        """
        Card security code.
        """
        exp_month: int
        """
        Two-digit number representing the card's expiration month.
        """
        exp_year: int
        """
        Two- or four-digit number representing the card's expiration year.
        """
        number: str
        """
        The card number, as a string without any separators.
        """

    class PresentPaymentMethodParamsCardPresent(TypedDict):
        number: NotRequired[str]
        """
        The card number, as a string without any separators.
        """

    class PresentPaymentMethodParamsInteracPresent(TypedDict):
        number: NotRequired[str]
        """
        Card Number
        """

    class ProcessPaymentIntentParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        payment_intent: str
        """
        PaymentIntent ID
        """
        process_config: NotRequired[
            "Reader.ProcessPaymentIntentParamsProcessConfig"
        ]
        """
        Configuration overrides
        """

    class ProcessPaymentIntentParamsProcessConfig(TypedDict):
        allow_redisplay: NotRequired[
            Literal["always", "limited", "unspecified"]
        ]
        """
        This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow.
        """
        enable_customer_cancellation: NotRequired[bool]
        """
        Enables cancel button on transaction screens.
        """
        return_url: NotRequired[str]
        """
        The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.
        """
        skip_tipping: NotRequired[bool]
        """
        Override showing a tipping selection screen on this transaction.
        """
        tipping: NotRequired[
            "Reader.ProcessPaymentIntentParamsProcessConfigTipping"
        ]
        """
        Tipping configuration for this transaction.
        """

    class ProcessPaymentIntentParamsProcessConfigTipping(TypedDict):
        amount_eligible: NotRequired[int]
        """
        Amount used to calculate tip suggestions on tipping selection screen for this transaction. Must be a positive integer in the smallest currency unit (e.g., 100 cents to represent $1.00 or 100 to represent ¥100, a zero-decimal currency).
        """

    class ProcessSetupIntentParams(RequestOptions):
        allow_redisplay: Literal["always", "limited", "unspecified"]
        """
        This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        process_config: NotRequired[
            "Reader.ProcessSetupIntentParamsProcessConfig"
        ]
        """
        Configuration overrides
        """
        setup_intent: str
        """
        SetupIntent ID
        """

    class ProcessSetupIntentParamsProcessConfig(TypedDict):
        enable_customer_cancellation: NotRequired[bool]
        """
        Enables cancel button on transaction screens.
        """

    class RefundPaymentParams(RequestOptions):
        amount: NotRequired[int]
        """
        A positive integer in __cents__ representing how much of this charge to refund.
        """
        charge: NotRequired[str]
        """
        ID of the Charge to refund.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        payment_intent: NotRequired[str]
        """
        ID of the PaymentIntent to refund.
        """
        refund_application_fee: NotRequired[bool]
        """
        Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.
        """
        refund_payment_config: NotRequired[
            "Reader.RefundPaymentParamsRefundPaymentConfig"
        ]
        """
        Configuration overrides
        """
        reverse_transfer: NotRequired[bool]
        """
        Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge.
        """

    class RefundPaymentParamsRefundPaymentConfig(TypedDict):
        enable_customer_cancellation: NotRequired[bool]
        """
        Enables cancel button on transaction screens.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class SetReaderDisplayParams(RequestOptions):
        cart: NotRequired["Reader.SetReaderDisplayParamsCart"]
        """
        Cart
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        type: Literal["cart"]
        """
        Type
        """

    class SetReaderDisplayParamsCart(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        line_items: List["Reader.SetReaderDisplayParamsCartLineItem"]
        """
        Array of line items that were purchased.
        """
        tax: NotRequired[int]
        """
        The amount of tax in cents.
        """
        total: int
        """
        Total balance of cart due in cents.
        """

    class SetReaderDisplayParamsCartLineItem(TypedDict):
        amount: int
        """
        The price of the item in cents.
        """
        description: str
        """
        The description or name of the item.
        """
        quantity: int
        """
        The quantity of the line item being purchased.
        """

    class SucceedInputCollectionParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        skip_non_required_inputs: NotRequired[Literal["all", "none"]]
        """
        This parameter defines the skip behavior for input collection.
        """

    class TimeoutInputCollectionParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

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
        "simulated_wisepos_e",
        "stripe_m2",
        "stripe_s700",
        "verifone_P400",
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
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    location: Optional[ExpandableField["Location"]]
    """
    The location identifier of the reader.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
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
        cls, reader: str, **params: Unpack["Reader.CancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action.
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
        reader: str, **params: Unpack["Reader.CancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action.
        """
        ...

    @overload
    def cancel_action(
        self, **params: Unpack["Reader.CancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action.
        """
        ...

    @class_method_variant("_cls_cancel_action")
    def cancel_action(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.CancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/cancel_action".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_cancel_action_async(
        cls, reader: str, **params: Unpack["Reader.CancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action.
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
        reader: str, **params: Unpack["Reader.CancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action.
        """
        ...

    @overload
    async def cancel_action_async(
        self, **params: Unpack["Reader.CancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action.
        """
        ...

    @class_method_variant("_cls_cancel_action_async")
    async def cancel_action_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.CancelActionParams"]
    ) -> "Reader":
        """
        Cancels the current reader action.
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/cancel_action".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_collect_inputs(
        cls, reader: str, **params: Unpack["Reader.CollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an input collection flow on a Reader.
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
        reader: str, **params: Unpack["Reader.CollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an input collection flow on a Reader.
        """
        ...

    @overload
    def collect_inputs(
        self, **params: Unpack["Reader.CollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an input collection flow on a Reader.
        """
        ...

    @class_method_variant("_cls_collect_inputs")
    def collect_inputs(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.CollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an input collection flow on a Reader.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/collect_inputs".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_collect_inputs_async(
        cls, reader: str, **params: Unpack["Reader.CollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an input collection flow on a Reader.
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
        reader: str, **params: Unpack["Reader.CollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an input collection flow on a Reader.
        """
        ...

    @overload
    async def collect_inputs_async(
        self, **params: Unpack["Reader.CollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an input collection flow on a Reader.
        """
        ...

    @class_method_variant("_cls_collect_inputs_async")
    async def collect_inputs_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.CollectInputsParams"]
    ) -> "Reader":
        """
        Initiates an input collection flow on a Reader.
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/collect_inputs".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_collect_payment_method(
        cls, reader: str, **params: Unpack["Reader.CollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation.
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
        reader: str, **params: Unpack["Reader.CollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation.
        """
        ...

    @overload
    def collect_payment_method(
        self, **params: Unpack["Reader.CollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation.
        """
        ...

    @class_method_variant("_cls_collect_payment_method")
    def collect_payment_method(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.CollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/collect_payment_method".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_collect_payment_method_async(
        cls, reader: str, **params: Unpack["Reader.CollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation.
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
        reader: str, **params: Unpack["Reader.CollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation.
        """
        ...

    @overload
    async def collect_payment_method_async(
        self, **params: Unpack["Reader.CollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation.
        """
        ...

    @class_method_variant("_cls_collect_payment_method_async")
    async def collect_payment_method_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.CollectPaymentMethodParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation.
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/collect_payment_method".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_confirm_payment_intent(
        cls, reader: str, **params: Unpack["Reader.ConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader.
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
        reader: str, **params: Unpack["Reader.ConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader.
        """
        ...

    @overload
    def confirm_payment_intent(
        self, **params: Unpack["Reader.ConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader.
        """
        ...

    @class_method_variant("_cls_confirm_payment_intent")
    def confirm_payment_intent(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.ConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/confirm_payment_intent".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_confirm_payment_intent_async(
        cls, reader: str, **params: Unpack["Reader.ConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader.
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
        reader: str, **params: Unpack["Reader.ConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader.
        """
        ...

    @overload
    async def confirm_payment_intent_async(
        self, **params: Unpack["Reader.ConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader.
        """
        ...

    @class_method_variant("_cls_confirm_payment_intent_async")
    async def confirm_payment_intent_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.ConfirmPaymentIntentParams"]
    ) -> "Reader":
        """
        Finalizes a payment on a Reader.
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/confirm_payment_intent".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def create(cls, **params: Unpack["Reader.CreateParams"]) -> "Reader":
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
        cls, **params: Unpack["Reader.CreateParams"]
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
        cls, sid: str, **params: Unpack["Reader.DeleteParams"]
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
    def delete(sid: str, **params: Unpack["Reader.DeleteParams"]) -> "Reader":
        """
        Deletes a Reader object.
        """
        ...

    @overload
    def delete(self, **params: Unpack["Reader.DeleteParams"]) -> "Reader":
        """
        Deletes a Reader object.
        """
        ...

    @class_method_variant("_cls_delete")
    def delete(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.DeleteParams"]
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
        cls, sid: str, **params: Unpack["Reader.DeleteParams"]
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
        sid: str, **params: Unpack["Reader.DeleteParams"]
    ) -> "Reader":
        """
        Deletes a Reader object.
        """
        ...

    @overload
    async def delete_async(
        self, **params: Unpack["Reader.DeleteParams"]
    ) -> "Reader":
        """
        Deletes a Reader object.
        """
        ...

    @class_method_variant("_cls_delete_async")
    async def delete_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.DeleteParams"]
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
        cls, **params: Unpack["Reader.ListParams"]
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
        cls, **params: Unpack["Reader.ListParams"]
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
        cls, id: str, **params: Unpack["Reader.ModifyParams"]
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
        cls, id: str, **params: Unpack["Reader.ModifyParams"]
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
        cls, reader: str, **params: Unpack["Reader.ProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader.
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
        reader: str, **params: Unpack["Reader.ProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader.
        """
        ...

    @overload
    def process_payment_intent(
        self, **params: Unpack["Reader.ProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader.
        """
        ...

    @class_method_variant("_cls_process_payment_intent")
    def process_payment_intent(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.ProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/process_payment_intent".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_process_payment_intent_async(
        cls, reader: str, **params: Unpack["Reader.ProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader.
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
        reader: str, **params: Unpack["Reader.ProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader.
        """
        ...

    @overload
    async def process_payment_intent_async(
        self, **params: Unpack["Reader.ProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader.
        """
        ...

    @class_method_variant("_cls_process_payment_intent_async")
    async def process_payment_intent_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.ProcessPaymentIntentParams"]
    ) -> "Reader":
        """
        Initiates a payment flow on a Reader.
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/process_payment_intent".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_process_setup_intent(
        cls, reader: str, **params: Unpack["Reader.ProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a setup intent flow on a Reader.
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
        reader: str, **params: Unpack["Reader.ProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a setup intent flow on a Reader.
        """
        ...

    @overload
    def process_setup_intent(
        self, **params: Unpack["Reader.ProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a setup intent flow on a Reader.
        """
        ...

    @class_method_variant("_cls_process_setup_intent")
    def process_setup_intent(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.ProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a setup intent flow on a Reader.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/process_setup_intent".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_process_setup_intent_async(
        cls, reader: str, **params: Unpack["Reader.ProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a setup intent flow on a Reader.
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
        reader: str, **params: Unpack["Reader.ProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a setup intent flow on a Reader.
        """
        ...

    @overload
    async def process_setup_intent_async(
        self, **params: Unpack["Reader.ProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a setup intent flow on a Reader.
        """
        ...

    @class_method_variant("_cls_process_setup_intent_async")
    async def process_setup_intent_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.ProcessSetupIntentParams"]
    ) -> "Reader":
        """
        Initiates a setup intent flow on a Reader.
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/process_setup_intent".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_refund_payment(
        cls, reader: str, **params: Unpack["Reader.RefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates a refund on a Reader
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
        reader: str, **params: Unpack["Reader.RefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates a refund on a Reader
        """
        ...

    @overload
    def refund_payment(
        self, **params: Unpack["Reader.RefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates a refund on a Reader
        """
        ...

    @class_method_variant("_cls_refund_payment")
    def refund_payment(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.RefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates a refund on a Reader
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/refund_payment".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_refund_payment_async(
        cls, reader: str, **params: Unpack["Reader.RefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates a refund on a Reader
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
        reader: str, **params: Unpack["Reader.RefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates a refund on a Reader
        """
        ...

    @overload
    async def refund_payment_async(
        self, **params: Unpack["Reader.RefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates a refund on a Reader
        """
        ...

    @class_method_variant("_cls_refund_payment_async")
    async def refund_payment_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.RefundPaymentParams"]
    ) -> "Reader":
        """
        Initiates a refund on a Reader
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/refund_payment".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Reader.RetrieveParams"]
    ) -> "Reader":
        """
        Retrieves a Reader object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["Reader.RetrieveParams"]
    ) -> "Reader":
        """
        Retrieves a Reader object.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def _cls_set_reader_display(
        cls, reader: str, **params: Unpack["Reader.SetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets reader display to show cart details.
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
        reader: str, **params: Unpack["Reader.SetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets reader display to show cart details.
        """
        ...

    @overload
    def set_reader_display(
        self, **params: Unpack["Reader.SetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets reader display to show cart details.
        """
        ...

    @class_method_variant("_cls_set_reader_display")
    def set_reader_display(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.SetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets reader display to show cart details.
        """
        return cast(
            "Reader",
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/set_reader_display".format(
                    reader=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_set_reader_display_async(
        cls, reader: str, **params: Unpack["Reader.SetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets reader display to show cart details.
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
        reader: str, **params: Unpack["Reader.SetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets reader display to show cart details.
        """
        ...

    @overload
    async def set_reader_display_async(
        self, **params: Unpack["Reader.SetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets reader display to show cart details.
        """
        ...

    @class_method_variant("_cls_set_reader_display_async")
    async def set_reader_display_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Reader.SetReaderDisplayParams"]
    ) -> "Reader":
        """
        Sets reader display to show cart details.
        """
        return cast(
            "Reader",
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/set_reader_display".format(
                    reader=sanitize_id(self.get("id"))
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
            **params: Unpack["Reader.PresentPaymentMethodParams"],
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
            reader: str, **params: Unpack["Reader.PresentPaymentMethodParams"]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            ...

        @overload
        def present_payment_method(
            self, **params: Unpack["Reader.PresentPaymentMethodParams"]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            ...

        @class_method_variant("_cls_present_payment_method")
        def present_payment_method(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["Reader.PresentPaymentMethodParams"]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            return cast(
                "Reader",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
                        reader=sanitize_id(self.resource.get("id"))
                    ),
                    params=params,
                ),
            )

        @classmethod
        async def _cls_present_payment_method_async(
            cls,
            reader: str,
            **params: Unpack["Reader.PresentPaymentMethodParams"],
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
            reader: str, **params: Unpack["Reader.PresentPaymentMethodParams"]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            ...

        @overload
        async def present_payment_method_async(
            self, **params: Unpack["Reader.PresentPaymentMethodParams"]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            ...

        @class_method_variant("_cls_present_payment_method_async")
        async def present_payment_method_async(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["Reader.PresentPaymentMethodParams"]
        ) -> "Reader":
            """
            Presents a payment method on a simulated reader. Can be used to simulate accepting a payment, saving a card or refunding a transaction.
            """
            return cast(
                "Reader",
                await self.resource._request_async(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
                        reader=sanitize_id(self.resource.get("id"))
                    ),
                    params=params,
                ),
            )

        @classmethod
        def _cls_succeed_input_collection(
            cls,
            reader: str,
            **params: Unpack["Reader.SucceedInputCollectionParams"],
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
            reader: str,
            **params: Unpack["Reader.SucceedInputCollectionParams"],
        ) -> "Reader":
            """
            Use this endpoint to trigger a successful input collection on a simulated reader.
            """
            ...

        @overload
        def succeed_input_collection(
            self, **params: Unpack["Reader.SucceedInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to trigger a successful input collection on a simulated reader.
            """
            ...

        @class_method_variant("_cls_succeed_input_collection")
        def succeed_input_collection(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["Reader.SucceedInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to trigger a successful input collection on a simulated reader.
            """
            return cast(
                "Reader",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/succeed_input_collection".format(
                        reader=sanitize_id(self.resource.get("id"))
                    ),
                    params=params,
                ),
            )

        @classmethod
        async def _cls_succeed_input_collection_async(
            cls,
            reader: str,
            **params: Unpack["Reader.SucceedInputCollectionParams"],
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
            reader: str,
            **params: Unpack["Reader.SucceedInputCollectionParams"],
        ) -> "Reader":
            """
            Use this endpoint to trigger a successful input collection on a simulated reader.
            """
            ...

        @overload
        async def succeed_input_collection_async(
            self, **params: Unpack["Reader.SucceedInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to trigger a successful input collection on a simulated reader.
            """
            ...

        @class_method_variant("_cls_succeed_input_collection_async")
        async def succeed_input_collection_async(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["Reader.SucceedInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to trigger a successful input collection on a simulated reader.
            """
            return cast(
                "Reader",
                await self.resource._request_async(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/succeed_input_collection".format(
                        reader=sanitize_id(self.resource.get("id"))
                    ),
                    params=params,
                ),
            )

        @classmethod
        def _cls_timeout_input_collection(
            cls,
            reader: str,
            **params: Unpack["Reader.TimeoutInputCollectionParams"],
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
            reader: str,
            **params: Unpack["Reader.TimeoutInputCollectionParams"],
        ) -> "Reader":
            """
            Use this endpoint to complete an input collection with a timeout error on a simulated reader.
            """
            ...

        @overload
        def timeout_input_collection(
            self, **params: Unpack["Reader.TimeoutInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to complete an input collection with a timeout error on a simulated reader.
            """
            ...

        @class_method_variant("_cls_timeout_input_collection")
        def timeout_input_collection(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["Reader.TimeoutInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to complete an input collection with a timeout error on a simulated reader.
            """
            return cast(
                "Reader",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/timeout_input_collection".format(
                        reader=sanitize_id(self.resource.get("id"))
                    ),
                    params=params,
                ),
            )

        @classmethod
        async def _cls_timeout_input_collection_async(
            cls,
            reader: str,
            **params: Unpack["Reader.TimeoutInputCollectionParams"],
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
            reader: str,
            **params: Unpack["Reader.TimeoutInputCollectionParams"],
        ) -> "Reader":
            """
            Use this endpoint to complete an input collection with a timeout error on a simulated reader.
            """
            ...

        @overload
        async def timeout_input_collection_async(
            self, **params: Unpack["Reader.TimeoutInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to complete an input collection with a timeout error on a simulated reader.
            """
            ...

        @class_method_variant("_cls_timeout_input_collection_async")
        async def timeout_input_collection_async(  # pyright: ignore[reportGeneralTypeIssues]
            self, **params: Unpack["Reader.TimeoutInputCollectionParams"]
        ) -> "Reader":
            """
            Use this endpoint to complete an input collection with a timeout error on a simulated reader.
            """
            return cast(
                "Reader",
                await self.resource._request_async(
                    "post",
                    "/v1/test_helpers/terminal/readers/{reader}/timeout_input_collection".format(
                        reader=sanitize_id(self.resource.get("id"))
                    ),
                    params=params,
                ),
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {"action": Action}


Reader.TestHelpers._resource_cls = Reader
