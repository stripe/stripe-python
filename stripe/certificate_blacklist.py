import hashlib
from stripe.error import APIError


BLACKLISTED_DIGESTS = {
    'api.stripe.com': (
        '33946398e5490d6b62a6e721d1cbfd308c3069c2',
    ),
    'revoked.stripe.com': (
        '9df351754b71fc29c59afce7350627710ed7f8b7',
    ),
}


def verify(hostname, certificate):
    """Verifies a PEM encoded certficate against a blacklist of known revoked
    fingerprints.

    returns True on success, raises RuntimeError on failure.
    """

    if hostname not in BLACKLISTED_DIGESTS:
        return True

    sha = hashlib.sha1()
    sha.update(certificate.encode('utf-8'))
    fingerprint = sha.hexdigest()

    if fingerprint in BLACKLISTED_DIGESTS[hostname]:
        raise APIError("Invalid server certificate. You tried to "
                       "connect to a server that has a revoked "
                       "SSL certificate, which means we cannot "
                       "securely send data to that server. "
                       "Please email support@stripe.com if you "
                       "need help connecting to the correct API "
                       "server.")
    return True
