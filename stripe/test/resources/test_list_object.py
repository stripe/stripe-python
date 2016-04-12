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

    def test_list(self):
        res = self.lo.list(myparam='you')

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

    @staticmethod
    def pageable_model_response(ids, has_more):
        return {
            'object': 'list',
            'url': '/v1/pageablemodels',
            'data': [{'id': id, 'object': 'pageablemodel'} for id in ids],
            'has_more': has_more,
        }

    def test_iter_one_page(self):
        lo = stripe.resource.ListObject.construct_from(
            self.pageable_model_response(['pm_123', 'pm_124'], False),
            'mykey'
        )

        self.requestor_mock.request.assert_not_called()

        seen = [item['id'] for item in lo.auto_paging_iter()]

        self.assertEqual(['pm_123', 'pm_124'], seen)

    def test_iter_two_pages(self):
        lo = stripe.resource.ListObject.construct_from(
            self.pageable_model_response(['pm_123', 'pm_124'], True),
            'mykey'
        )
        lo._retrieve_params = {'foo': 'bar'}

        self.mock_response(
            self.pageable_model_response(['pm_125', 'pm_126'], False)
        )

        seen = [item['id'] for item in lo.auto_paging_iter()]

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/pageablemodels',
            {
                'starting_after': 'pm_124',
                'foo': 'bar'
            },
            None
        )

        self.assertEqual(['pm_123', 'pm_124', 'pm_125', 'pm_126'], seen)

    def test_class_method_two_pages(self):
        self.mock_response({
            'object': 'list',
            'data': [{'id': 'ch_001'}],
            'url': '/v1/charges',
            'has_more': False,
        })

        seen = [item['id'] for item in stripe.Charge.auto_paging_iter(
            limit=25,
            foo='bar'
        )]

        self.requestor_mock.request.assert_called_with(
            'get', '/v1/charges', {'limit': 25, 'foo': 'bar'}
        )

        self.assertEqual(['ch_001'], seen)
