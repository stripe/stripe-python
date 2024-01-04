import stripe


TEST_RESOURCE_ID = "250FF"


class TestCoupon(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Coupon.list()
        http_client_mock.assert_requested("get", path="/v1/coupons")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Coupon)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Coupon.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/coupons/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Coupon)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Coupon.create(
            percent_off=25,
            duration="repeating",
            duration_in_months=3,
            id="250FF",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/coupons",
            post_data="duration=repeating&duration_in_months=3&id=250FF&percent_off=25",
        )
        assert isinstance(resource, stripe.Coupon)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Coupon.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/coupons/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Coupon.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post", path="/v1/coupons/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Coupon)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.Coupon.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/coupons/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, http_client_mock):
        resource = stripe.Coupon.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/coupons/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
