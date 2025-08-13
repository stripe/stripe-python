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

    def test_search(self, http_client_mock, search_result_object):
        http_client_mock.stub_request(
            "get",
            path="/my/path",
            query_string="myparam=you",
            rbody=json.dumps(
                {
                    "object": "search_result",
                    "data": [{"object": "charge", "foo": "bar"}],
                }
            ),
        )

        res = search_result_object.search(
            myparam="you", stripe_account="acct_123"
        )

        http_client_mock.assert_requested(
            "get",
            path="/my/path",
            query_string="myparam=you",
            stripe_account="acct_123",
        )
        assert isinstance(res, stripe.SearchResultObject)
        assert res.stripe_account == "acct_123"
        assert isinstance(res.data, list)
        assert isinstance(res.data[0], stripe.Charge)
        assert res.data[0].foo == "bar"

    @pytest.mark.anyio
    async def test_search_async(self, http_client_mock, search_result_object):
        http_client_mock.stub_request(
            "get",
            path="/my/path",
            query_string="myparam=you",
            rbody=json.dumps(
                {
                    "object": "search_result",
                    "data": [{"object": "charge", "foo": "bar"}],
                }
            ),
        )

        res = await search_result_object._search_async(
            myparam="you", stripe_account="acct_123"
        )

        http_client_mock.assert_requested(
            "get",
            path="/my/path",
            query_string="myparam=you",
            stripe_account="acct_123",
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
        sro = stripe.SearchResultObject._empty_search_result()
        assert sro.is_empty

    def test_iter(self):
        arr = [{"id": 1}, {"id": 2}, {"id": 3}]
        expected = stripe.util.convert_to_stripe_object(arr, api_mode="V1")
        sro = stripe.SearchResultObject.construct_from({"data": arr}, None)
        assert list(sro) == expected

    def test_len(self, search_result_object):
        assert len(search_result_object) == 1

    def test_bool(self, search_result_object):
        assert search_result_object

        empty = stripe.SearchResultObject.construct_from(
            {"object": "search_result", "url": "/my/path", "data": []}, "mykey"
        )
        assert bool(empty) is False

    def test_next_search_result_page(self, http_client_mock):
        sro = stripe.SearchResultObject.construct_from(
            {
                "object": "search_result",
                "data": [{"id": 1}],
                "has_more": True,
                "next_page": "next_page_token",
                "url": "/things",
            },
            None,
        )

        http_client_mock.stub_request(
            "get",
            path="/things",
            query_string="page=next_page_token",
            rbody=json.dumps(
                {
                    "object": "search_result",
                    "data": [{"id": 2}],
                    "has_more": False,
                    "url": "/things",
                }
            ),
        )

        next_sro = sro.next_search_result_page()

        http_client_mock.assert_requested(
            "get", path="/things", query_string="page=next_page_token"
        )
        assert not next_sro.is_empty
        assert next_sro.data[0].id == 2

    def test_next_search_result_page_with_filters(self, http_client_mock):
        sro = stripe.SearchResultObject.construct_from(
            {
                "object": "search_result",
                "data": [{"id": 1}],
                "has_more": True,
                "next_page": "next_page_token",
                "url": "/things",
            },
            None,
        )
        sro._retrieve_params = {"expand": ["data.source"], "limit": 3}

        http_client_mock.stub_request(
            "get",
            path="/things",
            query_string="expand[0]=data.source&limit=3&page=next_page_token",
            rbody=json.dumps(
                {
                    "object": "search_result",
                    "data": [{"id": 2}],
                    "has_more": False,
                    "next_page": None,
                    "url": "/things",
                }
            ),
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
                "object": "search_result",
                "data": [{"id": 1}],
                "has_more": False,
                "next_page": None,
                "url": "/things",
            },
            None,
        )

        next_sro = sro.next_search_result_page()
        assert next_sro == stripe.SearchResultObject._empty_search_result()

    def test_serialize_empty_search_result(self):
        empty = stripe.SearchResultObject.construct_from(
            {"object": "search_result", "data": []}, "mykey"
        )
        serialized = str(empty)
        deserialized = stripe.SearchResultObject.construct_from(
            json.loads(serialized), "mykey"
        )
        assert deserialized == empty

    def test_serialize_nested_empty_search_result(self):
        empty = stripe.SearchResultObject.construct_from(
            {"object": "search_result", "data": []}, "mykey"
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

    def test_iter_one_page(self, http_client_mock):
        sro = stripe.SearchResultObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], False, None),
            "mykey",
        )

        http_client_mock.assert_no_request()

        seen = [item["id"] for item in sro.auto_paging_iter()]

        assert seen == ["pm_123", "pm_124"]

    def test_iter_two_pages(self, http_client_mock):
        sro = stripe.SearchResultObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], True, "token"),
            "mykey",
        )
        sro._retrieve_params = {"foo": "bar"}

        http_client_mock.stub_request(
            "get",
            path="/v1/pageablemodels",
            query_string="page=token&foo=bar",
            rbody=json.dumps(
                self.pageable_model_response(["pm_125", "pm_126"], False, None)
            ),
        )

        seen = [item["id"] for item in sro.auto_paging_iter()]

        http_client_mock.assert_requested(
            "get",
            path="/v1/pageablemodels",
            query_string="page=token&foo=bar",
        )

        assert seen == ["pm_123", "pm_124", "pm_125", "pm_126"]


class TestAutoPagingAsync:
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

    @pytest.mark.anyio
    async def test_iter_one_page(self, http_client_mock):
        sro = stripe.SearchResultObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], False, None),
            "mykey",
        )

        http_client_mock.assert_no_request()

        seen = [item["id"] async for item in sro.auto_paging_iter()]

        assert seen == ["pm_123", "pm_124"]

    @pytest.mark.anyio
    async def test_iter_two_pages(self, http_client_mock):
        sro = stripe.SearchResultObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], True, "token"),
            "mykey",
        )
        sro._retrieve_params = {"foo": "bar"}

        http_client_mock.stub_request(
            "get",
            path="/v1/pageablemodels",
            query_string="page=token&foo=bar",
            rbody=json.dumps(
                self.pageable_model_response(["pm_125", "pm_126"], False, None)
            ),
        )

        seen = [item["id"] async for item in sro.auto_paging_iter()]

        http_client_mock.assert_requested(
            "get",
            path="/v1/pageablemodels",
            query_string="page=token&foo=bar",
        )

        assert seen == ["pm_123", "pm_124", "pm_125", "pm_126"]
