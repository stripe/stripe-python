# -*- coding: utf-8 -*-


import re
import io

from stripe._multipart_data_generator import MultipartDataGenerator


class TestMultipartDataGenerator(object):
    def run_test_multipart_data_with_file(self, test_file):
        params = {
            "key1": b"ASCII value",
            "key2": "Üñìçôdé value",
            "key3": test_file,
            "key4": {
                "string": "Hello!",
                "int": 234,
                "float": 3.14159,
                "bool": True,
                "dict": {"foo": "bar"},
            },
        }
        generator = MultipartDataGenerator()
        generator.add_params(params)
        http_body = generator.get_post_data().decode("utf-8")

        assert re.search(
            r"Content-Disposition: form-data; name=\"key1\"", http_body
        )
        assert re.search(r"ASCII value", http_body)
        assert re.search(
            r"Content-Disposition: form-data; name=\"key2\"", http_body
        )
        assert re.search(r"Üñìçôdé value", http_body)
        assert re.search(
            r"Content-Disposition: form-data; name=\"key3\"; "
            r"filename=\".+\"",
            http_body,
        )
        assert re.search(r"Content-Type: application/octet-stream", http_body)
        assert re.search(
            r"Content-Disposition: form-data; name=\"key4\[string\]\"",
            http_body,
        )
        assert re.search(r"Hello!", http_body)
        assert re.search(
            r"Content-Disposition: form-data; name=\"key4\[int\]\"", http_body
        )
        assert re.search(r"234", http_body)
        assert re.search(
            r"Content-Disposition: form-data; name=\"key4\[float\]\"",
            http_body,
        )
        assert re.search(r"3.14159", http_body)
        assert re.search(
            r"Content-Disposition: form-data; name=\"key4\[bool\]\"", http_body
        )
        assert re.search(r"true", http_body)
        assert re.search(
            r"Content-Disposition: form-data; name=\"key4\[dict\]\[foo\]\"",
            http_body,
        )
        assert re.search(r"bar", http_body)

        test_file.seek(0)
        file_contents = test_file.read()

        if isinstance(file_contents, bytes):
            file_contents = file_contents.decode("utf-8")

        assert http_body.find(file_contents) != -1

    def test_multipart_data_file_text(self):
        with open(__file__, mode="r") as test_file:
            self.run_test_multipart_data_with_file(test_file)

    def test_multipart_data_file_binary(self):
        with open(__file__, mode="rb") as test_file:
            self.run_test_multipart_data_with_file(test_file)

    def test_multipart_data_stringio(self):
        string = io.StringIO("foo")
        self.run_test_multipart_data_with_file(string)

    def test_multipart_data_unicode_file_name(self):
        string = io.StringIO("foo")
        string.name = "паспорт.png"
        self.run_test_multipart_data_with_file(string)
