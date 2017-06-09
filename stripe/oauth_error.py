from stripe.error import StripeError


class OAuthError(StripeError):
    def __init__(self, code, description, http_body=None,
                 http_status=None, json_body=None, headers=None):
        super(OAuthError, self).__init__(
            description, http_body, http_status, json_body, headers)
        self.code = code


class InvalidGrantError(OAuthError):
    pass


class InvalidRequestError(OAuthError):
    pass


class InvalidScopeError(OAuthError):
    pass


class UnsupportedGrantTypeError(OAuthError):
    pass


class UnsupportedResponseTypeError(OAuthError):
    pass
