import calendar
import datetime
import time
from collections import OrderedDict
from typing import Any, Dict, Generator, Mapping, Optional, Tuple, Union


def _encode_datetime(dttime: datetime.datetime):
    if dttime.tzinfo and dttime.tzinfo.utcoffset(dttime) is not None:
        utc_timestamp = calendar.timegm(dttime.utctimetuple())
    else:
        utc_timestamp = time.mktime(dttime.timetuple())

    return int(utc_timestamp)


def _encode_nested_dict(key, data, fmt="%s[%s]"):
    d = OrderedDict()
    for subkey, subvalue in data.items():
        d[fmt % (key, subkey)] = subvalue
    return d


def _json_encode_date_callback(value):
    if isinstance(value, datetime.datetime):
        return _encode_datetime(value)
    return value


# Type for a request encoding schema node: either a leaf encoding string
# (e.g. "int64_string") or a nested dict mapping field names to sub-schemas.
_SchemaNode = Union[str, Dict[str, Any]]


def _coerce_v2_params(
    params: Optional[Mapping[str, Any]],
    schema: Dict[str, _SchemaNode],
) -> Optional[Mapping[str, Any]]:
    """
    Coerce V2 request params according to the given encoding schema.

    For fields marked as "int64_string", converts int values to str so they
    are serialized as JSON strings on the wire. Recurses into nested objects
    and arrays.
    """
    if params is None:
        return None

    result: Dict[str, Any] = {}
    for key, value in params.items():
        field_schema = schema.get(key)
        if field_schema is not None:
            result[key] = _coerce_value(value, field_schema)
        else:
            result[key] = value
    return result


def _coerce_value(value: Any, schema: _SchemaNode) -> Any:
    """Coerce a single value according to its schema node."""
    if value is None:
        return None

    if schema == "int64_string":
        # Scalar or array of int64_string
        if isinstance(value, list):
            return [str(v) if isinstance(v, int) else v for v in value]
        if isinstance(value, int):
            return str(value)
        return value

    if isinstance(schema, dict):
        # Nested object schema
        if isinstance(value, list):
            # Array of objects with int64_string fields
            return [
                dict(_coerce_v2_params(v, schema) or {})
                if isinstance(v, dict)
                else v
                for v in value
            ]
        if isinstance(value, dict):
            return dict(_coerce_v2_params(value, schema) or {})
        return value

    return value


def _api_encode(data) -> Generator[Tuple[str, Any], None, None]:
    for key, value in data.items():
        if value is None:
            continue
        elif hasattr(value, "id"):
            yield (key, getattr(value, "id"))
        elif isinstance(value, list) or isinstance(value, tuple):
            for i, sv in enumerate(value):
                # Always use indexed format for arrays
                encoded_key = "%s[%d]" % (key, i)
                if isinstance(sv, dict):
                    subdict = _encode_nested_dict(encoded_key, sv)
                    for k, v in _api_encode(subdict):
                        yield (k, v)
                else:
                    yield (encoded_key, sv)
        elif isinstance(value, dict):
            subdict = _encode_nested_dict(key, value)
            for subkey, subvalue in _api_encode(subdict):
                yield (subkey, subvalue)
        elif isinstance(value, datetime.datetime):
            yield (key, _encode_datetime(value))
        elif isinstance(value, bool):
            yield (key, str(value).lower())
        else:
            yield (key, value)
