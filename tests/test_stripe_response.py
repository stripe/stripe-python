from __future__ import absolute_import, division, print_function

import json
from collections import OrderedDict

from stripe import six
from stripe.stripe_response import StripeResponse


class TestStripeResponse(object):
    def test_idempotency_key(self):
        response, headers, _, _ = self.mock_stripe_response()
        assert response.idempotency_key == headers["idempotency-key"]

    def test_request_id(self):
        response, headers, _, _ = self.mock_stripe_response()
        assert response.request_id == headers["request-id"]

    def test_code(self):
        response, _, _, code = self.mock_stripe_response()
        assert response.code == code

    def test_headers(self):
        response, headers, _, _ = self.mock_stripe_response()
        assert response.headers == headers

    def test_body(self):
        response, _, body, _ = self.mock_stripe_response()
        assert response.body == body

    def test_data(self):
        response, _, body, _ = self.mock_stripe_response()
        deserialized = json.loads(body, object_pairs_hook=OrderedDict)
        assert response.data == deserialized

        # Previous assert does not check order, so explicitly check order here
        assert list(six.iterkeys(response.data["metadata"])) == list(
            six.iterkeys(deserialized["metadata"])
        )

    @staticmethod
    def mock_stripe_response():
        code = 200
        headers = TestStripeResponse.mock_headers()
        body = TestStripeResponse.mock_body()
        response = StripeResponse(body, code, headers)
        return response, headers, body, code

    @staticmethod
    def mock_headers():
        return {"idempotency-key": "123456", "request-id": "req_123456"}

    @staticmethod
    def mock_body():
        return """{
    "id": "ch_12345",
    "object": "charge",
    "amount": 1,
    "metadata": {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5"
    }
}"""
