from __future__ import absolute_import, division, print_function

import json

from stripe.stripe_response import StripeResponse


class TestStripeResponse(object):
    def test_idempotency_key(self):
        response, headers, body, code = self.mock_stripe_response()
        assert response.idempotency_key == headers["idempotency-key"]

    def test_request_id(self):
        response, headers, body, code = self.mock_stripe_response()
        assert response.request_id == headers["request-id"]

    def test_code(self):
        response, headers, body, code = self.mock_stripe_response()
        assert response.code == code

    def test_headers(self):
        response, headers, body, code = self.mock_stripe_response()
        assert response.headers == headers

    def test_body(self):
        response, headers, body, code = self.mock_stripe_response()
        assert response.body == body

    def test_data(self):
        response, headers, body, code = self.mock_stripe_response()
        assert response.data == json.loads(body)

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
        return '{ "id": "ch_12345", "object": "charge", "amount": 1 }'
