import re
import sys

from stripe.multipart_data_generator import MultipartDataGenerator
from stripe.test.helper import StripeTestCase


class MultipartDataGeneratorTests(StripeTestCase):

    def test_generate_simple_multipart_data(self):
        with open(__file__) as test_file:
            params = {
                "key1": "value1",
                "key2": "value2",
                "key3": test_file
                }
            generator = MultipartDataGenerator()
            generator.add_params(params)
            post_data = generator.get_post_data()

            if sys.version_info < (3, 0):
                http_body = "".join([line for line in post_data])
            else:
                byte_array = bytearray([i for i in post_data])
                http_body = byte_array.decode('utf-8')

            self.assertTrue(re.search(
                r"Content-Disposition: form-data; name=\"key1\"", http_body))
            self.assertTrue(re.search(
                r"Content-Disposition: form-data; name=\"key2\"", http_body))
            self.assertTrue(re.search(
                r"Content-Disposition: form-data; name=\"key3\"; "
                r"filename=\".+\"",
                http_body))
            self.assertTrue(re.search(
                r"Content-Type: application/octet-stream", http_body))

            test_file.seek(0)
            file_contents = test_file.read()
            self.assertNotEqual(-1, http_body.find(file_contents))
