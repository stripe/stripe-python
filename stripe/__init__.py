from typing_extensions import TYPE_CHECKING, Literal
from typing import Optional
import os
import warnings

# Stripe Python bindings
# API docs at http://stripe.com/docs/api
# Authors:
# Patrick Collison <patrick@stripe.com>
# Greg Brockman <gdb@stripe.com>
# Andrew Metcalf <andrew@stripe.com>

# Configuration variables
from stripe._api_version import _ApiVersion

from stripe._app_info import AppInfo as AppInfo
from stripe._version import VERSION as VERSION

# Constants
DEFAULT_API_BASE: str = "https://api.stripe.com"
DEFAULT_CONNECT_API_BASE: str = "https://connect.stripe.com"
DEFAULT_UPLOAD_API_BASE: str = "https://files.stripe.com"
DEFAULT_METER_EVENTS_API_BASE: str = "https://meter-events.stripe.com"


api_key: Optional[str] = None
client_id: Optional[str] = None
api_base: str = DEFAULT_API_BASE
connect_api_base: str = DEFAULT_CONNECT_API_BASE
upload_api_base: str = DEFAULT_UPLOAD_API_BASE
meter_events_api_base: str = DEFAULT_METER_EVENTS_API_BASE
api_version: str = _ApiVersion.CURRENT
verify_ssl_certs: bool = True
proxy: Optional[str] = None
default_http_client: Optional["HTTPClient"] = None
app_info: Optional[AppInfo] = None
enable_telemetry: bool = True
max_network_retries: int = 2
ca_bundle_path: str = os.path.join(
    os.path.dirname(__file__), "data", "ca-certificates.crt"
)

# Lazily initialized stripe.default_http_client
default_http_client = None
_default_proxy = None

from stripe._http_client import (
    new_default_http_client as new_default_http_client,
)


def ensure_default_http_client():
    if default_http_client:
        _warn_if_mismatched_proxy()
        return
    _init_default_http_client()


def _init_default_http_client():
    global _default_proxy
    global default_http_client

    # If the stripe.default_http_client has not been set by the user
    # yet, we'll set it here. This way, we aren't creating a new
    # HttpClient for every request.
    default_http_client = new_default_http_client(
        verify_ssl_certs=verify_ssl_certs, proxy=proxy
    )
    _default_proxy = proxy


def _warn_if_mismatched_proxy():
    global _default_proxy
    from stripe import proxy

    if proxy != _default_proxy:
        warnings.warn(
            "stripe.proxy was updated after sending a "
            "request - this is a no-op. To use a different proxy, "
            "set stripe.default_http_client to a new client "
            "configured with the proxy."
        )


# Set to either 'debug' or 'info', controls console logging
log: Optional[Literal["debug", "info"]] = None


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


# The beginning of the section generated from our OpenAPI spec
# The end of the section generated from our OpenAPI spec
