from __future__ import absolute_import, division, print_function

from stripe import api_requestor, util
from stripe.stripe_object import StripeObject

from stripe.six.moves.urllib.parse import quote_plus


class ListObject(StripeObject):
    OBJECT_NAME = "list"

    def list(
        self, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        stripe_object = self._request(
            "get",
            self.get("url"),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            **params
        )
        stripe_object._retrieve_params = params
        return stripe_object

    def auto_paging_iter(self):
        page = self
        params = dict(self._retrieve_params)

        while True:
            item_id = None
            for item in page:
                item_id = item.get("id", None)
                yield item

            if not getattr(page, "has_more", False) or item_id is None:
                return

            params["starting_after"] = item_id
            page = self.list(**params)

    def create(
        self,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return self._request(
            "post",
            self.get("url"),
            api_key=api_key,
            idempotency_key=idempotency_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            **params
        )

    def retrieve(
        self,
        id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        url = "%s/%s" % (self.get("url"), quote_plus(util.utf8(id)))
        return self._request(
            "get",
            url,
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            **params
        )

    def __iter__(self):
        return getattr(self, "data", []).__iter__()

    def __len__(self):
        return getattr(self, "data", []).__len__()

    def _request(
        self,
        method,
        url,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        api_key = api_key or self.api_key
        stripe_version = stripe_version or self.stripe_version
        stripe_account = stripe_account or self.stripe_account

        requestor = api_requestor.APIRequestor(
            api_key, api_version=stripe_version, account=stripe_account
        )
        headers = util.populate_headers(idempotency_key)
        response, api_key = requestor.request(method, url, params, headers)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        return stripe_object
