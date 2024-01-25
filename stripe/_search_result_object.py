# pyright: strict
from typing_extensions import Self, Unpack
from typing import (
    Generic,
    List,
    TypeVar,
    cast,
    Any,
    Mapping,
    Iterator,
)

from stripe._api_requestor import (
    _APIRequestor,  # pyright: ignore[reportPrivateUsage]
)
from stripe._stripe_object import StripeObject
from stripe import _util
import warnings
from stripe._request_options import RequestOptions, extract_options_from_dict

T = TypeVar("T", bound=StripeObject)


class SearchResultObject(StripeObject, Generic[T]):
    OBJECT_NAME = "search_result"
    data: List[StripeObject]
    has_more: bool
    next_page: str

    def _search(self, **params: Mapping[str, Any]) -> Self:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DeprecationWarning)
            return self.search(  # pyright: ignore[reportDeprecated]
                **params,
            )

    @_util.deprecated(
        "This will be removed in a future version of stripe-python. Please call the `search` method on the corresponding resource directly, instead of the generic search on SearchResultObject."
    )
    def search(self, **params: Mapping[str, Any]) -> Self:
        url = self.get("url")
        if not isinstance(url, str):
            raise ValueError(
                'Cannot call .list on a list object without a string "url" property'
            )
        return cast(
            Self,
            self._request(
                "get",
                url,
                params=params,
                base_address="api",
                api_mode="V1",
            ),
        )

    def __getitem__(self, k: str) -> T:
        if isinstance(k, str):  # pyright: ignore
            return super(SearchResultObject, self).__getitem__(k)
        else:
            raise KeyError(
                "You tried to access the %s index, but SearchResultObject types "
                "only support string keys. (HINT: Search calls return an object "
                "with  a 'data' (which is the data array). You likely want to "
                "call .data[%s])" % (repr(k), repr(k))
            )

    #  Pyright doesn't like this because SearchResultObject inherits from StripeObject inherits from Dict[str, Any]
    #  and so it wants the type of __iter__ to agree with __iter__ from Dict[str, Any]
    #  But we are iterating through "data", which is a List[T].
    def __iter__(self) -> Iterator[T]:  # pyright: ignore
        return getattr(self, "data", []).__iter__()

    def __len__(self) -> int:
        return getattr(self, "data", []).__len__()

    def auto_paging_iter(self) -> Iterator[T]:
        page = self

        while True:
            for item in page:
                yield item
            page = page.next_search_result_page()

            if page.is_empty:
                break

    @classmethod
    def _empty_search_result(
        cls,
        **params: Unpack[RequestOptions],
    ) -> Self:
        return cls._construct_from(
            values={"data": [], "has_more": False, "next_page": None},
            last_response=None,
            requestor=_APIRequestor._global_with_options(  # pyright: ignore[reportPrivateUsage]
                **params,
            ),
            api_mode="V1",
        )

    @property
    def is_empty(self) -> bool:
        return not self.data

    def next_search_result_page(
        self, **params: Unpack[RequestOptions]
    ) -> Self:
        if not self.has_more:
            options, _ = extract_options_from_dict(params)
            return self._empty_search_result(
                api_key=options.get("api_key"),
                stripe_version=options.get("stripe_version"),
                stripe_account=options.get("stripe_account"),
            )

        params_with_filters = dict(self._retrieve_params)
        params_with_filters.update({"page": self.next_page})
        params_with_filters.update(params)

        return self._search(
            **params_with_filters,
        )
