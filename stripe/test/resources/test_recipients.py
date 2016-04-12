import stripe
from stripe.test.helper import (
    StripeResourceTest, DUMMY_CARD
)


class RecipientTest(StripeResourceTest):

    def test_list_recipients(self):
        stripe.Recipient.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/recipients',
            {}
        )

    def test_recipient_transfers(self):
        recipient = stripe.Recipient(id='rp_transfer')
        recipient.transfers()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/transfers',
            {'recipient': 'rp_transfer'},
        )

    def test_recipient_add_card(self):
        recipient = stripe.Recipient.construct_from({
            'id': 'rp_add_card',
            'sources': {
                'object': 'list',
                'url': '/v1/recipients/rp_add_card/sources',
            },
        }, 'api_key')
        recipient.sources.create(card=DUMMY_CARD)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/recipients/rp_add_card/sources',
            {
                'card': DUMMY_CARD,
            },
            None
        )

    def test_recipient_update_card(self):
        card = stripe.Card.construct_from({
            'recipient': 'rp_update_card',
            'id': 'ca_update_card',
        }, 'api_key')
        card.name = 'The Best'
        card.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/recipients/rp_update_card/cards/ca_update_card',
            {
                'name': 'The Best',
            },
            None
        )

    def test_recipient_delete_card(self):
        card = stripe.Card.construct_from({
            'recipient': 'rp_delete_card',
            'id': 'ca_delete_card',
        }, 'api_key')
        card.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/recipients/rp_delete_card/cards/ca_delete_card',
            {},
            None
        )
