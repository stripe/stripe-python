# -*- coding: utf-8 -*-


import json
import pickle

import pytest

from stripe import oauth_error


class TestOAuthError(object):
    def test_error_object(self):
        err = oauth_error.OAuthError(
            "message", "description", json_body={"error": "some_oauth_error"}
        )
        assert err.error is not None
        assert err.error.error == "some_oauth_error"


@pytest.mark.parametrize(
    "error_class",
    [
        oauth_error.OAuthError,
        oauth_error.InvalidClientError,
        oauth_error.InvalidGrantError,
        oauth_error.InvalidRequestError,
        oauth_error.InvalidScopeError,
        oauth_error.UnsupportedGrantTypeError,
        oauth_error.UnsupportedResponseTypeError,
    ],
)
def test_oauth_error_round_trips(error_class):
    err = error_class(
        code="oauth_code",
        description="description",
        http_body=b"body",
        http_status=400,
        json_body={"error": "oauth_code"},
        headers={"request-id": "req_123"},
    )
    json_args = json.loads(json.dumps(err.args))

    for round_tripped in (
        pickle.loads(pickle.dumps(err)),
        error_class(*json_args),
    ):
        assert type(round_tripped) is error_class
        assert round_tripped.args == err.args
        assert vars(round_tripped) == vars(err)
