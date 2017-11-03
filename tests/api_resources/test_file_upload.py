from __future__ import absolute_import, division, print_function

import tempfile

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'file_123'


class FileUploadTest(StripeTestCase):
    FIXTURE = {
        'id': TEST_RESOURCE_ID,
        'object': 'file_upload'
    }

    def test_is_listable(self):
        self.stub_request(
            'get',
            '/v1/files',
            {
                'object': 'list',
                'data': [self.FIXTURE],
            }
        )

        resources = stripe.FileUpload.list()
        self.assert_requested(
            'get',
            '/v1/files'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.FileUpload)

    def test_is_retrievable(self):
        self.stub_request(
            'get',
            '/v1/files/%s' % TEST_RESOURCE_ID,
            self.FIXTURE
        )

        resource = stripe.FileUpload.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/files/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.FileUpload)

    def test_is_creatable(self):
        self.stub_request(
            'post',
            '/v1/files',
            self.FIXTURE
        )

        test_file = tempfile.TemporaryFile()
        resource = stripe.FileUpload.create(
            purpose='dispute_evidence',
            file=test_file
        )
        self.assert_requested(
            'post',
            '/v1/files',
            headers={'Content-Type': 'multipart/form-data'}
        )
        self.assertIsInstance(resource, stripe.FileUpload)
