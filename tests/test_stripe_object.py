import datetime
from decimal import Decimal
import json
import pickle
from copy import copy, deepcopy

import pytest

import stripe
from stripe._invoice import Invoice
from stripe._stripe_object import StripeObject
from stripe._subscription import Subscription

# We use this because it has a map, "restriction.currency_options" from string -> CurrencyOptions nested class.
SAMPLE_PROMOTION_CODE = json.loads(
    """{
  "id": "promo_1NzO4FIFdHa3DensTcbAA0mz",
  "object": "promotion_code",
  "restrictions": {
    "currency_options": {
      "gbp": {
        "minimum_amount": 10
      },
      "usd": {
        "minimum_amount": 5
      }
    }
  }
}
"""
)

SAMPLE_INVOICE = json.loads(
    """{
  "id": "in_xyz",
  "object": "invoice",
  "automatic_tax": {
    "enabled": false,
    "status": null
  },
  "created": 1694725031,
  "lines": {
    "object": "list",
    "data": [
      {
        "id": "sli_xyz",
        "object": "line_item",
        "period": {
          "end": 1697316491,
          "start": 1694724491
        },
        "plan": {
          "id": "price_xyz",
          "object": "plan"
        },
        "price": {
          "id": "price_xyz",
          "object": "price",
          "billing_scheme": "per_unit",
          "recurring": {
            "aggregate_usage": null,
            "interval": "month",
            "interval_count": 1,
            "trial_period_days": null,
            "usage_type": "licensed"
          }
        }
      }
    ],
    "has_more": false,
    "total_count": 1,
    "url": "/v1/invoices/in_1NqMb5IFdHa3DenshEllwgEX/lines"
  },
  "livemode": false,
  "next_payment_attempt": null,
  "shipping_cost": {
    "taxes": [{"amount": 10, "rate": {"id": "rate_xyz", "object": "tax_rate", "active": false}}]
  }
}
"""
)


