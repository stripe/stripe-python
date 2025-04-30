import json

import pytest

import stripe


class TestListObject(object):
    @pytest.fixture
    def list_object(self):
        return stripe.ListObject.construct_from(
            {"object": "list", "url": "/my/path", "data": ["foo"]}, "mykey"
        )

    def test_list(self, http_client_mock, list_object):
        http_client_mock.stub_request(
            "get",
            path="/my/path",
            query_string="myparam=you",
            rbody='{"object": "list", "data": [{"object": "charge", "foo": "bar"}]}',
        )

        res = list_object.list(myparam="you", stripe_account="acct_123")

        http_client_mock.assert_requested(
            "get",
            path="/my/path",
            query_string="myparam=you",
            stripe_account="acct_123",
        )
        assert isinstance(res, stripe.ListObject)
        assert res.stripe_account == "acct_123"
        assert isinstance(res.data, list)
        assert isinstance(res.data[0], stripe.Charge)
        assert res.data[0].foo == "bar"

    def test_create(self, http_client_mock, list_object):
        http_client_mock.stub_request(
            "post", path="/my/path", rbody='{"object": "charge", "foo": "bar"}'
        )

        res = list_object.create(myparam="eter", stripe_account="acct_123")

        http_client_mock.assert_requested(
            "post",
            path="/my/path",
            post_data="myparam=eter",
            stripe_account="acct_123",
        )
        assert isinstance(res, stripe.Charge)
        assert res.foo == "bar"
        assert res.stripe_account == "acct_123"

    def test_retrieve_maintains_list_properties(
        self, http_client_mock, list_object
    ):
        # Testing with real requests because our mock makes it impossible to
        # test otherwise
        charge = stripe.Charge.retrieve("ch_123", api_key="sk_test_custom")
        res = charge.refunds.retrieve("re_abc")
        http_client_mock.assert_requested(
            "get", path="/v1/charges/ch_123/refunds/re_abc"
        )
        assert res.api_key == "sk_test_custom"

    def test_retrieve(self, http_client_mock, list_object):
        http_client_mock.stub_request(
            "get",
            path="/my/path/myid",
            query_string="myparam=cow",
            rbody='{"object": "charge", "foo": "bar"}',
        )

        res = list_object.retrieve(
            "myid", myparam="cow", stripe_account="acct_123"
        )

        http_client_mock.assert_requested(
            "get",
            path="/my/path/myid",
            query_string="myparam=cow",
            stripe_account="acct_123",
        )
        assert isinstance(res, stripe.Charge)
        assert res.foo == "bar"
        assert res.stripe_account == "acct_123"

    def test_is_empty(self):
        lo = stripe.ListObject.construct_from({"data": []}, None)
        assert lo.is_empty is True

    def test_empty_list(self):
        lo = stripe.ListObject._empty_list()
        assert lo.is_empty

    def test_iter(self):
        arr = [{"id": 1}, {"id": 2}, {"id": 3}]
        expected = stripe.util.convert_to_stripe_object(arr, api_mode="V1")
        lo = stripe.ListObject.construct_from({"data": arr}, None)
        assert list(lo) == expected

    def test_iter_reversed(self):
        arr = [{"id": 1}, {"id": 2}, {"id": 3}]
        expected = stripe.util.convert_to_stripe_object(
            list(reversed(arr)), api_mode="V1"
        )
        lo = stripe.ListObject.construct_from({"data": arr}, None)
        assert list(reversed(lo)) == expected

    def test_len(self, list_object):
        assert len(list_object) == 1

    def test_bool(self, list_object):
        assert list_object

        empty = stripe.ListObject.construct_from(
            {"object": "list", "url": "/my/path", "data": []}, "mykey"
        )
        assert bool(empty) is False

    def test_next_page(self, http_client_mock):
        lo = stripe.ListObject.construct_from(
            {
                "object": "list",
                "data": [{"id": 1}],
                "has_more": True,
                "url": "/things",
            },
            None,
        )

        http_client_mock.stub_request(
            "get",
            path="/things",
            query_string="starting_after=1",
            rbody='{"object": "list", "data": [{"id": 2}], "has_more": false, "url": "/things"}',
        )

        next_lo = lo.next_page()
        assert not next_lo.is_empty
        assert next_lo.data[0].id == 2

    def test_next_page_with_filters(self, http_client_mock):
        lo = stripe.ListObject.construct_from(
            {
                "object": "list",
                "data": [{"id": 1}],
                "has_more": True,
                "url": "/things",
            },
            None,
        )
        lo._retrieve_params = {"expand": ["data.source"], "limit": 3}

        http_client_mock.stub_request(
            "get",
            path="/things",
            query_string="expand[0]=data.source&limit=3&starting_after=1",
            rbody='{"object": "list", "data": [{"id": 2}], "has_more": false, "url": "/things"}',
        )

        next_lo = lo.next_page()
        assert next_lo._retrieve_params == {
            "expand": ["data.source"],
            "limit": 3,
            "starting_after": 1,
        }

    def test_next_page_empty_list(self):
        lo = stripe.ListObject.construct_from(
            {
                "object": "list",
                "data": [{"id": 1}],
                "has_more": False,
                "url": "/things",
            },
            None,
        )

        next_lo = lo.next_page()
        assert next_lo == stripe.ListObject._empty_list()

    def test_prev_page(self, http_client_mock):
        lo = stripe.ListObject.construct_from(
            {
                "object": "list",
                "data": [{"id": 2}],
                "has_more": True,
                "url": "/things",
            },
            None,
        )

        http_client_mock.stub_request(
            "get",
            path="/things",
            query_string="ending_before=2",
            rbody='{"object": "list", "data": [{"id": 1}], "has_more": false, "url": "/things"}',
        )

        previous_lo = lo.previous_page()
        assert not previous_lo.is_empty
        assert previous_lo.data[0].id == 1

    def test_prev_page_with_filters(self, http_client_mock):
        lo = stripe.ListObject.construct_from(
            {
                "object": "list",
                "data": [{"id": 2}],
                "has_more": True,
                "url": "/things",
            },
            None,
        )
        lo._retrieve_params = {"expand": ["data.source"], "limit": 3}

        http_client_mock.stub_request(
            "get",
            path="/things",
            query_string="ending_before=2&expand[0]=data.source&limit=3",
            rbody='{"object": "list", "data": [{"id": 1}], "has_more": false, "url": "/things"}',
        )

        previous_lo = lo.previous_page()
        assert previous_lo._retrieve_params == {
            "expand": ["data.source"],
            "limit": 3,
            "ending_before": 2,
        }

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

    def test_iter_one_page(self, http_client_mock):
        lo = stripe.ListObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], False), "mykey"
        )

        http_client_mock.assert_no_request()

        seen = [item["id"] for item in lo.auto_paging_iter()]

        assert seen == ["pm_123", "pm_124"]

    def test_iter_two_pages(self, http_client_mock):
        lo = stripe.ListObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], True), "mykey"
        )
        lo._retrieve_params = {"foo": "bar"}

        http_client_mock.stub_request(
            "get",
            path="/v1/pageablemodels",
            query_string="starting_after=pm_124&foo=bar",
            rbody=json.dumps(
                self.pageable_model_response(["pm_125", "pm_126"], False)
            ),
        )

        seen = [item["id"] for item in lo.auto_paging_iter()]

        http_client_mock.assert_requested(
            "get",
            path="/v1/pageablemodels",
            query_string="starting_after=pm_124&foo=bar",
        )

        assert seen == ["pm_123", "pm_124", "pm_125", "pm_126"]

    def test_iter_reverse(self, http_client_mock):
        lo = stripe.ListObject.construct_from(
            self.pageable_model_response(["pm_125", "pm_126"], True), "mykey"
        )
        lo._retrieve_params = {"foo": "bar", "ending_before": "pm_127"}

        http_client_mock.stub_request(
            "get",
            path="/v1/pageablemodels",
            query_string="ending_before=pm_125&foo=bar",
            rbody=json.dumps(
                self.pageable_model_response(["pm_123", "pm_124"], False)
            ),
        )

        seen = [item["id"] for item in lo.auto_paging_iter()]

        http_client_mock.assert_requested(
            "get",
            path="/v1/pageablemodels",
            query_string="ending_before=pm_125&foo=bar",
        )

        assert seen == ["pm_126", "pm_125", "pm_124", "pm_123"]

    def test_class_method_two_pages(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path="/v1/charges",
            query_string="limit=25&foo=bar",
            rbody='{"object": "list", "data": [{"id": "ch_001"}], "url": "/v1/charges", "has_more": false}',
        )

        seen = [
            item["id"]
            for item in stripe.Charge.auto_paging_iter(limit=25, foo="bar")
        ]

        http_client_mock.assert_requested(
            "get", path="/v1/charges", query_string="limit=25&foo=bar"
        )
        assert seen == ["ch_001"]

    def test_iter_forwards_api_key_resource(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path="/v1/charges",
            rbody='{"object": "list", "data": [{"id": "ch_001"}], "url": "/v1/charges", "has_more": true}',
        )

        http_client_mock.stub_request(
            "get",
            path="/v1/charges",
            query_string="starting_after=ch_001",
            rbody='{"object": "list", "data": [{"id": "ch_002"}], "url": "/v1/charges", "has_more": false}',
        )

        lo = stripe.Charge.list(api_key="sk_test_iter_forwards_options")

        assert lo.api_key == "sk_test_iter_forwards_options"

        seen = [item["id"] for item in lo.auto_paging_iter()]

        http_client_mock.assert_requested(
            "get", path="/v1/charges", api_key="sk_test_iter_forwards_options"
        )

        http_client_mock.assert_requested(
            "get",
            path="/v1/charges",
            query_string="starting_after=ch_001",
            api_key="sk_test_iter_forwards_options",
        )
        assert seen == ["ch_001", "ch_002"]

    def test_iter_forwards_api_key_client(self, http_client_mock):
        client = stripe.StripeClient(
            http_client=http_client_mock.get_mock_http_client(),
            api_key="sk_test_xyz",
        )

        http_client_mock.stub_request(
            "get",
            path="/v1/charges",
            rbody='{"object": "list", "data": [{"id": "x"}], "url": "/v1/charges", "has_more": true}',
        )

        http_client_mock.stub_request(
            "get",
            path="/v1/charges",
            query_string="starting_after=x",
            rbody='{"object": "list", "data": [{"id": "y"}, {"id": "z"}], "url": "/v1/charges", "has_more": false}',
        )

        lo = client.charges.list(
            options={"api_key": "sk_test_iter_forwards_options"}
        )

        seen = [item["id"] for item in lo.auto_paging_iter()]

        assert seen == ["x", "y", "z"]
        http_client_mock.assert_requested(
            "get",
            path="/v1/charges",
            api_key="sk_test_iter_forwards_options",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/charges",
            query_string="starting_after=x",
            api_key="sk_test_iter_forwards_options",
        )

    def test_forwards_api_key_to_nested_resources(self, http_client_mock):
        http_client_mock.stub_request(
            "get",
            path="/v1/products",
            rbody='{"object": "list", "data": [{"id": "prod_001", "object": "product"}], "url": "/v1/products", "has_more": true}',
        )

        lo = stripe.Product.list(api_key="sk_test_iter_forwards_options")
        assert lo.api_key == "sk_test_iter_forwards_options"

        http_client_mock.assert_requested(
            "get", path="/v1/products", api_key="sk_test_iter_forwards_options"
        )

        http_client_mock.stub_request(
            "delete",
            path="/v1/products/prod_001",
        )

        lo.data[0].delete()

        http_client_mock.assert_requested(
            "delete",
            path="/v1/products/prod_001",
            api_key="sk_test_iter_forwards_options",
        )
        assert lo.data[0].api_key == "sk_test_iter_forwards_options"

    # TODO(xavdid): re-add test with a new endpoint
    # def test_iter_with_params(self, http_client_mock: HTTPClientMock):
    #     http_client_mock.stub_request(
    #         "get",
    #         path="/v1/invoices/upcoming/lines",
    #         query_string="customer=cus_123&expand[0]=data.price&limit=1",
    #         rbody=json.dumps(
    #             {
    #                 "object": "list",
    #                 "data": [
    #                     {
    #                         "id": "prod_001",
    #                         "object": "product",
    #                         "price": {"object": "price", "id": "price_123"},
    #                     }
    #                 ],
    #                 "url": "/v1/invoices/upcoming/lines?customer=cus_123&expand%5B%5D=data.price",
    #                 "has_more": True,
    #             }
    #         ),
    #     )
    #     # second page
    #     http_client_mock.stub_request(
    #         "get",
    #         path="/v1/invoices/upcoming/lines",
    #         query_string="customer=cus_123&expand[0]=data.price&limit=1&starting_after=prod_001",
    #         rbody=json.dumps(
    #             {
    #                 "object": "list",
    #                 "data": [
    #                     {
    #                         "id": "prod_002",
    #                         "object": "product",
    #                         "price": {"object": "price", "id": "price_123"},
    #                     }
    #                 ],
    #                 "url": "/v1/invoices/upcoming/lines?customer=cus_123&expand%5B%5D=data.price",
    #                 "has_more": False,
    #             }
    #         ),
    #     )

    #     lo = stripe.Invoice.upcoming_lines(
    #         api_key="sk_test_invoice_lines",
    #         customer="cus_123",
    #         expand=["data.price"],
    #         limit=1,
    #     )

    #     seen = [item["id"] for item in lo.auto_paging_iter()]

    #     assert seen == ["prod_001", "prod_002"]


