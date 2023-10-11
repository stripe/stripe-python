# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    APIResourceTestHelpers,
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal, Type
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.refund import Refund
    from stripe.api_resources.setup_intent import SetupIntent
    from stripe.api_resources.terminal.location import Location


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

    OBJECT_NAME = "terminal.reader"

    class Action(StripeObject):
        class CollectInputs(StripeObject):
            class Input(StripeObject):
                class CustomText(StripeObject):
                    description: Optional[str]
                    skip_button: Optional[str]
                    submit_button: Optional[str]
                    title: Optional[str]

                class Selection(StripeObject):
                    class Choice(StripeObject):
                        style: Optional[Literal["primary", "secondary"]]
                        value: str

                    choices: List[Choice]
                    value: Optional[str]
                    _inner_class_types = {"choices": Choice}

                class Signature(StripeObject):
                    value: Optional[str]

                custom_text: Optional[CustomText]
                required: Optional[bool]
                selection: Optional[Selection]
                signature: Optional[Signature]
                skipped: Optional[bool]
                type: Literal[
                    "email",
                    "numeric",
                    "phone",
                    "selection",
                    "signature",
                    "text",
                ]
                _inner_class_types = {
                    "custom_text": CustomText,
                    "selection": Selection,
                    "signature": Signature,
                }

            inputs: List[Input]
            metadata: Optional[Dict[str, str]]
            _inner_class_types = {"inputs": Input}

        class CollectPaymentMethod(StripeObject):
            class CollectConfig(StripeObject):
                class Tipping(StripeObject):
                    amount_eligible: Optional[int]

                skip_tipping: Optional[bool]
                tipping: Optional[Tipping]
                _inner_class_types = {"tipping": Tipping}

            collect_config: Optional[CollectConfig]
            payment_intent: ExpandableField["PaymentIntent"]
            payment_method: Optional["PaymentMethod"]
            stripe_account: Optional[str]
            _inner_class_types = {"collect_config": CollectConfig}

        class ConfirmPaymentIntent(StripeObject):
            payment_intent: ExpandableField["PaymentIntent"]
            stripe_account: Optional[str]

        class ProcessPaymentIntent(StripeObject):
            class ProcessConfig(StripeObject):
                class Tipping(StripeObject):
                    amount_eligible: Optional[int]

                skip_tipping: Optional[bool]
                tipping: Optional[Tipping]
                _inner_class_types = {"tipping": Tipping}

            payment_intent: ExpandableField["PaymentIntent"]
            process_config: Optional[ProcessConfig]
            stripe_account: Optional[str]
            _inner_class_types = {"process_config": ProcessConfig}

        class ProcessSetupIntent(StripeObject):
            class ProcessConfig(StripeObject):
                pass

            generated_card: Optional[str]
            process_config: Optional[ProcessConfig]
            setup_intent: ExpandableField["SetupIntent"]
            _inner_class_types = {"process_config": ProcessConfig}

        class RefundPayment(StripeObject):
            amount: Optional[int]
            charge: Optional[ExpandableField["Charge"]]
            metadata: Optional[Dict[str, str]]
            payment_intent: Optional[ExpandableField["PaymentIntent"]]
            reason: Optional[
                Literal["duplicate", "fraudulent", "requested_by_customer"]
            ]
            refund: Optional[ExpandableField["Refund"]]
            refund_application_fee: Optional[bool]
            reverse_transfer: Optional[bool]
            stripe_account: Optional[str]

        class SetReaderDisplay(StripeObject):
            class Cart(StripeObject):
                class LineItem(StripeObject):
                    amount: int
                    description: str
                    quantity: int

                currency: str
                line_items: List[LineItem]
                tax: Optional[int]
                total: int
                _inner_class_types = {"line_items": LineItem}

            cart: Optional[Cart]
            type: Literal["cart"]
            _inner_class_types = {"cart": Cart}

        collect_inputs: Optional[CollectInputs]
        collect_payment_method: Optional[CollectPaymentMethod]
        confirm_payment_intent: Optional[ConfirmPaymentIntent]
        failure_code: Optional[str]
        failure_message: Optional[str]
        process_payment_intent: Optional[ProcessPaymentIntent]
        process_setup_intent: Optional[ProcessSetupIntent]
        refund_payment: Optional[RefundPayment]
        set_reader_display: Optional[SetReaderDisplay]
        status: Literal["failed", "in_progress", "succeeded"]
        type: Literal[
            "collect_inputs",
            "collect_payment_method",
            "confirm_payment_intent",
            "process_payment_intent",
            "process_setup_intent",
            "refund_payment",
            "set_reader_display",
        ]
        _inner_class_types = {
            "collect_inputs": CollectInputs,
            "collect_payment_method": CollectPaymentMethod,
            "confirm_payment_intent": ConfirmPaymentIntent,
            "process_payment_intent": ProcessPaymentIntent,
            "process_setup_intent": ProcessSetupIntent,
            "refund_payment": RefundPayment,
            "set_reader_display": SetReaderDisplay,
        }

    action: Optional[Action]
    device_sw_version: Optional[str]
    device_type: Literal[
        "bbpos_chipper2x",
        "bbpos_wisepad3",
        "bbpos_wisepos_e",
        "simulated_wisepos_e",
        "stripe_m2",
        "verifone_P400",
    ]
    id: str
    ip_address: Optional[str]
    label: str
    livemode: bool
    location: Optional[ExpandableField["Location"]]
    metadata: Dict[str, str]
    object: Literal["terminal.reader"]
    serial_number: str
    status: Optional[str]
    deleted: Optional[Literal[True]]

    @classmethod
    def _cls_cancel_action(
        cls,
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/terminal/readers/{reader}/cancel_action".format(
                reader=util.sanitize_id(reader)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel_action")
    def cancel_action(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/terminal/readers/{reader}/cancel_action".format(
                reader=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_collect_inputs(
        cls,
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/terminal/readers/{reader}/collect_inputs".format(
                reader=util.sanitize_id(reader)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_collect_inputs")
    def collect_inputs(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/terminal/readers/{reader}/collect_inputs".format(
                reader=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_collect_payment_method(
        cls,
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/terminal/readers/{reader}/collect_payment_method".format(
                reader=util.sanitize_id(reader)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_collect_payment_method")
    def collect_payment_method(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/terminal/readers/{reader}/collect_payment_method".format(
                reader=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_confirm_payment_intent(
        cls,
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/terminal/readers/{reader}/confirm_payment_intent".format(
                reader=util.sanitize_id(reader)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_confirm_payment_intent")
    def confirm_payment_intent(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/terminal/readers/{reader}/confirm_payment_intent".format(
                reader=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Reader":
        return cast(
            "Reader",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def _cls_delete(cls, sid: str, **params: Any) -> "Reader":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Reader",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Any) -> "Reader":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["Reader"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(cls, id, **params: Any) -> "Reader":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Reader",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def _cls_process_payment_intent(
        cls,
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/terminal/readers/{reader}/process_payment_intent".format(
                reader=util.sanitize_id(reader)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_process_payment_intent")
    def process_payment_intent(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/terminal/readers/{reader}/process_payment_intent".format(
                reader=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_process_setup_intent(
        cls,
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/terminal/readers/{reader}/process_setup_intent".format(
                reader=util.sanitize_id(reader)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_process_setup_intent")
    def process_setup_intent(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/terminal/readers/{reader}/process_setup_intent".format(
                reader=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_refund_payment(
        cls,
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/terminal/readers/{reader}/refund_payment".format(
                reader=util.sanitize_id(reader)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_refund_payment")
    def refund_payment(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/terminal/readers/{reader}/refund_payment".format(
                reader=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Reader":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_set_reader_display(
        cls,
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/terminal/readers/{reader}/set_reader_display".format(
                reader=util.sanitize_id(reader)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_set_reader_display")
    def set_reader_display(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/terminal/readers/{reader}/set_reader_display".format(
                reader=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    class TestHelpers(APIResourceTestHelpers["Reader"]):
        _resource_cls: Type["Reader"]

        @classmethod
        def _cls_present_payment_method(
            cls,
            reader: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Any
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
                    reader=util.sanitize_id(reader)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_present_payment_method")
        def present_payment_method(
            self, idempotency_key: Optional[str] = None, **params: Any
        ):
            return self.resource._request(
                "post",
                "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
                    reader=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {"action": Action}


Reader.TestHelpers._resource_cls = Reader
