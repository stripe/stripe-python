from stripe.test.helper import (
    StripeApiTestCase, MyUpdateable
)


class UpdateableAPIResourceTests(StripeApiTestCase):

    def setUp(self):
        super(UpdateableAPIResourceTests, self).setUp()

        self.mock_response({
            'thats': 'it'
        })

        self.obj = MyUpdateable.construct_from({
            'id': 'myid',
            'foo': 'bar',
            'baz': 'boz',
            'metadata': {
                'size': 'l',
                'score': 4,
                'height': 10
            }
        }, 'mykey')

    def checkSave(self):
        self.assertTrue(self.obj is self.obj.save())

        self.assertEqual('it', self.obj.thats)
        # TODO: Should we force id to be retained?
        # self.assertEqual('myid', obj.id)
        self.assertRaises(AttributeError, getattr, self.obj, 'baz')

    def test_idempotent_save(self):
        self.obj.baz = 'updated'
        self.obj.save(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'metadata': {},
                'baz': 'updated',
            },
            {
                'Idempotency-Key': 'foo',
            },
        )

    def test_save(self):
        self.obj.baz = 'updated'
        self.obj.other = 'newval'
        self.obj.metadata.size = 'm'
        self.obj.metadata.info = 'a2'
        self.obj.metadata.height = None

        self.checkSave()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'baz': 'updated',
                'other': 'newval',
                'metadata': {
                    'size': 'm',
                    'info': 'a2',
                    'height': '',
                }
            },
            None
        )

    def test_add_key_to_nested_object(self):
        acct = MyUpdateable.construct_from({
            'id': 'myid',
            'legal_entity': {
                'size': 'l',
                'score': 4,
                'height': 10
            }
        }, 'mykey')

        acct.legal_entity['first_name'] = 'bob'

        self.assertTrue(acct is acct.save())

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'legal_entity': {
                    'first_name': 'bob',
                }
            },
            None
        )

    def test_save_nothing(self):
        acct = MyUpdateable.construct_from({
            'id': 'myid',
            'metadata': {
                'key': 'value',
            }
        }, 'mykey')

        self.assertTrue(acct is acct.save())

        # Note: ideally, we'd want the library to NOT issue requests in this
        # case (i.e. the assert should actually be `assert_not_called()`).
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {'metadata': {}},
            None
        )

    def test_replace_nested_object(self):
        acct = MyUpdateable.construct_from({
            'id': 'myid',
            'legal_entity': {
                'last_name': 'smith',
            }
        }, 'mykey')

        acct.legal_entity = {
            'first_name': 'bob',
        }

        self.assertTrue(acct is acct.save())

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'legal_entity': {
                    'first_name': 'bob',
                    'last_name': '',
                }
            },
            None
        )

    def test_array_setting(self):
        acct = MyUpdateable.construct_from({
            'id': 'myid',
            'legal_entity': {}
        }, 'mykey')

        acct.legal_entity.additional_owners = [{'first_name': 'Bob'}]

        self.assertTrue(acct is acct.save())

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'legal_entity': {
                    'additional_owners': [
                        {'first_name': 'Bob'}
                    ]
                }
            },
            None
        )

    def test_array_none(self):
        acct = MyUpdateable.construct_from({
            'id': 'myid',
            'legal_entity': {
                'additional_owners': None,
            }
        }, 'mykey')

        acct.foo = 'bar'

        self.assertTrue(acct is acct.save())

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'foo': 'bar',
                'legal_entity': {},
            },
            None
        )

    def test_array_insertion(self):
        acct = MyUpdateable.construct_from({
            'id': 'myid',
            'legal_entity': {
                'additional_owners': []
            }
        }, 'mykey')

        acct.legal_entity.additional_owners.append({'first_name': 'Bob'})

        self.assertTrue(acct is acct.save())

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'legal_entity': {
                    'additional_owners': {
                        '0': {'first_name': 'Bob'},
                    }
                }
            },
            None
        )

    def test_array_update(self):
        acct = MyUpdateable.construct_from({
            'id': 'myid',
            'legal_entity': {
                'additional_owners': [
                    {'first_name': 'Bob'},
                    {'first_name': 'Jane'}
                ]
            }
        }, 'mykey')

        acct.legal_entity.additional_owners[1].first_name = 'Janet'

        self.assertTrue(acct is acct.save())

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'legal_entity': {
                    'additional_owners': {
                        '0': {},
                        '1': {'first_name': 'Janet'}
                    }
                }
            },
            None
        )

    def test_array_noop(self):
        acct = MyUpdateable.construct_from({
            'id': 'myid',
            'legal_entity': {
                'additional_owners': [{'first_name': 'Bob'}]
            },
            'currencies_supported': ['usd', 'cad']
        }, 'mykey')

        self.assertTrue(acct is acct.save())

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'legal_entity': {'additional_owners': {'0': {}}}
            },
            None
        )

    def test_hash_noop(self):
        acct = MyUpdateable.construct_from({
            'id': 'myid',
            'legal_entity': {
                'address': {'line1': '1 Two Three'}
            }
        }, 'mykey')

        self.assertTrue(acct is acct.save())

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {'legal_entity': {'address': {}}},
            None
        )

    def test_save_replace_metadata_with_number(self):
        self.obj.baz = 'updated'
        self.obj.other = 'newval'
        self.obj.metadata = 3

        self.checkSave()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'baz': 'updated',
                'other': 'newval',
                'metadata': 3,
            },
            None
        )

    def test_save_overwrite_metadata(self):
        self.obj.metadata = {}
        self.checkSave()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'metadata': {
                    'size': '',
                    'score': '',
                    'height': '',
                }
            },
            None
        )

    def test_save_replace_metadata(self):
        self.obj.baz = 'updated'
        self.obj.other = 'newval'
        self.obj.metadata = {
            'size': 'm',
            'info': 'a2',
            'score': 4,
        }

        self.checkSave()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'baz': 'updated',
                'other': 'newval',
                'metadata': {
                    'size': 'm',
                    'info': 'a2',
                    'height': '',
                    'score': 4,
                }
            },
            None
        )

    def test_save_update_metadata(self):
        self.obj.baz = 'updated'
        self.obj.other = 'newval'
        self.obj.metadata.update({
            'size': 'm',
            'info': 'a2',
            'score': 4,
        })

        self.checkSave()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'baz': 'updated',
                'other': 'newval',
                'metadata': {
                    'size': 'm',
                    'info': 'a2',
                    'score': 4,
                }
            },
            None
        )
