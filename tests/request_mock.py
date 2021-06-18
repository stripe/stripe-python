from __future__ import absolute_import, division, print_function

import json

import stripe
from stripe import six, util
from stripe.stripe_response import StripeResponse, StripeStreamResponse


class RequestMock(object):
    def __init__(self, mocker):
        self._mocker = mocker

        self._real_request = stripe.api_requestor.APIRequestor.request
        self._real_request_stream = (
            stripe.api_requestor.APIRequestor.request_stream
        )
        self._stub_request_handler = StubRequestHandler()

        self.constructor_patcher = self._mocker.patch(
            "stripe.api_requestor.APIRequestor.__init__",
            side_effect=stripe.api_requestor.APIRequestor.__init__,
            autospec=True,
        )

        self.request_patcher = self._mocker.patch(
            "stripe.api_requestor.APIRequestor.request",
            side_effect=self._patched_request,
            autospec=True,
        )

        self.request_stream_patcher = self._mocker.patch(
            "stripe.api_requestor.APIRequestor.request_stream",
            side_effect=self._patched_request_stream,
            autospec=True,
        )

    def _patched_request(self, requestor, method, url, *args, **kwargs):
        response = self._stub_request_handler.get_response(
            method, url, expect_stream=False
        )
        if response is not None:
            return response, stripe.api_key

        return self._real_request(requestor, method, url, *args, **kwargs)

    def _patched_request_stream(self, requestor, method, url, *args, **kwargs):
        response = self._stub_request_handler.get_response(
            method, url, expect_stream=True
        )
        if response is not None:
            return response, stripe.api_key

        return self._real_request_stream(
            requestor, method, url, *args, **kwargs
        )

    def stub_request(self, method, url, rbody={}, rcode=200, rheaders={}):
        self._stub_request_handler.register(
            method, url, rbody, rcode, rheaders, is_streaming=False
        )

    def stub_request_stream(
        self, method, url, rbody={}, rcode=200, rheaders={}
    ):
        self._stub_request_handler.register(
            method, url, rbody, rcode, rheaders, is_streaming=True
        )

    def assert_api_base(self, expected_api_base):
        # Note that this method only checks that an API base was provided
        # as a keyword argument in APIRequestor's constructor, not as a
        # positional argument.

        if "api_base" not in self.constructor_patcher.call_args[1]:
            msg = (
                "Expected APIRequestor to have been constructed with "
                "api_base='%s'. No API base was provided." % expected_api_base
            )
            raise AssertionError(msg)

        actual_api_base = self.constructor_patcher.call_args[1]["api_base"]
        if actual_api_base != expected_api_base:
            msg = (
                "Expected APIRequestor to have been constructed with "
                "api_base='%s'. Constructed with api_base='%s' "
                "instead." % (expected_api_base, actual_api_base)
            )
            raise AssertionError(msg)

    def assert_api_version(self, expected_api_version):
        # Note that this method only checks that an API version was provided
        # as a keyword argument in APIRequestor's constructor, not as a
        # positional argument.

        if "api_version" not in self.constructor_patcher.call_args[1]:
            msg = (
                "Expected APIRequestor to have been constructed with "
                "api_version='%s'. No API version was provided."
                % expected_api_version
            )
            raise AssertionError(msg)

        actual_api_version = self.constructor_patcher.call_args[1][
            "api_version"
        ]
        if actual_api_version != expected_api_version:
            msg = (
                "Expected APIRequestor to have been constructed with "
                "api_version='%s'. Constructed with api_version='%s' "
                "instead." % (expected_api_version, actual_api_version)
            )
            raise AssertionError(msg)

    def assert_requested(self, method, url, params=None, headers=None):
        self.assert_requested_internal(
            self.request_patcher, method, url, params, headers
        )

    def assert_requested_stream(self, method, url, params=None, headers=None):
        self.assert_requested_internal(
            self.request_stream_patcher, method, url, params, headers
        )

    def assert_requested_internal(self, patcher, method, url, params, headers):
        params = params or self._mocker.ANY
        headers = headers or self._mocker.ANY
        called = False
        exception = None

        # Sadly, ANY does not match a missing optional argument, so we
        # check all the possible signatures of the request method
        possible_called_args = [
            (self._mocker.ANY, method, url),
            (self._mocker.ANY, method, url, params),
            (self._mocker.ANY, method, url, params, headers),
        ]

        for args in possible_called_args:
            try:
                patcher.assert_called_with(*args)
            except AssertionError as e:
                exception = e
            else:
                called = True
                break

        if not called:
            raise exception

    def assert_no_request(self):
        if self.request_patcher.call_count != 0:
            msg = (
                "Expected 'request' to not have been called. "
                "Called %s times." % (self.request_patcher.call_count)
            )
            raise AssertionError(msg)

    def assert_no_request_stream(self):
        if self.request_stream_patcher.call_count != 0:
            msg = (
                "Expected 'request_stream' to not have been called. "
                "Called %s times." % (self.request_stream_patcher.call_count)
            )
            raise AssertionError(msg)

    def reset_mock(self):
        self.request_patcher.reset_mock()
        self.request_stream_patcher.reset_mock()


class StubRequestHandler(object):
    def __init__(self):
        self._entries = {}

    def register(
        self, method, url, rbody={}, rcode=200, rheaders={}, is_streaming=False
    ):
        self._entries[(method, url)] = (rbody, rcode, rheaders, is_streaming)

    def get_response(self, method, url, expect_stream=False):
        if (method, url) in self._entries:
            rbody, rcode, rheaders, is_streaming = self._entries.pop(
                (method, url)
            )

            if expect_stream != is_streaming:
                return None

            if not isinstance(rbody, six.string_types):
                rbody = json.dumps(rbody)
            if is_streaming:
                stripe_response = StripeStreamResponse(
                    util.io.BytesIO(str.encode(rbody)), rcode, rheaders
                )
            else:
                stripe_response = StripeResponse(rbody, rcode, rheaders)
            return stripe_response

        return None
