import hashlib
from stripe.error import APIError


BLACKLISTED_DIGESTS = {
    'api.stripe.com': (
        '05c0b3643694470a888c6e7feb5c9e24e823dc53',
    ),
    'revoked.stripe.com': (
        '5b7dc7fbc98d78bf76d4d4fa6f597a0c901fad5c',
    ),
}


def verify(hostname, certificate):
    """Verifies a PEM encoded certificate against a blacklist of known revoked
    fingerprints.

    returns True on success, raises RuntimeError on failure.
    """

    if hostname not in BLACKLISTED_DIGESTS:
        return True

    sha = hashlib.sha1()
    sha.update(certificate)
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
