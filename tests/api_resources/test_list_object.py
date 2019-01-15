from __future__ import absolute_import, division, print_function

import json

import pytest

import stripe


class TestListObject(object):
    @pytest.fixture
    def list_object(self):
        return stripe.ListObject.construct_from(
            {"object": "list", "url": "/my/path", "data": ["foo"]}, "mykey"
        )

    def assert_response(self, res):
        assert isinstance(res[0], stripe.Charge)
        assert res[0].foo == "bar"

    def test_for_loop(self, list_object):
        seen = []

        for item in list_object:
            seen.append(item)

        assert seen == ["foo"]

    def test_list(self, request_mock, list_object):
        request_mock.stub_request(
            "get", "/my/path", [{"object": "charge", "foo": "bar"}]
        )

        res = list_object.list(myparam="you")

        request_mock.assert_requested(
            "get", "/my/path", {"myparam": "you"}, None
        )
        self.assert_response(res)

    def test_create(self, request_mock, list_object):
        request_mock.stub_request(
            "post", "/my/path", [{"object": "charge", "foo": "bar"}]
        )

        res = list_object.create(myparam="eter")

        request_mock.assert_requested(
            "post", "/my/path", {"myparam": "eter"}, None
        )
        self.assert_response(res)

    def test_retrieve(self, request_mock, list_object):
        request_mock.stub_request(
            "get", "/my/path/myid", [{"object": "charge", "foo": "bar"}]
        )

        res = list_object.retrieve("myid", myparam="cow")

        request_mock.assert_requested(
            "get", "/my/path/myid", {"myparam": "cow"}, None
        )

        self.assert_response(res)

    def test_len(self, list_object):
        assert len(list_object) == 1

    def test_bool(self, list_object):
        assert list_object

        empty = stripe.ListObject.construct_from(
            {"object": "list", "url": "/my/path", "data": []}, "mykey"
        )
        assert bool(empty) is False

    def test_serialize_empty_list(self):
        empty = stripe.ListObject.construct_from(
            {"object": "list", "data": []}, "mykey"
        )
        serialized = str(empty)
        deserialized = stripe.ListObject.construct_from(
            json.loads(serialized), "mykey"
        )
        assert deserialized == empty

    def test_serialize_nested_empty_list(self):
        empty = stripe.ListObject.construct_from(
            {"object": "list", "data": []}, "mykey"
        )
        obj = stripe.stripe_object.StripeObject.construct_from(
            {"nested": empty}, "mykey"
        )
        serialized = str(obj)
        deserialized = stripe.stripe_object.StripeObject.construct_from(
            json.loads(serialized), "mykey"
        )
        assert deserialized.nested == empty


class TestAutoPaging:
    @staticmethod
    def pageable_model_response(ids, has_more):
        return {
            "object": "list",
            "url": "/v1/pageablemodels",
            "data": [{"id": id, "object": "pageablemodel"} for id in ids],
            "has_more": has_more,
        }

    def test_iter_one_page(self, request_mock):
        lo = stripe.ListObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], False), "mykey"
        )

        request_mock.assert_no_request()

        seen = [item["id"] for item in lo.auto_paging_iter()]

        assert seen == ["pm_123", "pm_124"]

    def test_iter_two_pages(self, request_mock):
        lo = stripe.ListObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], True), "mykey"
        )
        lo._retrieve_params = {"foo": "bar"}

        request_mock.stub_request(
            "get",
            "/v1/pageablemodels",
            self.pageable_model_response(["pm_125", "pm_126"], False),
        )

        seen = [item["id"] for item in lo.auto_paging_iter()]

        request_mock.assert_requested(
            "get",
            "/v1/pageablemodels",
            {"starting_after": "pm_124", "foo": "bar"},
            None,
        )

        assert seen == ["pm_123", "pm_124", "pm_125", "pm_126"]

    def test_class_method_two_pages(self, request_mock):
        request_mock.stub_request(
            "get",
            "/v1/charges",
            {
                "object": "list",
                "data": [{"id": "ch_001"}],
                "url": "/v1/charges",
                "has_more": False,
            },
        )

        seen = [
            item["id"]
            for item in stripe.Charge.auto_paging_iter(limit=25, foo="bar")
        ]

        request_mock.assert_requested(
            "get", "/v1/charges", {"limit": 25, "foo": "bar"}
        )
        assert seen == ["ch_001"]
