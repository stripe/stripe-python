# -*- coding: utf-8 -*-


import random
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
        with open(__file__, mode="r", encoding="utf-8") as test_file:
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

    def test_boundary_is_not_derived_from_the_random_module(self):
        # Seeding the `random` module must not determine the boundary. A
        # boundary an attacker can predict lets a caller-influenced value
        # (including file bytes) inject additional parts.
        random.seed(0)
        first = MultipartDataGenerator().boundary
        random.seed(0)
        second = MultipartDataGenerator().boundary

        assert first != second
        assert re.fullmatch(r"[0-9a-f]{60}", first)
        assert re.fullmatch(r"[0-9a-f]{60}", second)

    @staticmethod
    def lines_starting_with(http_body, prefix):
        return [
            line for line in http_body.split("\r\n") if line.startswith(prefix)
        ]

    def test_escapes_quotes_and_crlf_in_param_names(self):
        injected = 'a\r\nContent-Disposition: form-data; name="purpose'
        generator = MultipartDataGenerator()
        generator.add_params({injected: "value"})
        http_body = generator.get_post_data().decode("utf-8")

        # The injected CRLF must not begin a second header line, and the
        # injected quote must not end the quoted-string early.
        assert self.lines_starting_with(http_body, "Content-Disposition:") == [
            'Content-Disposition: form-data; name="a  Content-Disposition: '
            'form-data; name=%22purpose"'
        ]
        # One opening delimiter and one closing delimiter: a single part.
        assert http_body.count("--%s" % generator.boundary) == 2

    def test_escapes_quotes_and_crlf_in_file_names(self):
        test_file = io.StringIO("foo")
        test_file.name = 'a\r\nX-Injected: yes"b.png'
        generator = MultipartDataGenerator()
        generator.add_params({"file": test_file})
        http_body = generator.get_post_data().decode("utf-8")

        assert self.lines_starting_with(http_body, "Content-Disposition:") == [
            'Content-Disposition: form-data; name="file"; '
            'filename="a  X-Injected: yes%22b.png"'
        ]
        assert self.lines_starting_with(http_body, "X-Injected:") == []
        assert http_body.count("--%s" % generator.boundary) == 2
