from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'ic_123'


class TestCard(object):
    def test_is_creatable(self, request_mock):
        resource = stripe.issuing.Card.create(
            currency='usd',
            type='physical'
        )
        request_mock.assert_requested(
            'post',
            '/v1/issuing/cards'
        )
        assert isinstance(resource, stripe.issuing.Card)

    def test_is_listable(self, request_mock):
        resources = stripe.issuing.Card.list()
        request_mock.assert_requested(
            'get',
            '/v1/issuing/cards'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.issuing.Card)

    def test_is_modifiable(self, request_mock):
        resource = stripe.issuing.Card.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/issuing/cards/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Card)

    def test_is_retrievable(self, request_mock):
        resource = stripe.issuing.Card.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/issuing/cards/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Card)

    def test_is_saveable(self, request_mock):
        resource = stripe.issuing.Card.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        card = resource.save()
        request_mock.assert_requested(
            'post',
            '/v1/issuing/cards/%s' % resource.id
        )
        assert isinstance(resource, stripe.issuing.Card)
        assert resource is card

    def test_can_retrieve_details(self, request_mock):
        resource = stripe.issuing.Card.retrieve(TEST_RESOURCE_ID)
        card_details = resource.details()
        request_mock.assert_requested(
            'get',
            '/v1/issuing/cards/%s/details' % resource.id
        )
        assert isinstance(card_details, stripe.issuing.CardDetails)
