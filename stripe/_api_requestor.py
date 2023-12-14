from io import BytesIO, IOBase
import json
import platform
from typing import (
    Any,
    Dict,
    List,
    Mapping,
    Optional,
    Tuple,
    cast,
)
from typing_extensions import NoReturn
import uuid
import warnings

# breaking circular dependency
import stripe  # noqa: IMP101
from stripe import _http_client, _util, _version
from stripe import oauth_error  # noqa: SPY101
from stripe._encode import _api_encode
from stripe._multipart_data_generator import MultipartDataGenerator
from urllib.parse import urlencode, urlsplit, urlunsplit
from stripe._stripe_response import StripeResponse, StripeStreamResponse


def _build_api_url(url, query):
    scheme, netloc, path, base_query, fragment = urlsplit(url)

    if base_query:
        query = "%s&%s" % (base_query, query)

    return urlunsplit((scheme, netloc, path, query, fragment))


class APIRequestor(object):
    api_key: Optional[str]
    api_base: str
    api_version: str
    stripe_account: Optional[str]

    def __init__(
        self,
        key=None,
        client=None,
        api_base=None,
        api_version=None,
        account=None,
    ):
        self.api_base = api_base or stripe.api_base
        self.api_key = key
        self.api_version = api_version or stripe.api_version
        self.stripe_account = account

        self._default_proxy = None

        from stripe import verify_ssl_certs as verify
        from stripe import proxy

        if client:
            self._client = client
        elif stripe.default_http_client:
            self._client = stripe.default_http_client
            if proxy != self._default_proxy:
                warnings.warn(
                    "stripe.proxy was updated after sending a "
                    "request - this is a no-op. To use a different proxy, "
                    "set stripe.default_http_client to a new client "
                    "configured with the proxy."
                )
        else:
            # If the stripe.default_http_client has not been set by the user
            # yet, we'll set it here. This way, we aren't creating a new
            # HttpClient for every request.
            stripe.default_http_client = _http_client.new_default_http_client(
                verify_ssl_certs=verify, proxy=proxy
            )
            self._client = stripe.default_http_client
            self._default_proxy = proxy

    @classmethod
    @_util.deprecated(
        "This method is internal to stripe-python and the public interface will be removed in a future stripe-python version"
    )
    def format_app_info(cls, info):
        return cls._format_app_info(info)

    @classmethod
    def _format_app_info(cls, info):
        str = info["name"]
        if info["version"]:
            str += "/%s" % (info["version"],)
        if info["url"]:
            str += " (%s)" % (info["url"],)
        return str

    def request(
        self,
        method: str,
        url: str,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
        *,
        _usage: Optional[List[str]] = None,
    ) -> Tuple[StripeResponse, str]:
        rbody, rcode, rheaders, my_api_key = self.request_raw(
            method.lower(),
            url,
            params,
            headers,
            is_streaming=False,
            _usage=_usage,
        )
        resp = self.interpret_response(rbody, rcode, rheaders)
        return resp, my_api_key

    def request_stream(
        self,
        method: str,
        url: str,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
        *,
        _usage: Optional[List[str]] = None,
    ) -> Tuple[StripeStreamResponse, str]:
        stream, rcode, rheaders, my_api_key = self.request_raw(
            method.lower(),
            url,
            params,
            headers,
            is_streaming=True,
            _usage=_usage,
        )
        resp = self.interpret_streaming_response(
            # TODO: should be able to remove this cast once self._client.request_stream_with_retries
            # returns a more specific type.
            cast(IOBase, stream),
            rcode,
            rheaders,
        )
        return resp, my_api_key

    def handle_error_response(self, rbody, rcode, resp, rheaders) -> NoReturn:
        try:
            error_data = resp["error"]
        except (KeyError, TypeError):
            raise stripe.APIError(
                "Invalid response object from API: %r (HTTP response code "
                "was %d)" % (rbody, rcode),
                rbody,
                rcode,
                resp,
            )

        err = None

        # OAuth errors are a JSON object where `error` is a string. In
        # contrast, in API errors, `error` is a hash with sub-keys. We use
        # this property to distinguish between OAuth and API errors.
        if isinstance(error_data, str):
            err = self.specific_oauth_error(
                rbody, rcode, resp, rheaders, error_data
            )

        if err is None:
            err = self.specific_api_error(
                rbody, rcode, resp, rheaders, error_data
            )

        raise err

    def specific_api_error(self, rbody, rcode, resp, rheaders, error_data):
        _util.log_info(
            "Stripe API error received",
            error_code=error_data.get("code"),
            error_type=error_data.get("type"),
            error_message=error_data.get("message"),
            error_param=error_data.get("param"),
        )

        # Rate limits were previously coded as 400's with code 'rate_limit'
        if rcode == 429 or (
            rcode == 400 and error_data.get("code") == "rate_limit"
        ):
            return stripe.RateLimitError(
                error_data.get("message"), rbody, rcode, resp, rheaders
            )
        elif rcode in [400, 404]:
            if error_data.get("type") == "idempotency_error":
                return stripe.IdempotencyError(
                    error_data.get("message"), rbody, rcode, resp, rheaders
                )
            else:
                return stripe.InvalidRequestError(
                    error_data.get("message"),
                    error_data.get("param"),
                    error_data.get("code"),
                    rbody,
                    rcode,
                    resp,
                    rheaders,
                )
        elif rcode == 401:
            return stripe.AuthenticationError(
                error_data.get("message"), rbody, rcode, resp, rheaders
            )
        elif rcode == 402:
            return stripe.CardError(
                error_data.get("message"),
                error_data.get("param"),
                error_data.get("code"),
                rbody,
                rcode,
                resp,
                rheaders,
            )
        elif rcode == 403:
            return stripe.PermissionError(
                error_data.get("message"), rbody, rcode, resp, rheaders
            )
        else:
            return stripe.APIError(
                error_data.get("message"), rbody, rcode, resp, rheaders
            )

    def specific_oauth_error(self, rbody, rcode, resp, rheaders, error_code):
        description = resp.get("error_description", error_code)

        _util.log_info(
            "Stripe OAuth error received",
            error_code=error_code,
            error_description=description,
        )

        args = [error_code, description, rbody, rcode, resp, rheaders]

        if error_code == "invalid_client":
            return oauth_error.InvalidClientError(*args)
        elif error_code == "invalid_grant":
            return oauth_error.InvalidGrantError(*args)
        elif error_code == "invalid_request":
            return oauth_error.InvalidRequestError(*args)
        elif error_code == "invalid_scope":
            return oauth_error.InvalidScopeError(*args)
        elif error_code == "unsupported_grant_type":
            return oauth_error.UnsupportedGrantTypeError(*args)
        elif error_code == "unsupported_response_type":
            return oauth_error.UnsupportedResponseTypeError(*args)

        return None

    def request_headers(self, api_key, method):
        user_agent = "Stripe/v1 PythonBindings/%s" % (_version.VERSION,)
        if stripe.app_info:
            user_agent += " " + self._format_app_info(stripe.app_info)

        ua = {
            "bindings_version": _version.VERSION,
            "lang": "python",
            "publisher": "stripe",
            "httplib": self._client.name,
        }
        for attr, func in [
            ["lang_version", platform.python_version],
            ["platform", platform.platform],
            ["uname", lambda: " ".join(platform.uname())],
        ]:
            try:
                val = func()
            except Exception:
                val = "(disabled)"
            ua[attr] = val
        if stripe.app_info:
            ua["application"] = stripe.app_info

        headers = {
            "X-Stripe-Client-User-Agent": json.dumps(ua),
            "User-Agent": user_agent,
            "Authorization": "Bearer %s" % (api_key,),
        }

        if self.stripe_account:
            headers["Stripe-Account"] = self.stripe_account

        if method == "post":
            headers["Content-Type"] = "application/x-www-form-urlencoded"
            headers.setdefault("Idempotency-Key", str(uuid.uuid4()))

        headers["Stripe-Version"] = self.api_version

        return headers

    def request_raw(
        self,
        method: str,
        url: str,
        params: Optional[Mapping[str, Any]] = None,
        supplied_headers: Optional[Mapping[str, str]] = None,
        is_streaming: bool = False,
        *,
        _usage: Optional[List[str]] = None,
    ) -> Tuple[object, int, Mapping[str, str], str]:
        """
        Mechanism for issuing an API call
        """

        supplied_headers_dict: Optional[Dict[str, str]] = (
            dict(supplied_headers) if supplied_headers is not None else None
        )

        if self.api_key:
            my_api_key = self.api_key
        else:
            from stripe import api_key

            my_api_key = api_key

        if my_api_key is None:
            raise stripe.AuthenticationError(
                "No API key provided. (HINT: set your API key using "
                '"stripe.api_key = <API-KEY>"). You can generate API keys '
                "from the Stripe web interface.  See https://stripe.com/api "
                "for details, or email support@stripe.com if you have any "
                "questions."
            )

        abs_url = "%s%s" % (self.api_base, url)

        encoded_params = urlencode(list(_api_encode(params or {})))

        # Don't use strict form encoding by changing the square bracket control
        # characters back to their literals. This is fine by the server, and
        # makes these parameter strings easier to read.
        encoded_params = encoded_params.replace("%5B", "[").replace("%5D", "]")

        if method == "get" or method == "delete":
            if params:
                abs_url = _build_api_url(abs_url, encoded_params)
            post_data = None
        elif method == "post":
            if (
                supplied_headers_dict is not None
                and supplied_headers_dict.get("Content-Type")
                == "multipart/form-data"
            ):
                generator = MultipartDataGenerator()
                generator.add_params(params or {})
                post_data = generator.get_post_data()
                supplied_headers_dict[
                    "Content-Type"
                ] = "multipart/form-data; boundary=%s" % (generator.boundary,)
            else:
                post_data = encoded_params
        else:
            raise stripe.APIConnectionError(
                "Unrecognized HTTP method %r.  This may indicate a bug in the "
                "Stripe bindings.  Please contact support@stripe.com for "
                "assistance." % (method,)
            )

        headers = self.request_headers(my_api_key, method)
        if supplied_headers_dict is not None:
            for key, value in supplied_headers_dict.items():
                headers[key] = value

        _util.log_info("Request to Stripe api", method=method, path=abs_url)
        _util.log_debug(
            "Post details",
            post_data=encoded_params,
            api_version=self.api_version,
        )

        if is_streaming:
            (
                rcontent,
                rcode,
                rheaders,
            ) = self._client.request_stream_with_retries(
                method, abs_url, headers, post_data, _usage=_usage
            )
        else:
            rcontent, rcode, rheaders = self._client.request_with_retries(
                method, abs_url, headers, post_data, _usage=_usage
            )

        _util.log_info(
            "Stripe API response", path=abs_url, response_code=rcode
        )
        _util.log_debug("API response body", body=rcontent)

        if "Request-Id" in rheaders:
            request_id = rheaders["Request-Id"]
            _util.log_debug(
                "Dashboard link for request",
                link=_util.dashboard_link(request_id),
            )

        return rcontent, rcode, rheaders, my_api_key

    def _should_handle_code_as_error(self, rcode):
        return not 200 <= rcode < 300

    def interpret_response(
        self, rbody: object, rcode: int, rheaders: Mapping[str, str]
    ) -> StripeResponse:
        try:
            if hasattr(rbody, "decode"):
                # TODO: should be able to remove this cast once self._client.request_with_retries
                # returns a more specific type.
                rbody = cast(bytes, rbody).decode("utf-8")
            resp = StripeResponse(
                cast(str, rbody),
                rcode,
                rheaders,
            )
        except Exception:
            raise stripe.APIError(
                "Invalid response body from API: %s "
                "(HTTP response code was %d)" % (rbody, rcode),
                cast(bytes, rbody),
                rcode,
                rheaders,
            )
        if self._should_handle_code_as_error(rcode):
            self.handle_error_response(rbody, rcode, resp.data, rheaders)
        return resp

    def interpret_streaming_response(
        self, stream: IOBase, rcode: int, rheaders: Mapping[str, str]
    ) -> StripeStreamResponse:
        # Streaming response are handled with minimal processing for the success
        # case (ie. we don't want to read the content). When an error is
        # received, we need to read from the stream and parse the received JSON,
        # treating it like a standard JSON response.
        if self._should_handle_code_as_error(rcode):
            if hasattr(stream, "getvalue"):
                json_content = cast(BytesIO, stream).getvalue()
            elif hasattr(stream, "read"):
                json_content = stream.read()
            else:
                raise NotImplementedError(
                    "HTTP client %s does not return an IOBase object which "
                    "can be consumed when streaming a response."
                )

            self.interpret_response(json_content, rcode, rheaders)
            # interpret_response is guaranteed to throw since we've checked self._should_handle_code_as_error
            raise RuntimeError(
                "interpret_response should have raised an error"
            )
        else:
            return StripeStreamResponse(stream, rcode, rheaders)
