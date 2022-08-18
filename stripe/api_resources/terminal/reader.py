# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import APIResourceTestHelpers
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import test_helpers


@test_helpers
class Reader(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    A Reader represents a physical device for accepting payment details.

    Related guide: [Connecting to a Reader](https://stripe.com/docs/terminal/payments/connect-reader).
    """

    OBJECT_NAME = "terminal.reader"

    @classmethod
    def _cls_cancel_action(
        cls,
        reader,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
    def cancel_action(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/terminal/readers/{reader}/cancel_action".format(
                reader=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_process_payment_intent(
        cls,
        reader,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
    def process_payment_intent(self, idempotency_key=None, **params):
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
        reader,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
    def process_setup_intent(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/terminal/readers/{reader}/process_setup_intent".format(
                reader=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_set_reader_display(
        cls,
        reader,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
    def set_reader_display(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/terminal/readers/{reader}/set_reader_display".format(
                reader=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    class TestHelpers(APIResourceTestHelpers):
        @classmethod
        def _cls_present_payment_method(
            cls,
            reader,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
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
        def present_payment_method(self, idempotency_key=None, **params):
            return self.resource._request(
                "post",
                "/v1/test_helpers/terminal/readers/{reader}/present_payment_method".format(
                    reader=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )
