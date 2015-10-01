import pickle
import sys
import time
import datetime
import tempfile

import stripe
import stripe.resource

from stripe.test.helper import (
    StripeUnitTestCase, StripeApiTestCase,
    MySingleton, MyListable, MyCreatable, MyUpdateable, MyDeletable,
    MyResource, SAMPLE_INVOICE, NOW,
    DUMMY_CARD, DUMMY_CHARGE, DUMMY_PLAN, DUMMY_COUPON,
    DUMMY_INVOICE_ITEM, DUMMY_DISPUTE)

from stripe import util


class StripeObjectTests(StripeUnitTestCase):

    def test_initializes_with_parameters(self):
        obj = stripe.resource.StripeObject(
            'foo', 'bar', myparam=5, yourparam='boo')

        self.assertEqual('foo', obj.id)
        self.assertEqual('bar', obj.api_key)

    def test_access(self):
        obj = stripe.resource.StripeObject('myid', 'mykey', myparam=5)

        # Empty
        self.assertRaises(AttributeError, getattr, obj, 'myattr')
        self.assertRaises(KeyError, obj.__getitem__, 'myattr')
        self.assertEqual('def', obj.get('myattr', 'def'))
        self.assertEqual(None, obj.get('myattr'))

        # Setters
        obj.myattr = 'myval'
        obj['myitem'] = 'itval'
        self.assertEqual('sdef', obj.setdefault('mydef', 'sdef'))

        # Getters
        self.assertEqual('myval', obj.setdefault('myattr', 'sdef'))
        self.assertEqual('myval', obj.myattr)
        self.assertEqual('myval', obj['myattr'])
        self.assertEqual('myval', obj.get('myattr'))

        self.assertEqual(['id', 'myattr', 'mydef', 'myitem'],
                         sorted(obj.keys()))
        self.assertEqual(['itval', 'myid', 'myval', 'sdef'],
                         sorted(obj.values()))

        # Illegal operations
        self.assertRaises(ValueError, setattr, obj, 'foo', '')

    def test_refresh_from(self):
        obj = stripe.resource.StripeObject.construct_from({
            'foo': 'bar',
            'trans': 'me',
        }, 'mykey')

        self.assertEqual('mykey', obj.api_key)
        self.assertEqual('bar', obj.foo)
        self.assertEqual('me', obj['trans'])
        self.assertEqual(None, obj.stripe_account)

        obj.refresh_from({
            'foo': 'baz',
            'johnny': 5,
        }, 'key2', stripe_account='acct_foo')

        self.assertEqual(5, obj.johnny)
        self.assertEqual('baz', obj.foo)
        self.assertRaises(AttributeError, getattr, obj, 'trans')
        self.assertEqual('key2', obj.api_key)
        self.assertEqual('acct_foo', obj.stripe_account)

        obj.refresh_from({
            'trans': 4,
            'metadata': {'amount': 42}
        }, 'key2', True)

        self.assertEqual('baz', obj.foo)
        self.assertEqual(4, obj.trans)

    def test_passing_nested_refresh(self):
        obj = stripe.resource.StripeObject.construct_from({
            'foos': {
                'type': 'list',
                'data': [
                    {'id': 'nested'}
                ],
            }
        }, 'key', stripe_account='acct_foo')

        nested = obj.foos.data[0]

        self.assertEqual('key', obj.api_key)
        self.assertEqual('nested', nested.id)
        self.assertEqual('key', nested.api_key)
        self.assertEqual('acct_foo', nested.stripe_account)

    def test_refresh_from_nested_object(self):
        obj = stripe.resource.StripeObject.construct_from(
            SAMPLE_INVOICE, 'key')

        self.assertEqual(1, len(obj.lines.subscriptions))
        self.assertTrue(
            isinstance(obj.lines.subscriptions[0],
                       stripe.resource.StripeObject))
        self.assertEqual('month', obj.lines.subscriptions[0].plan.interval)

    def test_to_json(self):
        obj = stripe.resource.StripeObject.construct_from(
            SAMPLE_INVOICE, 'key')

        self.check_invoice_data(util.json.loads(str(obj)))

    def check_invoice_data(self, data):
        # Check rough structure
        self.assertEqual(20, len(data.keys()))
        self.assertEqual(3, len(data['lines'].keys()))
        self.assertEqual(0, len(data['lines']['invoiceitems']))
        self.assertEqual(1, len(data['lines']['subscriptions']))

        # Check various data types
        self.assertEqual(1338238728, data['date'])
        self.assertEqual(None, data['next_payment_attempt'])
        self.assertEqual(False, data['livemode'])
        self.assertEqual('month',
                         data['lines']['subscriptions'][0]['plan']['interval'])

    def test_repr(self):
        obj = stripe.resource.StripeObject(
            'foo', 'bar', myparam=5)

        obj['object'] = u'\u4e00boo\u1f00'

        res = repr(obj)

        if sys.version_info[0] < 3:
            res = unicode(repr(obj), 'utf-8')

        self.assertTrue(u'<StripeObject \u4e00boo\u1f00' in res)
        self.assertTrue(u'id=foo' in res)

    def test_pickling(self):
        obj = stripe.resource.StripeObject(
            'foo', 'bar', myparam=5)

        obj['object'] = 'boo'
        obj.refresh_from({'fala': 'lalala'}, api_key='bar', partial=True)

        self.assertEqual('lalala', obj.fala)

        pickled = pickle.dumps(obj)
        newobj = pickle.loads(pickled)

        self.assertEqual('foo', newobj.id)
        self.assertEqual('bar', newobj.api_key)
        self.assertEqual('boo', newobj['object'])
        self.assertEqual('lalala', newobj.fala)

    def test_deletion(self):
        obj = stripe.resource.StripeObject('id', 'key')

        obj.coupon = "foo"
        self.assertEqual('foo', obj.coupon)

        del obj.coupon
        self.assertRaises(AttributeError, getattr, obj, 'coupon')

        obj.refresh_from({'coupon': 'foo'}, api_key='bar', partial=True)
        self.assertEqual('foo', obj.coupon)


class ListObjectTests(StripeApiTestCase):

    def setUp(self):
        super(ListObjectTests, self).setUp()

        self.lo = stripe.resource.ListObject.construct_from({
            'id': 'me',
            'url': '/my/path',
        }, 'mykey')

        self.mock_response([{
            'object': 'charge',
            'foo': 'bar',
        }])

    def assertResponse(self, res):
        self.assertTrue(isinstance(res[0], stripe.Charge))
        self.assertEqual('bar', res[0].foo)

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


class APIResourceTests(StripeApiTestCase):

    def test_retrieve_and_refresh(self):
        self.mock_response({
            'id': 'foo2',
            'bobble': 'scrobble',
        })

        res = MyResource.retrieve('foo*', myparam=5)

        url = '/v1/myresources/foo%2A'
        self.requestor_mock.request.assert_called_with(
            'get', url, {'myparam': 5}, None
        )

        self.assertEqual('scrobble', res.bobble)
        self.assertEqual('foo2', res.id)
        self.assertEqual('reskey', res.api_key)

        self.mock_response({
            'frobble': 5,
        })

        res = res.refresh()

        url = '/v1/myresources/foo2'
        self.requestor_mock.request.assert_called_with(
            'get', url, {'myparam': 5}, None
        )

        self.assertEqual(5, res.frobble)
        self.assertRaises(KeyError, res.__getitem__, 'bobble')

    def test_convert_to_stripe_object(self):
        sample = {
            'foo': 'bar',
            'adict': {
                'object': 'charge',
                'id': 42,
                'amount': 7,
            },
            'alist': [
                {
                    'object': 'customer',
                    'name': 'chilango'
                }
            ]
        }

        converted = stripe.resource.convert_to_stripe_object(
            sample, 'akey', None)

        # Types
        self.assertTrue(isinstance(converted, stripe.resource.StripeObject))
        self.assertTrue(isinstance(converted.adict, stripe.Charge))
        self.assertEqual(1, len(converted.alist))
        self.assertTrue(isinstance(converted.alist[0], stripe.Customer))

        # Values
        self.assertEqual('bar', converted.foo)
        self.assertEqual(42, converted.adict.id)
        self.assertEqual('chilango', converted.alist[0].name)

        # Stripping
        # TODO: We should probably be stripping out this property
        # self.assertRaises(AttributeError, getattr, converted.adict, 'object')


class SingletonAPIResourceTests(StripeApiTestCase):

    def test_retrieve(self):
        self.mock_response({
            'single': 'ton'
        })
        res = MySingleton.retrieve()

        self.requestor_mock.request.assert_called_with(
            'get', '/v1/mysingleton', {}, None)

        self.assertEqual('ton', res.single)