class TestStripeObject(object):
    def test_initializes_with_parameters(self):
        obj = StripeObject("foo", "bar", myparam=5, yourparam="boo")

        assert obj.id == "foo"
        assert obj.api_key == "bar"

    def test_access(self):
        obj = StripeObject("myid", "mykey", myparam=5)

        # Empty
        with pytest.raises(AttributeError):
            obj.myattr
        with pytest.raises(KeyError):
            obj["myattr"]
        assert getattr(obj, "myattr", "def") == "def"
        assert "myattr" not in obj

        # Setters
        obj.myattr = "myval"
        obj["myitem"] = "itval"
        obj.mydef = getattr(obj, "mydef", "sdef")
        assert obj.mydef == "sdef"

        # Getters
        assert obj.myattr == "myval"
        assert obj["myattr"] == "myval"

        assert sorted(obj.to_dict().keys()) == [
            "id",
            "myattr",
            "mydef",
            "myitem",
        ]

        assert sorted(obj.to_dict().values()) == [
            "itval",
            "myid",
            "myval",
            "sdef",
        ]

        # Illegal operations
        with pytest.raises(ValueError):
            obj.foo = ""

    def test_refresh_from(self, mocker):
        obj = StripeObject.construct_from(
            {"foo": "bar", "trans": "me"}, "mykey"
        )

        assert obj.api_key == "mykey"
        assert obj.foo == "bar"
        assert obj["trans"] == "me"
        assert obj.stripe_version is stripe.api_version
        assert obj.stripe_account is None
        assert obj.last_response is None

        last_response = mocker.Mock()
        obj.refresh_from(
            {"foo": "baz", "johnny": 5},
            "key2",
            stripe_version="2017-08-15",
            stripe_account="acct_foo",
            last_response=last_response,
        )

        assert obj.johnny == 5
        assert obj.foo == "baz"
        with pytest.raises(AttributeError):
            obj.trans
        assert obj.api_key == "key2"
        assert obj.stripe_version == "2017-08-15"
        assert obj.stripe_account == "acct_foo"
        assert obj.last_response == last_response

        obj.refresh_from(
            {"trans": 4, "metadata": {"amount": 42}}, "key2", True
        )

        assert obj.foo == "baz"
        assert obj.trans == 4

    def test_passing_nested_refresh(self):
        obj = StripeObject.construct_from(
            {"foos": {"type": "list", "data": [{"id": "nested"}]}},
            "key",
            stripe_account="acct_foo",
        )

        nested = obj.foos.data[0]

        assert obj.api_key == "key"
        assert nested.id == "nested"
        assert nested.api_key == "key"
        assert nested.stripe_account == "acct_foo"

    def test_refresh_from_nested_object(self):
        obj = stripe.Invoice.construct_from(SAMPLE_INVOICE, "key")

        assert len(obj.lines) == 1
        # Does a list get deserialized to the correct class?
        assert isinstance(obj.lines, stripe.ListObject)
        # Do items within a list get deserialized to the correct class?
        assert isinstance(obj.lines.data[0], stripe.InvoiceLineItem)
        # Do references to other top-level resources get deserialized to the correct class?
        assert isinstance(obj.lines.data[0].price, stripe.Price)
        assert obj.lines.data[0].price.billing_scheme == "per_unit"
        # Do inner classes on referenced top-level resources get deserialized to the correct inner class.
        assert isinstance(
            obj.lines.data[0].price.recurring, stripe.Price.Recurring
        )
        assert isinstance(
            obj.lines.data[0].price.recurring, stripe.Price.Recurring
        )

        # Test: do nested objects get deserialized to the correct inner class?
        assert isinstance(obj.automatic_tax, stripe.Invoice.AutomaticTax)
        assert isinstance(obj.shipping_cost, stripe.Invoice.ShippingCost)
        # Test: do nested objects inside lists get deserialized to the correct inner class?
        assert isinstance(
            obj.shipping_cost.taxes[0], stripe.Invoice.ShippingCost.Tax
        )

    def test_refresh_from_nested_object_can_be_paged(self):
        obj = stripe.Invoice.construct_from(SAMPLE_INVOICE, "key")

        assert len(obj.lines) == 1
        assert isinstance(obj.lines, stripe.ListObject)
        seen = [item["id"] for item in obj.lines.auto_paging_iter()]

        assert seen == ["sli_xyz"]

        assert isinstance(obj.lines.data[0], stripe.InvoiceLineItem)
        assert isinstance(obj.lines.data[0].price, StripeObject)
        assert isinstance(obj.lines.data[0].price, stripe.Price)
        assert obj.lines.data[0].price.billing_scheme == "per_unit"

    def test_refresh_on_map_to_nested_object(self):
        obj = stripe.PromotionCode.construct_from(SAMPLE_PROMOTION_CODE, "key")

        assert isinstance(
            obj.restrictions.currency_options,
            dict,
        )
        assert not isinstance(
            obj.restrictions.currency_options,
            StripeObject,
        )
        assert isinstance(
            obj.restrictions.currency_options["gbp"],
            stripe.PromotionCode.Restrictions.CurrencyOptions,
        )

    def test_to_json(self):
        obj = StripeObject.construct_from(SAMPLE_INVOICE, "key")

        self.check_invoice_data(json.loads(str(obj)))

    def check_invoice_data(self, data):
        # Check rough structure
        assert len(list(data.keys())) == 8
        assert len(list(data["lines"]["data"][0].keys())) == 5
        assert len(data["lines"]["data"]) == 1

        # Check various data types
        assert data["created"] == 1694725031
        assert data["next_payment_attempt"] is None
        assert data["livemode"] is False
        assert (
            data["lines"]["data"][0]["price"]["billing_scheme"] == "per_unit"
        )

    def test_repr(self):
        obj = StripeObject("foo", "bar", myparam=5)

        obj["object"] = "\u4e00boo\u1f00"
        obj.date = datetime.datetime.fromtimestamp(1511136000)
        obj.dec = Decimal("1.23")

        res = repr(obj)

        assert "<StripeObject \u4e00boo\u1f00" in res
        assert "id=foo" in res
        assert '"date": 1511136000' in res
        assert '"dec": "1.23"' in res

    def test_pickling(self):
        obj = StripeObject("foo", "bar", myparam=5)

        obj["object"] = "boo"
        obj.refresh_from(
            {
                "fala": "lalala",
                # ensures that empty strings are correctly unpickled in Py3
                "emptystring": "",
            },
            api_key="bar",
            partial=True,
        )

        assert obj.fala == "lalala"

        pickled = pickle.dumps(obj)
        newobj = pickle.loads(pickled)

        assert newobj.id == "foo"
        assert newobj.api_key == "bar"
        assert newobj["object"] == "boo"
        assert newobj.fala == "lalala"
        assert newobj.emptystring == ""

    def test_deletion(self):
        obj = StripeObject("id", "key")

        obj.coupon = "foo"
        assert obj.coupon == "foo"

        del obj.coupon
        with pytest.raises(AttributeError):
            obj.coupon

        obj.refresh_from({"coupon": "foo"}, api_key="bar", partial=True)
        assert obj.coupon == "foo"

    def test_deletion_metadata(self):
        obj = StripeObject.construct_from(
            {"metadata": {"key": "value"}}, "mykey"
        )

        assert obj.metadata["key"] == "value"

        del obj.metadata["key"]
        with pytest.raises(KeyError):
            obj.metadata["key"]

    def test_copy(self):
        nested = StripeObject.construct_from({"value": "bar"}, "mykey")
        obj = StripeObject.construct_from(
            {"empty": "", "value": "foo", "nested": nested},
            "mykey",
            stripe_account="myaccount",
        )

        copied = copy(obj)

        assert copied.empty == ""
        assert copied.value == "foo"
        assert copied.nested.value == "bar"

        assert copied.api_key == "mykey"
        assert copied.stripe_account == "myaccount"

        # Verify that we're not deep copying nested values.
        assert id(nested) == id(copied.nested)

    def test_deepcopy(self):
        nested = StripeObject.construct_from({"value": "bar"}, "mykey")
        obj = StripeObject.construct_from(
            {"empty": "", "value": "foo", "nested": nested},
            "mykey",
            stripe_account="myaccount",
        )

        copied = deepcopy(obj)

        assert copied.empty == ""
        assert copied.value == "foo"
        assert copied.nested.value == "bar"

        assert copied.api_key == "mykey"
        assert copied.stripe_account == "myaccount"

        # Verify that we're actually deep copying nested values.
        assert id(nested) != id(copied.nested)

    def test_to_dict_recursive(self):
        foo = StripeObject.construct_from({"value": "foo"}, "mykey")
        bar = StripeObject.construct_from({"value": "bar"}, "mykey")
        obj = StripeObject.construct_from(
            {"empty": "", "value": "foobar", "nested": [foo, bar]}, "mykey"
        )

        d = obj._to_dict_recursive()
        assert d == {
            "empty": "",
            "value": "foobar",
            "nested": [{"value": "foo"}, {"value": "bar"}],
        }
        assert not isinstance(d["nested"][0], StripeObject)
        assert not isinstance(d["nested"][1], StripeObject)

    def test_serialize_empty_string_unsets(self):
        class SerializeToEmptyString(StripeObject):
            def serialize(self, previous):
                return ""

        nested = SerializeToEmptyString.construct_from(
            {"value": "bar"}, "mykey"
        )
        obj = StripeObject.construct_from({"nested": nested}, "mykey")

        assert obj.serialize(None) == {"nested": ""}

    def test_serialize_empty_when_nothing_changed(self):
        obj = StripeObject.construct_from({"id": "x", "name": "alice"}, "key")
        assert obj.serialize(None) == {}

    def test_serialize_includes_unsaved_values(self):
        obj = StripeObject.construct_from({"id": "x", "name": "alice"}, "key")
        obj.name = "bob"
        assert obj.serialize(None) == {"name": "bob"}

    def test_serialize_multiple_unsaved_values(self):
        obj = StripeObject.construct_from(
            {"id": "x", "name": "alice", "email": "a@example.com"}, "key"
        )
        obj.name = "bob"
        obj.email = "b@example.com"
        result = obj.serialize(None)
        assert result == {"name": "bob", "email": "b@example.com"}

    def test_serialize_setting_same_value_still_serializes(self):
        obj = StripeObject.construct_from({"id": "x", "name": "alice"}, "key")
        obj.name = "alice"
        assert obj.serialize(None) == {"name": "alice"}

    def test_serialize_skips_id(self):
        obj = StripeObject.construct_from({"id": "x"}, "key")
        obj._unsaved_values.add("id")
        assert obj.serialize(None) == {}

    def test_serialize_skips_underscore_prefixed_keys(self):
        obj = StripeObject.construct_from({"id": "x", "_secret": "s"}, "key")
        obj._unsaved_values.add("_secret")
        assert obj.serialize(None) == {}

    def test_serialize_skips_api_resources(self):
        inner = stripe.Customer.construct_from(
            {"id": "cus_123", "object": "customer"}, "key"
        )
        obj = StripeObject.construct_from(
            {"id": "x", "customer": inner}, "key"
        )
        obj._unsaved_values.add("customer")
        assert obj.serialize(None) == {}

    def test_serialize_nested_changed_object(self):
        obj = StripeObject.construct_from(
            {"id": "x", "metadata": {"key1": "val1"}}, "key"
        )
        obj.metadata["key1"] = "val2"
        result = obj.serialize(None)
        assert result == {"metadata": {"key1": "val2"}}

    def test_serialize_nested_unchanged_excluded(self):
        obj = StripeObject.construct_from(
            {"id": "x", "metadata": {"key1": "val1"}}, "key"
        )
        assert obj.serialize(None) == {}

    def test_serialize_nested_new_key(self):
        obj = StripeObject.construct_from(
            {"id": "x", "metadata": {"key1": "val1"}}, "key"
        )
        obj.metadata["key2"] = "val2"
        result = obj.serialize(None)
        assert result == {"metadata": {"key2": "val2"}}

    def test_serialize_deeply_nested(self):
        obj = StripeObject.construct_from(
            {
                "id": "x",
                "level1": {
                    "level2": {"deep": "original"},
                },
            },
            "key",
        )
        obj.level1.level2.deep = "changed"
        result = obj.serialize(None)
        assert result == {"level1": {"level2": {"deep": "changed"}}}

    def test_serialize_diff_removed_key_becomes_empty_string(self):
        obj = StripeObject.construct_from(
            {"id": "x", "metadata": {"key1": "v1", "key2": "v2"}}, "key"
        )
        obj.metadata = {"key1": "v1"}
        result = obj.serialize(None)
        assert result == {"metadata": {"key1": "v1", "key2": ""}}

    def test_serialize_unsaved_none_becomes_empty_string(self):
        obj = StripeObject.construct_from({"id": "x", "name": "alice"}, "key")
        obj.name = None
        assert obj.serialize(None) == {"name": ""}

    def test_serialize_unsaved_empty_string(self):
        # __setitem__ rejects empty strings, so construct with it
        # already empty and mark it as unsaved
        obj = StripeObject.construct_from({"id": "x", "name": ""}, "key")
        obj._unsaved_values.add("name")
        assert obj.serialize(None) == {"name": ""}

    def test_serialize_explicit_previous_used_for_diff(self):
        obj = StripeObject.construct_from({"id": "x", "metadata": {}}, "key")
        obj.metadata = {"key1": "new"}
        previous = {"metadata": {"key1": "old", "removed_key": "gone"}}
        result = obj.serialize(previous)
        assert result == {"metadata": {"key1": "new", "removed_key": ""}}

    def test_serialize_previous_none_uses_internal_previous(self):
        obj = StripeObject.construct_from(
            {"id": "x", "metadata": {"key1": "v1", "key2": "v2"}}, "key"
        )
        obj.metadata = {"key1": "v1"}
        result = obj.serialize(None)
        assert result == {"metadata": {"key1": "v1", "key2": ""}}

    def test_serialize_additional_owners(self):
        obj = StripeObject.construct_from(
            {
                "id": "x",
                "additional_owners": [
                    {"first_name": "alice"},
                    {"first_name": "bob"},
                ],
            },
            "key",
        )
        result = obj.serialize(None)
        # additional_owners is always serialized when non-None;
        # child objects have no unsaved values so they serialize to {}
        assert "additional_owners" in result
        assert result["additional_owners"]["0"] == {}
        assert result["additional_owners"]["1"] == {}

    def test_serialize_additional_owners_none_excluded(self):
        obj = StripeObject.construct_from(
            {"id": "x", "additional_owners": None}, "key"
        )
        assert obj.serialize(None) == {}

    def test_serialize_after_construct_and_modify(self):
        obj = StripeObject.construct_from(
            {
                "id": "obj_123",
                "name": "original",
                "metadata": {"env": "test"},
            },
            "key",
        )
        obj.name = "updated"
        obj.metadata["env"] = "prod"
        result = obj.serialize(None)
        assert result == {
            "name": "updated",
            "metadata": {"env": "prod"},
        }

    def test_serialize_after_refresh_resets_unsaved(self):
        obj = StripeObject.construct_from(
            {"id": "x", "name": "original"}, "key"
        )
        obj.name = "changed"
        assert obj.serialize(None) == {"name": "changed"}

        obj.refresh_from({"id": "x", "name": "from_api"}, "key")
        assert obj.serialize(None) == {}

    def test_serialize_after_refresh_then_modify(self):
        obj = StripeObject.construct_from(
            {"id": "x", "name": "v1", "email": "a@example.com"}, "key"
        )
        obj.refresh_from(
            {"id": "x", "name": "v2", "email": "a@example.com"}, "key"
        )
        obj.email = "new@example.com"
        result = obj.serialize(None)
        assert result == {"email": "new@example.com"}

    def test_serialize_new_key(self):
        obj = StripeObject.construct_from({"id": "x"}, "key")
        obj["new_field"] = "value"
        assert obj.serialize(None) == {"new_field": "value"}

    def test_serialize_new_key_via_attribute(self):
        obj = StripeObject.construct_from({"id": "x"}, "key")
        obj.new_field = "value"
        assert obj.serialize(None) == {"new_field": "value"}

    def test_field_name_remapping(self):
        class Foo(StripeObject):
            _field_remappings = {"getter_name": "data_name"}

        obj = Foo.construct_from({"data_name": "foo"}, "mykey")
        assert obj.getter_name == "foo"

    def test_sends_request_with_api_key(self, http_client_mock):
        obj = StripeObject("id", "key")

        http_client_mock.stub_request(
            "get",
            path="/foo",
        )

        obj._request("get", "/foo", base_address="api")

        http_client_mock.assert_requested(
            api_key="key",
            stripe_account=None,
        )

    @pytest.mark.anyio
    async def test_request_async_succeeds(self, http_client_mock):
        http_client_mock.stub_request("get", "/foo")
        obj = StripeObject("id", "key")
        await obj._request_async("get", "/foo", base_address="api")
        http_client_mock.assert_requested(
            api_key="key",
            stripe_account=None,
        )

    def test_refresh_from_creates_new_requestor(self):
        obj = StripeObject.construct_from({}, key="origkey")

        orig_requestor = obj._requestor
        assert obj.api_key == "origkey"

        obj.refresh_from({}, "newkey")

        new_requestor = obj._requestor
        assert orig_requestor is not new_requestor
        assert obj.api_key == "newkey"
        assert orig_requestor.api_key == "origkey"

    def test_can_update_api_key(self, http_client_mock):
        obj = StripeObject("id", "key")

        http_client_mock.stub_request(
            "get",
            path="/foo",
        )

        obj.api_key = "key2"
        obj._request("get", "/foo", base_address="api")

        assert "api_key" not in obj.to_dict()

        http_client_mock.assert_requested(
            api_key="key2",
            stripe_account=None,
        )

    def test_invoice_payment_method_gets_special_error(self):
        def is_good_error(e: Exception) -> bool:
            return "multiple-partial-payments-on-invoices" in str(e)

        i = Invoice()

        with pytest.raises(AttributeError) as e:
            i.payment_intent  # type: ignore
        assert is_good_error(e.value)

        with pytest.raises(KeyError) as e:
            i["payment_intent"]
        assert is_good_error(e.value)

        # only that property gets the special error
        with pytest.raises(AttributeError) as e:
            i.blah  # type: ignore
        assert not is_good_error(e.value)

        with pytest.raises(KeyError) as e:
            i["blah"]
        assert not is_good_error(e.value)

        # other classes don't have that special error
        so = StripeObject()
        with pytest.raises(AttributeError) as e:
            so.payment_intent  # type: ignore
        assert not is_good_error(e.value)

        with pytest.raises(KeyError) as e:
            so["payment_intent"]
        assert not is_good_error(e.value)

    def test_eq_same_data(self):
        a = StripeObject.construct_from({"id": "x", "name": "a"}, "key")
        b = StripeObject.construct_from({"id": "x", "name": "a"}, "key")
        assert a == b

    def test_eq_different_data(self):
        a = StripeObject.construct_from({"id": "x", "name": "a"}, "key")
        b = StripeObject.construct_from({"id": "x", "name": "b"}, "key")
        assert a != b

    def test_eq_different_types_not_equal(self):
        data = {"id": "x", "name": "a"}
        invoice = stripe.Invoice.construct_from(
            {**data, "object": "invoice"}, "key"
        )
        customer = stripe.Customer.construct_from(
            {**data, "object": "customer"}, "key"
        )
        assert invoice != customer

    def test_eq_same_resource_type(self):
        a = stripe.Customer.construct_from(
            {"id": "cus_1", "object": "customer", "name": "alice"}, "key"
        )
        b = stripe.Customer.construct_from(
            {"id": "cus_1", "object": "customer", "name": "alice"}, "key"
        )
        assert a == b

    def test_eq_diff_resource_type_same_data(self):
        a = stripe.Customer.construct_from(
            {"id": "cus_1", "object": "customer", "name": "alice"}, "key"
        )
        b = stripe.Invoice.construct_from(
            {"id": "cus_1", "object": "customer", "name": "alice"}, "key"
        )
        assert a != b

    def test_eq_not_equal_to_dict(self):
        obj = StripeObject.construct_from({"id": "x"}, "key")
        assert obj != {"id": "x"}

    def test_is_not_dict(self):
        obj = StripeObject("id", "key")
        assert not isinstance(obj, dict)

    def test_items_field_not_shadowed_by_dict_items(self):
        obj = StripeObject.construct_from(
            {
                "id": "sub_123",
                "object": "subscription",
                "items": {"object": "list", "data": [{"id": "si_123"}]},
            },
            "key",
        )
        assert isinstance(obj.items, stripe.ListObject)

    def test_to_dict(self):
        obj = StripeObject.construct_from(
            {"id": "foo", "name": "bar"},
            "key",
        )
        d = obj.to_dict()
        assert d == {"id": "foo", "name": "bar"}
        assert isinstance(d, dict)
        assert not isinstance(d, StripeObject)

    def test_to_dict_recursive_by_default(self):
        inner = StripeObject.construct_from({"nested": "val"}, "key")
        obj = StripeObject.construct_from({"id": "x", "child": inner}, "key")
        d = obj.to_dict()
        assert d == {"id": "x", "child": {"nested": "val"}}
        assert isinstance(d["child"], dict)
        assert not isinstance(d["child"], StripeObject)

    def test_to_dict_non_recursive(self):
        inner = StripeObject.construct_from({"nested": "val"}, "key")
        obj = StripeObject.construct_from({"id": "x", "child": inner}, "key")
        d = obj.to_dict(recursive=False)
        assert d["id"] == "x"
        # non-recursive preserves nested StripeObjects
        assert isinstance(d["child"], StripeObject)

    def test_to_dict_is_a_copy(self):
        obj = StripeObject.construct_from({"id": "x", "name": "a"}, "key")
        d = obj.to_dict()
        d["name"] = "mutated"
        assert obj.name == "a"

    def test_to_dict_with_list_of_nested_objects(self):
        obj = StripeObject.construct_from(
            {"id": "x", "items": [{"a": 1}, {"b": 2}]}, "key"
        )
        d = obj.to_dict()
        assert d == {"id": "x", "items": [{"a": 1}, {"b": 2}]}
        assert not isinstance(d["items"][0], StripeObject)

    def test_to_dict_json_serializable_converts_decimal(self):
        obj = StripeObject.construct_from(
            {"amount": Decimal("9.99"), "name": "foo"}, "key"
        )
        d = obj.to_dict(for_json=True)
        assert d == {"amount": "9.99", "name": "foo"}
        assert isinstance(d["amount"], str)

    def test_to_dict_json_serializable_converts_datetime(self):
        dt = datetime.datetime(
            2024, 1, 15, 12, 0, 0, tzinfo=datetime.timezone.utc
        )
        obj = StripeObject.construct_from({"created": dt, "id": "x"}, "key")
        d = obj.to_dict(for_json=True)
        assert isinstance(d["created"], int)

    def test_to_dict_json_serializable_nested(self):
        inner = StripeObject.construct_from({"amount": Decimal("1.23")}, "key")
        obj = StripeObject.construct_from({"child": inner, "id": "x"}, "key")
        d = obj.to_dict(for_json=True)
        assert d["child"] == {"amount": "1.23"}
        assert isinstance(d["child"]["amount"], str)

    def test_to_dict_json_serializable_false_preserves_decimal(self):
        obj = StripeObject.construct_from({"amount": Decimal("9.99")}, "key")
        d = obj.to_dict()
        assert isinstance(d["amount"], Decimal)

    def test_update_sets_values(self):
        obj = StripeObject.construct_from({"id": "x", "name": "a"}, "key")
        obj.update({"name": "b", "email": "b@example.com"})
        assert obj.name == "b"
        assert obj.email == "b@example.com"

    def test_update_marks_keys_unsaved(self):
        obj = StripeObject.construct_from({"id": "x", "name": "a"}, "key")
        obj.update({"name": "b", "email": "b@example.com"})
        assert "name" in obj._unsaved_values
        assert "email" in obj._unsaved_values

    def test_update_shows_in_serialize(self):
        obj = StripeObject.construct_from({"id": "x", "name": "a"}, "key")
        obj.update({"name": "b"})
        assert obj.serialize(None) == {"name": "b"}

    def test_update_multiple_calls(self):
        obj = StripeObject.construct_from({"id": "x"}, "key")
        obj.update({"a": 1})
        obj.update({"b": 2})
        assert obj.a == 1
        assert obj.b == 2
        assert obj.serialize(None) == {"a": 1, "b": 2}
