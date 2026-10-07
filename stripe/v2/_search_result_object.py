from copy import deepcopy
from typing import (
    AsyncIterator,
    Generic,
    Iterator,
    List,
    Mapping,
    Any,
    Optional,
    TypeVar,
)

from stripe._any_iterator import AnyIterator
from stripe._stripe_object import StripeObject


T = TypeVar("T", bound=StripeObject)


class SearchResultObject(StripeObject, Generic[T]):
    """A page of API v2 search results with POST-based auto-pagination."""

    OBJECT_NAME = "v2.search_result"
    data: List[T]
    next_page_url: Optional[str]
    previous_page_url: Optional[str]
    total_count: int

    def __iter__(self) -> Iterator[T]:
        return getattr(self, "data", []).__iter__()

    def __len__(self) -> int:
        return getattr(self, "data", []).__len__()

    def auto_paging_iter(self) -> AnyIterator[T]:
        return AnyIterator(self._auto_paging_iter(), self._auto_paging_iter_async())

    def _original_params(self) -> Mapping[str, Any]:
        return deepcopy(self._retrieve_params)

    def _body_params(self, params: Mapping[str, Any]) -> Mapping[str, Any]:
        body_params = dict(params)
        body_params.pop("limit", None)
        return body_params

    def _auto_paging_iter(self) -> Iterator[T]:
        page: SearchResultObject[T] = self
        params = self._original_params()
        while True:
            for item in page.data:
                yield item
            if page.next_page_url is None:
                break
            result = self._request(
                "post",
                page.next_page_url,
                params=self._body_params(params),
                base_address="api",
            )
            assert isinstance(result, SearchResultObject)
            page = result

    async def _auto_paging_iter_async(self) -> AsyncIterator[T]:
        page: SearchResultObject[T] = self
        params = self._original_params()
        while True:
            for item in page.data:
                yield item
            if page.next_page_url is None:
                break
            result = await self._request_async(
                "post",
                page.next_page_url,
                params=self._body_params(params),
                base_address="api",
            )
            assert isinstance(result, SearchResultObject)
            page = result