class ListableAPIResourceTests(StripeApiTestCase):

    def test_all(self):
        self.mock_response([
            {
                'object': 'charge',
                'name': 'jose',
            },
            {
                'object': 'charge',
                'name': 'curly',
            }
        ])

        res = MyListable.all()

        self.requestor_mock.request.assert_called_with(
            'get', '/v1/mylistables', {})

        self.assertEqual(2, len(res))
        self.assertTrue(all(isinstance(obj, stripe.Charge) for obj in res))
        self.assertEqual('jose', res[0].name)
        self.assertEqual('curly', res[1].name)


class CreateableAPIResourceTests(StripeApiTestCase):

    def test_create(self):
        self.mock_response({
            'object': 'charge',
            'foo': 'bar',
        })

        res = MyCreatable.create()

        self.requestor_mock.request.assert_called_with(
            'post', '/v1/mycreatables', {}, None)

        self.assertTrue(isinstance(res, stripe.Charge))
        self.assertEqual('bar', res.foo)

    def test_idempotent_create(self):
        self.mock_response({
            'object': 'charge',
            'foo': 'bar',
        })

        res = MyCreatable.create(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post', '/v1/mycreatables', {}, {'Idempotency-Key': 'foo'})

        self.assertTrue(isinstance(res, stripe.Charge))
        self.assertEqual('bar', res.foo)


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
        self.requestor_mock.request.assert_not_called()

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


class StripeResourceTest(StripeApiTestCase):

    def setUp(self):
        super(StripeResourceTest, self).setUp()
        self.mock_response({})


class ChargeTest(StripeResourceTest):

    def test_charge_list_all(self):
        stripe.Charge.all(created={'lt': NOW})

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/charges',
            {
                'created': {'lt': NOW},
            }
        )

    def test_charge_list_create(self):
        stripe.Charge.create(idempotency_key='foo', **DUMMY_CHARGE)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/charges',
            DUMMY_CHARGE,
            {'Idempotency-Key': 'foo'},
        )

    def test_charge_list_retrieve(self):
        stripe.Charge.retrieve('ch_test_id')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/charges/ch_test_id',
            {},
            None
        )

    def test_charge_update_dispute(self):
        charge = stripe.Charge(id='ch_update_id')
        charge.update_dispute(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/charges/ch_update_id/dispute',
            {},
            {'Idempotency-Key': 'foo'},
        )

    def test_charge_close_dispute(self):
        charge = stripe.Charge(id='ch_update_id')
        charge.close_dispute(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/charges/ch_update_id/dispute/close',
            {},
            {'Idempotency-Key': 'foo'},
        )

    def test_mark_as_fraudulent(self):
        charge = stripe.Charge(id='ch_update_id')
        charge.mark_as_fraudulent(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/charges/ch_update_id',
            {
                'fraud_details': {'user_report': 'fraudulent'}
            },
            {'Idempotency-Key': 'foo'},
        )

    def test_mark_as_safe(self):
        charge = stripe.Charge(id='ch_update_id')
        charge.mark_as_safe(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/charges/ch_update_id',
            {
                'fraud_details': {'user_report': 'safe'}
            },
            {'Idempotency-Key': 'foo'},
        )

    def test_create_with_source_param(self):
        stripe.Charge.create(amount=100, currency='usd',
                             source='btcrcv_test_receiver')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/charges',
            {
                'amount': 100,
                'currency': 'usd',
                'source': 'btcrcv_test_receiver'
            },
            None,
        )


class DisputeTest(StripeResourceTest):

    def test_list_all_disputes(self):
        stripe.Dispute.all(created={'lt': NOW})

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/disputes',
            {
                'created': {'lt': NOW},
            }
        )

    def test_create_dispute(self):
        stripe.Dispute.create(idempotency_key='foo', **DUMMY_DISPUTE)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/disputes',
            DUMMY_DISPUTE,
            {'Idempotency-Key': 'foo'},
        )

    def test_retrieve_dispute(self):
        stripe.Dispute.retrieve('dp_test_id')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/disputes/dp_test_id',
            {},
            None
        )

    def test_update_dispute(self):
        dispute = stripe.Dispute.construct_from({
            'id': 'dp_update_id',
            'evidence': {
                'product_description': 'description',
            },
        }, 'api_key')
        dispute.evidence['customer_name'] = 'customer'
        dispute.evidence['uncategorized_text'] = 'text'
        dispute.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/disputes/dp_update_id',
            {'evidence': {
                'customer_name': 'customer',
                'uncategorized_text': 'text',
            }},
            None
        )

    def test_close_dispute(self):
        dispute = stripe.Dispute(id='dp_close_id')
        dispute.close(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/disputes/dp_close_id/close',
            {},
            {'Idempotency-Key': 'foo'},
        )


