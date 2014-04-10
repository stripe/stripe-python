import ssl

import stripe
from stripe import certificate_blacklist
from stripe.api_requestor import APIRequestor
from stripe.error import APIError
from stripe.test.helper import StripeTestCase


class RequestorBlacklistTest(StripeTestCase):

    def test_revoked_cert_is_revoked(self):
        stripe.api_base = "https://revoked.stripe.com:444"
        requestor = APIRequestor()
        self.assertRaises(APIError, requestor._check_ssl_cert)

    def test_live_cert_is_not_revoked(self):
        stripe.api_base = "https://api.stripe.com"
        requestor = APIRequestor()
        requestor._check_ssl_cert()
        self.assertTrue(requestor._CERTIFICATE_VERIFIED)

    def tearDown(self):
        stripe.api_base = "https://api.stripe.com"


class BlacklistTest(StripeTestCase):

    def test_revoked_cert_is_revoked(self):
        hostname = "revoked.stripe.com"
        cert = ssl.get_server_certificate((hostname, 444))
        der_cert = ssl.PEM_cert_to_DER_cert(cert)
        self.assertRaises(APIError,
                          lambda: certificate_blacklist.verify(
                              hostname, der_cert))

    def test_live_cert_is_not_revoked(self):
        hostname = "api.stripe.com"
        cert = ssl.get_server_certificate((hostname, 443))
        der_cert = ssl.PEM_cert_to_DER_cert(cert)
        self.assertTrue(certificate_blacklist.verify(hostname, der_cert))
