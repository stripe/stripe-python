import calendar
import datetime
import logging
import re
import sys
import time

logger = logging.getLogger('stripe')

try:
    # Python 3
    from urllib.parse import parse_qsl
except ImportError:
    try:
        from urlparse import parse_qsl
    except ImportError:
        # Python < 2.6
        from cgi import parse_qsl

try:
    import json
except ImportError:
    json = None

if not (json and hasattr(json, 'loads')):
    try:
        import simplejson as json
    except ImportError:
        if not json:
            raise ImportError(
                "Stripe requires a JSON library, such as simplejson. "
                "HINT: Try installing the "
                "python simplejson library via 'pip install simplejson' or "
                "'easy_install simplejson', or contact support@stripe.com "
                "with questions.")
        else:
            raise ImportError(
                "Stripe requires a JSON library with the same interface as "
                "the Python 2.6 'json' library.  You appear to have a 'json' "
                "library with a different interface.  Please install "
                "the simplejson library.  HINT: Try installing the "
                "python simplejson library via 'pip install simplejson' "
                "or 'easy_install simplejson', or contact support@stripe.com"
                "with questions.")


def utf8(value):
    if isinstance(value, unicode) and sys.version_info < (3, 0):
        return value.encode('utf-8')
    else:
        return value

def _encode_datetime(dttime):
    if dttime.tzinfo and dttime.tzinfo.utcoffset(dttime) is not None:
        utc_timestamp = calendar.timegm(dttime.utctimetuple())
    else:
        utc_timestamp = time.mktime(dttime.timetuple())

    return int(utc_timestamp)

def api_encode(data):
    for key, value in data.iteritems():
        key = utf8(key)
        if value is None:
            continue
        elif hasattr(value, 'stripe_id'):
            yield (key, value.stripe_id)
        elif isinstance(value, list) or isinstance(value, tuple):
            for subvalue in value:
                yield ("%s[]" % (key,), utf8(subvalue))
        elif isinstance(value, dict):
            subdict = dict(('%s[%s]' % (key, subkey), subvalue) for
                           subkey, subvalue in value.iteritems())
            for subkey, subvalue in api_encode(subdict):
                yield (subkey, subvalue)
        elif isinstance(value, datetime.datetime):
            yield (key, _encode_datetime(value))
        else:
            yield (key, utf8(value))