class AccountTest(StripeResourceTest):

    def test_retrieve_account_deprecated(self):
        stripe.Account.retrieve()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/account',
            {},
            None
        )

    def test_retrieve_account(self):
        stripe.Account.retrieve('acct_foo')
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/accounts/acct_foo',
            {},
            None
        )

    def test_list_accounts(self):
        stripe.Account.all()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/accounts',
            {}
        )

    def test_create_account(self):
        pii = {
            'type': 'individual',
            'first_name': 'Joe',
            'last_name': 'Smith',
        }
        stripe.Account.create(legal_entity=pii)
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/accounts',
            {
                'legal_entity': pii,
            },
            None,
        )

    def test_update_account(self):
        acct = stripe.Account.construct_from({
            'id': 'acct_update',
            'legal_entity': {'first_name': 'Joe'},
        }, 'api_key')
        acct.legal_entity['first_name'] = 'Bob'
        acct.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/accounts/acct_update',
            {
                'legal_entity': {
                    'first_name': 'Bob',
                },
            },
            None,
        )

    def test_account_delete_bank_account(self):
        source = stripe.BankAccount.construct_from({
            'account': 'acc_delete_ba',
            'id': 'ba_delete_ba',
        }, 'api_key')
        source.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/accounts/acc_delete_ba/external_accounts/ba_delete_ba',
            {},
            None
        )

    def test_verify_additional_owner(self):
        acct = stripe.Account.construct_from({
            'id': 'acct_update',
            'additional_owners': [{
                'first_name': 'Alice',
                'verification': {},
            }]
        }, 'api_key')
        owner = acct.additional_owners[0]
        owner.verification.document = 'file_foo'
        acct.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/accounts/acct_update',
            {
                'additional_owners': {
                    '0': {
                        'verification': {
                            'document': 'file_foo',
                        },
                    },
                },
            },
            None,
        )


class BalanceTest(StripeResourceTest):

    def test_retrieve_balance(self):
        stripe.Balance.retrieve()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/balance',
            {},
            None
        )


class BalanceTransactionTest(StripeResourceTest):

    def test_list_balance_transactions(self):
        stripe.BalanceTransaction.all()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/balance/history',
            {}
        )


class ApplicationFeeTest(StripeResourceTest):

    def test_list_application_fees(self):
        stripe.ApplicationFee.all()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/application_fees',
            {}
        )


class CustomerTest(StripeResourceTest):

    def test_list_customers(self):
        stripe.Customer.all()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/customers',
            {},
        )

    def test_create_customer(self):
        stripe.Customer.create(description="foo bar", card=DUMMY_CARD,
                               coupon='cu_discount', idempotency_key='foo')
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers',
            {
                'coupon': 'cu_discount',
                'description': 'foo bar',
                'card': DUMMY_CARD
            },
            {'Idempotency-Key': 'foo'}
        )

    def test_unset_description(self):
        customer = stripe.Customer(id="cus_unset_desc")
        customer.description = "Hey"
        customer.save(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_unset_desc',
            {
                'description': 'Hey',
            },
            {'Idempotency-Key': 'foo'}
        )

    def test_del_coupon(self):
        customer = stripe.Customer(id="cus_unset_desc")
        customer.description = "bar"
        customer.coupon = "foo"
        del customer.coupon
        customer.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_unset_desc',
            {
                'description': 'bar'
            },
            None
        )

    def test_cannot_set_empty_string(self):
        customer = stripe.Customer()
        self.assertRaises(ValueError, setattr, customer, "description", "")

    def test_customer_add_card(self):
        customer = stripe.Customer.construct_from({
            'id': 'cus_add_card',
            'sources': {
                'object': 'list',
                'url': '/v1/customers/cus_add_card/sources',
            },
        }, 'api_key')
        customer.sources.create(card=DUMMY_CARD, idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_add_card/sources',
            {
                'card': DUMMY_CARD,
            },
            {'Idempotency-Key': 'foo'}
        )

    def test_customer_add_source(self):
        customer = stripe.Customer.construct_from({
            'id': 'cus_add_source',
            'sources': {
                'object': 'list',
                'url': '/v1/customers/cus_add_source/sources',
            },
        }, 'api_key')
        customer.sources.create(source=DUMMY_CARD, idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_add_source/sources',
            {
                'source': DUMMY_CARD,
            },
            {'Idempotency-Key': 'foo'}
        )

    def test_customer_update_card(self):
        card = stripe.Card.construct_from({
            'customer': 'cus_update_card',
            'id': 'ca_update_card',
        }, 'api_key')
        card.name = 'The Best'
        card.save(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_update_card/sources/ca_update_card',
            {
                'name': 'The Best',
            },
            {'Idempotency-Key': 'foo'}
        )

    def test_customer_update_source(self):
        source = stripe.BitcoinReceiver.construct_from({
            'customer': 'cus_update_source',
            'id': 'btcrcv_update_source',
        }, 'api_key')
        source.name = 'The Best'
        source.save(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_update_source/sources/btcrcv_update_source',
            {
                'name': 'The Best',
            },
            {'Idempotency-Key': 'foo'}
        )

    def test_customer_delete_card(self):
        card = stripe.Card.construct_from({
            'customer': 'cus_delete_card',
            'id': 'ca_delete_card',
        }, 'api_key')
        card.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/customers/cus_delete_card/sources/ca_delete_card',
            {},
            None
        )

    def test_customer_delete_source(self):
        source = stripe.BitcoinReceiver.construct_from({
            'customer': 'cus_delete_source',
            'id': 'btcrcv_delete_source',
        }, 'api_key')
        source.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/customers/cus_delete_source/sources/btcrcv_delete_source',
            {},
            None
        )

    def test_customer_delete_bank_account(self):
        source = stripe.BankAccount.construct_from({
            'customer': 'cus_delete_source',
            'id': 'ba_delete_source',
        }, 'api_key')
        source.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/customers/cus_delete_source/sources/ba_delete_source',
            {},
            None
        )

    def test_customer_verify_bank_account(self):
        source = stripe.BankAccount.construct_from({
            'customer': 'cus_verify_source',
            'id': 'ba_verify_source',
        }, 'api_key')
        source.verify()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_verify_source/sources/ba_verify_source/verify',
            {},
            None
        )


