import tempfile

import pytest

import stripe
from stripe import File
from stripe._multipart_data_generator import MultipartDataGenerator
from stripe._util import convert_to_stripe_object


TEST_RESOURCE_ID = "file_123"


class TestFileUpload(object):
    @pytest.fixture(scope="function")
    def setup_upload_api_base(self):
        stripe.upload_api_base = stripe.api_base
        stripe.api_base = None
        yield
        stripe.api_base = stripe.upload_api_base
        stripe.upload_api_base = "https://files.stripe.com"

    def test_is_listable(self, http_client_mock):
        resources = File.list()
        http_client_mock.assert_requested("get", path="/v1/files")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], File)

    def test_is_retrievable(self, http_client_mock):
        resource = File.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/files/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, File)

    def test_is_creatable(self, setup_upload_api_base, http_client_mock):
        MultipartDataGenerator._initialize_boundary = lambda self: 1234567890
        test_file = tempfile.TemporaryFile()
        resource = File.create(
            purpose="dispute_evidence",
            file=test_file,
            file_link_data={"create": True},
        )
        http_client_mock.assert_requested(
            "post",
            api_base=stripe.upload_api_base,
            path="/v1/files",
            content_type="multipart/form-data; boundary=1234567890",
        )
        assert isinstance(resource, File)

    def test_deserializes_from_file(self):
        obj = convert_to_stripe_object({"object": "file"}, api_mode="V1")
        assert isinstance(obj, File)

    def test_deserializes_from_file_upload(self):
        obj = convert_to_stripe_object(
            {"object": "file_upload"}, api_mode="V1"
        )
        assert isinstance(obj, File)
