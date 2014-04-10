import ssl

from stripe import certificate_blacklist
from stripe.error import APIError
from stripe.test.helper import StripeTestCase


class BlacklistTest(StripeTestCase):

    def test_revoked_cert_is_revoked(self):
        hostname = "revoked.stripe.com"
        cert = ssl.get_server_certificate((hostname, 443))
        der_cert = ssl.PEM_cert_to_DER_cert(cert)
        self.assertRaises(APIError, lambda: certificate_blacklist.verify(hostname, der_cert))

    def test_live_cert_is_not_revoked(self):
        hostname = "api.stripe.com"
        cert = ssl.get_server_certificate((hostname, 443))
        der_cert = ssl.PEM_cert_to_DER_cert(cert)
        self.assertTrue(certificate_blacklist.verify(hostname, der_cert))
