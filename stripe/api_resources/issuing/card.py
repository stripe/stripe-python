# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_requestor
from stripe import util
from stripe.api_resources.abstract import APIResourceTestHelpers
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method
from stripe.api_resources.abstract import test_helpers


@custom_method("details", http_verb="get")
@test_helpers
class Card(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "issuing.card"

    def details(self, idempotency_key=None, **params):
        return self.request("get", self.instance_url() + "/details", params)

    class TestHelpers(APIResourceTestHelpers):
        @classmethod
        def _cls_deliver_card(
            cls,
            card,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            requestor = api_requestor.APIRequestor(
                api_key, api_version=stripe_version, account=stripe_account
            )
            url = "/v1/test_helpers/issuing/cards/{card}/shipping/deliver".format(
                card=util.sanitize_id(card)
            )
            response, api_key = requestor.request("post", url, params)
            stripe_object = util.convert_to_stripe_object(
                response, api_key, stripe_version, stripe_account
            )
            return stripe_object

        @util.class_method_variant("_cls_deliver_card")
        def deliver_card(self, idempotency_key=None, **params):
            url = "/v1/test_helpers/issuing/cards/{card}/shipping/deliver".format(
                card=util.sanitize_id(self.get("id"))
            )
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource

        @classmethod
        def _cls_fail_card(
            cls,
            card,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            requestor = api_requestor.APIRequestor(
                api_key, api_version=stripe_version, account=stripe_account
            )
            url = "/v1/test_helpers/issuing/cards/{card}/shipping/fail".format(
                card=util.sanitize_id(card)
            )
            response, api_key = requestor.request("post", url, params)
            stripe_object = util.convert_to_stripe_object(
                response, api_key, stripe_version, stripe_account
            )
            return stripe_object

        @util.class_method_variant("_cls_fail_card")
        def fail_card(self, idempotency_key=None, **params):
            url = "/v1/test_helpers/issuing/cards/{card}/shipping/fail".format(
                card=util.sanitize_id(self.get("id"))
            )
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource

        @classmethod
        def _cls_return_card(
            cls,
            card,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            requestor = api_requestor.APIRequestor(
                api_key, api_version=stripe_version, account=stripe_account
            )
            url = (
                "/v1/test_helpers/issuing/cards/{card}/shipping/return".format(
                    card=util.sanitize_id(card)
                )
            )
            response, api_key = requestor.request("post", url, params)
            stripe_object = util.convert_to_stripe_object(
                response, api_key, stripe_version, stripe_account
            )
            return stripe_object

        @util.class_method_variant("_cls_return_card")
        def return_card(self, idempotency_key=None, **params):
            url = (
                "/v1/test_helpers/issuing/cards/{card}/shipping/return".format(
                    card=util.sanitize_id(self.get("id"))
                )
            )
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource

        @classmethod
        def _cls_ship_card(
            cls,
            card,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            requestor = api_requestor.APIRequestor(
                api_key, api_version=stripe_version, account=stripe_account
            )
            url = "/v1/test_helpers/issuing/cards/{card}/shipping/ship".format(
                card=util.sanitize_id(card)
            )
            response, api_key = requestor.request("post", url, params)
            stripe_object = util.convert_to_stripe_object(
                response, api_key, stripe_version, stripe_account
            )
            return stripe_object

        @util.class_method_variant("_cls_ship_card")
        def ship_card(self, idempotency_key=None, **params):
            url = "/v1/test_helpers/issuing/cards/{card}/shipping/ship".format(
                card=util.sanitize_id(self.get("id"))
            )
            headers = util.populate_headers(idempotency_key)
            self.resource.refresh_from(
                self.resource.request("post", url, params, headers)
            )
            return self.resource
