from typing_extensions import Literal
from typing import Union, Optional

import os

# Stripe Python bindings
# API docs at http://stripe.com/docs/api
# Authors:
# Patrick Collison <patrick@stripe.com>
# Greg Brockman <gdb@stripe.com>
# Andrew Metcalf <andrew@stripe.com>

# Configuration variables
from stripe.api_version import _ApiVersion

from stripe.app_info import AppInfo

api_key: Optional[str] = None
client_id: Optional[str] = None
api_base = "https://api.stripe.com"
connect_api_base = "https://connect.stripe.com"
upload_api_base = "https://files.stripe.com"
api_version = _ApiVersion.CURRENT
verify_ssl_certs = True
proxy = None
default_http_client = None
app_info: Optional[AppInfo] = None
enable_telemetry = True
max_network_retries = 0
ca_bundle_path = os.path.join(
    os.path.dirname(__file__), "data", "ca-certificates.crt"
)

# Set to either 'debug' or 'info', controls console logging
log: Optional[Union[Literal["debug"], Literal["info"]]] = None

# API resources
from stripe.api_resources import *  # pyright: ignore # noqa

from stripe.api_resources import abstract  # pyright: ignore # noqa

# OAuth
from stripe.oauth import OAuth  # noqa

# Webhooks
from stripe.webhook import Webhook, WebhookSignature  # noqa

from . import stripe_response  # noqa
from . import stripe_object  # noqa


# Sets some basic information about the running application that's sent along
# with API requests. Useful for plugin authors to identify their plugin when
# communicating with Stripe.
#
# Takes a name and optional version and plugin URL.
def set_app_info(
    name: str,
    partner_id: Optional[str] = None,
    url: Optional[str] = None,
    version: Optional[str] = None,
):
    global app_info
    app_info = {
        "name": name,
        "partner_id": partner_id,
        "url": url,
        "version": version,
    }
