import stripe
from stripe._test_helpers import APIResourceTestHelpers


class TestTestHelperAPIResource(object):
    class MyTestHelpersResource(stripe.api_resources.abstract.APIResource):
        OBJECT_NAME = "myresource"

        @stripe.api_resources.abstract.custom_method(
            "do_stuff", http_verb="post", http_path="do_the_thing"
        )
        class TestHelpers(APIResourceTestHelpers):
            def __init__(self, resource):
                self.resource = resource

            def do_stuff(self, idempotency_key=None, **params):
                url = self.instance_url() + "/do_the_thing"
                self.resource._request_and_refresh(
                    "post", url, {**params, "idempotency_key": idempotency_key}
                )
                return self.resource

        @property
        def test_helpers(self):
            return self.TestHelpers(self)

    MyTestHelpersResource.TestHelpers._resource_cls = MyTestHelpersResource

    def test_call_custom_method_class(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/v1/test_helpers/myresources/mid/do_the_thing",
            rbody='{"id": "mid", "thing_done": true}',
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyTestHelpersResource.TestHelpers.do_stuff("mid", foo="bar")

        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/myresources/mid/do_the_thing",
            post_data="foo=bar",
        )
        assert obj.thing_done is True

    def test_call_custom_method_instance_via_property(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/v1/test_helpers/myresources/mid/do_the_thing",
            rbody='{"id": "mid", "thing_done": true}',
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyTestHelpersResource.construct_from({"id": "mid"}, "mykey")
        obj.test_helpers.do_stuff(foo="bar")

        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/myresources/mid/do_the_thing",
            post_data="foo=bar",
        )
        assert obj.thing_done is True
