# pyright: strict
import json
from copy import deepcopy
from typing_extensions import TYPE_CHECKING, Type, Literal, Self, deprecated
from typing import (
    Any,
    Dict,
    Generic,
    List,
    Optional,
    Mapping,
    Set,
    Tuple,
    ClassVar,
    TypeVar,
    Union,
    cast,
    overload,
)

# Used to break circular imports
import stripe  # noqa: IMP101
from stripe import _util

from stripe._stripe_response import (
    StripeResponse,
    StripeStreamResponse,
    StripeStreamResponseAsync,
)
from stripe._encode import (
    _coerce_int64_string,  # pyright: ignore[reportPrivateUsage]
    _coerce_decimal_string,  # pyright: ignore[reportPrivateUsage]
    _make_suitable_for_json,  # pyright: ignore[reportPrivateUsage]
)
from stripe._request_options import (
    PERSISTENT_OPTIONS_KEYS,
    extract_options_from_dict,
)
from stripe._api_mode import ApiMode
from stripe._base_address import BaseAddress

if TYPE_CHECKING:
    from stripe._api_requestor import _APIRequestor  # pyright: ignore[reportPrivateUsage]


@overload
def _compute_diff(
    current: Dict[str, Any], previous: Optional[Dict[str, Any]]
) -> Dict[str, Any]: ...


@overload
def _compute_diff(
    current: object, previous: Optional[Dict[str, Any]]
) -> object: ...


def _compute_diff(
    current: object, previous: Optional[Dict[str, Any]]
) -> object:
    if isinstance(current, dict):
        current = cast(Dict[str, Any], current)
        previous = previous or {}
        diff = current.copy()
        for key in set(previous.keys()) - set(diff.keys()):
            diff[key] = ""
        return diff
    return current if current is not None else ""


def _serialize_list(
    array: Optional[List[Any]], previous: List[Any]
) -> Dict[str, Any]:
    array = array or []
    previous = previous or []
    params: Dict[str, Any] = {}

    for i, v in enumerate(array):
        previous_item = previous[i] if len(previous) > i else None
        if hasattr(v, "serialize"):
            params[str(i)] = v.serialize(previous_item)
        else:
            params[str(i)] = _compute_diff(v, previous_item)

    return params


