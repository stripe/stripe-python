import tempfile

import stripe
from stripe.test.helper import StripeResourceTest


class FileUploadTest(StripeResourceTest):

    def test_create_file_upload(self):
        test_file = tempfile.TemporaryFile()
        stripe.FileUpload.create(
            purpose='dispute_evidence',
            file=test_file
        )
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/files',
            params={
                'purpose': 'dispute_evidence',
                'file': test_file
            },
            headers={'Content-Type': 'multipart/form-data'}
        )

    def test_fetch_file_upload(self):
        stripe.FileUpload.retrieve("fil_foo")
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/files/fil_foo',
            {},
            None
        )

    def test_list_file_uploads(self):
        stripe.FileUpload.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/files',
            {}
        )
