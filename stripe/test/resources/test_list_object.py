import stripe
from stripe.test.helper import StripeApiTestCase


class ListObjectTests(StripeApiTestCase):

    def setUp(self):
        super(ListObjectTests, self).setUp()

        self.lo = stripe.resource.ListObject.construct_from({
            'id': 'me',
            'url': '/my/path',
            'data': ['foo'],
        }, 'mykey')

        self.mock_response([{
            'object': 'charge',
            'foo': 'bar',
        }])

    def assertResponse(self, res):
        self.assertTrue(isinstance(res[0], stripe.Charge))
        self.assertEqual('bar', res[0].foo)

    def test_for_loop(self):
        seen = []

        for item in self.lo:
            seen.append(item)

        self.assertEqual(['foo'], seen)

    def test_all(self):
        res = self.lo.all(myparam='you')

        self.requestor_mock.request.assert_called_with(
            'get', '/my/path', {'myparam': 'you'}, None)

        self.assertResponse(res)

    def test_create(self):
        res = self.lo.create(myparam='eter')

        self.requestor_mock.request.assert_called_with(
            'post', '/my/path', {'myparam': 'eter'}, None)

        self.assertResponse(res)

    def test_retrieve(self):
        res = self.lo.retrieve('myid', myparam='cow')

        self.requestor_mock.request.assert_called_with(
            'get', '/my/path/myid', {'myparam': 'cow'}, None)

        self.assertResponse(res)
