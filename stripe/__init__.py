from typing_extensions import TYPE_CHECKING, Literal
from typing import Optional

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

if TYPE_CHECKING:
    from stripe.http_client import HTTPClient

api_key: Optional[str] = None
client_id: Optional[str] = None
api_base: str = "https://api.stripe.com"
connect_api_base: str = "https://connect.stripe.com"
upload_api_base: str = "https://files.stripe.com"
api_version: str = _ApiVersion.CURRENT
verify_ssl_certs: bool = True
proxy: Optional[str] = None
default_http_client: Optional["HTTPClient"] = None
app_info: Optional[AppInfo] = None
enable_telemetry: bool = True
max_network_retries: int = 0
ca_bundle_path: str = os.path.join(
    os.path.dirname(__file__), "data", "ca-certificates.crt"
)

# Set to either 'debug' or 'info', controls console logging
log: Optional[Literal["debug", "info"]] = None

# API resources
from stripe.api_resources import *  # noqa

from stripe.api_resources import abstract  # noqa

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
