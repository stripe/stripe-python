from __future__ import absolute_import, division, print_function

import json

import pytest

import stripe


class TestSearchResultObject(object):
    @pytest.fixture
    def search_result_object(self):
        return stripe.SearchResultObject.construct_from(
            {"object": "search_result", "url": "/my/path", "data": ["foo"]},
            "mykey",
        )

    def test_search(self, request_mock, search_result_object):
        request_mock.stub_request(
            "get",
            "/my/path",
            {
                "object": "search_result",
                "data": [{"object": "charge", "foo": "bar"}],
            },
        )

        res = search_result_object.search(
            myparam="you", stripe_account="acct_123"
        )

        request_mock.assert_requested(
            "get", "/my/path", {"myparam": "you"}, None
        )
        assert isinstance(res, stripe.SearchResultObject)
        assert res.stripe_account == "acct_123"
        assert isinstance(res.data, list)
        assert isinstance(res.data[0], stripe.Charge)
        assert res.data[0].foo == "bar"

    def test_is_empty(self):
        sro = stripe.SearchResultObject.construct_from({"data": []}, None)
        assert sro.is_empty is True

    def test_empty_search_result(self):
        sro = stripe.SearchResultObject.empty_search_result()
        assert sro.is_empty

    def test_iter(self):
        arr = [{"id": 1}, {"id": 2}, {"id": 3}]
        expected = stripe.util.convert_to_stripe_object(arr)
        sro = stripe.SearchResultObject.construct_from({"data": arr}, None)
        assert list(sro) == expected

    def test_len(self, search_result_object):
        assert len(search_result_object) == 1

    def test_bool(self, search_result_object):
        assert search_result_object

        empty = stripe.SearchResultObject.construct_from(
            {"object": "list", "url": "/my/path", "data": []}, "mykey"
        )
        assert bool(empty) is False

    def test_next_search_result_page(self, request_mock):
        sro = stripe.SearchResultObject.construct_from(
            {
                "object": "list",
                "data": [{"id": 1}],
                "has_more": True,
                "next_page": "next_page_token",
                "url": "/things",
            },
            None,
        )

        request_mock.stub_request(
            "get",
            "/things",
            {
                "object": "list",
                "data": [{"id": 2}],
                "has_more": False,
                "url": "/things",
            },
        )

        next_sro = sro.next_search_result_page()

        request_mock.assert_requested(
            "get", "/things", {"page": "next_page_token"}, None
        )
        assert not next_sro.is_empty
        assert next_sro.data[0].id == 2

    def test_next_search_result_page_with_filters(self, request_mock):
        sro = stripe.SearchResultObject.construct_from(
            {
                "object": "list",
                "data": [{"id": 1}],
                "has_more": True,
                "next_page": "next_page_token",
                "url": "/things",
            },
            None,
        )
        sro._retrieve_params = {"expand": ["data.source"], "limit": 3}

        request_mock.stub_request(
            "get",
            "/things",
            {
                "object": "list",
                "data": [{"id": 2}],
                "has_more": False,
                "next_page": None,
                "url": "/things",
            },
        )

        next_sro = sro.next_search_result_page()
        assert next_sro._retrieve_params == {
            "expand": ["data.source"],
            "limit": 3,
            "page": "next_page_token",
        }

    def test_next_search_result_page_empty_search_result(self):
        sro = stripe.SearchResultObject.construct_from(
            {
                "object": "list",
                "data": [{"id": 1}],
                "has_more": False,
                "next_page": None,
                "url": "/things",
            },
            None,
        )

        next_sro = sro.next_search_result_page()
        assert next_sro == stripe.SearchResultObject.empty_search_result()

    def test_serialize_empty_search_result(self):
        empty = stripe.SearchResultObject.construct_from(
            {"object": "list", "data": []}, "mykey"
        )
        serialized = str(empty)
        deserialized = stripe.SearchResultObject.construct_from(
            json.loads(serialized), "mykey"
        )
        assert deserialized == empty

    def test_serialize_nested_empty_search_result(self):
        empty = stripe.SearchResultObject.construct_from(
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
    def pageable_model_response(ids, has_more, next_page_token):
        model = {
            "object": "search_result",
            "url": "/v1/pageablemodels",
            "data": [{"id": id, "object": "pageablemodel"} for id in ids],
            "has_more": has_more,
            "next_page": next_page_token,
        }

        return model

    def test_iter_one_page(self, request_mock):
        sro = stripe.SearchResultObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], False, None),
            "mykey",
        )

        request_mock.assert_no_request()

        seen = [item["id"] for item in sro.auto_paging_iter()]

        assert seen == ["pm_123", "pm_124"]

    def test_iter_two_pages(self, request_mock):
        sro = stripe.SearchResultObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], True, "token"),
            "mykey",
        )
        sro._retrieve_params = {"foo": "bar"}

        request_mock.stub_request(
            "get",
            "/v1/pageablemodels",
            self.pageable_model_response(["pm_125", "pm_126"], False, None),
        )

        seen = [item["id"] for item in sro.auto_paging_iter()]

        request_mock.assert_requested(
            "get",
            "/v1/pageablemodels",
            {"page": "token", "foo": "bar"},
            None,
        )

        assert seen == ["pm_123", "pm_124", "pm_125", "pm_126"]
