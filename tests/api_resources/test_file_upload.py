from __future__ import absolute_import, division, print_function

import tempfile

import pytest

import stripe


TEST_RESOURCE_ID = 'file_123'


class TestFileUpload(object):
    @pytest.fixture(scope='function')
    def setup_upload_api_base(self):
        stripe.upload_api_base = stripe.api_base
        stripe.api_base = None
        yield
        stripe.api_base = stripe.upload_api_base
        stripe.upload_api_base = 'https://files.stripe.com'

    def test_is_listable(self, request_mock):
        resources = stripe.FileUpload.list()
        request_mock.assert_requested(
            'get',
            '/v1/files'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.FileUpload)

    def test_is_retrievable(self, request_mock):
        resource = stripe.FileUpload.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/files/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.FileUpload)

    def test_is_creatable(self, setup_upload_api_base, request_mock):
        stripe.multipart_data_generator.MultipartDataGenerator\
            ._initialize_boundary = lambda self: 1234567890
        test_file = tempfile.TemporaryFile()
        resource = stripe.FileUpload.create(
            purpose='dispute_evidence',
            file=test_file
        )
        request_mock.assert_api_base(stripe.upload_api_base)
        request_mock.assert_requested(
            'post',
            '/v1/files',
            headers={
                'Content-Type': 'multipart/form-data; boundary=1234567890',
            }
        )
        assert isinstance(resource, stripe.FileUpload)

    def test_deserializes_from_file(self):
        obj = stripe.util.convert_to_stripe_object({
            'object': 'file',
        })
        assert isinstance(obj, stripe.FileUpload)

    def test_deserializes_from_file_upload(self):
        obj = stripe.util.convert_to_stripe_object({
            'object': 'file_upload',
        })
        assert isinstance(obj, stripe.FileUpload)
