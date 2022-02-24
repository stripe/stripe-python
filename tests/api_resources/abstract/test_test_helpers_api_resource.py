from __future__ import absolute_import, division, print_function

import pytest

import stripe
from stripe import util


class TestTestHelperAPIResource(object):

    @stripe.api_resources.abstract.test_helpers
    class MyTestHelpersResource(stripe.api_resources.abstract.APIResource):
        OBJECT_NAME = "myresource"

        @stripe.api_resources.abstract.custom_method("do_stuff", http_verb="post", http_path="do_the_thing")
        class TestHelpers:
            def __init__(self, resource):
                self.resource = resource

            def do_stuff(self, idempotency_key=None, **params):
                url = self.resource.instance_url() + "/do_the_thing"
                headers = util.populate_headers(idempotency_key)
                self.resource.refresh_from(self.resource.request("post", url, params, headers))
                return self.resource


    def test_call_custom_method_class(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v1/myresources/mid/do_the_thing",
            {"id": "mid", "thing_done": True},
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyTestHelpersResource.TestHelpers.do_stuff("mid", foo="bar")

        request_mock.assert_requested(
            "post", "/v1/myresources/mid/do_the_thing", {"foo": "bar"}
        )
        assert obj.thing_done is True

    def test_call_custom_method_instance(self, request_mock):
        request_mock.stub_request(
            "post",
            "/v1/myresources/mid/do_the_thing",
            {"id": "mid", "thing_done": True},
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyTestHelpersResource.construct_from({"id": "mid"}, "mykey")
        obj.test_helpers.do_stuff(foo="bar")

        request_mock.assert_requested(
            "post", "/v1/myresources/mid/do_the_thing", {"foo": "bar"}
        )
        assert obj.thing_done is True
