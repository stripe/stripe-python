import os

from stripe import (
    StripeClient,
    RequestsClient,
    HTTPClient,
    UrllibClient,
    verify_ssl_certs,
    PycurlClient,
)

print("Attempting charge...")

proxy: HTTPClient._Proxy = {
    "http": "http://<user>:<pass>@<proxy>:<port>",
    "https": "http://<user>:<pass>@<proxy>:<port>",
}

http_clients = (
    RequestsClient(verify_ssl_certs=verify_ssl_certs, proxy=proxy),
    PycurlClient(verify_ssl_certs=verify_ssl_certs, proxy=proxy),
    UrllibClient(verify_ssl_certs=verify_ssl_certs, proxy=proxy),
)

for http_client in http_clients:
    client_with_proxy = StripeClient(
        api_key=os.environ["STRIPE_SECRET_KEY"],
        http_client=http_client,
    )

    resp = client_with_proxy.v1.charges.create(
        params={
            "amount": 200,
            "currency": "usd",
            "description": "customer@example.com",
        }
    )

    print("Success: %s, %r" % (http_client.name, resp))
