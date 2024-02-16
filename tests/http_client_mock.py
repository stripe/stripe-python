from __future__ import absolute_import, division, print_function
from typing import List

import stripe
from urllib.parse import urlsplit, urlencode, parse_qsl
import json
from unittest.mock import Mock


def parse_and_sort(query_string, strict_parsing=False):
    """
    Helper function to parse a query string and return a sorted list of tuples.
    """
    return sorted(parse_qsl(query_string, strict_parsing=strict_parsing))


def extract_api_base(abs_url):
    """
    Helper function to extract the api_base from an absolute URL.
    """
    return urlsplit(abs_url).scheme + "://" + urlsplit(abs_url).netloc


class StripeRequestCall(object):
    def __init__(
        self,
        method=None,
        abs_url=None,
        headers=None,
        post_data=None,
        usage=None,
        max_network_retries=None,
    ):
        self.method = method
        self.abs_url = abs_url
        self.headers = headers
        self.post_data = post_data
        self.usage = usage
        self.max_network_retries = max_network_retries

    @classmethod
    def from_mock_call(cls, mock_call):
        return cls(
            method=mock_call[0][0],
            abs_url=mock_call[0][1],
            headers=mock_call[0][2],
            post_data=mock_call[0][3],
            usage=mock_call[1]["_usage"],
            max_network_retries=mock_call[1]["max_network_retries"],
        )

    def __repr__(self):
        return "<StripeRequestCall method={method} abs_url={abs_url} headers={headers} post_data={post_data}>".format(
            method=self.method,
            abs_url=self.abs_url,
            headers=self.headers,
            post_data=self.post_data,
        )

    def get_raw_header(self, header):
        if self.headers is None:
            return None
        return self.headers.get(header)

    def check(
        self,
        method=None,
        abs_url=None,
        api_base=None,
        path=None,
        query_string=None,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        stripe_context=None,
        content_type=None,
        idempotency_key=None,
        user_agent=None,
        extra_headers=None,
        post_data=None,
        is_json=False,
        usage=None,
        max_network_retries=None,
    ):
        # METHOD
        if method is not None:
            self.assert_method(method)

        # URL
        if abs_url is not None:
            self.assert_abs_url(abs_url)
        if api_base is not None:
            self.assert_api_base(api_base)
        if path is not None:
            self.assert_path(path)
        if query_string is not None:
            self.assert_query_string(query_string)

        # HEADERS
        if api_key is not None:
            self.assert_header("Authorization", "Bearer %s" % (api_key,))
        if stripe_version is not None:
            self.assert_header("Stripe-Version", stripe_version)
        if stripe_account is not None:
            self.assert_header("Stripe-Account", stripe_account)
        if stripe_context is not None:
            self.assert_header("Stripe-Context", stripe_context)
        if content_type is not None:
            self.assert_header("Content-Type", content_type)
        if idempotency_key is not None:
            self.assert_header("Idempotency-Key", idempotency_key)
        if user_agent is not None:
            self.assert_header("User-Agent", user_agent)
        if extra_headers is not None:
            self.assert_extra_headers(extra_headers)
        if usage is not None:
            self.assert_usage(usage)

        # BODY
        if post_data is not None:
            self.assert_post_data(post_data, is_json=is_json)

        # OPTIONS
        if max_network_retries is not None:
            self.assert_max_network_retries(max_network_retries)

        return True

    def assert_max_network_retries(self, expected):
        actual = self.max_network_retries
        if actual != expected:
            raise AssertionError(
                "Expected max_network_retries to be %s, got %s"
                % (expected, actual)
            )

    def assert_method(self, expected):
        if self.method != expected:
            raise AssertionError(
                "Expected request method %s, got %s" % (expected, self.method)
            )

    def assert_abs_url(self, expected):
        expected_url = urlsplit(expected)
        self.assert_api_base(extract_api_base(expected))
        self.assert_path(expected_url.path)
        self.assert_query_string(expected_url.query)

    def assert_api_base(self, expected):
        actual_base = (
            urlsplit(self.abs_url).scheme
            + "://"
            + urlsplit(self.abs_url).netloc
        )
        if actual_base != expected:
            raise AssertionError(
                "Expected URL base %s, got %s" % (expected, actual_base)
            )

    def assert_path(self, expected):
        actual_path = urlsplit(self.abs_url).path
        if actual_path != expected:
            raise AssertionError(
                "Expected URL path %s, got %s" % (expected, actual_path)
            )

    def assert_query_string(self, expected):
        splitted = urlsplit(self.abs_url)
        actual_query = None
        if splitted.query:
            actual_query = splitted.query
        actual_query_params = parse_and_sort(actual_query)
        expected_query_params = parse_and_sort(expected)
        if actual_query_params != expected_query_params:
            raise AssertionError(
                "Expected URL query string %s, got %s"
                % (expected, actual_query)
            )

    def assert_header(self, header, expected):
        actual = self.headers.get(header)
        if actual != expected:
            raise AssertionError(
                "Expected %s to be %s, got %s" % (header, expected, actual)
            )

    def assert_extra_headers(self, expected):
        for header, value in expected.items():
            actual_value = self.headers.get(header)
            if actual_value != value:
                raise AssertionError(
                    "Expected header %s to be %s, got %s"
                    % (header, value, actual_value)
                )

    def assert_usage(self, expected):
        if self.usage != expected:
            raise AssertionError(
                "Expected usage to be %s, got %s" % (expected, self.usage)
            )

    def assert_post_data(self, expected, is_json=False):
        actual_data = self.post_data
        expected_data = expected
        if is_json:
            actual_data = json.loads(self.post_data)
            expected_data = json.loads(expected)
        elif expected:  # only attempt to parse non-empty query strings
            actual_data = parse_and_sort(self.post_data, strict_parsing=True)
            expected_data = parse_and_sort(expected, strict_parsing=True)
        if actual_data != expected_data:
            raise AssertionError(
                "Expected POST data %s, got %s" % (expected, self.post_data)
            )


