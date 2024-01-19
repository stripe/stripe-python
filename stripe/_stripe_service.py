from stripe._api_requestor import _APIRequestor


class StripeService(object):
    _requestor: _APIRequestor

    def __init__(self, requestor):
        self._requestor = requestor