class TransferTest(StripeResourceTest):

    def test_list_transfers(self):
        stripe.Transfer.all()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/transfers',
            {}
        )

    def test_cancel_transfer(self):
        transfer = stripe.Transfer(id='tr_cancel')
        transfer.cancel()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/transfers/tr_cancel/cancel',
            {},
            None
        )


class ReversalTest(StripeResourceTest):

    def test_fetch_reversal(self):
        transfer = stripe.Charge.construct_from({
            'id': 'tr_get',
            'reversals': {
                'object': 'list',
                'url': '/v1/transfers/tr_get/reversals',
            }
        }, 'api_key')

        transfer.reversals.retrieve("foo")

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/transfers/tr_get/reversals/foo',
            {},
            None
        )

    def test_list_reversals(self):
        transfer = stripe.Charge.construct_from({
            'id': 'tr_list',
            'reversals': {
                'object': 'list',
                'url': '/v1/transfers/tr_list/reversals',
            }
        }, 'api_key')

        transfer.reversals.all()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/transfers/tr_list/reversals',
            {},
            None
        )

    def test_update_transfer(self):
        reversal = stripe.resource.Reversal.construct_from({
            'id': "rev_update",
            'transfer': "tr_update",
            'metadata': {},
        }, 'api_key')
        reversal.metadata["key"] = "value"
        reversal.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/transfers/tr_update/reversals/rev_update',
            {
                'metadata': {
                    'key': 'value',
                }
            },
            None
        )


class RecipientTest(StripeResourceTest):

    def test_list_recipients(self):
        stripe.Recipient.all()
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


