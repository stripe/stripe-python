from stripe._api_requestor import APIRequestor
from stripe._client_options import _ClientOptions

from typing import Optional


class StripeService(object):
    _requestor: APIRequestor
    _options: Optional[_ClientOptions]

    def __init__(self, requestor, options=None):
        self._requestor = requestor
        self._options = options
