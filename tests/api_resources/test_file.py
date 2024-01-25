import tempfile

import pytest

import stripe


TEST_RESOURCE_ID = "file_123"


class TestFile(object):
    @pytest.fixture(scope="function")
    def setup_upload_api_base(self):
        stripe.upload_api_base = stripe.api_base
        stripe.api_base = None
        yield
        stripe.api_base = stripe.upload_api_base
        stripe.upload_api_base = "https://files.stripe.com"

    def test_is_listable(self, http_client_mock):
        resources = stripe.File.list()
        http_client_mock.assert_requested("get", path="/v1/files")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.File)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.File.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/files/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.File)

    def test_is_creatable(self, setup_upload_api_base, http_client_mock):
        stripe.multipart_data_generator.MultipartDataGenerator._initialize_boundary = (
            lambda self: 1234567890
        )
        test_file = tempfile.TemporaryFile()
        resource = stripe.File.create(
            purpose="dispute_evidence",
            file=test_file,
            file_link_data={"create": True},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/files",
            api_base=stripe.upload_api_base,
            content_type="multipart/form-data; boundary=1234567890",
        )
        assert isinstance(resource, stripe.File)

    def test_create_respects_stripe_version(
        self, setup_upload_api_base, http_client_mock
    ):
        test_file = tempfile.TemporaryFile()
        stripe.File.create(
            purpose="dispute_evidence", file=test_file, stripe_version="foo"
        )
        http_client_mock.assert_requested(
            "post",
            api_base=stripe.upload_api_base,
            path="/v1/files",
            stripe_version="foo",
        )

    # You can use api_version instead of stripe_version
    # in File.create. We preserve it for backwards compatibility
    def test_create_respects_api_version(
        self, setup_upload_api_base, http_client_mock
    ):
        test_file = tempfile.TemporaryFile()
        stripe.File.create(
            purpose="dispute_evidence", file=test_file, stripe_version="foo"
        )
        http_client_mock.assert_requested(
            "post",
            api_base=stripe.upload_api_base,
            path="/v1/files",
            stripe_version="foo",
        )

    def test_deserializes_from_file(self):
        obj = stripe.util.convert_to_stripe_object(
            {"object": "file"}, api_mode="V1"
        )
        assert isinstance(obj, stripe.File)

    def test_deserializes_from_file_upload(self):
        obj = stripe.util.convert_to_stripe_object(
            {"object": "file_upload"}, api_mode="V1"
        )
        assert isinstance(obj, stripe.File)