class CustomerPlanTest(StripeResourceTest):

    def test_create_customer(self):
        stripe.Customer.create(plan=DUMMY_PLAN['id'], card=DUMMY_CARD)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers',
            {
                'card': DUMMY_CARD,
                'plan': DUMMY_PLAN['id'],
            },
            None
        )

    def test_legacy_update_subscription(self):
        customer = stripe.Customer(id="cus_legacy_sub_update")
        customer.update_subscription(idempotency_key='foo',
                                     plan=DUMMY_PLAN['id'])

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_legacy_sub_update/subscription',
            {
                'plan': DUMMY_PLAN['id'],
            },
            {'Idempotency-Key': 'foo'}
        )

    def test_legacy_delete_subscription(self):
        customer = stripe.Customer(id="cus_legacy_sub_delete")
        customer.cancel_subscription()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/customers/cus_legacy_sub_delete/subscription',
            {},
            None
        )

    def test_create_customer_subscription(self):
        customer = stripe.Customer.construct_from({
            'id': 'cus_sub_create',
            'subscriptions': {
                'object': 'list',
                'url': '/v1/customers/cus_sub_create/subscriptions',
            }
        }, 'api_key')

        customer.subscriptions.create(plan=DUMMY_PLAN['id'], coupon='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_sub_create/subscriptions',
            {
                'plan': DUMMY_PLAN['id'],
                'coupon': 'foo',
            },
            None
        )

    def test_retrieve_customer_subscription(self):
        customer = stripe.Customer.construct_from({
            'id': 'cus_foo',
            'subscriptions': {
                'object': 'list',
                'url': '/v1/customers/cus_foo/subscriptions',
            }
        }, 'api_key')

        customer.subscriptions.retrieve('sub_cus')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/customers/cus_foo/subscriptions/sub_cus',
            {},
            None
        )

    def test_update_customer_subscription(self):
        subscription = stripe.Subscription.construct_from({
            'id': "sub_update",
            'customer': "cus_foo",
        }, 'api_key')

        trial_end_dttm = datetime.datetime.now() + datetime.timedelta(days=15)
        trial_end_int = int(time.mktime(trial_end_dttm.timetuple()))

        subscription.trial_end = trial_end_int
        subscription.plan = DUMMY_PLAN['id']
        subscription.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_foo/subscriptions/sub_update',
            {
                'plan': DUMMY_PLAN['id'],
                'trial_end': trial_end_int,
            },
            None
        )

    def test_delete_customer_subscription(self):
        subscription = stripe.Subscription.construct_from({
            'id': "sub_delete",
            'customer': "cus_foo",
        }, 'api_key')

        subscription.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/customers/cus_foo/subscriptions/sub_delete',
            {},
            None
        )


class InvoiceTest(StripeResourceTest):

    def test_add_invoice_item(self):
        customer = stripe.Customer(id="cus_invoice_items")
        customer.add_invoice_item(**DUMMY_INVOICE_ITEM)

        expected = DUMMY_INVOICE_ITEM.copy()
        expected['customer'] = 'cus_invoice_items'

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/invoiceitems',
            expected,
            None,
        )

    def test_retrieve_invoice_items(self):
        customer = stripe.Customer(id="cus_get_invoice_items")
        customer.invoice_items()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/invoiceitems',
            {'customer': 'cus_get_invoice_items'},
        )

    def test_invoice_create(self):
        customer = stripe.Customer(id="cus_invoice")
        stripe.Invoice.create(customer=customer.id)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/invoices',
            {
                'customer': 'cus_invoice',
            },
            None
        )

    def test_retrieve_customer_invoices(self):
        customer = stripe.Customer(id="cus_invoice_items")
        customer.invoices()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/invoices',
            {
                'customer': 'cus_invoice_items',
            },
        )

    def test_pay_invoice(self):
        invoice = stripe.Invoice(id="ii_pay")
        invoice.pay()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/invoices/ii_pay/pay',
            {},
            None
        )

    def test_upcoming_invoice(self):
        stripe.Invoice.upcoming()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/invoices/upcoming',
            {},
        )


class CouponTest(StripeResourceTest):

    def test_create_coupon(self):
        stripe.Coupon.create(**DUMMY_COUPON)
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/coupons',
            DUMMY_COUPON,
            None
        )

    def test_update_coupon(self):
        coup = stripe.Coupon.construct_from({
            'id': 'cu_update',
            'metadata': {},
        }, 'api_key')
        coup.metadata["key"] = "value"
        coup.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            "/v1/coupons/cu_update",
            {
                'metadata': {
                    'key': 'value',
                }
            },
            None
        )

    def test_delete_coupon(self):
        c = stripe.Coupon(id='cu_delete')
        c.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/coupons/cu_delete',
            {},
            None
        )

    def test_detach_coupon(self):
        customer = stripe.Customer(id="cus_delete_discount")
        customer.delete_discount()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/customers/cus_delete_discount/discount',
        )


class PlanTest(StripeResourceTest):

    def test_create_plan(self):
        stripe.Plan.create(**DUMMY_PLAN)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/plans',
            DUMMY_PLAN,
            None
        )

    def test_delete_plan(self):
        p = stripe.Plan(id="pl_delete")
        p.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/plans/pl_delete',
            {},
            None
        )

    def test_update_plan(self):
        p = stripe.Plan(id="pl_update")
        p.name = "Plan Name"
        p.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/plans/pl_update',
            {
                'name': 'Plan Name',
            },
            None
        )


