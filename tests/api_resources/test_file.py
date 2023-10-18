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

    def test_is_listable(self, request_mock):
        resources = stripe.File.list()
        request_mock.assert_requested("get", "/v1/files")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.File)

    def test_is_retrievable(self, request_mock):
        resource = stripe.File.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested("get", "/v1/files/%s" % TEST_RESOURCE_ID)
        assert isinstance(resource, stripe.File)

    def test_is_creatable(self, mocker):
        hc = mocker.Mock(stripe.http_client.HTTPClient)
        hc.name = "mockclient"
        stripe.default_http_client = hc
        hc.request_with_retries.return_value = ('{"object": "file"}', 200, {})
        stripe.multipart_data_generator.MultipartDataGenerator._initialize_boundary = (
            lambda self: 1234567890
        )
        test_file = tempfile.TemporaryFile()
        resource = stripe.File.create(
            purpose="dispute_evidence",
            file=test_file,
            file_link_data={"create": True},
        )
        method, url, headers, body = hc.request_with_retries.call_args[0]
        assert method == "post"
        assert url.endswith("/v1/files")
        assert (
            headers["Content-Type"]
            == "multipart/form-data; boundary=1234567890"
        )
        parts = body.split(b"--1234567890")
        assert len(parts) == 5
        assert parts[0] == b""
        assert b'name="purpose"' in parts[1]
        assert b'name="file"' in parts[2]
        assert b'name="file_link_data[create]"' in parts[3]
        assert isinstance(resource, stripe.File)

    def test_create_respects_stripe_version(
        self, setup_upload_api_base, request_mock
    ):
        test_file = tempfile.TemporaryFile()
        stripe.File.create(
            purpose="dispute_evidence", file=test_file, stripe_version="foo"
        )
        request_mock.assert_api_version("foo")

    # You can use api_version instead of stripe_version
    # in File.create. We preserve it for backwards compatibility
    def test_create_respects_api_version(
        self, setup_upload_api_base, request_mock
    ):
        test_file = tempfile.TemporaryFile()
        stripe.File.create(
            purpose="dispute_evidence", file=test_file, api_version="foo"
        )
        request_mock.assert_api_version("foo")

    def test_deserializes_from_file(self):
        obj = stripe.util.convert_to_stripe_object({"object": "file"})
        assert isinstance(obj, stripe.File)

    def test_deserializes_from_file_upload(self):
        obj = stripe.util.convert_to_stripe_object({"object": "file_upload"})
        assert isinstance(obj, stripe.File)
