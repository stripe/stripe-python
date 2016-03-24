# -*- encoding: utf-8 -*-

import re
import sys

from stripe.multipart_data_generator import MultipartDataGenerator
from stripe.test.helper import StripeTestCase


class MultipartDataGeneratorTests(StripeTestCase):

    def run_test_multipart_data_with_file(self, test_file):
        params = {
            "key1": b"ASCII value",
            "key2": u"Üñìçôdé value",
            "key3": test_file
        }
        generator = MultipartDataGenerator()
        generator.add_params(params)
        http_body = generator.get_post_data()

        if sys.version_info >= (3,):
            http_body = http_body.decode('utf-8')

        self.assertTrue(re.search(
            r"Content-Disposition: form-data; name=\"key1\"", http_body))
        self.assertTrue(re.search(r"ASCII value", http_body))
        self.assertTrue(re.search(
            r"Content-Disposition: form-data; name=\"key2\"", http_body))
        self.assertTrue(re.search(r"Üñìçôdé value", http_body))
        self.assertTrue(re.search(
            r"Content-Disposition: form-data; name=\"key3\"; "
            r"filename=\".+\"",
            http_body))
        self.assertTrue(re.search(
            r"Content-Type: application/octet-stream", http_body))

        test_file.seek(0)
        file_contents = test_file.read()

        if sys.version_info >= (3,) and isinstance(file_contents, bytes):
            file_contents = file_contents.decode('utf-8')

        self.assertNotEqual(-1, http_body.find(file_contents))

    def test_multipart_data_file_text(self):
        with open(__file__, mode='r') as test_file:
            self.run_test_multipart_data_with_file(test_file)

    def test_multipart_data_file_binary(self):
        with open(__file__, mode='rb') as test_file:
            self.run_test_multipart_data_with_file(test_file)
