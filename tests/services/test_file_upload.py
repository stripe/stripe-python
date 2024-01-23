from __future__ import absolute_import, division, print_function

import tempfile

import stripe


TEST_RESOURCE_ID = "file_123"


class TestFileUpload(object):
    def test_is_listable(self, http_client_mock, stripe_mock_stripe_client):
        resources = stripe_mock_stripe_client.files.list()
        http_client_mock.assert_requested("get", path="/v1/files")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.FileUpload)

    def test_is_retrievable(self, http_client_mock, stripe_mock_stripe_client):
        resource = stripe_mock_stripe_client.files.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/files/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.FileUpload)

    def test_is_creatable(
        self,
        file_stripe_mock_stripe_client,
        http_client_mock,
    ):
        stripe.multipart_data_generator.MultipartDataGenerator._initialize_boundary = (
            lambda self: 1234567890
        )
        test_file = tempfile.TemporaryFile()

        # We create a new client here instead of re-using the stripe_mock_stripe_client fixture
        # because stripe_mock_stripe_client overrides the "api" base address, which we want to
        # be empty for this test.
        resource = file_stripe_mock_stripe_client.files.create(
            params={
                "purpose": "dispute_evidence",
                "file": test_file,
                "file_link_data": {"create": True},
            }
        )
        http_client_mock.assert_requested(
            "post",
            api_base=stripe.upload_api_base,
            path="/v1/files",
            content_type="multipart/form-data; boundary=1234567890",
        )
        assert isinstance(resource, stripe.FileUpload)
