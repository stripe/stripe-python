from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject


class SearchResultObject(StripeObject):
    OBJECT_NAME = "search_result"

    def search(
        self, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        return self._request(
            "get",
            self.get("url"),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    def __getitem__(self, k):
        if isinstance(k, str):
            return super(SearchResultObject, self).__getitem__(k)
        else:
            raise KeyError(
                "You tried to access the %s index, but SearchResultObject types "
                "only support string keys. (HINT: Search calls return an object "
                "with  a 'data' (which is the data array). You likely want to "
                "call .data[%s])" % (repr(k), repr(k))
            )

    def __iter__(self):
        return getattr(self, "data", []).__iter__()

    def __len__(self):
        return getattr(self, "data", []).__len__()

    def auto_paging_iter(self):
        page = self

        while True:
            for item in page:
                yield item
            page = page.next_search_result_page()

            if page.is_empty:
                break

    @classmethod
    def empty_search_result(
        cls, api_key=None, stripe_version=None, stripe_account=None
    ):
        return cls.construct_from(
            {"data": [], "has_more": False, "next_page": None},
            key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            last_response=None,
        )

    @property
    def is_empty(self):
        return not self.data

    def next_search_result_page(
        self, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        if not self.has_more:
            return self.empty_search_result(
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
            )

        params_with_filters = self._retrieve_params.copy()
        params_with_filters.update({"page": self.next_page})
        params_with_filters.update(params)

        result = self.search(
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            **params_with_filters
        )
        assert isinstance(result, SearchResultObject)
        return result
