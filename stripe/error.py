from __future__ import absolute_import, division, print_function

from stripe.six import python_2_unicode_compatible


@python_2_unicode_compatible
class StripeError(Exception):

    def __init__(self, message=None, http_body=None, http_status=None,
                 json_body=None, headers=None, code=None):
        super(StripeError, self).__init__(message)

        if http_body and hasattr(http_body, 'decode'):
            try:
                http_body = http_body.decode('utf-8')
            except BaseException:
                http_body = ('<Could not decode body as utf-8. '
                             'Please report to support@stripe.com>')

        self._message = message
        self.http_body = http_body
        self.http_status = http_status
        self.json_body = json_body
        self.headers = headers or {}
        self.code = code
        self.request_id = self.headers.get('request-id', None)

    def __str__(self):
        msg = self._message or "<empty message>"
        if self.request_id is not None:
            return u"Request {0}: {1}".format(self.request_id, msg)
        else:
            return msg

    # Returns the underlying `Exception` (base class) message, which is usually
    # the raw message returned by Stripe's API. This was previously available
    # in python2 via `error.message`. Unlike `str(error)`, it omits "Request
    # req_..." from the beginning of the string.
    @property
    def user_message(self):
        return self._message


class APIError(StripeError):
    pass


class APIConnectionError(StripeError):
    pass


class CardError(StripeError):

    def __init__(self, message, param, code, http_body=None,
                 http_status=None, json_body=None, headers=None):
        super(CardError, self).__init__(
            message, http_body, http_status, json_body,
            headers, code)
        self.param = param


class IdempotencyError(StripeError):
    pass


class InvalidRequestError(StripeError):

    def __init__(self, message, param, code=None, http_body=None,
                 http_status=None, json_body=None, headers=None):
        super(InvalidRequestError, self).__init__(
            message, http_body, http_status, json_body,
            headers, code)
        self.param = param


class AuthenticationError(StripeError):
    pass


class PermissionError(StripeError):
    pass


class RateLimitError(StripeError):
    pass


class SignatureVerificationError(StripeError):
    def __init__(self, message, sig_header, http_body=None):
        super(SignatureVerificationError, self).__init__(
            message, http_body)
        self.sig_header = sig_header
