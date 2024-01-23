from stripe._api_requestor import APIRequestor


class StripeService(object):
    _requestor: APIRequestor

    def __init__(self, requestor):
        self._requestor = requestor
