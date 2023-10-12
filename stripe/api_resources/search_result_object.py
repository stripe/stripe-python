# pyright: strict
from typing_extensions import Self
from typing import (
    Generic,
    List,
    TypeVar,
    cast,
    Optional,
    Any,
    Mapping,
    Iterator,
)

from stripe.stripe_object import StripeObject

T = TypeVar("T", bound=StripeObject)


class SearchResultObject(StripeObject, Generic[T]):
    OBJECT_NAME = "search_result"
    data: List[StripeObject]
    has_more: bool
    next_page: str

    def search(
        self,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Mapping[str, Any]
    ) -> Self:
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
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
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
    def empty_search_result(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
    ) -> Self:
        return cls.construct_from(
            {"data": [], "has_more": False, "next_page": None},
            key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            last_response=None,
        )

    @property
    def is_empty(self) -> bool:
        return not self.data

    def next_search_result_page(
        self,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Mapping[str, Any]
    ) -> Self:
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
