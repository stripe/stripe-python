import stripe


TEST_RESOURCE_ID = "cs_123"


class TestSession(object):
    def test_is_creatable(self, http_client_mock):
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
        http_client_mock.assert_requested(
            "post",
            path="/v1/checkout/sessions",
            post_data="cancel_url=https://stripe.com/cancel&client_reference_id=1234&line_items[0][amount]=123&line_items[0][currency]=usd&line_items[0][description]=item+1&line_items[0][images][0]=https://stripe.com/img1&line_items[0][name]=name&line_items[0][quantity]=2&payment_intent_data[receipt_email]=test@stripe.com&payment_method_types[0]=card&success_url=https://stripe.com/success",
        )
        assert isinstance(resource, stripe.checkout.Session)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.checkout.Session.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/checkout/sessions/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.checkout.Session)


class TestSessionLineItems(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.checkout.Session.list_line_items(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get",
            path="/v1/checkout/sessions/%s/line_items" % TEST_RESOURCE_ID,
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.LineItem)
