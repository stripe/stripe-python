import warnings

warnings.warn("The importers module is deprecated and will be removed in "
              "version 2.0. Check the `util` module for json imports",
              DeprecationWarning)


def import_json():
    warnings.warn(
        "'import_json function is deprecated and will be removed in version "
        "2.0 of the Stripe python bindings.  Please use"
        "`from importer import json` instead'",
        DeprecationWarning)

    from stripe.util import json
    return json