class HTTPClientMock(object):
    def __init__(self, mocker):
        self.mock_client = mocker.Mock(
            wraps=stripe.http_client.new_default_http_client(
                async_fallback_client=stripe.http_client.new_http_client_async_fallback()
            )
        )

        self.mock_client._verify_ssl_certs = True
        self.mock_client.name = "mockclient"
        self.registered_responses = {}
        self.funcs = [
            self.mock_client.request_with_retries,
            self.mock_client.request_stream_with_retries,
            self.mock_client.request_with_retries_async,
            self.mock_client.request_stream_with_retries_async,
        ]
        self.func_call_order = []

    def get_mock_http_client(self) -> Mock:
        return self.mock_client

    def stub_request(
        self,
        method,
        path="",
        query_string="",
        rbody="{}",
        rcode=200,
        rheaders={},
    ) -> None:
        def custom_side_effect_for_func(func):
            def custom_side_effect(
                called_method, called_abs_url, *args, **kwargs
            ):
                self.func_call_order.append(func)
                called_path = urlsplit(called_abs_url).path
                called_query = ""
                if urlsplit(called_abs_url).query:
                    called_query = urlencode(
                        parse_and_sort(urlsplit(called_abs_url).query)
                    )
                if (
                    called_method,
                    called_path,
                    called_query,
                ) not in self.registered_responses:
                    raise AssertionError(
                        "Unexpected request made to %s %s %s"
                        % (called_method, called_path, called_query)
                    )
                ret = self.registered_responses[
                    (called_method, called_path, called_query)
                ]
                if func._mock_name.endswith("async"):
                    return awaitable(ret)
                return ret

            return custom_side_effect

        async def awaitable(x):
            return x

        self.registered_responses[
            (method, path, urlencode(parse_and_sort(query_string)))
        ] = (rbody, rcode, rheaders)

        for func in self.funcs:
            func.side_effect = custom_side_effect_for_func(func)

    def get_last_call(self) -> StripeRequestCall:
        if len(self.func_call_order) == 0:
            raise AssertionError(
                "Expected request to have been made, but no calls were found."
            )
        return StripeRequestCall.from_mock_call(
            self.func_call_order[-1].call_args
        )

    def get_all_calls(self) -> List[StripeRequestCall]:
        calls_by_func = {
            func: list(func.call_args_list) for func in self.funcs
        }

        calls = []
        for func in self.func_call_order:
            calls.append(calls_by_func[func].pop(0))

        return [
            StripeRequestCall.from_mock_call(call_args) for call_args in calls
        ]

    def find_call(
        self, method, api_base, path, query_string
    ) -> StripeRequestCall:
        for func in self.funcs:
            for call_args in func.call_args_list:
                request_call = StripeRequestCall.from_mock_call(call_args)
                try:
                    if request_call.check(
                        method=method,
                        api_base=api_base,
                        path=path,
                        query_string=query_string,
                    ):
                        return request_call
                except AssertionError:
                    pass
        raise AssertionError(
            "Expected request to have been made, but no calls were found."
        )

    def assert_requested(
        self,
        method=None,
        abs_url=None,
        api_base=None,
        path=None,
        query_string=None,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        stripe_context=None,
        content_type=None,
        idempotency_key=None,
        user_agent=None,
        extra_headers=None,
        post_data=None,
        is_json=False,
        usage=None,
        max_network_retries=None,
    ) -> None:
        if abs_url and (api_base or path or query_string):
            raise ValueError(
                "Received both `abs_url` and one of `api_base`, `path`, or `query_string`. Please only use `abs_url`."
            )

        if abs_url:
            api_base = extract_api_base(abs_url)
            path = urlsplit(abs_url).path
            query_string = urlsplit(abs_url).query

        last_call = self.find_call(method, api_base, path, query_string)

        last_call.check(
            method=method,
            abs_url=abs_url,
            api_base=api_base,
            path=path,
            query_string=query_string,
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            stripe_context=stripe_context,
            content_type=content_type,
            idempotency_key=idempotency_key,
            user_agent=user_agent,
            extra_headers=extra_headers,
            post_data=post_data,
            is_json=is_json,
            usage=usage,
            max_network_retries=max_network_retries,
        )

    def assert_no_request(self):
        for func in self.funcs:
            if func.called:
                msg = (
                    "Expected no request to have been made, but %s calls were "
                    "found." % (sum([func.call_count for func in self.funcs]))
                )
                raise AssertionError(msg)

    def reset_mock(self):
        for func in self.funcs:
            func.reset_mock()
        self.registered_responses = {}
