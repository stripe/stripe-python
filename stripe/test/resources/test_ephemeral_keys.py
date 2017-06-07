import stripe
from stripe.test.helper import StripeResourceTest


class EphemeralKeyTest(StripeResourceTest):

    def test_create(self):
        stripe.EphemeralKey.create(customer='cus_123',
                                   api_version='2017-05-25')

        self.requestor_class_mock.assert_called_with(
            None,
            api_version='2017-05-25',
            account=None
        )

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/ephemeral_keys',
            {'customer': 'cus_123'},
            None
        )

    def do_version_tests(self):
        with self.assertRaisesRegexp(ValueError,
                                     'api_version must be specified'):
            stripe.EphemeralKey.create(customer='cus_123')

        stripe.EphemeralKey.create(customer='cus_123',
                                   api_version='2017-06-05')

        self.requestor_class_mock.assert_called_with(
            None,
            api_version='2017-06-05',
            account=None
        )

    def test_create_without_global_version(self):
        stripe.api_version = None
        self.do_version_tests()

    def test_create_with_global_version(self):
        stripe.api_version = '2017-05-25'

        try:
            self.do_version_tests()
        finally:
            stripe.api_version = None

    def test_delete(self):
        stripe.EphemeralKey(id='ephkey_123').delete()
        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/ephemeral_keys/ephkey_123',
            {},
            None
        )