class TestAutoPagingAsync:
    @staticmethod
    def pageable_model_response(ids, has_more):
        return {
            "object": "list",
            "url": "/v1/pageablemodels",
            "data": [{"id": id, "object": "pageablemodel"} for id in ids],
            "has_more": has_more,
        }

    @pytest.mark.anyio
    async def test_iter_one_page(self, http_client_mock):
        lo = stripe.ListObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], False), "mykey"
        )

        http_client_mock.assert_no_request()

        seen = [item["id"] async for item in lo.auto_paging_iter()]

        assert seen == ["pm_123", "pm_124"]

    @pytest.mark.anyio
    async def test_iter_two_pages(self, http_client_mock):
        lo = stripe.ListObject.construct_from(
            self.pageable_model_response(["pm_123", "pm_124"], True), "mykey"
        )
        lo._retrieve_params = {"foo": "bar"}

        http_client_mock.stub_request(
            "get",
            path="/v1/pageablemodels",
            query_string="starting_after=pm_124&foo=bar",
            rbody=json.dumps(
                self.pageable_model_response(["pm_125", "pm_126"], False)
            ),
        )

        seen = [item["id"] async for item in lo.auto_paging_iter()]

        http_client_mock.assert_requested(
            "get",
            path="/v1/pageablemodels",
            query_string="starting_after=pm_124&foo=bar",
        )

        assert seen == ["pm_123", "pm_124", "pm_125", "pm_126"]

    @pytest.mark.anyio
    async def test_iter_reverse(self, http_client_mock):
        lo = stripe.ListObject.construct_from(
            self.pageable_model_response(["pm_125", "pm_126"], True), "mykey"
        )
        lo._retrieve_params = {"foo": "bar", "ending_before": "pm_127"}

        http_client_mock.stub_request(
            "get",
            path="/v1/pageablemodels",
            query_string="ending_before=pm_125&foo=bar",
            rbody=json.dumps(
                self.pageable_model_response(["pm_123", "pm_124"], False)
            ),
        )

        seen = [item["id"] async for item in lo.auto_paging_iter()]

        http_client_mock.assert_requested(
            "get",
            path="/v1/pageablemodels",
            query_string="ending_before=pm_125&foo=bar",
        )

        assert seen == ["pm_126", "pm_125", "pm_124", "pm_123"]
