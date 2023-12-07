# Used for global variables
import stripe  # noqa: IMP101
from stripe._error import AuthenticationError
from stripe._api_requestor import APIRequestor
from stripe._encode import _api_encode
from urllib.parse import urlencode


class OAuth(object):
    @staticmethod
    def _set_client_id(params):
        if "client_id" in params:
            return

        from stripe import client_id

        if client_id:
            params["client_id"] = client_id
            return

        raise AuthenticationError(
            "No client_id provided. (HINT: set your client_id using "
            '"stripe.client_id = <CLIENT-ID>"). You can find your client_ids '
            "in your Stripe dashboard at "
            "https://dashboard.stripe.com/account/applications/settings, "
            "after registering your account as a platform. See "
            "https://stripe.com/docs/connect/standalone-accounts for details, "
            "or email support@stripe.com if you have any questions."
        )

    @staticmethod
    def authorize_url(express=False, **params):
        if express is False:
            path = "/oauth/authorize"
        else:
            path = "/express/oauth/authorize"

        OAuth._set_client_id(params)
        if "response_type" not in params:
            params["response_type"] = "code"
        query = urlencode(list(_api_encode(params)))
        url = stripe.connect_api_base + path + "?" + query
        return url

    @staticmethod
    def token(api_key=None, **params):
        requestor = APIRequestor(api_key, api_base=stripe.connect_api_base)
        response, _ = requestor.request("post", "/oauth/token", params, None)
        return response.data

    @staticmethod
    def deauthorize(api_key=None, **params):
        requestor = APIRequestor(api_key, api_base=stripe.connect_api_base)
        OAuth._set_client_id(params)
        response, _ = requestor.request(
            "post", "/oauth/deauthorize", params, None
        )
        return response.data
