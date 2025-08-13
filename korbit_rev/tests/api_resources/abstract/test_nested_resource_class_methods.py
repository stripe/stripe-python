import stripe


class TestNestedResourceClassMethods(object):
    @stripe.api_resources.abstract.nested_resource_class_methods(
        "nested", operations=["create", "retrieve", "update", "delete", "list"]
    )
    class MainResource(stripe.api_resources.abstract.APIResource):
        OBJECT_NAME = "mainresource"

    def test_create_nested(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/v1/mainresources/id/nesteds",
            rbody='{"id": "nested_id", "object": "nested", "foo": "bar"}',
        )
        nested_resource = self.MainResource.create_nested("id", foo="bar")
        http_client_mock.assert_requested(
            "post", path="/v1/mainresources/id/nesteds", post_data="foo=bar"
        )
        assert nested_resource.foo == "bar"

    def test_retrieve_nested(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path="/v1/mainresources/id/nesteds/nested_id",
            rbody='{"id": "nested_id", "object": "nested", "foo": "bar"}',
        )
        nested_resource = self.MainResource.retrieve_nested("id", "nested_id")
        http_client_mock.assert_requested(
            "get",
            path="/v1/mainresources/id/nesteds/nested_id",
            query_string="",
        )
        assert nested_resource.foo == "bar"

    def test_modify_nested(self, http_client_mock):
        http_client_mock.stub_request(
            "post",
            path="/v1/mainresources/id/nesteds/nested_id",
            rbody='{"id": "nested_id", "object": "nested", "foo": "baz"}',
        )
        nested_resource = self.MainResource.modify_nested(
            "id", "nested_id", foo="baz"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/mainresources/id/nesteds/nested_id",
            post_data="foo=baz",
        )
        assert nested_resource.foo == "baz"

    def test_delete_nested(self, http_client_mock):
        http_client_mock.stub_request(
            "delete",
            path="/v1/mainresources/id/nesteds/nested_id",
            rbody='{"id": "nested_id", "object": "nested", "deleted": true}',
        )
        nested_resource = self.MainResource.delete_nested("id", "nested_id")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/mainresources/id/nesteds/nested_id",
            query_string="",
        )
        assert nested_resource.deleted is True

    def test_list_nesteds(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path="/v1/mainresources/id/nesteds",
            rbody='{"object": "list", "data": []}',
        )
        nested_resource = self.MainResource.list_nesteds("id")
        http_client_mock.assert_requested(
            "get", path="/v1/mainresources/id/nesteds", query_string=""
        )
        assert isinstance(nested_resource.data, list)
