from __future__ import absolute_import, division, print_function

from stripe import api_requestor, error, util
from stripe.stripe_object import StripeObject
from urllib.parse import quote_plus


class APIResource(StripeObject):
    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    def refresh(self):
        return self._request_and_refresh("get", self.instance_url())

    @classmethod
    def class_url(cls):
        if cls == APIResource:
            raise NotImplementedError(
                "APIResource is an abstract class.  You should perform "
                "actions on its subclasses (e.g. Charge, Customer)"
            )
        # Namespaces are separated in object names with periods (.) and in URLs
        # with forward slashes (/), so replace the former with the latter.
        base = cls.OBJECT_NAME.replace(".", "/")
        return "/v1/%ss" % (base,)

    def instance_url(self):
        id = self.get("id")

        if not isinstance(id, str):
            raise error.InvalidRequestError(
                "Could not determine which URL to request: %s instance "
                "has invalid ID: %r, %s. ID should be of type `str` (or"
                " `unicode`)" % (type(self).__name__, id, type(id)),
                "id",
            )

        base = self.class_url()
        extn = quote_plus(id)
        return "%s/%s" % (base, extn)

    # The `method_` and `url_` arguments are suffixed with an underscore to
    # avoid conflicting with actual request parameters in `params`.
    def _request(
        self,
        method_,
        url_,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        headers=None,
        params=None,
    ):
        obj = StripeObject._request(
            self,
            method_,
            url_,
            api_key,
            idempotency_key,
            stripe_version,
            stripe_account,
            headers,
            params,
        )

        if type(self) is type(obj):
            self.refresh_from(obj)
            return self
        else:
            return obj

    # The `method_` and `url_` arguments are suffixed with an underscore to
    # avoid conflicting with actual request parameters in `params`.
    def _request_and_refresh(
        self,
        method_,
        url_,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        headers=None,
        params=None,
    ):
        obj = StripeObject._request(
            self,
            method_,
            url_,
            api_key,
            idempotency_key,
            stripe_version,
            stripe_account,
            headers,
            params,
        )

        self.refresh_from(obj)
        return self

    # The `method_` and `url_` arguments are suffixed with an underscore to
    # avoid conflicting with actual request parameters in `params`.
    @classmethod
    def _static_request(
        cls,
        method_,
        url_,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        params=None,
    ):
        params = None if params is None else params.copy()
        api_key = util.read_special_variable(params, "api_key", api_key)
        idempotency_key = util.read_special_variable(
            params, "idempotency_key", idempotency_key
        )
        stripe_version = util.read_special_variable(
            params, "stripe_version", stripe_version
        )
        stripe_account = util.read_special_variable(
            params, "stripe_account", stripe_account
        )
        headers = util.read_special_variable(params, "headers", None)

        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )

        if idempotency_key is not None:
            headers = {} if headers is None else headers.copy()
            headers.update(util.populate_headers(idempotency_key))

        response, api_key = requestor.request(method_, url_, params, headers)
        return util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account, params
        )

    # The `method_` and `url_` arguments are suffixed with an underscore to
    # avoid conflicting with actual request parameters in `params`.
    @classmethod
    def _static_request_stream(
        cls,
        method_,
        url_,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        params=None,
    ):
        params = None if params is None else params.copy()
        api_key = util.read_special_variable(params, "api_key", api_key)
        idempotency_key = util.read_special_variable(
            params, "idempotency_key", idempotency_key
        )
        stripe_version = util.read_special_variable(
            params, "stripe_version", stripe_version
        )
        stripe_account = util.read_special_variable(
            params, "stripe_account", stripe_account
        )
        headers = util.read_special_variable(params, "headers", None)

        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )

        if idempotency_key is not None:
            headers = {} if headers is None else headers.copy()
            headers.update(util.populate_headers(idempotency_key))

        response, _ = requestor.request_stream(method_, url_, params, headers)
        return response
