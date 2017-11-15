from stripe import util


class StripeResponse:

    def __init__(self, body, code, headers):
        self.body = body
        self.code = code
        self.headers = headers
        self.data = util.json.loads(body)

    @property
    def idempotency_key(self):
        try:
            return self.headers['idempotency-key']
        except KeyError:
            return None

    @property
    def request_id(self):
        try:
            return self.headers['request-id']
        except KeyError:
            return None
