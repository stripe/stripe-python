import stripe


TEST_RESOURCE_ID = "prv_123"


class TestReview(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Review.list()
        http_client_mock.assert_requested("get", path="/v1/reviews")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Review)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Review.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/reviews/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Review)

    def test_can_approve(self, http_client_mock):
        resource = stripe.Review.retrieve(TEST_RESOURCE_ID)
        resource.approve()
        http_client_mock.assert_requested(
            "post", path="/v1/reviews/%s/approve" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Review)

    def test_can_approve_classmethod(self, http_client_mock):
        resource = stripe.Review.approve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/reviews/%s/approve" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Review)
