from __future__ import absolute_import, division, print_function

import tempfile

import pytest

import stripe


TEST_RESOURCE_ID = 'file_123'


class TestFileUpload(object):
    @pytest.fixture
    def file_upload_dict(self):
        return {
            'id': TEST_RESOURCE_ID,
            'object': 'file_upload'
        }

    def test_is_listable(self, request_mock, file_upload_dict):
        request_mock.stub_request(
            'get',
            '/v1/files',
            {
                'object': 'list',
                'data': [file_upload_dict],
            }
        )

        resources = stripe.FileUpload.list()
        request_mock.assert_requested(
            'get',
            '/v1/files'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.FileUpload)

    def test_is_retrievable(self, request_mock, file_upload_dict):
        request_mock.stub_request(
            'get',
            '/v1/files/%s' % TEST_RESOURCE_ID,
            file_upload_dict
        )

        resource = stripe.FileUpload.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/files/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.FileUpload)

    def test_is_creatable(self, request_mock, file_upload_dict):
        request_mock.stub_request(
            'post',
            '/v1/files',
            file_upload_dict
        )

        test_file = tempfile.TemporaryFile()
        resource = stripe.FileUpload.create(
            purpose='dispute_evidence',
            file=test_file
        )
        request_mock.assert_requested(
            'post',
            '/v1/files',
            headers={'Content-Type': 'multipart/form-data'}
        )
        assert isinstance(resource, stripe.FileUpload)
