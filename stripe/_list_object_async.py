# pyright: strict, reportUnnecessaryTypeIgnoreComment=false
# reportUnnecessaryTypeIgnoreComment is set to false because some type ignores are required in some
# python versions but not the others
from typing_extensions import Self, Unpack

from typing import (
    Any,
    AsyncIterator,
    Iterator,
    List,
    Generic,
    TypeVar,
    cast,
    Mapping,
)
from stripe._api_requestor import (
    _APIRequestor,  # pyright: ignore[reportPrivateUsage]
)
from stripe._stripe_object import StripeObject
from stripe._request_options import RequestOptions, extract_options_from_dict

from urllib.parse import quote_plus
from stripe._list_object_base import ListObjectBase

T = TypeVar("T", bound=StripeObject)


class ListObjectAsync(ListObjectBase, Generic[T]):
    """
    Variant of ListObject that contains *only* async versions of request-making methods.
    """
    async def list_async(self, **params: Mapping[str, Any]) -> Self:
        return cast(
            Self,
            await self._request_async(
                "get",
                self._get_url_for_list(),
                params=params,
                base_address="api",
                api_mode="V1",
            ),
        )

    async def auto_paging_iter_async(self) -> AsyncIterator[T]:
        page = self

        while True:
            if (
                "ending_before" in self._retrieve_params
                and "starting_after" not in self._retrieve_params
            ):
                for item in reversed(page):
                    yield item
                page = await page.previous_page_async()
            else:
                for item in page:
                    yield item
                page = await page.next_page_async()

            if page.is_empty:
                break

    async def next_page_async(self, **params: Unpack[RequestOptions]) -> Self:
        if not self.has_more:
            request_options, _ = extract_options_from_dict(params)
            return self._empty_list(
                **request_options,
            )

        return await self.list_async(**self._get_filters_for_next_page(params))

    async def previous_page_async(
        self, **params: Unpack[RequestOptions]
    ) -> Self:
        if not self.has_more:
            request_options, _ = extract_options_from_dict(params)
            return self._empty_list(
                **request_options,
            )

        result = await self.list_async(
            **self._get_filters_for_previous_page(params)
        )
        return result
