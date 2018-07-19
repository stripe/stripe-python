from __future__ import absolute_import, division, print_function

import stripe


class TestDeletableAPIResource(object):
    class MyDeletable(stripe.api_resources.abstract.DeletableAPIResource):
        OBJECT_NAME = 'mydeletable'

    def test_delete(self, request_mock):
        request_mock.stub_request(
            'delete',
            '/v1/mydeletables/mid',
            {
                'id': 'mid',
                'deleted': True,
            },
            rheaders={'request-id': 'req_id'}
        )

        obj = self.MyDeletable.construct_from({
            'id': 'mid'
        }, 'mykey')

        assert obj is obj.delete()
        request_mock.assert_requested(
            'delete',
            '/v1/mydeletables/mid',
            {}
        )
        assert obj.deleted is True
        assert obj.id == 'mid'

        assert obj.last_response is not None
        assert obj.last_response.request_id == 'req_id'
