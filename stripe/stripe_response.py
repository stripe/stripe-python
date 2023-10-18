from io import IOBase
import json
from collections import OrderedDict
from typing import Dict


class StripeResponseBase(object):
    code: int
    headers: Dict[str, str]

    def __init__(self, code, headers):
        self.code = code
        self.headers = headers

    @property
    def idempotency_key(self):
        try:
            return self.headers["idempotency-key"]
        except KeyError:
            return None

    @property
    def request_id(self):
        try:
            return self.headers["request-id"]
        except KeyError:
            return None


class StripeResponse(StripeResponseBase):
    body: str
    data: object

    def __init__(self, body, code, headers):
        StripeResponseBase.__init__(self, code, headers)
        self.body = body
        self.data = json.loads(body, object_pairs_hook=OrderedDict)


class StripeStreamResponse(StripeResponseBase):
    io: IOBase

    def __init__(self, io, code, headers):
        StripeResponseBase.__init__(self, code, headers)
        self.io = io
