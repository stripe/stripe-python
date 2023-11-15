from stripe.error import StripeError


class OAuthError(StripeError):
    def __init__(
        self,
        code,
        description,
        http_body=None,
        http_status=None,
        json_body=None,
        headers=None,
    ):
        super(OAuthError, self).__init__(
            description, http_body, http_status, json_body, headers, code
        )

    def construct_error_object(self):
        if self.json_body is None:
            return None

        from stripe import api_key
        return stripe.api_resources.error_object.OAuthErrorObject.construct_from(  # type: ignore
            self.json_body, api_key
        )


class InvalidClientError(OAuthError):
    pass


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