class FileUploadTest(StripeResourceTest):
    def test_create_file_upload(self):
        test_file = tempfile.TemporaryFile()
        stripe.FileUpload.create(
            purpose='dispute_evidence',
            file=test_file
        )
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/files',
            params={
                'purpose': 'dispute_evidence',
                'file': test_file
            },
            headers={'Content-Type': 'multipart/form-data'}
        )

    def test_fetch_file_upload(self):
        stripe.FileUpload.retrieve("fil_foo")
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/files/fil_foo',
            {},
            None
        )

    def test_list_file_uploads(self):
        stripe.FileUpload.all()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/files',
            {}
        )


class RefundTest(StripeResourceTest):

    def test_create_refund(self):
        stripe.Refund.create(charge='ch_foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/refunds',
            {'charge': 'ch_foo'},
            None
        )

    def test_fetch_refund(self):
        stripe.Refund.retrieve('re_foo')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/refunds/re_foo',
            {},
            None
        )

    def test_list_refunds(self):
        stripe.Refund.all(limit=3, charge='ch_foo')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/refunds',
            {'limit': 3, 'charge': 'ch_foo'}
        )

    def test_update_refund(self):
        refund = stripe.resource.Refund.construct_from({
            'id': "ref_update",
            'charge': "ch_update",
            'metadata': {},
        }, 'api_key')
        refund.metadata["key"] = "value"
        refund.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/refunds/ref_update',
            {
                'metadata': {
                    'key': 'value',
                }
            },
            None
        )


class ChargeRefundTest(StripeResourceTest):

    def test_create_refund(self):
        charge = stripe.Charge.construct_from({
            'id': 'ch_foo',
            'refunds': {
                'object': 'list',
                'url': '/v1/charges/ch_foo/refunds',
            }
        }, 'api_key')

        charge.refunds.create()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/charges/ch_foo/refunds',
            {},
            None
        )

    def test_non_recursive_save(self):
        charge = stripe.Charge.construct_from({
            'id': 'ch_nested_update',
            'customer': {
                'object': 'customer',
                'description': 'foo',
            },
            'refunds': {
                'object': 'list',
                'url': '/v1/charges/ch_foo/refunds',
                'data': [{
                    'id': 'ref_123',
                }],
            },
        }, 'api_key')

        charge.customer.description = 'bar'
        charge.refunds.has_more = True
        charge.refunds.data[0].description = 'bar'
        charge.save()

        self.requestor_mock.request.assert_not_called()

    def test_fetch_refund(self):
        charge = stripe.Charge.construct_from({
            'id': 'ch_get_refund',
            'refunds': {
                'object': 'list',
                'url': '/v1/charges/ch_get_refund/refunds',
            }
        }, 'api_key')

        charge.refunds.retrieve("ref_get")

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/charges/ch_get_refund/refunds/ref_get',
            {},
            None
        )

    def test_list_refunds(self):
        charge = stripe.Charge.construct_from({
            'id': 'ch_get_refund',
            'refunds': {
                'object': 'list',
                'url': '/v1/charges/ch_get_refund/refunds',
            }
        }, 'api_key')

        charge.refunds.all()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/charges/ch_get_refund/refunds',
            {},
            None
        )

    def test_update_refund(self):
        refund = stripe.resource.Refund.construct_from({
            'id': "ref_update",
            'charge': "ch_update",
            'metadata': {},
        }, 'api_key')
        refund.metadata["key"] = "value"
        refund.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/refunds/ref_update',
            {
                'metadata': {
                    'key': 'value',
                }
            },
            None
        )


class MetadataTest(StripeResourceTest):

    def test_noop_metadata(self):
        charge = stripe.Charge(id='ch_foo')
        charge.description = 'test'
        charge.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/charges/ch_foo',
            {
                'description': 'test',
            },
            None
        )

    def test_unset_metadata(self):
        charge = stripe.Charge(id='ch_foo')
        charge.metadata = {}
        charge.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/charges/ch_foo',
            {
                'metadata': {},
            },
            None
        )

    def test_whole_update(self):
        charge = stripe.Charge(id='ch_foo')
        charge.metadata = {'whole': 'update'}
        charge.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/charges/ch_foo',
            {
                'metadata': {'whole': 'update'},
            },
            None
        )

    def test_individual_delete(self):
        charge = stripe.Charge(id='ch_foo')
        charge.metadata = {'whole': None}
        charge.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/charges/ch_foo',
            {
                'metadata': {'whole': None},
            },
            None
        )


