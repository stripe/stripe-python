import sys

import logging
logger = logging.getLogger('stripe')

try:
    import json
except ImportError:
    json = None

if not (json and hasattr(json, 'loads')):
    try:
        import simplejson as json
    except ImportError:
        pass

    if not json:
        raise ImportError(
            "Stripe requires a JSON library, which you do not appear to have. "
            "Please install the simplejson library.  HINT: Try installing the "
            "python simplejson library via 'pip install simplejson' or "
            "'easy_install simplejson', or contact support@stripe.com "
            "with questions.")
    else:
        raise ImportError(
            "Stripe requires a JSON library with the same interface as the "
            "Python 2.6 'json' library.  You appear to have a 'json' "
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
