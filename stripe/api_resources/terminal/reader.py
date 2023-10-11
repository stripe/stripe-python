# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

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
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, Type, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
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

    class CancelActionParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class CreateParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        label: NotRequired[Optional[str]]
        location: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        registration_code: str

    class DeleteParams(RequestOptions):
        pass

    class ListParams(RequestOptions):
        device_type: NotRequired[
            Optional[
                Literal[
                    "bbpos_chipper2x",
                    "bbpos_wisepad3",
                    "bbpos_wisepos_e",
                    "simulated_wisepos_e",
                    "stripe_m2",
                    "verifone_P400",
                ]
            ]
        ]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        location: NotRequired[Optional[str]]
        serial_number: NotRequired[Optional[str]]
        starting_after: NotRequired[Optional[str]]
        status: NotRequired[Optional[Literal["offline", "online"]]]

    class ModifyParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        label: NotRequired[Optional[Union[Literal[""], str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]

    class ProcessPaymentIntentParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        payment_intent: str
        process_config: NotRequired[
            Optional["Reader.ProcessPaymentIntentParamsProcessConfig"]
        ]

    class ProcessPaymentIntentParamsProcessConfig(TypedDict):
        skip_tipping: NotRequired[Optional[bool]]
        tipping: NotRequired[
            Optional["Reader.ProcessPaymentIntentParamsProcessConfigTipping"]
        ]

    class ProcessPaymentIntentParamsProcessConfigTipping(TypedDict):
        amount_eligible: NotRequired[Optional[int]]

    class ProcessSetupIntentParams(RequestOptions):
        customer_consent_collected: bool
        expand: NotRequired[Optional[List[str]]]
        process_config: NotRequired[
            Optional["Reader.ProcessSetupIntentParamsProcessConfig"]
        ]
        setup_intent: str

    class ProcessSetupIntentParamsProcessConfig(TypedDict):
        pass

    class RefundPaymentParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        charge: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        payment_intent: NotRequired[Optional[str]]
        refund_application_fee: NotRequired[Optional[bool]]
        reverse_transfer: NotRequired[Optional[bool]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class SetReaderDisplayParams(RequestOptions):
        cart: NotRequired[Optional["Reader.SetReaderDisplayParamsCart"]]
        expand: NotRequired[Optional[List[str]]]
        type: Literal["cart"]

    class SetReaderDisplayParamsCart(TypedDict):
        currency: str
        line_items: List["Reader.SetReaderDisplayParamsCartLineItem"]
        tax: NotRequired[Optional[int]]
        total: int

    class SetReaderDisplayParamsCartLineItem(TypedDict):
        amount: int
        description: str
        quantity: int

    class PresentPaymentMethodParams(RequestOptions):
        amount_tip: NotRequired[Optional[int]]
        card_present: NotRequired[
            Optional["Reader.PresentPaymentMethodParamsCardPresent"]
        ]
        expand: NotRequired[Optional[List[str]]]
        interac_present: NotRequired[
            Optional["Reader.PresentPaymentMethodParamsInteracPresent"]
        ]
        type: NotRequired[Optional[Literal["card_present", "interac_present"]]]

    class PresentPaymentMethodParamsInteracPresent(TypedDict):
        number: NotRequired[Optional[str]]

    class PresentPaymentMethodParamsCardPresent(TypedDict):
        number: NotRequired[Optional[str]]

    action: Optional[StripeObject]
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
        **params: Unpack["Reader.CancelActionParams"]
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
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Reader.CancelActionParams"]
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
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Reader.CreateParams"]
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
    def _cls_delete(
        cls, sid: str, **params: Unpack["Reader.DeleteParams"]
    ) -> "Reader":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Reader",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Unpack["Reader.DeleteParams"]) -> "Reader":
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
        **params: Unpack["Reader.ListParams"]
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
    def modify(cls, id, **params: Unpack["Reader.ModifyParams"]) -> "Reader":
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
        **params: Unpack["Reader.ProcessPaymentIntentParams"]
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
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Reader.ProcessPaymentIntentParams"]
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
        **params: Unpack["Reader.ProcessSetupIntentParams"]
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
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Reader.ProcessSetupIntentParams"]
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
        **params: Unpack["Reader.RefundPaymentParams"]
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
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Reader.RefundPaymentParams"]
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
        cls, id: str, **params: Unpack["Reader.RetrieveParams"]
    ) -> "Reader":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_set_reader_display(
        cls,
        reader: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Reader.SetReaderDisplayParams"]
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
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Reader.SetReaderDisplayParams"]
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
            **params: Unpack["Reader.PresentPaymentMethodParams"]
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
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["Reader.PresentPaymentMethodParams"]
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


Reader.TestHelpers._resource_cls = Reader
