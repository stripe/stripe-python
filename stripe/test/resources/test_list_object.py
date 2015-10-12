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


class AutoPagingTests(StripeApiTestCase):

    def test_iter_one_page(self):
        lo = stripe.resource.ListObject.construct_from({
            'object': 'list',
            'url': '/my/path',
            'data': [{'id': 'foo'}],
        }, 'mykey')

        self.requestor_mock.request.assert_not_called()

        seen = [item['id'] for item in lo.auto_paging_iter()]

        self.assertEqual(['foo'], seen)

    def test_iter_two_pages(self):
        lo = stripe.resource.ListObject.construct_from({
            'object': 'list',
            'url': '/my/path',
            'has_more': True,
            'data': [{'id': 'foo'}],
        }, 'mykey')

        self.mock_response({
            'object': 'list',
            'data': [{'id': 'bar'}],
            'url': '/my/path',
            'has_more': False,
        })

        seen = [item['id'] for item in lo.auto_paging_iter()]

        self.requestor_mock.request.assert_called_with(
            'get', '/my/path', {'starting_after': 'foo'}, None)

        self.assertEqual(['foo', 'bar'], seen)

    def test_class_method_two_pages(self):
        self.mock_response({
            'object': 'list',
            'data': [{'id': 'bar'}],
            'url': '/v1/charges',
            'has_more': False,
        })

        seen = [i['id'] for i in stripe.Charge.auto_paging_iter(limit=25)]

        self.requestor_mock.request.assert_called_with(
            'get', '/v1/charges', {'limit': 25})

        self.assertEqual(['bar'], seen)
