import stripe


TEST_RESOURCE_ID = "promo_123"


class TestPromotionCode(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.PromotionCode.list()
        http_client_mock.assert_requested("get", path="/v1/promotion_codes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.PromotionCode)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.PromotionCode.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/promotion_codes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.PromotionCode)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.PromotionCode.create(coupon="co_123", code="MYCODE")
        http_client_mock.assert_requested(
            "post",
            path="/v1/promotion_codes",
            post_data="code=MYCODE&coupon=co_123",
        )
        assert isinstance(resource, stripe.PromotionCode)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.PromotionCode.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/promotion_codes/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.PromotionCode.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/promotion_codes/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.PromotionCode)
