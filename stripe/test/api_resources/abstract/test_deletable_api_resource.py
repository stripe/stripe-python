from stripe.test.helper import (
    StripeApiTestCase, MyDeletable
)


class DeletableAPIResourceTests(StripeApiTestCase):

    def test_delete(self):
        self.mock_response({
            'id': 'mid',
            'deleted': True,
        })

        obj = MyDeletable.construct_from({
            'id': 'mid'
        }, 'mykey')

        self.assertTrue(obj is obj.delete())

        self.assertEqual(True, obj.deleted)
        self.assertEqual('mid', obj.id)
