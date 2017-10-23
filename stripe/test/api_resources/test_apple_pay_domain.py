import stripe
from stripe.test.helper import (
    StripeResourceTest, DUMMY_APPLE_PAY_DOMAIN
)


class ApplePayDomainTest(StripeResourceTest):

    def test_create_apple_pay_domain(self):
        stripe.ApplePayDomain.create(**DUMMY_APPLE_PAY_DOMAIN)
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/apple_pay/domains',
            DUMMY_APPLE_PAY_DOMAIN,
            None
        )

    def test_retrieve_apple_pay_domain(self):
        stripe.ApplePayDomain.retrieve("apwc_test")
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/apple_pay/domains/apwc_test',
            {},
            None
        )

    def test_list_apple_pay_domains(self):
        stripe.ApplePayDomain.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/apple_pay/domains',
            {},
        )

    def test_delete_apple_pay_domain(self):
        d = stripe.ApplePayDomain(id='apwc_delete')
        d.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/apple_pay/domains/apwc_delete',
            {},
            None
        )
