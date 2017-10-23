import stripe
from stripe.test.helper import (
    StripeResourceTest, DUMMY_PLAN
)


class PlanTest(StripeResourceTest):

    def test_create_plan(self):
        stripe.Plan.create(**DUMMY_PLAN)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/plans',
            DUMMY_PLAN,
            None
        )

    def test_delete_plan(self):
        p = stripe.Plan(id="pl_delete")
        p.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/plans/pl_delete',
            {},
            None
        )

    def test_update_plan(self):
        p = stripe.Plan(id="pl_update")
        p.name = "Plan Name"
        p.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/plans/pl_update',
            {
                'name': 'Plan Name',
            },
            None
        )
