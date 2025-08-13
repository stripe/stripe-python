import datetime
import json
import pickle
from copy import copy, deepcopy

import pytest

import stripe

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
        obj = stripe.stripe_object.StripeObject(
            "foo", "bar", myparam=5, yourparam="boo"
        )

        assert obj.id == "foo"
        assert obj.api_key == "bar"

    def test_access(self):
        obj = stripe.stripe_object.StripeObject("myid", "mykey", myparam=5)

        # Empty
        with pytest.raises(AttributeError):
            obj.myattr
        with pytest.raises(KeyError):
            obj["myattr"]
        assert obj.get("myattr", "def") == "def"
        assert obj.get("myattr") is None

        # Setters
        obj.myattr = "myval"
        obj["myitem"] = "itval"
        assert obj.setdefault("mydef", "sdef") == "sdef"

        # Getters
        assert obj.setdefault("myattr", "sdef") == "myval"
        assert obj.myattr == "myval"
        assert obj["myattr"] == "myval"
        assert obj.get("myattr") == "myval"

        assert sorted(obj.keys()) == ["id", "myattr", "mydef", "myitem"]

        assert sorted(obj.values()) == ["itval", "myid", "myval", "sdef"]

        # Illegal operations
        with pytest.raises(ValueError):
            obj.foo = ""

    def test_refresh_from(self, mocker):
        obj = stripe.stripe_object.StripeObject.construct_from(
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
        obj = stripe.stripe_object.StripeObject.construct_from(
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
        assert isinstance(
            obj.lines.data[0].price, stripe.stripe_object.StripeObject
        )
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
            stripe.stripe_object.StripeObject,
        )
        assert isinstance(
            obj.restrictions.currency_options["gbp"],
            stripe.PromotionCode.Restrictions.CurrencyOptions,
        )

    def test_to_json(self):
        obj = stripe.stripe_object.StripeObject.construct_from(
            SAMPLE_INVOICE, "key"
        )

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
        obj = stripe.stripe_object.StripeObject("foo", "bar", myparam=5)

        obj["object"] = "\u4e00boo\u1f00"
        obj.date = datetime.datetime.fromtimestamp(1511136000)

        res = repr(obj)

        assert "<StripeObject \u4e00boo\u1f00" in res
        assert "id=foo" in res
        assert '"date": 1511136000' in res

    def test_pickling(self):
        obj = stripe.stripe_object.StripeObject("foo", "bar", myparam=5)

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
        obj = stripe.stripe_object.StripeObject("id", "key")

        obj.coupon = "foo"
        assert obj.coupon == "foo"

        del obj.coupon
        with pytest.raises(AttributeError):
            obj.coupon

        obj.refresh_from({"coupon": "foo"}, api_key="bar", partial=True)
        assert obj.coupon == "foo"

    def test_deletion_metadata(self):
        obj = stripe.stripe_object.StripeObject.construct_from(
            {"metadata": {"key": "value"}}, "mykey"
        )

        assert obj.metadata["key"] == "value"

        del obj.metadata["key"]
        with pytest.raises(KeyError):
            obj.metadata["key"]

    def test_copy(self):
        nested = stripe.stripe_object.StripeObject.construct_from(
            {"value": "bar"}, "mykey"
        )
        obj = stripe.stripe_object.StripeObject.construct_from(
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
        nested = stripe.stripe_object.StripeObject.construct_from(
            {"value": "bar"}, "mykey"
        )
        obj = stripe.stripe_object.StripeObject.construct_from(
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
        foo = stripe.stripe_object.StripeObject.construct_from(
            {"value": "foo"}, "mykey"
        )
        bar = stripe.stripe_object.StripeObject.construct_from(
            {"value": "bar"}, "mykey"
        )
        obj = stripe.stripe_object.StripeObject.construct_from(
            {"empty": "", "value": "foobar", "nested": [foo, bar]}, "mykey"
        )

        d = obj.to_dict_recursive()
        assert d == {
            "empty": "",
            "value": "foobar",
            "nested": [{"value": "foo"}, {"value": "bar"}],
        }
        assert not isinstance(
            d["nested"][0], stripe.stripe_object.StripeObject
        )
        assert not isinstance(
            d["nested"][1], stripe.stripe_object.StripeObject
        )

    def test_serialize_empty_string_unsets(self):
        class SerializeToEmptyString(stripe.stripe_object.StripeObject):
            def serialize(self, previous):
                return ""

        nested = SerializeToEmptyString.construct_from(
            {"value": "bar"}, "mykey"
        )
        obj = stripe.stripe_object.StripeObject.construct_from(
            {"nested": nested}, "mykey"
        )

        assert obj.serialize(None) == {"nested": ""}

    def test_field_name_remapping(self):
        class Foo(stripe.stripe_object.StripeObject):
            _field_remappings = {"getter_name": "data_name"}

        obj = Foo.construct_from({"data_name": "foo"}, "mykey")
        assert obj.getter_name == "foo"

    def test_sends_request_with_api_key(self, http_client_mock):
        obj = stripe.stripe_object.StripeObject("id", "key")

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
        obj = stripe.stripe_object.StripeObject("id", "key")
        await obj._request_async("get", "/foo", base_address="api")
        http_client_mock.assert_requested(
            api_key="key",
            stripe_account=None,
        )

    def test_refresh_from_creates_new_requestor(self):
        obj = stripe.stripe_object.StripeObject.construct_from(
            {}, key="origkey"
        )

        orig_requestor = obj._requestor
        assert obj.api_key == "origkey"

        obj.refresh_from({}, "newkey")

        new_requestor = obj._requestor
        assert orig_requestor is not new_requestor
        assert obj.api_key == "newkey"
        assert orig_requestor.api_key == "origkey"

    def test_can_update_api_key(self, http_client_mock):
        obj = stripe.stripe_object.StripeObject("id", "key")

        http_client_mock.stub_request(
            "get",
            path="/foo",
        )

        obj.api_key = "key2"
        obj._request("get", "/foo", base_address="api")

        assert "api_key" not in obj.items()

        http_client_mock.assert_requested(
            api_key="key2",
            stripe_account=None,
        )