class StripeObject:
    _retrieve_params: Mapping[str, Any]
    _previous: Optional[Mapping[str, Any]]

    def __init__(
        self,
        id: Optional[str] = None,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        last_response: Optional[StripeResponse] = None,
        *,
        _requestor: Optional["_APIRequestor"] = None,
        # TODO: is a more specific type possible here?
        **params: Any,
    ):
        self._data: Dict[str, Any] = {}
        self._unsaved_values: Set[str] = set()
        self._transient_values: Set[str] = set()
        self._last_response = last_response

        self._retrieve_params = params
        self._previous = None

        from stripe._api_requestor import _APIRequestor  # pyright: ignore[reportPrivateUsage]

        self._requestor = (
            _APIRequestor._global_with_options(  # pyright: ignore[reportPrivateUsage]
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
            )
            if _requestor is None
            else _requestor
        )

        if id:
            self["id"] = id

    @property
    def api_key(self):
        return self._requestor.api_key

    @property
    def stripe_account(self):
        return self._requestor.stripe_account

    @property
    def stripe_version(self):
        return self._requestor.stripe_version

    @property
    def last_response(self) -> Optional[StripeResponse]:
        return self._last_response

    def update(self, update_dict: Mapping[str, Any]) -> None:
        for k in update_dict:
            self._unsaved_values.add(k)

        self._data.update(update_dict)

    if not TYPE_CHECKING:

        def __setattr__(self, k, v):
            if k in PERSISTENT_OPTIONS_KEYS:
                self._requestor = self._requestor._new_requestor_with_options(
                    {k: v}
                )
                return None

            if k[0] == "_" or k in self.__dict__:
                return super(StripeObject, self).__setattr__(k, v)

            self[k] = v
            return None

        def __getattr__(self, k):
            if k[0] == "_":
                raise AttributeError(k)

            try:
                if k in self._field_remappings:
                    k = self._field_remappings[k]
                return self[k]
            except KeyError as err:
                raise AttributeError(*err.args) from err

        def __delattr__(self, k):
            if k[0] == "_" or k in self.__dict__:
                return super(StripeObject, self).__delattr__(k)
            else:
                del self[k]

    def __setitem__(self, k: str, v: Any) -> None:
        if v == "":
            raise ValueError(
                "You cannot set %s to an empty string on this object. "
                "The empty string is treated specially in our requests. "
                "If you'd like to delete the property using the save() method on this object, you may set %s.%s=None. "
                "Alternatively, you can pass %s='' to delete the property when using a resource method such as modify()."
                % (k, str(self), k, k)
            )

        # Allows for unpickling in Python 3.x
        if not hasattr(self, "_unsaved_values"):
            self._unsaved_values = set()
        if not hasattr(self, "_data"):
            self._data = {}

        self._unsaved_values.add(k)

        self._data[k] = v

    def __getitem__(self, k: str) -> Any:
        try:
            return self._data[k]
        except KeyError as err:
            if k in self._transient_values:
                raise KeyError(
                    "%r.  HINT: The %r attribute was set in the past."
                    "It was then wiped when refreshing the object with "
                    "the result returned by Stripe's API, probably as a "
                    "result of a save().  The attributes currently "
                    "available on this object are: %s"
                    % (k, k, ", ".join(list(self._data.keys())))
                )
            else:
                from stripe._invoice import Invoice

                # super specific one-off case to help users debug this property disappearing
                # see also: https://go/j/DEVSDK-2835
                if isinstance(self, Invoice) and k == "payment_intent":
                    raise KeyError(
                        "The 'payment_intent' attribute is no longer available on Invoice objects. See the docs for more details: https://docs.stripe.com/changelog/basil/2025-03-31/add-support-for-multiple-partial-payments-on-invoices#why-is-this-a-breaking-change"
                    )

                raise err

    def __delitem__(self, k: str) -> None:
        del self._data[k]

        # Allows for unpickling in Python 3.x
        if hasattr(self, "_unsaved_values") and k in self._unsaved_values:
            self._unsaved_values.remove(k)

    def __contains__(self, k: object) -> bool:
        return k in self._data

    def __eq__(self, other: object) -> bool:
        if isinstance(other, StripeObject):
            return type(self) is type(other) and self._data == other._data
        return NotImplemented

    # Custom unpickling method that updates _data directly
    # without calling __setitem__, which would fail if any value is an empty
    # string
    def __setstate__(self, state: Dict[str, Any]) -> None:
        self._data.update(state)
        self._unsaved_values.update(state.keys())

    # Custom pickling method to ensure the instance is pickled as a custom
    # class and not as a dict, otherwise __setstate__ would not be called when
    # unpickling.
    def __reduce__(self) -> Tuple[Any, ...]:
        reduce_value = (
            type(self),  # callable
            (  # args
                getattr(self, "id", None),
                self.api_key,
                self.stripe_version,
                self.stripe_account,
            ),
            self._data.copy(),  # state
        )
        return reduce_value

    @classmethod
    def construct_from(
        cls,
        values: Dict[str, Any],
        key: Optional[str],
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        last_response: Optional[StripeResponse] = None,
        *,
        api_mode: ApiMode = "V1",
    ) -> Self:
        from stripe._api_requestor import _APIRequestor  # pyright: ignore[reportPrivateUsage]

        return cls._construct_from(
            values=values,
            requestor=_APIRequestor._global_with_options(  # pyright: ignore[reportPrivateUsage]
                api_key=key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
            ),
            api_mode=api_mode,
            last_response=last_response,
        )

    @classmethod
    def _construct_from(
        cls,
        *,
        values: "Union[Dict[str, Any], StripeObject]",
        last_response: Optional[StripeResponse] = None,
        requestor: "_APIRequestor",
        api_mode: ApiMode,
    ) -> Self:
        raw = values._data if isinstance(values, StripeObject) else values
        instance = cls(
            raw.get("id"),
            last_response=last_response,
            _requestor=requestor,
        )
        instance._refresh_from(
            values=values,
            last_response=last_response,
            requestor=requestor,
            api_mode=api_mode,
        )
        return instance

    def refresh_from(
        self,
        values: Dict[str, Any],
        api_key: Optional[str] = None,
        partial: Optional[bool] = False,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        last_response: Optional[StripeResponse] = None,
        *,
        api_mode: ApiMode = "V1",
    ) -> None:
        self._refresh_from(
            values=values,
            partial=partial,
            last_response=last_response,
            requestor=self._requestor._new_requestor_with_options(  # pyright: ignore[reportPrivateUsage]
                {
                    "api_key": api_key,
                    "stripe_version": stripe_version,
                    "stripe_account": stripe_account,
                }
            ),
            api_mode=api_mode,
        )

    def _refresh_from(
        self,
        *,
        values: "Union[Dict[str, Any], StripeObject]",
        partial: Optional[bool] = False,
        last_response: Optional[StripeResponse] = None,
        requestor: Optional["_APIRequestor"] = None,
        api_mode: ApiMode,
    ) -> None:
        self._requestor = requestor or self._requestor
        self._last_response = last_response or getattr(
            values, "_last_response", None
        )

        # When called from APIResource._request, values may be a StripeObject
        if isinstance(values, StripeObject):
            values = values._data

        # Wipe old state before setting new.  This is useful for e.g.
        # updating a customer, where there is no persistent card
        # parameter.  Mark those values which don't persist as transient
        if partial:
            self._unsaved_values = self._unsaved_values - set(values)
        else:
            removed = set(self._data.keys()) - set(values)
            self._transient_values = self._transient_values | removed
            self._unsaved_values = set()
            self._data.clear()

        self._transient_values = self._transient_values - set(values)

        for k, v in values.items():
            # Apply field encoding coercion (e.g. int64_string: str → int)
            v = self._coerce_field_value(k, v)
            inner_class = self._get_inner_class_type(k)
            is_dict = self._get_inner_class_is_beneath_dict(k)
            if is_dict:
                obj = {
                    k: None
                    if v is None
                    else cast(
                        StripeObject,
                        _util._convert_to_stripe_object(  # pyright: ignore[reportPrivateUsage]
                            resp=v,
                            params=None,
                            klass_=inner_class,
                            requestor=self._requestor,
                            api_mode=api_mode,
                        ),
                    )
                    for k, v in v.items()
                }
            else:
                obj = cast(
                    Union[StripeObject, List[StripeObject]],
                    _util._convert_to_stripe_object(  # pyright: ignore[reportPrivateUsage]
                        resp=v,
                        params=None,
                        klass_=inner_class,
                        requestor=self._requestor,
                        api_mode=api_mode,
                    ),
                )
            self._data[k] = obj

        self._previous = values

    @deprecated("This will be removed in a future version of stripe-python.")
    def request(
        self,
        method: Literal["get", "post", "delete"],
        url: str,
        params: Optional[Dict[str, Any]] = None,
        *,
        base_address: BaseAddress = "api",
    ) -> "StripeObject":
        return StripeObject._request(
            self,
            method,
            url,
            params=params,
            base_address=base_address,
        )

    def _request(
        self,
        method: Literal["get", "post", "delete"],
        url: str,
        params: Optional[Mapping[str, Any]] = None,
        usage: Optional[List[str]] = None,
        *,
        base_address: BaseAddress,
    ) -> "StripeObject":
        if params is None:
            params = self._retrieve_params

        request_options, request_params = extract_options_from_dict(params)

        return self._requestor.request(
            method,
            url,
            params=request_params,
            options=request_options,
            base_address=base_address,
            usage=usage,
        )

    async def _request_async(
        self,
        method: Literal["get", "post", "delete"],
        url: str,
        params: Optional[Mapping[str, Any]] = None,
        usage: Optional[List[str]] = None,
        *,
        base_address: BaseAddress,
    ) -> "StripeObject":
        if params is None:
            params = self._retrieve_params

        request_options, request_params = extract_options_from_dict(params)

        return await self._requestor.request_async(
            method,
            url,
            params=request_params,
            options=request_options,
            base_address=base_address,
            usage=usage,
        )

    def _request_stream(
        self,
        method: str,
        url: str,
        params: Optional[Mapping[str, Any]] = None,
        *,
        base_address: BaseAddress = "api",
    ) -> StripeStreamResponse:
        if params is None:
            params = self._retrieve_params

        request_options, request_params = extract_options_from_dict(params)
        return self._requestor.request_stream(
            method,
            url,
            params=request_params,
            options=request_options,
            base_address=base_address,
        )

    async def _request_stream_async(
        self,
        method: str,
        url: str,
        params: Optional[Mapping[str, Any]] = None,
        *,
        base_address: BaseAddress = "api",
    ) -> StripeStreamResponseAsync:
        if params is None:
            params = self._retrieve_params

        request_options, request_params = extract_options_from_dict(params)
        return await self._requestor.request_stream_async(
            method,
            url,
            params=request_params,
            options=request_options,
            base_address=base_address,
        )

    def __repr__(self) -> str:
        ident_parts = [type(self).__name__]

        obj_str = getattr(self, "object", None)
        if isinstance(obj_str, str):
            ident_parts.append(obj_str)

        obj_id = getattr(self, "id", None)
        if isinstance(obj_id, str):
            ident_parts.append("id=%s" % (obj_id,))

        unicode_repr = "<%s at %s> JSON: %s" % (
            " ".join(ident_parts),
            hex(id(self)),
            str(self),
        )
        return unicode_repr

    def __str__(self) -> str:
        return json.dumps(
            self._to_dict_recursive(),
            sort_keys=True,
            indent=2,
            default=_make_suitable_for_json,
        )

    def to_dict(
        self, recursive: bool = True, for_json: bool = False
    ) -> Dict[str, Any]:
        """
        Dump the object's backing data. Recurses by default, but you can opt-out of that behavior by passing `recursive=False`.
        Pass `for_json=True` to convert non-JSON-serializable values (e.g. Decimal -> str)
        """
        if recursive:
            return self._to_dict_recursive(for_json=for_json)

        # shallow copy, so nested objects will be shared
        return self._data.copy()

    def _to_dict_recursive(self, for_json: bool = False) -> Dict[str, Any]:
        """
        used by __str__ to serialize the whole object
        """

        def maybe_to_dict_recursive(
            value: Optional[Union[StripeObject, Dict[str, Any]]],
        ) -> Optional[Dict[str, Any]]:
            if value is None:
                return None
            elif isinstance(value, StripeObject):
                return value._to_dict_recursive(for_json=for_json)
            elif for_json:
                return _make_suitable_for_json(value)
            else:
                return value

        return {
            key: list(map(maybe_to_dict_recursive, cast(List[Any], value)))
            if isinstance(value, list)
            else maybe_to_dict_recursive(value)
            for key, value in self._data.items()
        }

    def serialize(
        self, previous: Optional[Mapping[str, Any]]
    ) -> Dict[str, Any]:
        params: Dict[str, Any] = {}
        unsaved_keys = self._unsaved_values or set()
        previous_raw = previous or self._previous or {}
        if isinstance(previous_raw, StripeObject):
            previous_raw = previous_raw._data
        prev: Dict[str, Any] = dict(previous_raw)

        for k, v in self._data.items():
            if k == "id" or k.startswith("_"):
                continue
            elif isinstance(v, stripe.APIResource):
                continue
            elif hasattr(v, "serialize"):
                child = v.serialize(prev.get(k, None))
                if child != {}:
                    params[k] = child
            elif k in unsaved_keys:
                params[k] = _compute_diff(v, prev.get(k, None))
            elif k == "additional_owners" and v is not None:
                params[k] = _serialize_list(v, prev.get(k, None))

        return params

    # This class overrides __setitem__ to throw exceptions on inputs that it
    # doesn't like. This can cause problems when we try to copy an object
    # wholesale because some data that's returned from the API may not be valid
    # if it was set to be set manually. Here we override the class' copy
    # arguments so that we can bypass these possible exceptions on __setitem__.
    def __copy__(self) -> "StripeObject":
        copied = StripeObject(
            getattr(self, "id", None),
            self.api_key,
            stripe_version=self.stripe_version,
            stripe_account=self.stripe_account,
        )

        copied._retrieve_params = self._retrieve_params

        for k, v in self._data.items():
            # Write to _data directly to avoid checks that we've added in the
            # overridden __setitem__ that can throw exceptions.
            copied._data[k] = v

        return copied

    # This class overrides __setitem__ to throw exceptions on inputs that it
    # doesn't like. This can cause problems when we try to copy an object
    # wholesale because some data that's returned from the API may not be valid
    # if it was set to be set manually. Here we override the class' copy
    # arguments so that we can bypass these possible exceptions on __setitem__.
    def __deepcopy__(self, memo: Dict[int, Any]) -> "StripeObject":
        copied = self.__copy__()
        memo[id(self)] = copied

        for k, v in self._data.items():
            # Write to _data directly to avoid checks that we've added in the
            # overridden __setitem__ that can throw exceptions.
            copied._data[k] = deepcopy(v, memo)

        return copied

    _field_remappings: ClassVar[Dict[str, str]] = {}

    _inner_class_types: ClassVar[Dict[str, Type["StripeObject"]]] = {}
    _inner_class_dicts: ClassVar[List[str]] = []
    _field_encodings: ClassVar[Dict[str, str]] = {}

    def _get_inner_class_type(
        self, field_name: str
    ) -> Optional[Type["StripeObject"]]:
        return self._inner_class_types.get(field_name)

    def _get_inner_class_is_beneath_dict(self, field_name: str):
        return field_name in self._inner_class_dicts

    def _coerce_field_value(self, field_name: str, value: Any) -> Any:
        """
        Convert JSON types to more applicable Python types, if able.

        For example, "int64_string"s become `int`s.
        """

        # WARNING: if you edit this function to produce a type that's not json-serializable, you need to update `_make_suitable_for_json` as well.
        # By default, Python will only correctly dump a few standard types, so we have to handle the rest

        encoding = self._field_encodings.get(field_name)
        if encoding is None or value is None:
            return value

        if encoding == "int64_string":
            return _coerce_int64_string(value, encode=False)

        if encoding == "decimal_string":
            return _coerce_decimal_string(value, encode=False)

        return value


T = TypeVar("T")


class UntypedStripeObject(StripeObject, Generic[T]):
    """
    A normal StripeObject, but it exposes `__getattr__`/`__setattr__` instead of hiding them, effectively removing type information.

    Because metadata & similar are supposed to be an untyped `dict`, we don't want to show type errors for arbitrary key access.

    Is generic on its value type
    """

    def __init__(*args, **kwargs: Any):
        raise ValueError("this is not for runtime use, just typing")

    # This class is never actually used at runtime, it's just here for typechecking reasons
    def __setattr__(self, k: str, v: T): ...

    def __getattr__(self, k: str) -> T: ...

    def __delattr__(self, k: str): ...
