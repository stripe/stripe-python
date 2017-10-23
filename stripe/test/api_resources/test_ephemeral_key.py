import warnings

import stripe
from stripe.test.helper import StripeResourceTest


class EphemeralKeyTest(StripeResourceTest):

    def test_create(self):
        stripe.EphemeralKey.create(customer='cus_123',
                                   stripe_version='2017-05-25')

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

    def test_create_legacy_parameter_api_version(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')

            stripe.EphemeralKey.create(customer='cus_123',
                                       api_version='2017-05-25')

            self.assertEqual(1, len(w))
            self.assertEqual(w[0].category, DeprecationWarning)

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

    def test_create_without_global_version(self):
        self._do_version_tests(None)

    def test_create_with_global_version(self):
        self._do_version_tests('2017-05-25')

    def test_delete(self):
        stripe.EphemeralKey(id='ephkey_123').delete()
        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/ephemeral_keys/ephkey_123',
            {},
            None
        )

    def _do_version_tests(self, version):
        old_api_version = stripe.api_version
        stripe.api_version = version

        try:
            with self.assertRaisesRegex(ValueError,
                                        'stripe_version must be specified'):
                stripe.EphemeralKey.create(customer='cus_123')

            stripe.EphemeralKey.create(customer='cus_123',
                                       stripe_version='2017-06-05')

            self.requestor_class_mock.assert_called_with(
                None,
                api_version='2017-06-05',
                account=None
            )
        finally:
            stripe.api_version = old_api_version
