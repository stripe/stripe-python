# Exceptions
class StripeError(Exception):

    def __init__(self, message=None, http_body=None, http_status=None,
                 json_body=None):
        super(StripeError, self).__init__(message)
        self.http_body = http_body and http_body.decode('utf-8')
        self.http_status = http_status
        self.json_body = json_body


class APIError(StripeError):
    pass


class APIConnectionError(StripeError):
    pass


class CardError(StripeError):

    def __init__(self, message, param, code, http_body=None,
                 http_status=None, json_body=None):
        super(CardError, self).__init__(message,
                                        http_body, http_status, json_body)
        self.param = param
        self.code = code
        self.http_body = http_body and http_body.decode('utf-8')
        self.http_status = http_status
        self.json_body = json_body


class InvalidRequestError(StripeError):

    def __init__(self, message, param, http_body=None,
                 http_status=None, json_body=None):
        super(InvalidRequestError, self).__init__(
            message, http_body, http_status, json_body)
        self.param = param


class AuthenticationError(StripeError):
    pass
