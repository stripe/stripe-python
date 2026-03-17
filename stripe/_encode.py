import calendar
import datetime
import time
from collections import OrderedDict
from typing import Generator, Mapping, Tuple, Any


def _encode_datetime(dttime: datetime.datetime):
    if dttime.tzinfo and dttime.tzinfo.utcoffset(dttime) is not None:
        utc_timestamp = calendar.timegm(dttime.utctimetuple())
    else:
        utc_timestamp = time.mktime(dttime.timetuple())

    return int(utc_timestamp)


def _encode_nested_dict(key, data, fmt="%s[%s]"):
    d = OrderedDict()
    items = data._data.items() if hasattr(data, "_data") else data.items()
    for subkey, subvalue in items:
        d[fmt % (key, subkey)] = subvalue
    return d


def _json_encode_date_callback(value):
    if isinstance(value, datetime.datetime):
        return _encode_datetime(value)
    return value


def _api_encode(
    data: Mapping[str, Any],
) -> Generator[Tuple[str, Any], None, None]:
    items = data.items()

    for key, value in items:
        if value is None:
            continue
        elif hasattr(value, "id"):
            yield (key, getattr(value, "id"))
        elif isinstance(value, list) or isinstance(value, tuple):
            for i, sv in enumerate(value):
                # Always use indexed format for arrays
                encoded_key = "%s[%d]" % (key, i)
                if isinstance(sv, dict) or hasattr(sv, "_data"):
                    subdict = _encode_nested_dict(encoded_key, sv)
                    for k, v in _api_encode(subdict):
                        yield (k, v)
                else:
                    yield (encoded_key, sv)
        elif isinstance(value, dict) or hasattr(value, "_data"):
            subdict = _encode_nested_dict(key, value)
            for subkey, subvalue in _api_encode(subdict):
                yield (subkey, subvalue)
        elif isinstance(value, datetime.datetime):
            yield (key, _encode_datetime(value))
        elif isinstance(value, bool):
            yield (key, str(value).lower())
        else:
            yield (key, value)
