# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from stripe import oauth_error


class TestOAuthError(object):
    def test_error_object(self):
        err = oauth_error.OAuthError(
            "message", "description", json_body={"error": "some_oauth_error"}
        )
        assert err.error is not None
        assert err.error.error == "some_oauth_error"
