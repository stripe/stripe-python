# Imports needed in setup.py and __init__.py

def import_json():
  # Python 2.5 and below do not ship with json
  _json_loaded = None
  try:
    import json
    if hasattr(json, 'loads'):
      return json
    _json_loaded = False
  except ImportError:
    pass

  try:
    import simplejson
    return simplejson
  except ImportError:
    if _json_loaded is None:
      raise ImportError("Stripe requires a JSON library, which you do not appear to have.  Please install the simplejson library.  HINT: Try installing the python simplejson library via 'pip install simplejson' or 'easy_install simplejson', or contact support@stripe.com with questions.")
    else:
      raise ImportError("Stripe requires a JSON library with the same interface as the Python 2.6 'json' library.  You appear to have a 'json' library with a different interface.  Please install the simplejson library.  HINT: Try installing the python simplejson library via 'pip install simplejson' or 'easy_install simplejson', or contact support@stripe.com with questions.")
