from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = "cs_123"


class TestSession(object):
    def test_is_creatable(self, request_mock):
        resource = stripe.checkout.Session.create(
            cancel_url="https://stripe.com/cancel",
            client_reference_id="1234",
            line_items=[
                {
                    "amount": 123,
                    "currency": "usd",
                    "description": "item 1",
                    "images": ["https://stripe.com/img1"],
                    "name": "name",
                    "quantity": 2,
                }
            ],
            payment_intent_data={"receipt_email": "test@stripe.com"},
            payment_method_types=["card"],
            success_url="https://stripe.com/success",
        )
        request_mock.assert_requested("post", "/v1/checkout/sessions")
        assert isinstance(resource, stripe.checkout.Session)

    def test_is_retrievable(self, request_mock):
        resource = stripe.checkout.Session.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/checkout/sessions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.checkout.Session)


class TestSessionLineItems(object):
    def test_is_listable(self, request_mock):
        resources = stripe.checkout.Session.list_line_items(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/checkout/sessions/%s/line_items" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.LineItem)
