from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'iauth_123'


class TestAuthorization(object):
    def test_is_listable(self, request_mock):
        resources = stripe.issuing.Authorization.list()
        request_mock.assert_requested(
            'get',
            '/v1/issuing/authorizations'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.issuing.Authorization)

    def test_is_modifiable(self, request_mock):
        resource = stripe.issuing.Authorization.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/issuing/authorizations/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Authorization)

    def test_is_retrievable(self, request_mock):
        resource = stripe.issuing.Authorization.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/issuing/authorizations/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Authorization)

    def test_is_saveable(self, request_mock):
        resource = stripe.issuing.Authorization.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        authorization = resource.save()
        request_mock.assert_requested(
            'post',
            '/v1/issuing/authorizations/%s' % resource.id
        )
        assert isinstance(resource, stripe.issuing.Authorization)
        assert resource is authorization

    def test_is_approveable(self, request_mock):
        resource = stripe.issuing.Authorization.retrieve(TEST_RESOURCE_ID)
        authorization = resource.approve()
        request_mock.assert_requested(
            'post',
            '/v1/issuing/authorizations/%s/approve' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Authorization)
        assert resource is authorization

    def test_is_declineable(self, request_mock):
        resource = stripe.issuing.Authorization.retrieve(TEST_RESOURCE_ID)
        authorization = resource.decline()
        request_mock.assert_requested(
            'post',
            '/v1/issuing/authorizations/%s/decline' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Authorization)
        assert resource is authorization