class ApplicationFeeRefundTest(StripeResourceTest):

    def test_fetch_refund(self):
        fee = stripe.ApplicationFee.construct_from({
            'id': 'fee_get_refund',
            'refunds': {
                'object': 'list',
                'url': '/v1/application_fees/fee_get_refund/refunds',
            }
        }, 'api_key')

        fee.refunds.retrieve("ref_get")

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/application_fees/fee_get_refund/refunds/ref_get',
            {},
            None
        )

    def test_list_refunds(self):
        fee = stripe.ApplicationFee.construct_from({
            'id': 'fee_get_refund',
            'refunds': {
                'object': 'list',
                'url': '/v1/application_fees/fee_get_refund/refunds',
            }
        }, 'api_key')

        fee.refunds.all()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/application_fees/fee_get_refund/refunds',
            {},
            None
        )

    def test_update_refund(self):
        refund = stripe.resource.ApplicationFeeRefund.construct_from({
            'id': "ref_update",
            'fee': "fee_update",
            'metadata': {},
        }, 'api_key')
        refund.metadata["key"] = "value"
        refund.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/application_fees/fee_update/refunds/ref_update',
            {
                'metadata': {
                    'key': 'value',
                }
            },
            None
        )


class BitcoinReceiverTest(StripeResourceTest):

    def test_retrieve_resource(self):
        stripe.BitcoinReceiver.retrieve("btcrcv_test_receiver")
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/bitcoin/receivers/btcrcv_test_receiver',
            {},
            None
        )

    def test_list_receivers(self):
        stripe.BitcoinReceiver.all()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/bitcoin/receivers',
            {},
        )

    def test_create_receiver(self):
        stripe.BitcoinReceiver.create(amount=100, description="some details",
                                      currency="usd",
                                      email="do+fill_now@stripe.com")
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/bitcoin/receivers',
            {
                'amount': 100,
                'description': 'some details',
                'currency': 'usd',
                'email': 'do+fill_now@stripe.com'
            },
            None
        )

    def test_update_receiver_without_customer(self):
        params = {'id': 'receiver', 'amount': 100,
                  'description': "some details", 'currency': "usd"}
        r = stripe.BitcoinReceiver.construct_from(params, 'api_key')
        r.description = "some other details"
        r.save()
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/bitcoin/receivers/receiver',
            {
                'description': 'some other details',
            },
            None
        )

    def test_update_receiver_with_customer(self):
        params = {'id': 'receiver', 'amount': 100,
                  'description': "some details", 'currency': "usd",
                  'customer': "cust"}
        r = stripe.BitcoinReceiver.construct_from(params, 'api_key')
        r.description = "some other details"
        r.save()
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cust/sources/receiver',
            {
                'description': 'some other details',
            },
            None
        )

    def test_delete_receiver_without_customer(self):
        params = {'id': 'receiver', 'amount': 100,
                  'description': "some details", 'currency': "usd"}
        r = stripe.BitcoinReceiver.construct_from(params, 'api_key')
        r.delete()
        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/bitcoin/receivers/receiver',
            {},
            None
        )

    def test_delete_receiver_with_customer(self):
        params = {'id': 'receiver', 'amount': 100,
                  'description': "some details", 'currency': "usd",
                  'customer': "cust"}
        r = stripe.BitcoinReceiver.construct_from(params, 'api_key')
        r.delete()
        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/customers/cust/sources/receiver',
            {},
            None
        )

    def test_list_transactions(self):
        receiver = stripe.BitcoinReceiver.construct_from({
            'id': 'btcrcv_foo',
            'transactions': {
                'object': 'list',
                'url': '/v1/bitcoin/receivers/btcrcv_foo/transactions',
            }
        }, 'api_key')

        receiver.transactions.all()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/bitcoin/receivers/btcrcv_foo/transactions',
            {},
            None
        )


class ProductTest(StripeResourceTest):

    def test_list_products(self):
        stripe.Product.all()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/products',
            {}
        )


class SKUTest(StripeResourceTest):

    def test_list_skus(self):
        stripe.SKU.all()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/skus',
            {}
        )


class OrderTest(StripeResourceTest):

    def test_list_orders(self):
        stripe.Order.all()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/orders',
            {}
        )

    def test_pay_order(self):
        order = stripe.Order(id="or_pay")
        order.pay()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/orders/or_pay/pay',
            {},
            None
        )
