import stripe
from stripe import util


class TestCustomMethod(object):
    @stripe.api_resources.abstract.custom_method(
        "do_stuff", http_verb="post", http_path="do_the_thing"
    )
    @stripe.api_resources.abstract.custom_method(
        "do_list_stuff", http_verb="get", http_path="do_the_list_thing"
    )
    @stripe.api_resources.abstract.custom_method(
        "do_stream_stuff",
        http_verb="post",
        http_path="do_the_stream_thing",
        is_streaming=True,
    )
    class MyResource(stripe.api_resources.abstract.APIResource):
        OBJECT_NAME = "myresource"

        def do_stuff(self, idempotency_key=None, **params):
            url = self.instance_url() + "/do_the_thing"
            self._request_and_refresh(
                "post", url, {**params, "idempotency_key": idempotency_key}
            )
            return self

        def do_stream_stuff(self, idempotency_key=None, **params):
            url = self.instance_url() + "/do_the_stream_thing"
            return self._request_stream(
                "post", url, {**params, "idempotency_key": idempotency_key}
            )

        @classmethod
        def _cls_do_stuff_new_codegen(cls, id, **params):
            return cls._static_request(
                "post",
                "/v1/myresources/{id}/do_the_thing".format(
                    id=util.sanitize_id(id)
                ),
                params=params,
            )

        @util.class_method_variant("_cls_do_stuff_new_codegen")
        def do_stuff_new_codegen(self, **params):
            return self._request(
                "post",
                "/v1/myresources/{id}/do_the_thing".format(
                    id=util.sanitize_id(self.get("id"))
                ),
                params=params,
            )

    def test_call_custom_method_class(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/v1/myresources/mid/do_the_thing",
            rbody='{"id": "mid", "thing_done": true}',
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyResource.do_stuff("mid", foo="bar")

        http_client_mock.assert_requested(
            "post",
            path="/v1/myresources/mid/do_the_thing",
            post_data="foo=bar",
        )
        assert obj.thing_done is True

    def test_call_custom_list_method_class_paginates(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path="/v1/myresources/mid/do_the_list_thing",
            query_string="param1=abc&param2=def",
            rbody='{"object": "list", "url": "/v1/myresources/mid/do_the_list_thing", "has_more": true, "data": [{"id": "cus_1", "object": "customer"}, {"id": "cus_2", "object": "customer"}]}',
            rheaders={"request-id": "req_123"},
        )

        resp = self.MyResource.do_list_stuff("mid", param1="abc", param2="def")

        http_client_mock.assert_requested(
            "get",
            path="/v1/myresources/mid/do_the_list_thing",
            query_string="param1=abc&param2=def",
        )

        # Stub out the second request which will happen automatically.
        http_client_mock.stub_request(
            "get",
            path="/v1/myresources/mid/do_the_list_thing",
            query_string="param1=abc&param2=def&starting_after=cus_2",
            rbody='{"object": "list", "url": "/v1/myresources/mid/do_the_list_thing", "has_more": false, "data": [{"id": "cus_3", "object": "customer"}]}',
            rheaders={"request-id": "req_123"},
        )

        # Iterate through entire content
        ids = []
        for i in resp.auto_paging_iter():
            ids.append(i.id)

        # Explicitly assert that the pagination parameter were kept for the
        # second request along with the starting_after param.
        http_client_mock.assert_requested(
            "get",
            path="/v1/myresources/mid/do_the_list_thing",
            query_string="param1=abc&param2=def&starting_after=cus_2",
        )

        assert ids == ["cus_1", "cus_2", "cus_3"]

    def test_call_custom_stream_method_class(self, http_client_mock_streaming):
        http_client_mock_streaming.stub_request(
            "post",
            path="/v1/myresources/mid/do_the_stream_thing",
            rbody=util.io.BytesIO(str.encode("response body")),
            rheaders={"request-id": "req_id"},
        )

        resp = self.MyResource.do_stream_stuff("mid", foo="bar")

        http_client_mock_streaming.assert_requested(
            "post",
            path="/v1/myresources/mid/do_the_stream_thing",
            post_data="foo=bar",
        )

        body_content = resp.io.read()
        if hasattr(body_content, "decode"):
            body_content = body_content.decode("utf-8")

        assert body_content == "response body"

    def test_call_custom_method_class_with_object(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/v1/myresources/mid/do_the_thing",
            rbody='{"id": "mid", "thing_done": true}',
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyResource.construct_from({"id": "mid"}, "mykey")
        self.MyResource.do_stuff(obj, foo="bar")

        http_client_mock.assert_requested(
            "post",
            path="/v1/myresources/mid/do_the_thing",
            post_data="foo=bar",
        )
        assert obj.thing_done is True

    def test_call_custom_stream_method_class_with_object(
        self, http_client_mock_streaming
    ):
        http_client_mock_streaming.stub_request(
            "post",
            path="/v1/myresources/mid/do_the_stream_thing",
            rbody=util.io.BytesIO(str.encode("response body")),
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyResource.construct_from({"id": "mid"}, "mykey")
        resp = self.MyResource.do_stream_stuff(obj, foo="bar")

        http_client_mock_streaming.assert_requested(
            "post",
            path="/v1/myresources/mid/do_the_stream_thing",
            post_data="foo=bar",
        )

        body_content = resp.io.read()
        if hasattr(body_content, "decode"):
            body_content = body_content.decode("utf-8")

        assert body_content == "response body"

    def test_call_custom_method_instance(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/v1/myresources/mid/do_the_thing",
            rbody='{"id": "mid", "thing_done": true}',
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyResource.construct_from({"id": "mid"}, "mykey")
        obj.do_stuff(foo="bar")

        http_client_mock.assert_requested(
            "post",
            path="/v1/myresources/mid/do_the_thing",
            post_data="foo=bar",
        )
        assert obj.thing_done is True

    def test_call_custom_stream_method_instance(
        self, http_client_mock_streaming
    ):
        http_client_mock_streaming.stub_request(
            "post",
            path="/v1/myresources/mid/do_the_stream_thing",
            rbody=util.io.BytesIO(str.encode("response body")),
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyResource.construct_from({"id": "mid"}, "mykey")
        resp = obj.do_stream_stuff(foo="bar")

        http_client_mock_streaming.assert_requested(
            "post",
            path="/v1/myresources/mid/do_the_stream_thing",
            post_data="foo=bar",
        )

        body_content = resp.io.read()
        if hasattr(body_content, "decode"):
            body_content = body_content.decode("utf-8")

        assert body_content == "response body"

    def test_call_custom_method_class_special_fields(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/v1/myresources/mid/do_the_thing",
            rbody='{"id": "mid", "thing_done": true}',
            rheaders={"request-id": "req_id"},
        )

        self.MyResource.do_stuff(
            "mid",
            foo="bar",
            stripe_version="2017-08-15",
            api_key="APIKEY",
            idempotency_key="IdempotencyKey",
            stripe_account="Acc",
        )

        http_client_mock.assert_requested(
            "post",
            path="/v1/myresources/mid/do_the_thing",
            post_data="foo=bar",
            api_key="APIKEY",
            stripe_version="2017-08-15",
            stripe_account="Acc",
            idempotency_key="IdempotencyKey",
        )

    def test_call_custom_method_class_newcodegen_special_fields(
        self, http_client_mock
    ):
        http_client_mock.stub_request(
            "post",
            path="/v1/myresources/mid/do_the_thing",
            rbody='{"id": "mid", "thing_done": true}',
            rheaders={"request-id": "req_id"},
        )

        self.MyResource.do_stuff_new_codegen(
            "mid",
            foo="bar",
            stripe_version="2017-08-15",
            api_key="APIKEY",
            idempotency_key="IdempotencyKey",
            stripe_account="Acc",
        )

        http_client_mock.assert_requested(
            "post",
            path="/v1/myresources/mid/do_the_thing",
            post_data="foo=bar",
            api_key="APIKEY",
            stripe_version="2017-08-15",
            stripe_account="Acc",
            idempotency_key="IdempotencyKey",
        )

    def test_call_custom_method_instance_newcodegen_special_fields(
        self, http_client_mock
    ):
        http_client_mock.stub_request(
            "post",
            path="/v1/myresources/mid/do_the_thing",
            rbody='{"id": "mid", "thing_done": true}',
            rheaders={"request-id": "req_id"},
        )

        obj = self.MyResource.construct_from({"id": "mid"}, "mykey")
        obj.do_stuff_new_codegen(
            foo="bar",
            stripe_version="2017-08-15",
            api_key="APIKEY",
            idempotency_key="IdempotencyKey",
            stripe_account="Acc",
            headers={"extra_header": "val"},
        )

        http_client_mock.assert_requested(
            "post",
            path="/v1/myresources/mid/do_the_thing",
            post_data="foo=bar",
            api_key="APIKEY",
            stripe_version="2017-08-15",
            stripe_account="Acc",
            idempotency_key="IdempotencyKey",
            extra_headers={"extra_header": "val"},
        )
