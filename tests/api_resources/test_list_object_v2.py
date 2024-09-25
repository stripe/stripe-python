from __future__ import absolute_import, division, print_function

import json

import pytest

import stripe
from stripe.v2._list_object import ListObject
from tests.http_client_mock import HTTPClientMock


class TestListObjectV2(object):
    @pytest.fixture
    def list_object(self):
        return ListObject.construct_from(
            {
                "data": ["a", "b", "c"],
                "next_page_url": None,
                "previous_page_url": None,
            },
            "mykey",
        )

    def test_iter(self):
        arr = ["a", "b", "c"]
        expected = stripe.util.convert_to_stripe_object(arr, api_mode="V2")
        lo = ListObject.construct_from({"data": arr}, None)
        assert list(lo) == expected

    @staticmethod
    def pageable_model_response(ids, next_page_url):
        return {
            "data": [{"id": id, "object": "pageablemodel"} for id in ids],
            "next_page_url": next_page_url,
        }

    def test_iter_one_page(self, http_client_mock):
        lo = ListObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], None), "mykey"
        )

        http_client_mock.assert_no_request()

        seen = [item["id"] for item in lo.auto_paging_iter()]

        assert seen == ["pm_123", "pm_124"]

    def test_iter_two_pages(self, http_client_mock):
        method = "get"
        path = "/v2/pageablemodels"

        lo = ListObject.construct_from(
            self.pageable_model_response(
                ["pm_123", "pm_124"], "/v2/pageablemodels?foo=bar&page=page_2"
            ),
            None,
        )

        http_client_mock.stub_request(
            method,
            path=path,
            query_string="foo=bar&page=page_3",
            rbody=json.dumps(
                self.pageable_model_response(["pm_127", "pm_128"], None)
            ),
        )

        http_client_mock.stub_request(
            method,
            path=path,
            query_string="foo=bar&page=page_2",
            rbody=json.dumps(
                self.pageable_model_response(
                    ["pm_125", "pm_126"],
                    "/v2/pageablemodels?foo=bar&page=page_3",
                )
            ),
        )

        seen = [item["id"] for item in lo.auto_paging_iter()]

        http_client_mock.assert_requested(
            method, path=path, query_string="foo=bar&page=page_2"
        )

        http_client_mock.assert_requested(
            method, path=path, query_string="foo=bar&page=page_3"
        )

        assert seen == [
            "pm_123",
            "pm_124",
            "pm_125",
            "pm_126",
            "pm_127",
            "pm_128",
        ]

    def test_iter_forwards_api_key(self, http_client_mock: HTTPClientMock):
        client = stripe.StripeClient(
            http_client=http_client_mock.get_mock_http_client(),
            api_key="sk_test_xyz",
        )

        method = "get"
        query_string_1 = "object_id=obj_123"
        query_string_2 = "object_id=obj_123&page=page_2"
        path = "/v2/core/events"

        http_client_mock.stub_request(
            method,
            path=path,
            query_string=query_string_1,
            rbody='{"data": [{"id": "x"}], "next_page_url": "/v2/core/events?object_id=obj_123&page=page_2"}',
            rcode=200,
            rheaders={},
        )

        http_client_mock.stub_request(
            method,
            path=path,
            query_string=query_string_2,
            rbody='{"data": [{"id": "y"}, {"id": "z"}], "next_page_url": null}',
            rcode=200,
            rheaders={},
        )

        lo = client.v2.core.events.list(
            params={"object_id": "obj_123"},
            options={"api_key": "sk_test_iter_forwards_options"},
        )

        seen = [item["id"] for item in lo.auto_paging_iter()]

        assert seen == ["x", "y", "z"]
        http_client_mock.assert_requested(
            method,
            path=path,
            query_string=query_string_1,
            api_key="sk_test_iter_forwards_options",
        )
        http_client_mock.assert_requested(
            method,
            path=path,
            query_string=query_string_2,
            api_key="sk_test_iter_forwards_options",
        )
