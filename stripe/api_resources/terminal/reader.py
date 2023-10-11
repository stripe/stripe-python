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
from stripe.stripe_object import StripeObject
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, Type
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


Reader.TestHelpers._resource_cls = Reader
