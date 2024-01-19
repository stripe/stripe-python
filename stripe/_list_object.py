# pyright: strict, reportUnnecessaryTypeIgnoreComment=false
# reportUnnecessaryTypeIgnoreComment is set to false because some type ignores are required in some
# python versions but not the others
from typing_extensions import Self, Unpack

from typing import (
    Any,
    Iterator,
    List,
    Generic,
    TypeVar,
    cast,
    Mapping,
)
from stripe import _util
from stripe._api_requestor import APIRequestor
from stripe._stripe_object import StripeObject
from stripe._request_options import RequestOptions, extract_options_from_dict

from urllib.parse import quote_plus
import warnings

T = TypeVar("T", bound=StripeObject)


class ListObject(StripeObject, Generic[T]):
    OBJECT_NAME = "list"
    data: List[T]
    has_more: bool
    url: str

    def _list(self, **params: Mapping[str, Any]) -> Self:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=DeprecationWarning)
            return self.list(  # pyright: ignore[reportDeprecated]
                **params,
            )

    @_util.deprecated(
        "This will be removed in a future version of stripe-python. Please call the `list` method on the corresponding resource directly, instead of using `list` from the list object."
    )
    def list(self, **params: Mapping[str, Any]) -> Self:
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

    @_util.deprecated(
        "This will be removed in a future version of stripe-python. Please call the `create` method on the corresponding resource directly, instead of using `create` from the list object."
    )
    def create(self, **params: Mapping[str, Any]) -> T:
        url = self.get("url")
        if not isinstance(url, str):
            raise ValueError(
                'Cannot call .create on a list object for the collection of an object without a string "url" property'
            )
        return cast(
            T,
            self._request(
                "post",
                url,
                params=params,
                base_address="api",
                api_mode="V1",
            ),
        )

    @_util.deprecated(
        "This will be removed in a future version of stripe-python. Please call the `retrieve` method on the corresponding resource directly, instead of using `retrieve` from the list object."
    )
    def retrieve(self, id: str, **params: Mapping[str, Any]):
        url = self.get("url")
        if not isinstance(url, str):
            raise ValueError(
                'Cannot call .retrieve on a list object for the collection of an object without a string "url" property'
            )

        url = "%s/%s" % (self.get("url"), quote_plus(id))
        return cast(
            T,
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
            return super(ListObject, self).__getitem__(k)
        else:
            raise KeyError(
                "You tried to access the %s index, but ListObject types only "
                "support string keys. (HINT: List calls return an object with "
                "a 'data' (which is the data array). You likely want to call "
                ".data[%s])" % (repr(k), repr(k))
            )

    #  Pyright doesn't like this because ListObject inherits from StripeObject inherits from Dict[str, Any]
    #  and so it wants the type of __iter__ to agree with __iter__ from Dict[str, Any]
    #  But we are iterating through "data", which is a List[T].
    def __iter__(  # pyright: ignore
        self,
    ) -> Iterator[T]:
        return getattr(self, "data", []).__iter__()

    def __len__(self) -> int:
        return getattr(self, "data", []).__len__()

    def __reversed__(self) -> Iterator[T]:  # pyright: ignore (see above)
        return getattr(self, "data", []).__reversed__()

    def auto_paging_iter(self) -> Iterator[T]:
        page = self

        while True:
            if (
                "ending_before" in self._retrieve_params
                and "starting_after" not in self._retrieve_params
            ):
                for item in reversed(page):
                    yield item
                page = page.previous_page()
            else:
                for item in page:
                    yield item
                page = page.next_page()

            if page.is_empty:
                break

    @classmethod
    def _empty_list(
        cls,
        **params: Unpack[RequestOptions],
    ) -> Self:
        return cls._construct_from(
            values={"data": []},
            last_response=None,
            requestor=APIRequestor._global_with_options(  # pyright: ignore[reportPrivateUsage]
                **params,
            ),
            api_mode="V1",
        )

    @property
    def is_empty(self) -> bool:
        return not self.data

    def next_page(self, **params: Unpack[RequestOptions]) -> Self:
        if not self.has_more:
            request_options, _ = extract_options_from_dict(params)
            return self._empty_list(
                **request_options,
            )

        last_id = getattr(self.data[-1], "id")
        if not last_id:
            raise ValueError(
                "Unexpected: element in .data of list object had no id"
            )

        params_with_filters = dict(self._retrieve_params)
        params_with_filters.update({"starting_after": last_id})
        params_with_filters.update(params)

        return self._list(
            **params_with_filters,
        )

    def previous_page(self, **params: Unpack[RequestOptions]) -> Self:
        if not self.has_more:
            request_options, _ = extract_options_from_dict(params)
            return self._empty_list(
                **request_options,
            )

        first_id = getattr(self.data[0], "id")
        if not first_id:
            raise ValueError(
                "Unexpected: element in .data of list object had no id"
            )

        params_with_filters = dict(self._retrieve_params)
        params_with_filters.update({"ending_before": first_id})
        params_with_filters.update(params)

        result = self._list(
            **params_with_filters,
        )
        return result
