# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.terminal._reader import Reader
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class ReaderService(StripeService):
    class CancelActionParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class CollectInputsParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        inputs: List["ReaderService.CollectInputsParamsInput"]
        """
        List of inputs to be collected using the Reader
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """

    class CollectInputsParamsInput(TypedDict):
        custom_text: "ReaderService.CollectInputsParamsInputCustomText"
        """
        Customize the text which will be displayed while collecting this input
        """
        required: NotRequired[bool]
        """
        Indicate that this input is required, disabling the skip button
        """
        selection: NotRequired[
            "ReaderService.CollectInputsParamsInputSelection"
        ]
        """
        Options for the `selection` input
        """
        toggles: NotRequired[
            List["ReaderService.CollectInputsParamsInputToggle"]
        ]
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
        choices: List["ReaderService.CollectInputsParamsInputSelectionChoice"]
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

    class CollectPaymentMethodParams(TypedDict):
        collect_config: NotRequired[
            "ReaderService.CollectPaymentMethodParamsCollectConfig"
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
            "ReaderService.CollectPaymentMethodParamsCollectConfigTipping"
        ]
        """
        Tipping configuration for this transaction.
        """

    class CollectPaymentMethodParamsCollectConfigTipping(TypedDict):
        amount_eligible: NotRequired[int]
        """
        Amount used to calculate tip suggestions on tipping selection screen for this transaction. Must be a positive integer in the smallest currency unit (e.g., 100 cents to represent $1.00 or 100 to represent ¥100, a zero-decimal currency).
        """

    class ConfirmPaymentIntentParams(TypedDict):
        confirm_config: NotRequired[
            "ReaderService.ConfirmPaymentIntentParamsConfirmConfig"
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

    class CreateParams(TypedDict):
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

    class DeleteParams(TypedDict):
        pass

    class ListParams(TypedDict):
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

    class ProcessPaymentIntentParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        payment_intent: str
        """
        PaymentIntent ID
        """
        process_config: NotRequired[
            "ReaderService.ProcessPaymentIntentParamsProcessConfig"
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
            "ReaderService.ProcessPaymentIntentParamsProcessConfigTipping"
        ]
        """
        Tipping configuration for this transaction.
        """

    class ProcessPaymentIntentParamsProcessConfigTipping(TypedDict):
        amount_eligible: NotRequired[int]
        """
        Amount used to calculate tip suggestions on tipping selection screen for this transaction. Must be a positive integer in the smallest currency unit (e.g., 100 cents to represent $1.00 or 100 to represent ¥100, a zero-decimal currency).
        """

    class ProcessSetupIntentParams(TypedDict):
        allow_redisplay: Literal["always", "limited", "unspecified"]
        """
        This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        process_config: NotRequired[
            "ReaderService.ProcessSetupIntentParamsProcessConfig"
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

    class RefundPaymentParams(TypedDict):
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
            "ReaderService.RefundPaymentParamsRefundPaymentConfig"
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

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class SetReaderDisplayParams(TypedDict):
        cart: NotRequired["ReaderService.SetReaderDisplayParamsCart"]
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
        line_items: List["ReaderService.SetReaderDisplayParamsCartLineItem"]
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

    class UpdateParams(TypedDict):
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

    def delete(
        self,
        reader: str,
        params: "ReaderService.DeleteParams" = {},
        options: RequestOptions = {},
    ) -> Reader:
        """
        Deletes a Reader object.
        """
        return cast(
            Reader,
            self._request(
                "delete",
                "/v1/terminal/readers/{reader}".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def delete_async(
        self,
        reader: str,
        params: "ReaderService.DeleteParams" = {},
        options: RequestOptions = {},
    ) -> Reader:
        """
        Deletes a Reader object.
        """
        return cast(
            Reader,
            await self._request_async(
                "delete",
                "/v1/terminal/readers/{reader}".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        reader: str,
        params: "ReaderService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Reader:
        """
        Retrieves a Reader object.
        """
        return cast(
            Reader,
            self._request(
                "get",
                "/v1/terminal/readers/{reader}".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        reader: str,
        params: "ReaderService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Reader:
        """
        Retrieves a Reader object.
        """
        return cast(
            Reader,
            await self._request_async(
                "get",
                "/v1/terminal/readers/{reader}".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        reader: str,
        params: "ReaderService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Reader:
        """
        Updates a Reader object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        return cast(
            Reader,
            self._request(
                "post",
                "/v1/terminal/readers/{reader}".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        reader: str,
        params: "ReaderService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Reader:
        """
        Updates a Reader object by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        return cast(
            Reader,
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def list(
        self,
        params: "ReaderService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Reader]:
        """
        Returns a list of Reader objects.
        """
        return cast(
            ListObject[Reader],
            self._request(
                "get",
                "/v1/terminal/readers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "ReaderService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Reader]:
        """
        Returns a list of Reader objects.
        """
        return cast(
            ListObject[Reader],
            await self._request_async(
                "get",
                "/v1/terminal/readers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "ReaderService.CreateParams",
        options: RequestOptions = {},
    ) -> Reader:
        """
        Creates a new Reader object.
        """
        return cast(
            Reader,
            self._request(
                "post",
                "/v1/terminal/readers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ReaderService.CreateParams",
        options: RequestOptions = {},
    ) -> Reader:
        """
        Creates a new Reader object.
        """
        return cast(
            Reader,
            await self._request_async(
                "post",
                "/v1/terminal/readers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel_action(
        self,
        reader: str,
        params: "ReaderService.CancelActionParams" = {},
        options: RequestOptions = {},
    ) -> Reader:
        """
        Cancels the current reader action.
        """
        return cast(
            Reader,
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/cancel_action".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_action_async(
        self,
        reader: str,
        params: "ReaderService.CancelActionParams" = {},
        options: RequestOptions = {},
    ) -> Reader:
        """
        Cancels the current reader action.
        """
        return cast(
            Reader,
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/cancel_action".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def collect_inputs(
        self,
        reader: str,
        params: "ReaderService.CollectInputsParams",
        options: RequestOptions = {},
    ) -> Reader:
        """
        Initiates an input collection flow on a Reader.
        """
        return cast(
            Reader,
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/collect_inputs".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def collect_inputs_async(
        self,
        reader: str,
        params: "ReaderService.CollectInputsParams",
        options: RequestOptions = {},
    ) -> Reader:
        """
        Initiates an input collection flow on a Reader.
        """
        return cast(
            Reader,
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/collect_inputs".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def collect_payment_method(
        self,
        reader: str,
        params: "ReaderService.CollectPaymentMethodParams",
        options: RequestOptions = {},
    ) -> Reader:
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation.
        """
        return cast(
            Reader,
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/collect_payment_method".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def collect_payment_method_async(
        self,
        reader: str,
        params: "ReaderService.CollectPaymentMethodParams",
        options: RequestOptions = {},
    ) -> Reader:
        """
        Initiates a payment flow on a Reader and updates the PaymentIntent with card details before manual confirmation.
        """
        return cast(
            Reader,
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/collect_payment_method".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def confirm_payment_intent(
        self,
        reader: str,
        params: "ReaderService.ConfirmPaymentIntentParams",
        options: RequestOptions = {},
    ) -> Reader:
        """
        Finalizes a payment on a Reader.
        """
        return cast(
            Reader,
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/confirm_payment_intent".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def confirm_payment_intent_async(
        self,
        reader: str,
        params: "ReaderService.ConfirmPaymentIntentParams",
        options: RequestOptions = {},
    ) -> Reader:
        """
        Finalizes a payment on a Reader.
        """
        return cast(
            Reader,
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/confirm_payment_intent".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def process_payment_intent(
        self,
        reader: str,
        params: "ReaderService.ProcessPaymentIntentParams",
        options: RequestOptions = {},
    ) -> Reader:
        """
        Initiates a payment flow on a Reader.
        """
        return cast(
            Reader,
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/process_payment_intent".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def process_payment_intent_async(
        self,
        reader: str,
        params: "ReaderService.ProcessPaymentIntentParams",
        options: RequestOptions = {},
    ) -> Reader:
        """
        Initiates a payment flow on a Reader.
        """
        return cast(
            Reader,
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/process_payment_intent".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def process_setup_intent(
        self,
        reader: str,
        params: "ReaderService.ProcessSetupIntentParams",
        options: RequestOptions = {},
    ) -> Reader:
        """
        Initiates a setup intent flow on a Reader.
        """
        return cast(
            Reader,
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/process_setup_intent".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def process_setup_intent_async(
        self,
        reader: str,
        params: "ReaderService.ProcessSetupIntentParams",
        options: RequestOptions = {},
    ) -> Reader:
        """
        Initiates a setup intent flow on a Reader.
        """
        return cast(
            Reader,
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/process_setup_intent".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def refund_payment(
        self,
        reader: str,
        params: "ReaderService.RefundPaymentParams" = {},
        options: RequestOptions = {},
    ) -> Reader:
        """
        Initiates a refund on a Reader
        """
        return cast(
            Reader,
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/refund_payment".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def refund_payment_async(
        self,
        reader: str,
        params: "ReaderService.RefundPaymentParams" = {},
        options: RequestOptions = {},
    ) -> Reader:
        """
        Initiates a refund on a Reader
        """
        return cast(
            Reader,
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/refund_payment".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def set_reader_display(
        self,
        reader: str,
        params: "ReaderService.SetReaderDisplayParams",
        options: RequestOptions = {},
    ) -> Reader:
        """
        Sets reader display to show cart details.
        """
        return cast(
            Reader,
            self._request(
                "post",
                "/v1/terminal/readers/{reader}/set_reader_display".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def set_reader_display_async(
        self,
        reader: str,
        params: "ReaderService.SetReaderDisplayParams",
        options: RequestOptions = {},
    ) -> Reader:
        """
        Sets reader display to show cart details.
        """
        return cast(
            Reader,
            await self._request_async(
                "post",
                "/v1/terminal/readers/{reader}/set_reader_display".format(
                    reader=sanitize_id(reader),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
