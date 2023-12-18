import stripe


TEST_RESOURCE_ID = "250FF"


class TestPlan(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Plan.list()
        http_client_mock.assert_requested("get", path="/v1/plans")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Plan)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Plan.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/plans/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Plan)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Plan.create(
            amount=100,
            currency="usd",
            id="plan_id",
            interval="month",
            nickname="plan_nickname",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/plans",
            post_data="amount=100&currency=usd&id=plan_id&interval=month&nickname=plan_nickname",
        )
        assert isinstance(resource, stripe.Plan)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Plan.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/plans/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Plan.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/plans/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Plan)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.Plan.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/plans/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, http_client_mock):
        resource = stripe.Plan.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/plans/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
