import logging
import sys
import os

logger = logging.getLogger('stripe')

__all__ = ['StringIO', 'parse_qsl', 'json', 'utf8']

try:
    # When cStringIO is available
    import cStringIO as StringIO
except ImportError:
    import StringIO

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


def is_appengine_dev():
    return ('APPENGINE_RUNTIME' in os.environ and
            'Dev' in os.environ.get('SERVER_SOFTWARE', ''))
