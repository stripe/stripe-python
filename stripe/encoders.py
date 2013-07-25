import datetime
import sys
import time
import types
import urllib


def utf8(value):
    if isinstance(value, unicode) and sys.version_info < (3, 0):
        return value.encode('utf-8')
    else:
        return value

def encode_dict(stk, key, dictvalue):
    n = {}
    for k, v in dictvalue.iteritems():
        k = utf8(k)
        v = utf8(v)
        n["%s[%s]" % (key, k)] = v
    stk.extend(_encode_inner(n))


def encode_list(stk, key, listvalue):
    for v in listvalue:
        v = utf8(v)
        stk.append(("%s[]" % (key), v))


def encode_datetime(stk, key, dttime):
    utc_timestamp = int(time.mktime(dttime.timetuple()))
    stk.append((key, utc_timestamp))


def encode_none(stk, k, v):
    pass # do not include None-valued params in request


ENCODERS = {
    list: encode_list,
    dict: encode_dict,
    datetime.datetime: encode_datetime,
    types.NoneType: encode_none,
}


def _encode_inner(d):
    """
    We want post vars of form:
    {'foo': 'bar', 'nested': {'a': 'b', 'c': 'd'}}
    to become:
    foo=bar&nested[a]=b&nested[c]=d
    """
    # special case value encoding
    stk = []
    for key, value in d.iteritems():
        key = utf8(key)
        try:
            encoder = ENCODERS[value.__class__]
            encoder(stk, key, value)
        except KeyError:
            # don't need special encoding
            value = utf8(value)
            stk.append((key, value))
    return stk


def encode(d):
    """
    Internal: encode a string for url representation
    """
    return urllib.urlencode(_encode_inner(d))