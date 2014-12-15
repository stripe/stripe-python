import random
import sys
import io


class MultipartDataGenerator(object):
    def __init__(self, chunk_size=1028):
        self.data = io.BytesIO()
        self.line_break = "\r\n"
        self.boundary = self._initialize_boundary()
        self.chunk_size = chunk_size

    def add_params(self, params):
        for key, value in params.iteritems():
            if value is None:
                continue

            self._write(self.param_header())
            self._write(self.line_break)
            if hasattr(value, 'read'):
                self._write("Content-Disposition: form-data; name=\"%s\"; "
                            "filename=\"%s\"" % (key, value.name))
                self._write(self.line_break)
                self._write("Content-Type: application/octet-stream")
                self._write(self.line_break)
                self._write(self.line_break)

                self._write_file(value)
            else:
                self._write("Content-Disposition: form-data; name=\"%s\"" %
                            (key,))
                self._write(self.line_break)
                self._write(self.line_break)
                self._write(value)

            self._write(self.line_break)

    def param_header(self):
        return "--%s" % self.boundary

    def get_post_data(self):
        self._write("--%s--" % (self.boundary,))
        self._write(self.line_break)
        return self.data.getvalue()

    def _write(self, value):
        if sys.version_info < (3, 0):
            self.data.write(value)
        else:
            self.data.write(bytes(value, 'utf-8'))

    def _write_file(self, f):
        while True:
            file_contents = f.read(self.chunk_size)
            if not file_contents:
                break
            self._write(file_contents)

    def _initialize_boundary(self):
        return random.randint(0, 2**63)
