from __future__ import absolute_import, division, print_function

import warnings

import pytest

import stripe


class TestEphemeralKey(object):
    def test_is_creatable(self, request_mock):
        resource = stripe.EphemeralKey.create(
            customer='cus_123',
            stripe_version='2017-05-25'
        )
        request_mock.assert_api_version('2017-05-25')
        request_mock.assert_requested(
            'post',
            '/v1/ephemeral_keys',
            {'customer': 'cus_123'}
        )
        assert isinstance(resource, stripe.EphemeralKey)

    def test_raises_a_warning_when_using_api_version_arg(self, request_mock):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')

            resource = stripe.EphemeralKey.create(
                customer='cus_123',
                api_version='2017-05-25'
            )
            request_mock.assert_api_version('2017-05-25')
            request_mock.assert_requested(
                'post',
                '/v1/ephemeral_keys',
                {'customer': 'cus_123'}
            )
            assert isinstance(resource, stripe.EphemeralKey)

            assert len(w) == 1
            assert w[0].category == DeprecationWarning

    def test_is_not_creatable_without_an_explicit_api_version(self):
        with pytest.raises(ValueError,
                           message='stripe_version must be specified'):
            stripe.EphemeralKey.create(customer='cus_123')

    def test_is_deletable(self, request_mock):
        resource = stripe.EphemeralKey.create(
            customer='cus_123',
            stripe_version='2017-05-25'
        )
        resource.delete()
        request_mock.assert_requested(
            'delete',
            '/v1/ephemeral_keys/%s' % resource.id
        )
