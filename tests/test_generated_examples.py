# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function
import stripe

from tests.http_client_mock import HTTPClientMock


class TestGeneratedExamples(object):
    def test_account_links_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.AccountLink.create(
            account="acct_xxxxxxxxxxxxx",
            refresh_url="https://example.com/reauth",
            return_url="https://example.com/return",
            type="account_onboarding",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/account_links",
            query_string="",
            post_data="account=acct_xxxxxxxxxxxxx&refresh_url=https%3A%2F%2Fexample.com%2Freauth&return_url=https%3A%2F%2Fexample.com%2Freturn&type=account_onboarding",
        )

    def test_accounts_capabilities_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.list_capabilities("acct_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/capabilities",
            query_string="",
        )

    def test_accounts_capabilities_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.retrieve_capability(
            "acct_xxxxxxxxxxxxx",
            "card_payments",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/capabilities/card_payments",
            query_string="",
        )

    def test_accounts_capabilities_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.modify_capability(
            "acct_xxxxxxxxxxxxx",
            "card_payments",
            requested=True,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/capabilities/card_payments",
            query_string="",
            post_data="requested=True",
        )

    def test_accounts_delete(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Account.delete("acct_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/accounts/acct_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_accounts_external_accounts_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.delete_external_account(
            "acct_xxxxxxxxxxxxx",
            "ba_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "delete",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts/ba_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_accounts_external_accounts_delete_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.delete_external_account(
            "acct_xxxxxxxxxxxxx",
            "card_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "delete",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts/card_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_accounts_external_accounts_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.list_external_accounts(
            "acct_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts",
            query_string="limit=3",
        )

    def test_accounts_external_accounts_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.list_external_accounts(
            "acct_xxxxxxxxxxxxx",
            object="bank_account",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts",
            query_string="object=bank_account&limit=3",
        )

    def test_accounts_external_accounts_get_3(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.list_external_accounts(
            "acct_xxxxxxxxxxxxx",
            object="card",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts",
            query_string="object=card&limit=3",
        )

    def test_accounts_external_accounts_get_4(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.retrieve_external_account(
            "acct_xxxxxxxxxxxxx",
            "ba_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts/ba_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_accounts_external_accounts_get_5(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.retrieve_external_account(
            "acct_xxxxxxxxxxxxx",
            "card_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts/card_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_accounts_external_accounts_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.create_external_account(
            "acct_xxxxxxxxxxxxx",
            external_account="btok_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts",
            query_string="",
            post_data="external_account=btok_xxxxxxxxxxxxx",
        )

    def test_accounts_external_accounts_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.create_external_account(
            "acct_xxxxxxxxxxxxx",
            external_account="tok_xxxx_debit",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts",
            query_string="",
            post_data="external_account=tok_xxxx_debit",
        )

    def test_accounts_external_accounts_post_3(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.modify_external_account(
            "acct_xxxxxxxxxxxxx",
            "ba_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts/ba_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_accounts_external_accounts_post_4(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.modify_external_account(
            "acct_xxxxxxxxxxxxx",
            "card_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/external_accounts/card_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_accounts_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Account.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/accounts",
            query_string="limit=3",
        )

    def test_accounts_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Account.retrieve("acct_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/accounts/acct_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_accounts_login_links_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.create_login_link("acct_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/login_links",
            query_string="",
        )

    def test_accounts_persons_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.delete_person(
            "acct_xxxxxxxxxxxxx",
            "person_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "delete",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/persons/person_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_accounts_persons_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.list_persons(
            "acct_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/persons",
            query_string="limit=3",
        )

    def test_accounts_persons_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.retrieve_person(
            "acct_xxxxxxxxxxxxx",
            "person_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/persons/person_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_accounts_persons_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.create_person(
            "acct_xxxxxxxxxxxxx",
            first_name="Jane",
            last_name="Diaz",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/persons",
            query_string="",
            post_data="first_name=Jane&last_name=Diaz",
        )

    def test_accounts_persons_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.modify_person(
            "acct_xxxxxxxxxxxxx",
            "person_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/persons/person_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_accounts_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Account.create(
            type="custom",
            country="US",
            email="jenny.rosen@example.com",
            capabilities={
                "card_payments": {"requested": True},
                "transfers": {"requested": True},
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts",
            query_string="",
            post_data="type=custom&country=US&email=jenny.rosen%40example.com&capabilities[card_payments][requested]=True&capabilities[transfers][requested]=True",
        )

    def test_accounts_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Account.modify(
            "acct_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/acct_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_accounts_reject_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Account.reject(
            "acct_xxxxxxxxxxxxx",
            reason="fraud",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/acct_xxxxxxxxxxxxx/reject",
            query_string="",
            post_data="reason=fraud",
        )

    def test_application_fees_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.ApplicationFee.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/application_fees",
            query_string="limit=3",
        )

    def test_application_fees_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.ApplicationFee.retrieve("fee_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/application_fees/fee_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_application_fees_refunds_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.ApplicationFee.list_refunds(
            "fee_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/application_fees/fee_xxxxxxxxxxxxx/refunds",
            query_string="limit=3",
        )

    def test_application_fees_refunds_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.ApplicationFee.retrieve_refund(
            "fee_xxxxxxxxxxxxx",
            "fr_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/application_fees/fee_xxxxxxxxxxxxx/refunds/fr_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_application_fees_refunds_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.ApplicationFee.create_refund("fee_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/application_fees/fee_xxxxxxxxxxxxx/refunds",
            query_string="",
        )

    def test_application_fees_refunds_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.ApplicationFee.modify_refund(
            "fee_xxxxxxxxxxxxx",
            "fr_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/application_fees/fee_xxxxxxxxxxxxx/refunds/fr_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_apps_secrets_delete_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.apps.Secret.delete_where(
            name="my-api-key",
            scope={"type": "account"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/apps/secrets/delete",
            query_string="",
            post_data="name=my-api-key&scope[type]=account",
        )

    def test_apps_secrets_find_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.apps.Secret.find(
            name="sec_123",
            scope={"type": "account"},
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/apps/secrets/find",
            query_string="name=sec_123&scope[type]=account",
        )

    def test_apps_secrets_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.apps.Secret.list(
            scope={"type": "account"},
            limit=2,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/apps/secrets",
            query_string="scope[type]=account&limit=2",
        )

    def test_apps_secrets_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.apps.Secret.list(
            scope={"type": "account"},
            limit=2,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/apps/secrets",
            query_string="scope[type]=account&limit=2",
        )

    def test_apps_secrets_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.apps.Secret.create(
            name="sec_123",
            payload="very secret string",
            scope={"type": "account"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/apps/secrets",
            query_string="",
            post_data="name=sec_123&payload=very%20secret%20string&scope[type]=account",
        )

    def test_apps_secrets_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.apps.Secret.create(
            name="my-api-key",
            payload="secret_key_xxxxxx",
            scope={"type": "account"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/apps/secrets",
            query_string="",
            post_data="name=my-api-key&payload=secret_key_xxxxxx&scope[type]=account",
        )

    def test_balance_transactions_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.BalanceTransaction.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/balance_transactions",
            query_string="limit=3",
        )

    def test_balance_transactions_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.BalanceTransaction.retrieve("txn_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/balance_transactions/txn_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_billing_portal_configurations_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.billing_portal.Configuration.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/billing_portal/configurations",
            query_string="limit=3",
        )

    def test_billing_portal_configurations_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.billing_portal.Configuration.retrieve("bpc_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/billing_portal/configurations/bpc_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_billing_portal_configurations_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.billing_portal.Configuration.create(
            features={
                "customer_update": {
                    "allowed_updates": ["email", "tax_id"],
                    "enabled": True,
                },
                "invoice_history": {"enabled": True},
            },
            business_profile={
                "privacy_policy_url": "https://example.com/privacy",
                "terms_of_service_url": "https://example.com/terms",
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/billing_portal/configurations",
            query_string="",
            post_data="features[customer_update][allowed_updates][0]=email&features[customer_update][allowed_updates][1]=tax_id&features[customer_update][enabled]=True&features[invoice_history][enabled]=True&business_profile[privacy_policy_url]=https%3A%2F%2Fexample.com%2Fprivacy&business_profile[terms_of_service_url]=https%3A%2F%2Fexample.com%2Fterms",
        )

    def test_billing_portal_configurations_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.billing_portal.Configuration.modify(
            "bpc_xxxxxxxxxxxxx",
            business_profile={
                "privacy_policy_url": "https://example.com/privacy",
                "terms_of_service_url": "https://example.com/terms",
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/billing_portal/configurations/bpc_xxxxxxxxxxxxx",
            query_string="",
            post_data="business_profile[privacy_policy_url]=https%3A%2F%2Fexample.com%2Fprivacy&business_profile[terms_of_service_url]=https%3A%2F%2Fexample.com%2Fterms",
        )

    def test_billing_portal_sessions_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.billing_portal.Session.create(
            customer="cus_xxxxxxxxxxxxx",
            return_url="https://example.com/account",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/billing_portal/sessions",
            query_string="",
            post_data="customer=cus_xxxxxxxxxxxxx&return_url=https%3A%2F%2Fexample.com%2Faccount",
        )

    def test_charges_capture_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Charge.capture("ch_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/charges/ch_xxxxxxxxxxxxx/capture",
            query_string="",
        )

    def test_charges_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Charge.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/charges",
            query_string="limit=3",
        )

    def test_charges_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Charge.retrieve("ch_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/charges/ch_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_charges_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Charge.create(
            amount=2000,
            currency="usd",
            source="tok_xxxx",
            description="My First Test Charge (created for API docs at https://www.stripe.com/docs/api)",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/charges",
            query_string="",
            post_data="amount=2000&currency=usd&source=tok_xxxx&description=My%20First%20Test%20Charge%20%28created%20for%20API%20docs%20at%20https%3A%2F%2Fwww.stripe.com%2Fdocs%2Fapi%29",
        )

    def test_charges_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Charge.modify(
            "ch_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/charges/ch_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_charges_search_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Charge.search(
            query="amount>999 AND metadata['order_id']:'6735'"
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/charges/search",
            query_string="query=amount%3E999%20AND%20metadata%5B%27order_id%27%5D%3A%276735%27",
        )

    def test_checkout_sessions_expire_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.checkout.Session.expire("sess_xyz")
        http_client_mock.assert_requested(
            "post",
            path="/v1/checkout/sessions/sess_xyz/expire",
            query_string="",
        )

    def test_checkout_sessions_expire_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.checkout.Session.expire("cs_test_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/checkout/sessions/cs_test_xxxxxxxxxxxxx/expire",
            query_string="",
        )

    def test_checkout_sessions_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.checkout.Session.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/checkout/sessions",
            query_string="limit=3",
        )

    def test_checkout_sessions_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.checkout.Session.retrieve("cs_test_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/checkout/sessions/cs_test_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_checkout_sessions_line_items_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.checkout.Session.list_line_items("sess_xyz")
        http_client_mock.assert_requested(
            "get",
            path="/v1/checkout/sessions/sess_xyz/line_items",
            query_string="",
        )

    def test_checkout_sessions_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.checkout.Session.create(
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
            mode="payment",
            shipping_options=[
                {"shipping_rate": "shr_standard"},
                {
                    "shipping_rate_data": {
                        "display_name": "Standard",
                        "delivery_estimate": {
                            "minimum": {"unit": "day", "value": 5},
                            "maximum": {"unit": "day", "value": 7},
                        },
                    },
                },
            ],
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/checkout/sessions",
            query_string="",
            post_data="success_url=https%3A%2F%2Fexample.com%2Fsuccess&cancel_url=https%3A%2F%2Fexample.com%2Fcancel&mode=payment&shipping_options[0][shipping_rate]=shr_standard&shipping_options[1][shipping_rate_data][display_name]=Standard&shipping_options[1][shipping_rate_data][delivery_estimate][minimum][unit]=day&shipping_options[1][shipping_rate_data][delivery_estimate][minimum][value]=5&shipping_options[1][shipping_rate_data][delivery_estimate][maximum][unit]=day&shipping_options[1][shipping_rate_data][delivery_estimate][maximum][value]=7",
        )

    def test_checkout_sessions_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.checkout.Session.create(
            success_url="https://example.com/success",
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 2}],
            mode="payment",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/checkout/sessions",
            query_string="",
            post_data="success_url=https%3A%2F%2Fexample.com%2Fsuccess&line_items[0][price]=price_xxxxxxxxxxxxx&line_items[0][quantity]=2&mode=payment",
        )

    def test_country_specs_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.CountrySpec.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/country_specs",
            query_string="limit=3",
        )

    def test_country_specs_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.CountrySpec.retrieve("US")
        http_client_mock.assert_requested(
            "get",
            path="/v1/country_specs/US",
            query_string="",
        )

    def test_coupons_delete(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Coupon.delete("Z4OV52SU")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/coupons/Z4OV52SU",
            query_string="",
        )

    def test_coupons_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Coupon.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/coupons",
            query_string="limit=3",
        )

    def test_coupons_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Coupon.retrieve("Z4OV52SU")
        http_client_mock.assert_requested(
            "get",
            path="/v1/coupons/Z4OV52SU",
            query_string="",
        )

    def test_coupons_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Coupon.create(
            percent_off=25.5,
            duration="repeating",
            duration_in_months=3,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/coupons",
            query_string="",
            post_data="percent_off=25.5&duration=repeating&duration_in_months=3",
        )

    def test_coupons_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Coupon.modify(
            "Z4OV52SU",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/coupons/Z4OV52SU",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_credit_notes_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.CreditNote.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/credit_notes",
            query_string="limit=3",
        )

    def test_credit_notes_lines_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.CreditNote.list_lines(
            "cn_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/credit_notes/cn_xxxxxxxxxxxxx/lines",
            query_string="limit=3",
        )

    def test_credit_notes_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.CreditNote.create(
            invoice="in_xxxxxxxxxxxxx",
            lines=[
                {
                    "type": "invoice_line_item",
                    "invoice_line_item": "il_xxxxxxxxxxxxx",
                    "quantity": 1,
                },
            ],
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/credit_notes",
            query_string="",
            post_data="invoice=in_xxxxxxxxxxxxx&lines[0][type]=invoice_line_item&lines[0][invoice_line_item]=il_xxxxxxxxxxxxx&lines[0][quantity]=1",
        )

    def test_credit_notes_preview_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.CreditNote.preview(
            invoice="in_xxxxxxxxxxxxx",
            lines=[
                {
                    "type": "invoice_line_item",
                    "invoice_line_item": "il_xxxxxxxxxxxxx",
                    "quantity": 1,
                },
            ],
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/credit_notes/preview",
            query_string="invoice=in_xxxxxxxxxxxxx&lines[0][type]=invoice_line_item&lines[0][invoice_line_item]=il_xxxxxxxxxxxxx&lines[0][quantity]=1",
        )

    def test_credit_notes_preview_lines_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.CreditNote.preview_lines(
            limit=3,
            invoice="in_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/credit_notes/preview/lines",
            query_string="limit=3&invoice=in_xxxxxxxxxxxxx",
        )

    def test_credit_notes_void_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.CreditNote.void_credit_note("cn_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/credit_notes/cn_xxxxxxxxxxxxx/void",
            query_string="",
        )

    def test_customers_balance_transactions_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.list_balance_transactions(
            "cus_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx/balance_transactions",
            query_string="limit=3",
        )

    def test_customers_balance_transactions_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.retrieve_balance_transaction(
            "cus_xxxxxxxxxxxxx",
            "cbtxn_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx/balance_transactions/cbtxn_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_customers_balance_transactions_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.create_balance_transaction(
            "cus_xxxxxxxxxxxxx",
            amount=-500,
            currency="usd",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/cus_xxxxxxxxxxxxx/balance_transactions",
            query_string="",
            post_data="amount=-500&currency=usd",
        )

    def test_customers_balance_transactions_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.modify_balance_transaction(
            "cus_xxxxxxxxxxxxx",
            "cbtxn_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/cus_xxxxxxxxxxxxx/balance_transactions/cbtxn_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_customers_cash_balance_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.retrieve_cash_balance("cus_123")
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_123/cash_balance",
            query_string="",
        )

    def test_customers_cash_balance_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.modify_cash_balance(
            "cus_123",
            settings={"reconciliation_mode": "manual"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/cus_123/cash_balance",
            query_string="",
            post_data="settings[reconciliation_mode]=manual",
        )

    def test_customers_delete(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Customer.delete("cus_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_customers_funding_instructions_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.create_funding_instructions(
            "cus_123",
            bank_transfer={
                "requested_address_types": ["zengin"],
                "type": "jp_bank_transfer",
            },
            currency="usd",
            funding_type="bank_transfer",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/cus_123/funding_instructions",
            query_string="",
            post_data="bank_transfer[requested_address_types][0]=zengin&bank_transfer[type]=jp_bank_transfer&currency=usd&funding_type=bank_transfer",
        )

    def test_customers_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Customer.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers",
            query_string="limit=3",
        )

    def test_customers_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Customer.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers",
            query_string="limit=3",
        )

    def test_customers_get_3(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Customer.retrieve("cus_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_customers_payment_methods_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.list_payment_methods(
            "cus_xyz",
            type="card",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xyz/payment_methods",
            query_string="type=card",
        )

    def test_customers_payment_methods_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.list_payment_methods(
            "cus_xxxxxxxxxxxxx",
            type="card",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx/payment_methods",
            query_string="type=card",
        )

    def test_customers_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Customer.create(
            description="My First Test Customer (created for API docs at https://www.stripe.com/docs/api)",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers",
            query_string="",
            post_data="description=My%20First%20Test%20Customer%20%28created%20for%20API%20docs%20at%20https%3A%2F%2Fwww.stripe.com%2Fdocs%2Fapi%29",
        )

    def test_customers_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Customer.modify(
            "cus_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/cus_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_customers_search_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.search(
            query="name:'fakename' AND metadata['foo']:'bar'",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/search",
            query_string="query=name%3A%27fakename%27%20AND%20metadata%5B%27foo%27%5D%3A%27bar%27",
        )

    def test_customers_search_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.search(
            query="name:'fakename' AND metadata['foo']:'bar'",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/search",
            query_string="query=name%3A%27fakename%27%20AND%20metadata%5B%27foo%27%5D%3A%27bar%27",
        )

    def test_customers_sources_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.delete_source(
            "cus_xxxxxxxxxxxxx",
            "ba_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "delete",
            path="/v1/customers/cus_xxxxxxxxxxxxx/sources/ba_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_customers_sources_delete_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.delete_source(
            "cus_xxxxxxxxxxxxx",
            "card_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "delete",
            path="/v1/customers/cus_xxxxxxxxxxxxx/sources/card_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_customers_sources_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.list_sources(
            "cus_xxxxxxxxxxxxx",
            object="bank_account",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx/sources",
            query_string="object=bank_account&limit=3",
        )

    def test_customers_sources_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.list_sources(
            "cus_xxxxxxxxxxxxx",
            object="card",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx/sources",
            query_string="object=card&limit=3",
        )

    def test_customers_sources_get_3(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.retrieve_source(
            "cus_xxxxxxxxxxxxx",
            "ba_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx/sources/ba_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_customers_sources_get_4(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.retrieve_source(
            "cus_xxxxxxxxxxxxx",
            "card_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx/sources/card_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_customers_sources_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.modify_source(
            "cus_123",
            "card_123",
            account_holder_name="Kamil",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/cus_123/sources/card_123",
            query_string="",
            post_data="account_holder_name=Kamil",
        )

    def test_customers_sources_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.create_source(
            "cus_xxxxxxxxxxxxx",
            source="btok_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/cus_xxxxxxxxxxxxx/sources",
            query_string="",
            post_data="source=btok_xxxxxxxxxxxxx",
        )

    def test_customers_sources_post_3(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.create_source(
            "cus_xxxxxxxxxxxxx",
            source="tok_xxxx",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/cus_xxxxxxxxxxxxx/sources",
            query_string="",
            post_data="source=tok_xxxx",
        )

    def test_customers_sources_post_4(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.modify_source(
            "cus_xxxxxxxxxxxxx",
            "ba_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/cus_xxxxxxxxxxxxx/sources/ba_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_customers_sources_post_5(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.modify_source(
            "cus_xxxxxxxxxxxxx",
            "card_xxxxxxxxxxxxx",
            name="Jenny Rosen",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/cus_xxxxxxxxxxxxx/sources/card_xxxxxxxxxxxxx",
            query_string="",
            post_data="name=Jenny%20Rosen",
        )

    def test_customers_tax_ids_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.delete_tax_id(
            "cus_xxxxxxxxxxxxx",
            "txi_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "delete",
            path="/v1/customers/cus_xxxxxxxxxxxxx/tax_ids/txi_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_customers_tax_ids_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.list_tax_ids(
            "cus_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx/tax_ids",
            query_string="limit=3",
        )

    def test_customers_tax_ids_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.retrieve_tax_id(
            "cus_xxxxxxxxxxxxx",
            "txi_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/customers/cus_xxxxxxxxxxxxx/tax_ids/txi_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_customers_tax_ids_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.create_tax_id(
            "cus_xxxxxxxxxxxxx",
            type="eu_vat",
            value="DE123456789",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/customers/cus_xxxxxxxxxxxxx/tax_ids",
            query_string="",
            post_data="type=eu_vat&value=DE123456789",
        )

    def test_disputes_close_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Dispute.close("dp_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/disputes/dp_xxxxxxxxxxxxx/close",
            query_string="",
        )

    def test_disputes_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Dispute.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/disputes",
            query_string="limit=3",
        )

    def test_disputes_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Dispute.retrieve("dp_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/disputes/dp_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_disputes_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Dispute.modify(
            "dp_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/disputes/dp_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_events_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Event.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/events",
            query_string="limit=3",
        )

    def test_events_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Event.retrieve("evt_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/events/evt_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_file_links_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.FileLink.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/file_links",
            query_string="limit=3",
        )

    def test_file_links_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.FileLink.retrieve("link_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/file_links/link_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_file_links_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.FileLink.create(file="file_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/file_links",
            query_string="",
            post_data="file=file_xxxxxxxxxxxxx",
        )

    def test_file_links_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.FileLink.modify(
            "link_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/file_links/link_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_files_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.File.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/files",
            query_string="limit=3",
        )

    def test_files_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.File.retrieve("file_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/files/file_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_financial_connections_accounts_disconnect_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Account.disconnect("fca_xyz")
        http_client_mock.assert_requested(
            "post",
            path="/v1/financial_connections/accounts/fca_xyz/disconnect",
            query_string="",
        )

    def test_financial_connections_accounts_disconnect_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Account.disconnect("fca_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/financial_connections/accounts/fca_xxxxxxxxxxxxx/disconnect",
            query_string="",
        )

    def test_financial_connections_accounts_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Account.list()
        http_client_mock.assert_requested(
            "get",
            path="/v1/financial_connections/accounts",
            query_string="",
        )

    def test_financial_connections_accounts_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Account.retrieve("fca_xyz")
        http_client_mock.assert_requested(
            "get",
            path="/v1/financial_connections/accounts/fca_xyz",
            query_string="",
        )

    def test_financial_connections_accounts_get_3(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Account.list(
            account_holder={"customer": "cus_xxxxxxxxxxxxx"},
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/financial_connections/accounts",
            query_string="account_holder[customer]=cus_xxxxxxxxxxxxx",
        )

    def test_financial_connections_accounts_get_4(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Account.retrieve("fca_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/financial_connections/accounts/fca_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_financial_connections_accounts_owners_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Account.list_owners(
            "fca_xyz",
            ownership="fcaowns_xyz",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/financial_connections/accounts/fca_xyz/owners",
            query_string="ownership=fcaowns_xyz",
        )

    def test_financial_connections_accounts_owners_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Account.list_owners(
            "fca_xxxxxxxxxxxxx",
            limit=3,
            ownership="fcaowns_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/financial_connections/accounts/fca_xxxxxxxxxxxxx/owners",
            query_string="limit=3&ownership=fcaowns_xxxxxxxxxxxxx",
        )

    def test_financial_connections_accounts_refresh_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Account.refresh_account(
            "fca_xyz",
            features=["balance"],
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/financial_connections/accounts/fca_xyz/refresh",
            query_string="",
            post_data="features[0]=balance",
        )

    def test_financial_connections_accounts_subscribe_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Account.subscribe(
            "fa_123",
            features=["transactions"],
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/financial_connections/accounts/fa_123/subscribe",
            query_string="",
            post_data="features[0]=transactions",
        )

    def test_financial_connections_accounts_unsubscribe_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Account.unsubscribe(
            "fa_123",
            features=["transactions"],
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/financial_connections/accounts/fa_123/unsubscribe",
            query_string="",
            post_data="features[0]=transactions",
        )

    def test_financial_connections_sessions_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Session.retrieve("fcsess_xyz")
        http_client_mock.assert_requested(
            "get",
            path="/v1/financial_connections/sessions/fcsess_xyz",
            query_string="",
        )

    def test_financial_connections_sessions_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Session.retrieve("fcsess_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/financial_connections/sessions/fcsess_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_financial_connections_sessions_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Session.create(
            account_holder={"type": "customer", "customer": "cus_123"},
            permissions=["balances"],
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/financial_connections/sessions",
            query_string="",
            post_data="account_holder[type]=customer&account_holder[customer]=cus_123&permissions[0]=balances",
        )

    def test_financial_connections_sessions_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Session.create(
            account_holder={
                "type": "customer",
                "customer": "cus_xxxxxxxxxxxxx",
            },
            permissions=["payment_method", "balances"],
            filters={"countries": ["US"]},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/financial_connections/sessions",
            query_string="",
            post_data="account_holder[type]=customer&account_holder[customer]=cus_xxxxxxxxxxxxx&permissions[0]=payment_method&permissions[1]=balances&filters[countries][0]=US",
        )

    def test_financial_connections_transactions_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Transaction.retrieve("tr_123")
        http_client_mock.assert_requested(
            "get",
            path="/v1/financial_connections/transactions/tr_123",
            query_string="",
        )

    def test_financial_connections_transactions_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.financial_connections.Transaction.list(account="fca_xyz")
        http_client_mock.assert_requested(
            "get",
            path="/v1/financial_connections/transactions",
            query_string="account=fca_xyz",
        )

    def test_identity_verification_reports_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.identity.VerificationReport.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/identity/verification_reports",
            query_string="limit=3",
        )

    def test_identity_verification_reports_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.identity.VerificationReport.retrieve("vr_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/identity/verification_reports/vr_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_identity_verification_sessions_cancel_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.identity.VerificationSession.cancel("vs_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/identity/verification_sessions/vs_xxxxxxxxxxxxx/cancel",
            query_string="",
        )

    def test_identity_verification_sessions_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.identity.VerificationSession.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/identity/verification_sessions",
            query_string="limit=3",
        )

    def test_identity_verification_sessions_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.identity.VerificationSession.retrieve("vs_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/identity/verification_sessions/vs_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_identity_verification_sessions_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.identity.VerificationSession.create(type="document")
        http_client_mock.assert_requested(
            "post",
            path="/v1/identity/verification_sessions",
            query_string="",
            post_data="type=document",
        )

    def test_identity_verification_sessions_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.identity.VerificationSession.modify(
            "vs_xxxxxxxxxxxxx",
            type="id_number",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/identity/verification_sessions/vs_xxxxxxxxxxxxx",
            query_string="",
            post_data="type=id_number",
        )

    def test_identity_verification_sessions_redact_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.identity.VerificationSession.redact("vs_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/identity/verification_sessions/vs_xxxxxxxxxxxxx/redact",
            query_string="",
        )

    def test_invoiceitems_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.InvoiceItem.delete("ii_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/invoiceitems/ii_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_invoiceitems_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.InvoiceItem.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/invoiceitems",
            query_string="limit=3",
        )

    def test_invoiceitems_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.InvoiceItem.retrieve("ii_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/invoiceitems/ii_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_invoiceitems_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.InvoiceItem.create(
            customer="cus_xxxxxxxxxxxxx",
            price="price_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/invoiceitems",
            query_string="",
            post_data="customer=cus_xxxxxxxxxxxxx&price=price_xxxxxxxxxxxxx",
        )

    def test_invoiceitems_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.InvoiceItem.modify(
            "ii_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/invoiceitems/ii_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_invoices_delete(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Invoice.delete("in_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/invoices/in_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_invoices_finalize_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Invoice.finalize_invoice("in_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/invoices/in_xxxxxxxxxxxxx/finalize",
            query_string="",
        )

    def test_invoices_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Invoice.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/invoices",
            query_string="limit=3",
        )

    def test_invoices_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Invoice.retrieve("in_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/invoices/in_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_invoices_get_3(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Invoice.retrieve(
            "in_xxxxxxxxxxxxx",
            expand=["customer"],
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/invoices/in_xxxxxxxxxxxxx",
            query_string="expand[0]=customer",
        )

    def test_invoices_mark_uncollectible_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Invoice.mark_uncollectible("in_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/invoices/in_xxxxxxxxxxxxx/mark_uncollectible",
            query_string="",
        )

    def test_invoices_pay_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Invoice.pay("in_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/invoices/in_xxxxxxxxxxxxx/pay",
            query_string="",
        )

    def test_invoices_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Invoice.create(customer="cus_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/invoices",
            query_string="",
            post_data="customer=cus_xxxxxxxxxxxxx",
        )

    def test_invoices_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Invoice.modify(
            "in_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/invoices/in_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_invoices_search_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Invoice.search(
            query="total>999 AND metadata['order_id']:'6735'"
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/invoices/search",
            query_string="query=total%3E999%20AND%20metadata%5B%27order_id%27%5D%3A%276735%27",
        )

    def test_invoices_send_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Invoice.send_invoice("in_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/invoices/in_xxxxxxxxxxxxx/send",
            query_string="",
        )

    def test_invoices_upcoming_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Invoice.upcoming(customer="cus_9utnxg47pWjV1e")
        http_client_mock.assert_requested(
            "get",
            path="/v1/invoices/upcoming",
            query_string="customer=cus_9utnxg47pWjV1e",
        )

    def test_invoices_void_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Invoice.void_invoice("in_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/invoices/in_xxxxxxxxxxxxx/void",
            query_string="",
        )

    def test_issuing_authorizations_approve_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Authorization.approve("iauth_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/authorizations/iauth_xxxxxxxxxxxxx/approve",
            query_string="",
        )

    def test_issuing_authorizations_decline_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Authorization.decline("iauth_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/authorizations/iauth_xxxxxxxxxxxxx/decline",
            query_string="",
        )

    def test_issuing_authorizations_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Authorization.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/issuing/authorizations",
            query_string="limit=3",
        )

    def test_issuing_authorizations_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Authorization.retrieve("iauth_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/issuing/authorizations/iauth_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_issuing_authorizations_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Authorization.modify(
            "iauth_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/authorizations/iauth_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_issuing_cardholders_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Cardholder.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/issuing/cardholders",
            query_string="limit=3",
        )

    def test_issuing_cardholders_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Cardholder.retrieve("ich_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/issuing/cardholders/ich_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_issuing_cardholders_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Cardholder.create(
            type="individual",
            name="Jenny Rosen",
            email="jenny.rosen@example.com",
            phone_number="+18888675309",
            billing={
                "address": {
                    "line1": "1234 Main Street",
                    "city": "San Francisco",
                    "state": "CA",
                    "country": "US",
                    "postal_code": "94111",
                },
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/cardholders",
            query_string="",
            post_data="type=individual&name=Jenny%20Rosen&email=jenny.rosen%40example.com&phone_number=%2B18888675309&billing[address][line1]=1234%20Main%20Street&billing[address][city]=San%20Francisco&billing[address][state]=CA&billing[address][country]=US&billing[address][postal_code]=94111",
        )

    def test_issuing_cardholders_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Cardholder.modify(
            "ich_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/cardholders/ich_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_issuing_cards_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.issuing.Card.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/issuing/cards",
            query_string="limit=3",
        )

    def test_issuing_cards_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Card.retrieve("ic_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/issuing/cards/ic_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_issuing_cards_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Card.create(
            cardholder="ich_xxxxxxxxxxxxx",
            currency="usd",
            type="virtual",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/cards",
            query_string="",
            post_data="cardholder=ich_xxxxxxxxxxxxx&currency=usd&type=virtual",
        )

    def test_issuing_cards_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Card.modify(
            "ic_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/cards/ic_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_issuing_disputes_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Dispute.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/issuing/disputes",
            query_string="limit=3",
        )

    def test_issuing_disputes_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Dispute.retrieve("idp_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/issuing/disputes/idp_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_issuing_disputes_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Dispute.create(
            transaction="ipi_xxxxxxxxxxxxx",
            evidence={
                "reason": "fraudulent",
                "fraudulent": {"explanation": "Purchase was unrecognized."},
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/disputes",
            query_string="",
            post_data="transaction=ipi_xxxxxxxxxxxxx&evidence[reason]=fraudulent&evidence[fraudulent][explanation]=Purchase%20was%20unrecognized.",
        )

    def test_issuing_disputes_submit_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Dispute.submit("idp_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/disputes/idp_xxxxxxxxxxxxx/submit",
            query_string="",
        )

    def test_issuing_transactions_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Transaction.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/issuing/transactions",
            query_string="limit=3",
        )

    def test_issuing_transactions_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Transaction.retrieve("ipi_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/issuing/transactions/ipi_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_issuing_transactions_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Transaction.modify(
            "ipi_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/issuing/transactions/ipi_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_mandates_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Mandate.retrieve("mandate_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/mandates/mandate_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_payment_intents_apply_customer_balance_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentIntent.apply_customer_balance("pi_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_intents/pi_xxxxxxxxxxxxx/apply_customer_balance",
            query_string="",
        )

    def test_payment_intents_cancel_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentIntent.cancel("pi_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_intents/pi_xxxxxxxxxxxxx/cancel",
            query_string="",
        )

    def test_payment_intents_capture_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentIntent.capture("pi_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_intents/pi_xxxxxxxxxxxxx/capture",
            query_string="",
        )

    def test_payment_intents_confirm_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentIntent.confirm(
            "pi_xxxxxxxxxxxxx",
            payment_method="pm_card_visa",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_intents/pi_xxxxxxxxxxxxx/confirm",
            query_string="",
            post_data="payment_method=pm_card_visa",
        )

    def test_payment_intents_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentIntent.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/payment_intents",
            query_string="limit=3",
        )

    def test_payment_intents_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentIntent.retrieve("pi_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/payment_intents/pi_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_payment_intents_increment_authorization_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentIntent.increment_authorization(
            "pi_xxxxxxxxxxxxx",
            amount=2099,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_intents/pi_xxxxxxxxxxxxx/increment_authorization",
            query_string="",
            post_data="amount=2099",
        )

    def test_payment_intents_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentIntent.create(
            amount=1099,
            currency="eur",
            automatic_payment_methods={"enabled": True},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_intents",
            query_string="",
            post_data="amount=1099&currency=eur&automatic_payment_methods[enabled]=True",
        )

    def test_payment_intents_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentIntent.create(
            amount=2000,
            currency="usd",
            automatic_payment_methods={"enabled": True},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_intents",
            query_string="",
            post_data="amount=2000&currency=usd&automatic_payment_methods[enabled]=True",
        )

    def test_payment_intents_post_3(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentIntent.modify(
            "pi_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_intents/pi_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_payment_intents_post_4(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentIntent.create(
            amount=200,
            currency="usd",
            payment_method_data={"type": "p24", "p24": {"bank": "blik"}},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_intents",
            query_string="",
            post_data="amount=200&currency=usd&payment_method_data[type]=p24&payment_method_data[p24][bank]=blik",
        )

    def test_payment_intents_search_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentIntent.search(
            query="status:'succeeded' AND metadata['order_id']:'6735'",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/payment_intents/search",
            query_string="query=status%3A%27succeeded%27%20AND%20metadata%5B%27order_id%27%5D%3A%276735%27",
        )

    def test_payment_intents_verify_microdeposits_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentIntent.verify_microdeposits("pi_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_intents/pi_xxxxxxxxxxxxx/verify_microdeposits",
            query_string="",
        )

    def test_payment_intents_verify_microdeposits_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentIntent.verify_microdeposits(
            "pi_xxxxxxxxxxxxx",
            amounts=[32, 45],
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_intents/pi_xxxxxxxxxxxxx/verify_microdeposits",
            query_string="",
            post_data="amounts[0]=32&amounts[1]=45",
        )

    def test_payment_links_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.PaymentLink.retrieve("pl_xyz")
        http_client_mock.assert_requested(
            "get",
            path="/v1/payment_links/pl_xyz",
            query_string="",
        )

    def test_payment_links_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentLink.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/payment_links",
            query_string="limit=3",
        )

    def test_payment_links_get_3(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentLink.retrieve("plink_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/payment_links/plink_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_payment_links_line_items_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentLink.list_line_items("pl_xyz")
        http_client_mock.assert_requested(
            "get",
            path="/v1/payment_links/pl_xyz/line_items",
            query_string="",
        )

    def test_payment_links_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentLink.create(
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 1}],
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_links",
            query_string="",
            post_data="line_items[0][price]=price_xxxxxxxxxxxxx&line_items[0][quantity]=1",
        )

    def test_payment_links_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentLink.create(
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 1}],
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_links",
            query_string="",
            post_data="line_items[0][price]=price_xxxxxxxxxxxxx&line_items[0][quantity]=1",
        )

    def test_payment_links_post_3(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentLink.modify(
            "plink_xxxxxxxxxxxxx",
            active=False,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_links/plink_xxxxxxxxxxxxx",
            query_string="",
            post_data="active=False",
        )

    def test_payment_method_configurations_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentMethodConfiguration.list(application="foo")
        http_client_mock.assert_requested(
            "get",
            path="/v1/payment_method_configurations",
            query_string="application=foo",
        )

    def test_payment_method_configurations_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentMethodConfiguration.retrieve("foo")
        http_client_mock.assert_requested(
            "get",
            path="/v1/payment_method_configurations/foo",
            query_string="",
        )

    def test_payment_method_configurations_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentMethodConfiguration.create(
            acss_debit={"display_preference": {"preference": "none"}},
            affirm={"display_preference": {"preference": "none"}},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_method_configurations",
            query_string="",
            post_data="acss_debit[display_preference][preference]=none&affirm[display_preference][preference]=none",
        )

    def test_payment_method_configurations_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentMethodConfiguration.modify(
            "foo",
            acss_debit={"display_preference": {"preference": "on"}},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_method_configurations/foo",
            query_string="",
            post_data="acss_debit[display_preference][preference]=on",
        )

    def test_payment_methods_attach_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentMethod.attach(
            "pm_xxxxxxxxxxxxx",
            customer="cus_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_methods/pm_xxxxxxxxxxxxx/attach",
            query_string="",
            post_data="customer=cus_xxxxxxxxxxxxx",
        )

    def test_payment_methods_detach_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentMethod.detach("pm_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_methods/pm_xxxxxxxxxxxxx/detach",
            query_string="",
        )

    def test_payment_methods_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentMethod.list(
            customer="cus_xxxxxxxxxxxxx",
            type="card",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/payment_methods",
            query_string="customer=cus_xxxxxxxxxxxxx&type=card",
        )

    def test_payment_methods_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentMethod.retrieve("pm_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/payment_methods/pm_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_payment_methods_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentMethod.create(
            type="card",
            card={
                "number": "4242424242424242",
                "exp_month": 8,
                "exp_year": 2024,
                "cvc": "314",
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_methods",
            query_string="",
            post_data="type=card&card[number]=4242424242424242&card[exp_month]=8&card[exp_year]=2024&card[cvc]=314",
        )

    def test_payment_methods_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PaymentMethod.modify(
            "pm_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payment_methods/pm_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_payouts_cancel_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Payout.cancel("po_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/payouts/po_xxxxxxxxxxxxx/cancel",
            query_string="",
        )

    def test_payouts_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Payout.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/payouts",
            query_string="limit=3",
        )

    def test_payouts_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Payout.retrieve("po_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/payouts/po_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_payouts_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Payout.create(
            amount=1100,
            currency="usd",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payouts",
            query_string="",
            post_data="amount=1100&currency=usd",
        )

    def test_payouts_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Payout.modify(
            "po_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/payouts/po_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_payouts_reverse_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Payout.reverse("po_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/payouts/po_xxxxxxxxxxxxx/reverse",
            query_string="",
        )

    def test_plans_delete(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Plan.delete("price_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/plans/price_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_plans_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Plan.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/plans",
            query_string="limit=3",
        )

    def test_plans_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Plan.retrieve("price_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/plans/price_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_plans_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Plan.create(
            amount=2000,
            currency="usd",
            interval="month",
            product="prod_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/plans",
            query_string="",
            post_data="amount=2000&currency=usd&interval=month&product=prod_xxxxxxxxxxxxx",
        )

    def test_plans_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Plan.create(
            amount=2000,
            currency="usd",
            interval="month",
            product={"name": "My product"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/plans",
            query_string="",
            post_data="amount=2000&currency=usd&interval=month&product[name]=My%20product",
        )

    def test_plans_post_3(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Plan.modify(
            "price_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/plans/price_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_prices_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Price.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/prices",
            query_string="limit=3",
        )

    def test_prices_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Price.retrieve("price_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/prices/price_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_prices_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Price.create(
            unit_amount=2000,
            currency="usd",
            currency_options={
                "uah": {"unit_amount": 5000},
                "eur": {"unit_amount": 1800},
            },
            recurring={"interval": "month"},
            product="prod_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/prices",
            query_string="",
            post_data="unit_amount=2000&currency=usd&currency_options[uah][unit_amount]=5000&currency_options[eur][unit_amount]=1800&recurring[interval]=month&product=prod_xxxxxxxxxxxxx",
        )

    def test_prices_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Price.create(
            unit_amount=2000,
            currency="usd",
            recurring={"interval": "month"},
            product="prod_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/prices",
            query_string="",
            post_data="unit_amount=2000&currency=usd&recurring[interval]=month&product=prod_xxxxxxxxxxxxx",
        )

    def test_prices_post_3(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Price.modify(
            "price_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/prices/price_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_prices_search_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Price.search(
            query="active:'true' AND metadata['order_id']:'6735'",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/prices/search",
            query_string="query=active%3A%27true%27%20AND%20metadata%5B%27order_id%27%5D%3A%276735%27",
        )

    def test_products_delete(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Product.delete("prod_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/products/prod_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_products_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Product.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/products",
            query_string="limit=3",
        )

    def test_products_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Product.retrieve("prod_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/products/prod_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_products_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Product.create(name="Gold Special")
        http_client_mock.assert_requested(
            "post",
            path="/v1/products",
            query_string="",
            post_data="name=Gold%20Special",
        )

    def test_products_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Product.modify(
            "prod_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/products/prod_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_products_search_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Product.search(
            query="active:'true' AND metadata['order_id']:'6735'",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/products/search",
            query_string="query=active%3A%27true%27%20AND%20metadata%5B%27order_id%27%5D%3A%276735%27",
        )

    def test_promotion_codes_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PromotionCode.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/promotion_codes",
            query_string="limit=3",
        )

    def test_promotion_codes_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PromotionCode.retrieve("promo_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/promotion_codes/promo_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_promotion_codes_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PromotionCode.create(coupon="Z4OV52SU")
        http_client_mock.assert_requested(
            "post",
            path="/v1/promotion_codes",
            query_string="",
            post_data="coupon=Z4OV52SU",
        )

    def test_promotion_codes_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.PromotionCode.modify(
            "promo_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/promotion_codes/promo_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_quotes_accept_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Quote.accept("qt_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/quotes/qt_xxxxxxxxxxxxx/accept",
            query_string="",
        )

    def test_quotes_cancel_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Quote.cancel("qt_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/quotes/qt_xxxxxxxxxxxxx/cancel",
            query_string="",
        )

    def test_quotes_finalize_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Quote.finalize_quote("qt_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/quotes/qt_xxxxxxxxxxxxx/finalize",
            query_string="",
        )

    def test_quotes_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Quote.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/quotes",
            query_string="limit=3",
        )

    def test_quotes_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Quote.retrieve("qt_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/quotes/qt_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_quotes_line_items_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Quote.list_line_items("qt_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/quotes/qt_xxxxxxxxxxxxx/line_items",
            query_string="",
        )

    def test_quotes_pdf_get(
        self, http_client_mock_streaming: HTTPClientMock
    ) -> None:
        stripe.Quote.pdf("qt_xxxxxxxxxxxxx")
        http_client_mock_streaming.assert_requested(
            "get",
            path="/v1/quotes/qt_xxxxxxxxxxxxx/pdf",
            query_string="",
        )

    def test_quotes_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Quote.create(
            customer="cus_xxxxxxxxxxxxx",
            line_items=[{"price": "price_xxxxxxxxxxxxx", "quantity": 2}],
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/quotes",
            query_string="",
            post_data="customer=cus_xxxxxxxxxxxxx&line_items[0][price]=price_xxxxxxxxxxxxx&line_items[0][quantity]=2",
        )

    def test_quotes_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Quote.modify(
            "qt_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/quotes/qt_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_radar_early_fraud_warnings_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.radar.EarlyFraudWarning.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/radar/early_fraud_warnings",
            query_string="limit=3",
        )

    def test_radar_early_fraud_warnings_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.radar.EarlyFraudWarning.retrieve("issfr_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/radar/early_fraud_warnings/issfr_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_radar_value_list_items_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.radar.ValueListItem.delete("rsli_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/radar/value_list_items/rsli_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_radar_value_list_items_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.radar.ValueListItem.list(
            limit=3,
            value_list="rsl_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/radar/value_list_items",
            query_string="limit=3&value_list=rsl_xxxxxxxxxxxxx",
        )

    def test_radar_value_list_items_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.radar.ValueListItem.retrieve("rsli_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/radar/value_list_items/rsli_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_radar_value_list_items_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.radar.ValueListItem.create(
            value_list="rsl_xxxxxxxxxxxxx",
            value="1.2.3.4",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/radar/value_list_items",
            query_string="",
            post_data="value_list=rsl_xxxxxxxxxxxxx&value=1.2.3.4",
        )

    def test_radar_value_lists_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.radar.ValueList.delete("rsl_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/radar/value_lists/rsl_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_radar_value_lists_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.radar.ValueList.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/radar/value_lists",
            query_string="limit=3",
        )

    def test_radar_value_lists_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.radar.ValueList.retrieve("rsl_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/radar/value_lists/rsl_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_radar_value_lists_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.radar.ValueList.create(
            alias="custom_ip_xxxxxxxxxxxxx",
            name="Custom IP Blocklist",
            item_type="ip_address",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/radar/value_lists",
            query_string="",
            post_data="alias=custom_ip_xxxxxxxxxxxxx&name=Custom%20IP%20Blocklist&item_type=ip_address",
        )

    def test_radar_value_lists_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.radar.ValueList.modify(
            "rsl_xxxxxxxxxxxxx",
            name="Updated IP Block List",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/radar/value_lists/rsl_xxxxxxxxxxxxx",
            query_string="",
            post_data="name=Updated%20IP%20Block%20List",
        )

    def test_refunds_cancel_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Refund.cancel("re_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/refunds/re_xxxxxxxxxxxxx/cancel",
            query_string="",
        )

    def test_refunds_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Refund.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/refunds",
            query_string="limit=3",
        )

    def test_refunds_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Refund.retrieve("re_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/refunds/re_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_refunds_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Refund.create(charge="ch_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/refunds",
            query_string="",
            post_data="charge=ch_xxxxxxxxxxxxx",
        )

    def test_refunds_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Refund.modify(
            "re_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/refunds/re_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_reporting_report_runs_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.reporting.ReportRun.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/reporting/report_runs",
            query_string="limit=3",
        )

    def test_reporting_report_runs_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.reporting.ReportRun.retrieve("frr_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/reporting/report_runs/frr_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_reporting_report_runs_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.reporting.ReportRun.create(
            report_type="balance.summary.1",
            parameters={
                "interval_start": 1522540800,
                "interval_end": 1525132800,
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/reporting/report_runs",
            query_string="",
            post_data="report_type=balance.summary.1&parameters[interval_start]=1522540800&parameters[interval_end]=1525132800",
        )

    def test_reporting_report_types_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.reporting.ReportType.list()
        http_client_mock.assert_requested(
            "get",
            path="/v1/reporting/report_types",
            query_string="",
        )

    def test_reporting_report_types_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.reporting.ReportType.retrieve("balance.summary.1")
        http_client_mock.assert_requested(
            "get",
            path="/v1/reporting/report_types/balance.summary.1",
            query_string="",
        )

    def test_reviews_approve_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Review.approve("prv_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/reviews/prv_xxxxxxxxxxxxx/approve",
            query_string="",
        )

    def test_reviews_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Review.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/reviews",
            query_string="limit=3",
        )

    def test_reviews_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Review.retrieve("prv_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/reviews/prv_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_setup_attempts_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SetupAttempt.list(
            limit=3,
            setup_intent="si_xyz",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/setup_attempts",
            query_string="limit=3&setup_intent=si_xyz",
        )

    def test_setup_intents_cancel_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SetupIntent.cancel("seti_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/setup_intents/seti_xxxxxxxxxxxxx/cancel",
            query_string="",
        )

    def test_setup_intents_confirm_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SetupIntent.confirm(
            "seti_xxxxxxxxxxxxx",
            payment_method="pm_card_visa",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/setup_intents/seti_xxxxxxxxxxxxx/confirm",
            query_string="",
            post_data="payment_method=pm_card_visa",
        )

    def test_setup_intents_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.SetupIntent.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/setup_intents",
            query_string="limit=3",
        )

    def test_setup_intents_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SetupIntent.retrieve("seti_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/setup_intents/seti_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_setup_intents_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SetupIntent.create(payment_method_types=["card"])
        http_client_mock.assert_requested(
            "post",
            path="/v1/setup_intents",
            query_string="",
            post_data="payment_method_types[0]=card",
        )

    def test_setup_intents_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SetupIntent.modify(
            "seti_xxxxxxxxxxxxx",
            metadata={"user_id": "3435453"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/setup_intents/seti_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[user_id]=3435453",
        )

    def test_setup_intents_verify_microdeposits_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SetupIntent.verify_microdeposits("seti_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/setup_intents/seti_xxxxxxxxxxxxx/verify_microdeposits",
            query_string="",
        )

    def test_setup_intents_verify_microdeposits_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SetupIntent.verify_microdeposits(
            "seti_xxxxxxxxxxxxx",
            amounts=[32, 45],
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/setup_intents/seti_xxxxxxxxxxxxx/verify_microdeposits",
            query_string="",
            post_data="amounts[0]=32&amounts[1]=45",
        )

    def test_shipping_rates_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.ShippingRate.list()
        http_client_mock.assert_requested(
            "get",
            path="/v1/shipping_rates",
            query_string="",
        )

    def test_shipping_rates_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.ShippingRate.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/shipping_rates",
            query_string="limit=3",
        )

    def test_shipping_rates_get_3(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.ShippingRate.retrieve("shr_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/shipping_rates/shr_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_shipping_rates_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.ShippingRate.create(
            display_name="Sample Shipper",
            fixed_amount={"currency": "usd", "amount": 400},
            type="fixed_amount",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/shipping_rates",
            query_string="",
            post_data="display_name=Sample%20Shipper&fixed_amount[currency]=usd&fixed_amount[amount]=400&type=fixed_amount",
        )

    def test_shipping_rates_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.ShippingRate.create(
            display_name="Ground shipping",
            type="fixed_amount",
            fixed_amount={"amount": 500, "currency": "usd"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/shipping_rates",
            query_string="",
            post_data="display_name=Ground%20shipping&type=fixed_amount&fixed_amount[amount]=500&fixed_amount[currency]=usd",
        )

    def test_shipping_rates_post_3(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.ShippingRate.modify(
            "shr_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/shipping_rates/shr_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_sigma_scheduled_query_runs_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.sigma.ScheduledQueryRun.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/sigma/scheduled_query_runs",
            query_string="limit=3",
        )

    def test_sigma_scheduled_query_runs_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.sigma.ScheduledQueryRun.retrieve("sqr_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/sigma/scheduled_query_runs/sqr_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_sources_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Source.retrieve("src_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/sources/src_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_sources_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Source.retrieve("src_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/sources/src_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_sources_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Source.modify(
            "src_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/sources/src_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_subscription_items_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SubscriptionItem.delete("si_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/subscription_items/si_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_subscription_items_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SubscriptionItem.list(subscription="sub_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/subscription_items",
            query_string="subscription=sub_xxxxxxxxxxxxx",
        )

    def test_subscription_items_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SubscriptionItem.retrieve("si_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/subscription_items/si_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_subscription_items_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SubscriptionItem.create(
            subscription="sub_xxxxxxxxxxxxx",
            price="price_xxxxxxxxxxxxx",
            quantity=2,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_items",
            query_string="",
            post_data="subscription=sub_xxxxxxxxxxxxx&price=price_xxxxxxxxxxxxx&quantity=2",
        )

    def test_subscription_items_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SubscriptionItem.modify(
            "si_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_items/si_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_subscription_items_usage_record_summaries_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SubscriptionItem.list_usage_record_summaries(
            "si_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/subscription_items/si_xxxxxxxxxxxxx/usage_record_summaries",
            query_string="limit=3",
        )

    def test_subscription_items_usage_records_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SubscriptionItem.create_usage_record(
            "si_xxxxxxxxxxxxx",
            quantity=100,
            timestamp=1571252444,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_items/si_xxxxxxxxxxxxx/usage_records",
            query_string="",
            post_data="quantity=100&timestamp=1571252444",
        )

    def test_subscription_schedules_cancel_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SubscriptionSchedule.cancel("sub_sched_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_schedules/sub_sched_xxxxxxxxxxxxx/cancel",
            query_string="",
        )

    def test_subscription_schedules_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SubscriptionSchedule.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/subscription_schedules",
            query_string="limit=3",
        )

    def test_subscription_schedules_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SubscriptionSchedule.retrieve("sub_sched_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/subscription_schedules/sub_sched_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_subscription_schedules_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SubscriptionSchedule.create(
            customer="cus_xxxxxxxxxxxxx",
            start_date=1676070661,
            end_behavior="release",
            phases=[
                {
                    "items": [{"price": "price_xxxxxxxxxxxxx", "quantity": 1}],
                    "iterations": 12,
                },
            ],
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_schedules",
            query_string="",
            post_data="customer=cus_xxxxxxxxxxxxx&start_date=1676070661&end_behavior=release&phases[0][items][0][price]=price_xxxxxxxxxxxxx&phases[0][items][0][quantity]=1&phases[0][iterations]=12",
        )

    def test_subscription_schedules_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SubscriptionSchedule.modify(
            "sub_sched_xxxxxxxxxxxxx",
            end_behavior="release",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_schedules/sub_sched_xxxxxxxxxxxxx",
            query_string="",
            post_data="end_behavior=release",
        )

    def test_subscription_schedules_release_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.SubscriptionSchedule.release("sub_sched_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscription_schedules/sub_sched_xxxxxxxxxxxxx/release",
            query_string="",
        )

    def test_subscriptions_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Subscription.cancel("sub_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/subscriptions/sub_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_subscriptions_discount_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Subscription.delete_discount("sub_xyz")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/subscriptions/sub_xyz/discount",
            query_string="",
        )

    def test_subscriptions_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Subscription.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/subscriptions",
            query_string="limit=3",
        )

    def test_subscriptions_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Subscription.retrieve("sub_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/subscriptions/sub_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_subscriptions_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Subscription.create(
            customer="cus_xxxxxxxxxxxxx",
            items=[{"price": "price_xxxxxxxxxxxxx"}],
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscriptions",
            query_string="",
            post_data="customer=cus_xxxxxxxxxxxxx&items[0][price]=price_xxxxxxxxxxxxx",
        )

    def test_subscriptions_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Subscription.modify(
            "sub_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/subscriptions/sub_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_subscriptions_search_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Subscription.search(
            query="status:'active' AND metadata['order_id']:'6735'",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/subscriptions/search",
            query_string="query=status%3A%27active%27%20AND%20metadata%5B%27order_id%27%5D%3A%276735%27",
        )

    def test_tax_calculations_line_items_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.tax.Calculation.list_line_items("xxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/tax/calculations/xxx/line_items",
            query_string="",
        )

    def test_tax_calculations_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.tax.Calculation.create(
            currency="usd",
            line_items=[{"amount": 1000, "reference": "L1"}],
            customer_details={
                "address": {
                    "line1": "354 Oyster Point Blvd",
                    "city": "South San Francisco",
                    "state": "CA",
                    "postal_code": "94080",
                    "country": "US",
                },
                "address_source": "shipping",
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/tax/calculations",
            query_string="",
            post_data="currency=usd&line_items[0][amount]=1000&line_items[0][reference]=L1&customer_details[address][line1]=354%20Oyster%20Point%20Blvd&customer_details[address][city]=South%20San%20Francisco&customer_details[address][state]=CA&customer_details[address][postal_code]=94080&customer_details[address][country]=US&customer_details[address_source]=shipping",
        )

    def test_tax_codes_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.TaxCode.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/tax_codes",
            query_string="limit=3",
        )

    def test_tax_codes_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.TaxCode.retrieve("txcd_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/tax_codes/txcd_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_tax_rates_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.TaxRate.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/tax_rates",
            query_string="limit=3",
        )

    def test_tax_rates_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.TaxRate.retrieve("txr_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/tax_rates/txr_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_tax_rates_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.TaxRate.create(
            display_name="VAT",
            description="VAT Germany",
            jurisdiction="DE",
            percentage=16,
            inclusive=False,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/tax_rates",
            query_string="",
            post_data="display_name=VAT&description=VAT%20Germany&jurisdiction=DE&percentage=16&inclusive=False",
        )

    def test_tax_rates_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.TaxRate.modify(
            "txr_xxxxxxxxxxxxx",
            active=False,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/tax_rates/txr_xxxxxxxxxxxxx",
            query_string="",
            post_data="active=False",
        )

    def test_tax_registrations_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.tax.Registration.list(status="all")
        http_client_mock.assert_requested(
            "get",
            path="/v1/tax/registrations",
            query_string="status=all",
        )

    def test_tax_registrations_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.tax.Registration.create(
            country="IE",
            country_options={"ie": {"type": "oss_union"}},
            active_from="now",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/tax/registrations",
            query_string="",
            post_data="country=IE&country_options[ie][type]=oss_union&active_from=now",
        )

    def test_tax_registrations_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.tax.Registration.modify(
            "taxreg_xxxxxxxxxxxxx",
            expires_at="now",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/tax/registrations/taxreg_xxxxxxxxxxxxx",
            query_string="",
            post_data="expires_at=now",
        )

    def test_tax_settings_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.tax.Settings.retrieve()
        http_client_mock.assert_requested(
            "get",
            path="/v1/tax/settings",
            query_string="",
        )

    def test_tax_settings_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.tax.Settings.modify(defaults={"tax_code": "txcd_10000000"})
        http_client_mock.assert_requested(
            "post",
            path="/v1/tax/settings",
            query_string="",
            post_data="defaults[tax_code]=txcd_10000000",
        )

    def test_tax_transactions_create_from_calculation_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.tax.Transaction.create_from_calculation(
            calculation="xxx",
            reference="yyy",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/tax/transactions/create_from_calculation",
            query_string="",
            post_data="calculation=xxx&reference=yyy",
        )

    def test_terminal_configurations_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Configuration.delete("uc_123")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/terminal/configurations/uc_123",
            query_string="",
        )

    def test_terminal_configurations_delete_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Configuration.delete("tmc_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/terminal/configurations/tmc_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_terminal_configurations_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Configuration.list()
        http_client_mock.assert_requested(
            "get",
            path="/v1/terminal/configurations",
            query_string="",
        )

    def test_terminal_configurations_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Configuration.retrieve("uc_123")
        http_client_mock.assert_requested(
            "get",
            path="/v1/terminal/configurations/uc_123",
            query_string="",
        )

    def test_terminal_configurations_get_3(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Configuration.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/terminal/configurations",
            query_string="limit=3",
        )

    def test_terminal_configurations_get_4(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Configuration.retrieve("tmc_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/terminal/configurations/tmc_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_terminal_configurations_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Configuration.create()
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/configurations",
            query_string="",
        )

    def test_terminal_configurations_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Configuration.modify(
            "uc_123",
            tipping={"usd": {"fixed_amounts": [10]}},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/configurations/uc_123",
            query_string="",
            post_data="tipping[usd][fixed_amounts][0]=10",
        )

    def test_terminal_configurations_post_3(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Configuration.create(
            bbpos_wisepos_e={"splashscreen": "file_xxxxxxxxxxxxx"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/configurations",
            query_string="",
            post_data="bbpos_wisepos_e[splashscreen]=file_xxxxxxxxxxxxx",
        )

    def test_terminal_configurations_post_4(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Configuration.modify(
            "tmc_xxxxxxxxxxxxx",
            bbpos_wisepos_e={"splashscreen": "file_xxxxxxxxxxxxx"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/configurations/tmc_xxxxxxxxxxxxx",
            query_string="",
            post_data="bbpos_wisepos_e[splashscreen]=file_xxxxxxxxxxxxx",
        )

    def test_terminal_connection_tokens_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.ConnectionToken.create()
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/connection_tokens",
            query_string="",
        )

    def test_terminal_locations_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Location.delete("tml_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/terminal/locations/tml_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_terminal_locations_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Location.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/terminal/locations",
            query_string="limit=3",
        )

    def test_terminal_locations_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Location.retrieve("tml_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/terminal/locations/tml_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_terminal_locations_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Location.create(
            display_name="My First Store",
            address={
                "line1": "1234 Main Street",
                "city": "San Francisco",
                "postal_code": "94111",
                "state": "CA",
                "country": "US",
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/locations",
            query_string="",
            post_data="display_name=My%20First%20Store&address[line1]=1234%20Main%20Street&address[city]=San%20Francisco&address[postal_code]=94111&address[state]=CA&address[country]=US",
        )

    def test_terminal_locations_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Location.modify(
            "tml_xxxxxxxxxxxxx",
            display_name="My First Store",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/locations/tml_xxxxxxxxxxxxx",
            query_string="",
            post_data="display_name=My%20First%20Store",
        )

    def test_terminal_readers_cancel_action_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Reader.cancel_action("tmr_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/readers/tmr_xxxxxxxxxxxxx/cancel_action",
            query_string="",
        )

    def test_terminal_readers_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Reader.delete("tmr_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/terminal/readers/tmr_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_terminal_readers_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Reader.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/terminal/readers",
            query_string="limit=3",
        )

    def test_terminal_readers_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Reader.retrieve("tmr_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/terminal/readers/tmr_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_terminal_readers_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Reader.create(
            registration_code="puppies-plug-could",
            label="Blue Rabbit",
            location="tml_1234",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/readers",
            query_string="",
            post_data="registration_code=puppies-plug-could&label=Blue%20Rabbit&location=tml_1234",
        )

    def test_terminal_readers_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Reader.modify(
            "tmr_xxxxxxxxxxxxx",
            label="Blue Rabbit",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/readers/tmr_xxxxxxxxxxxxx",
            query_string="",
            post_data="label=Blue%20Rabbit",
        )

    def test_terminal_readers_process_payment_intent_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Reader.process_payment_intent(
            "tmr_xxxxxxxxxxxxx",
            payment_intent="pi_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/readers/tmr_xxxxxxxxxxxxx/process_payment_intent",
            query_string="",
            post_data="payment_intent=pi_xxxxxxxxxxxxx",
        )

    def test_terminal_readers_process_setup_intent_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.terminal.Reader.process_setup_intent(
            "tmr_xxxxxxxxxxxxx",
            setup_intent="seti_xxxxxxxxxxxxx",
            customer_consent_collected=True,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/terminal/readers/tmr_xxxxxxxxxxxxx/process_setup_intent",
            query_string="",
            post_data="setup_intent=seti_xxxxxxxxxxxxx&customer_consent_collected=True",
        )

    def test_test_helpers_customers_fund_cash_balance_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Customer.TestHelpers.fund_cash_balance(
            "cus_123",
            amount=30,
            currency="eur",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/customers/cus_123/fund_cash_balance",
            query_string="",
            post_data="amount=30&currency=eur",
        )

    def test_test_helpers_issuing_authorizations_capture_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Authorization.TestHelpers.capture(
            "example_authorization",
            capture_amount=100,
            close_authorization=True,
            purchase_details={
                "flight": {
                    "departure_at": 1633651200,
                    "passenger_name": "John Doe",
                    "refundable": True,
                    "segments": [
                        {
                            "arrival_airport_code": "SFO",
                            "carrier": "Delta",
                            "departure_airport_code": "LAX",
                            "flight_number": "DL100",
                            "service_class": "Economy",
                            "stopover_allowed": True,
                        },
                    ],
                    "travel_agency": "Orbitz",
                },
                "fuel": {
                    "type": "diesel",
                    "unit": "liter",
                    "unit_cost_decimal": "3.5",
                    "volume_decimal": "10",
                },
                "lodging": {"check_in_at": 1633651200, "nights": 2},
                "receipt": [
                    {
                        "description": "Room charge",
                        "quantity": "1",
                        "total": 200,
                        "unit_cost": 200,
                    },
                ],
                "reference": "foo",
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/issuing/authorizations/example_authorization/capture",
            query_string="",
            post_data="capture_amount=100&close_authorization=True&purchase_details[flight][departure_at]=1633651200&purchase_details[flight][passenger_name]=John%20Doe&purchase_details[flight][refundable]=True&purchase_details[flight][segments][0][arrival_airport_code]=SFO&purchase_details[flight][segments][0][carrier]=Delta&purchase_details[flight][segments][0][departure_airport_code]=LAX&purchase_details[flight][segments][0][flight_number]=DL100&purchase_details[flight][segments][0][service_class]=Economy&purchase_details[flight][segments][0][stopover_allowed]=True&purchase_details[flight][travel_agency]=Orbitz&purchase_details[fuel][type]=diesel&purchase_details[fuel][unit]=liter&purchase_details[fuel][unit_cost_decimal]=3.5&purchase_details[fuel][volume_decimal]=10&purchase_details[lodging][check_in_at]=1633651200&purchase_details[lodging][nights]=2&purchase_details[receipt][0][description]=Room%20charge&purchase_details[receipt][0][quantity]=1&purchase_details[receipt][0][total]=200&purchase_details[receipt][0][unit_cost]=200&purchase_details[reference]=foo",
        )

    def test_test_helpers_issuing_authorizations_expire_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Authorization.TestHelpers.expire(
            "example_authorization"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/issuing/authorizations/example_authorization/expire",
            query_string="",
        )

    def test_test_helpers_issuing_authorizations_increment_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Authorization.TestHelpers.increment(
            "example_authorization",
            increment_amount=50,
            is_amount_controllable=True,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/issuing/authorizations/example_authorization/increment",
            query_string="",
            post_data="increment_amount=50&is_amount_controllable=True",
        )

    def test_test_helpers_issuing_authorizations_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Authorization.TestHelpers.create(
            amount=100,
            amount_details={"atm_fee": 10, "cashback_amount": 5},
            authorization_method="chip",
            card="foo",
            currency="usd",
            is_amount_controllable=True,
            merchant_data={
                "category": "ac_refrigeration_repair",
                "city": "foo",
                "country": "bar",
                "name": "foo",
                "network_id": "bar",
                "postal_code": "foo",
                "state": "bar",
                "terminal_id": "foo",
            },
            network_data={"acquiring_institution_id": "foo"},
            verification_data={
                "address_line1_check": "mismatch",
                "address_postal_code_check": "match",
                "cvc_check": "match",
                "expiry_check": "mismatch",
            },
            wallet="apple_pay",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/issuing/authorizations",
            query_string="",
            post_data="amount=100&amount_details[atm_fee]=10&amount_details[cashback_amount]=5&authorization_method=chip&card=foo&currency=usd&is_amount_controllable=True&merchant_data[category]=ac_refrigeration_repair&merchant_data[city]=foo&merchant_data[country]=bar&merchant_data[name]=foo&merchant_data[network_id]=bar&merchant_data[postal_code]=foo&merchant_data[state]=bar&merchant_data[terminal_id]=foo&network_data[acquiring_institution_id]=foo&verification_data[address_line1_check]=mismatch&verification_data[address_postal_code_check]=match&verification_data[cvc_check]=match&verification_data[expiry_check]=mismatch&wallet=apple_pay",
        )

    def test_test_helpers_issuing_authorizations_reverse_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Authorization.TestHelpers.reverse(
            "example_authorization",
            reverse_amount=20,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/issuing/authorizations/example_authorization/reverse",
            query_string="",
            post_data="reverse_amount=20",
        )

    def test_test_helpers_issuing_cards_shipping_deliver_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Card.TestHelpers.deliver_card("card_123")
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/issuing/cards/card_123/shipping/deliver",
            query_string="",
        )

    def test_test_helpers_issuing_cards_shipping_fail_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Card.TestHelpers.fail_card("card_123")
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/issuing/cards/card_123/shipping/fail",
            query_string="",
        )

    def test_test_helpers_issuing_cards_shipping_return_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Card.TestHelpers.return_card("card_123")
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/issuing/cards/card_123/shipping/return",
            query_string="",
        )

    def test_test_helpers_issuing_cards_shipping_ship_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Card.TestHelpers.ship_card("card_123")
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/issuing/cards/card_123/shipping/ship",
            query_string="",
        )

    def test_test_helpers_issuing_transactions_create_force_capture_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Transaction.TestHelpers.create_force_capture(
            amount=100,
            card="foo",
            currency="usd",
            merchant_data={
                "category": "ac_refrigeration_repair",
                "city": "foo",
                "country": "US",
                "name": "foo",
                "network_id": "bar",
                "postal_code": "10001",
                "state": "NY",
                "terminal_id": "foo",
            },
            purchase_details={
                "flight": {
                    "departure_at": 1633651200,
                    "passenger_name": "John Doe",
                    "refundable": True,
                    "segments": [
                        {
                            "arrival_airport_code": "SFO",
                            "carrier": "Delta",
                            "departure_airport_code": "LAX",
                            "flight_number": "DL100",
                            "service_class": "Economy",
                            "stopover_allowed": True,
                        },
                    ],
                    "travel_agency": "Orbitz",
                },
                "fuel": {
                    "type": "diesel",
                    "unit": "liter",
                    "unit_cost_decimal": "3.5",
                    "volume_decimal": "10",
                },
                "lodging": {"check_in_at": 1533651200, "nights": 2},
                "receipt": [
                    {
                        "description": "Room charge",
                        "quantity": "1",
                        "total": 200,
                        "unit_cost": 200,
                    },
                ],
                "reference": "foo",
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/issuing/transactions/create_force_capture",
            query_string="",
            post_data="amount=100&card=foo&currency=usd&merchant_data[category]=ac_refrigeration_repair&merchant_data[city]=foo&merchant_data[country]=US&merchant_data[name]=foo&merchant_data[network_id]=bar&merchant_data[postal_code]=10001&merchant_data[state]=NY&merchant_data[terminal_id]=foo&purchase_details[flight][departure_at]=1633651200&purchase_details[flight][passenger_name]=John%20Doe&purchase_details[flight][refundable]=True&purchase_details[flight][segments][0][arrival_airport_code]=SFO&purchase_details[flight][segments][0][carrier]=Delta&purchase_details[flight][segments][0][departure_airport_code]=LAX&purchase_details[flight][segments][0][flight_number]=DL100&purchase_details[flight][segments][0][service_class]=Economy&purchase_details[flight][segments][0][stopover_allowed]=True&purchase_details[flight][travel_agency]=Orbitz&purchase_details[fuel][type]=diesel&purchase_details[fuel][unit]=liter&purchase_details[fuel][unit_cost_decimal]=3.5&purchase_details[fuel][volume_decimal]=10&purchase_details[lodging][check_in_at]=1533651200&purchase_details[lodging][nights]=2&purchase_details[receipt][0][description]=Room%20charge&purchase_details[receipt][0][quantity]=1&purchase_details[receipt][0][total]=200&purchase_details[receipt][0][unit_cost]=200&purchase_details[reference]=foo",
        )

    def test_test_helpers_issuing_transactions_create_unlinked_refund_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Transaction.TestHelpers.create_unlinked_refund(
            amount=100,
            card="foo",
            currency="usd",
            merchant_data={
                "category": "ac_refrigeration_repair",
                "city": "foo",
                "country": "bar",
                "name": "foo",
                "network_id": "bar",
                "postal_code": "foo",
                "state": "bar",
                "terminal_id": "foo",
            },
            purchase_details={
                "flight": {
                    "departure_at": 1533651200,
                    "passenger_name": "John Doe",
                    "refundable": True,
                    "segments": [
                        {
                            "arrival_airport_code": "SFO",
                            "carrier": "Delta",
                            "departure_airport_code": "LAX",
                            "flight_number": "DL100",
                            "service_class": "Economy",
                            "stopover_allowed": True,
                        },
                    ],
                    "travel_agency": "Orbitz",
                },
                "fuel": {
                    "type": "diesel",
                    "unit": "liter",
                    "unit_cost_decimal": "3.5",
                    "volume_decimal": "10",
                },
                "lodging": {"check_in_at": 1533651200, "nights": 2},
                "receipt": [
                    {
                        "description": "Room charge",
                        "quantity": "1",
                        "total": 200,
                        "unit_cost": 200,
                    },
                ],
                "reference": "foo",
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/issuing/transactions/create_unlinked_refund",
            query_string="",
            post_data="amount=100&card=foo&currency=usd&merchant_data[category]=ac_refrigeration_repair&merchant_data[city]=foo&merchant_data[country]=bar&merchant_data[name]=foo&merchant_data[network_id]=bar&merchant_data[postal_code]=foo&merchant_data[state]=bar&merchant_data[terminal_id]=foo&purchase_details[flight][departure_at]=1533651200&purchase_details[flight][passenger_name]=John%20Doe&purchase_details[flight][refundable]=True&purchase_details[flight][segments][0][arrival_airport_code]=SFO&purchase_details[flight][segments][0][carrier]=Delta&purchase_details[flight][segments][0][departure_airport_code]=LAX&purchase_details[flight][segments][0][flight_number]=DL100&purchase_details[flight][segments][0][service_class]=Economy&purchase_details[flight][segments][0][stopover_allowed]=True&purchase_details[flight][travel_agency]=Orbitz&purchase_details[fuel][type]=diesel&purchase_details[fuel][unit]=liter&purchase_details[fuel][unit_cost_decimal]=3.5&purchase_details[fuel][volume_decimal]=10&purchase_details[lodging][check_in_at]=1533651200&purchase_details[lodging][nights]=2&purchase_details[receipt][0][description]=Room%20charge&purchase_details[receipt][0][quantity]=1&purchase_details[receipt][0][total]=200&purchase_details[receipt][0][unit_cost]=200&purchase_details[reference]=foo",
        )

    def test_test_helpers_issuing_transactions_refund_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.issuing.Transaction.TestHelpers.refund(
            "example_transaction",
            refund_amount=50,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/issuing/transactions/example_transaction/refund",
            query_string="",
            post_data="refund_amount=50",
        )

    def test_test_helpers_refunds_expire_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Refund.TestHelpers.expire("re_123")
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/refunds/re_123/expire",
            query_string="",
        )

    def test_test_helpers_test_clocks_advance_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.test_helpers.TestClock.advance(
            "clock_xyz",
            frozen_time=142,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/test_clocks/clock_xyz/advance",
            query_string="",
            post_data="frozen_time=142",
        )

    def test_test_helpers_test_clocks_advance_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.test_helpers.TestClock.advance(
            "clock_xxxxxxxxxxxxx",
            frozen_time=1675552261,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/test_clocks/clock_xxxxxxxxxxxxx/advance",
            query_string="",
            post_data="frozen_time=1675552261",
        )

    def test_test_helpers_test_clocks_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.test_helpers.TestClock.delete("clock_xyz")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/test_helpers/test_clocks/clock_xyz",
            query_string="",
        )

    def test_test_helpers_test_clocks_delete_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.test_helpers.TestClock.delete("clock_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/test_helpers/test_clocks/clock_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_test_helpers_test_clocks_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.test_helpers.TestClock.list()
        http_client_mock.assert_requested(
            "get",
            path="/v1/test_helpers/test_clocks",
            query_string="",
        )

    def test_test_helpers_test_clocks_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.test_helpers.TestClock.retrieve("clock_xyz")
        http_client_mock.assert_requested(
            "get",
            path="/v1/test_helpers/test_clocks/clock_xyz",
            query_string="",
        )

    def test_test_helpers_test_clocks_get_3(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.test_helpers.TestClock.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/test_helpers/test_clocks",
            query_string="limit=3",
        )

    def test_test_helpers_test_clocks_get_4(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.test_helpers.TestClock.retrieve("clock_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/test_helpers/test_clocks/clock_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_test_helpers_test_clocks_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.test_helpers.TestClock.create(
            frozen_time=123,
            name="cogsworth",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/test_clocks",
            query_string="",
            post_data="frozen_time=123&name=cogsworth",
        )

    def test_test_helpers_test_clocks_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.test_helpers.TestClock.create(frozen_time=1577836800)
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/test_clocks",
            query_string="",
            post_data="frozen_time=1577836800",
        )

    def test_test_helpers_treasury_inbound_transfers_fail_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.InboundTransfer.TestHelpers.fail(
            "ibt_123",
            failure_details={"code": "account_closed"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/treasury/inbound_transfers/ibt_123/fail",
            query_string="",
            post_data="failure_details[code]=account_closed",
        )

    def test_test_helpers_treasury_inbound_transfers_return_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.InboundTransfer.TestHelpers.return_inbound_transfer(
            "ibt_123",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/treasury/inbound_transfers/ibt_123/return",
            query_string="",
        )

    def test_test_helpers_treasury_inbound_transfers_succeed_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.InboundTransfer.TestHelpers.succeed("ibt_123")
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/treasury/inbound_transfers/ibt_123/succeed",
            query_string="",
        )

    def test_test_helpers_treasury_outbound_transfers_fail_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.OutboundTransfer.TestHelpers.fail("obt_123")
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/treasury/outbound_transfers/obt_123/fail",
            query_string="",
        )

    def test_test_helpers_treasury_outbound_transfers_post_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.OutboundTransfer.TestHelpers.post("obt_123")
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/treasury/outbound_transfers/obt_123/post",
            query_string="",
        )

    def test_test_helpers_treasury_outbound_transfers_return_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.OutboundTransfer.TestHelpers.return_outbound_transfer(
            "obt_123",
            returned_details={"code": "account_closed"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/treasury/outbound_transfers/obt_123/return",
            query_string="",
            post_data="returned_details[code]=account_closed",
        )

    def test_test_helpers_treasury_received_credits_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.ReceivedCredit.TestHelpers.create(
            financial_account="fa_123",
            network="ach",
            amount=1234,
            currency="usd",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/treasury/received_credits",
            query_string="",
            post_data="financial_account=fa_123&network=ach&amount=1234&currency=usd",
        )

    def test_test_helpers_treasury_received_debits_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.ReceivedDebit.TestHelpers.create(
            financial_account="fa_123",
            network="ach",
            amount=1234,
            currency="usd",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/test_helpers/treasury/received_debits",
            query_string="",
            post_data="financial_account=fa_123&network=ach&amount=1234&currency=usd",
        )

    def test_tokens_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Token.retrieve("tok_xxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/tokens/tok_xxxx",
            query_string="",
        )

    def test_tokens_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Token.create(
            card={
                "number": "4242424242424242",
                "exp_month": "5",
                "exp_year": "2023",
                "cvc": "314",
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/tokens",
            query_string="",
            post_data="card[number]=4242424242424242&card[exp_month]=5&card[exp_year]=2023&card[cvc]=314",
        )

    def test_tokens_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Token.create(
            bank_account={
                "country": "US",
                "currency": "usd",
                "account_holder_name": "Jenny Rosen",
                "account_holder_type": "individual",
                "routing_number": "110000000",
                "account_number": "000123456789",
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/tokens",
            query_string="",
            post_data="bank_account[country]=US&bank_account[currency]=usd&bank_account[account_holder_name]=Jenny%20Rosen&bank_account[account_holder_type]=individual&bank_account[routing_number]=110000000&bank_account[account_number]=000123456789",
        )

    def test_tokens_post_3(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Token.create(pii={"id_number": "000000000"})
        http_client_mock.assert_requested(
            "post",
            path="/v1/tokens",
            query_string="",
            post_data="pii[id_number]=000000000",
        )

    def test_tokens_post_4(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Token.create(
            account={
                "individual": {"first_name": "Jane", "last_name": "Doe"},
                "tos_shown_and_accepted": True,
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/tokens",
            query_string="",
            post_data="account[individual][first_name]=Jane&account[individual][last_name]=Doe&account[tos_shown_and_accepted]=True",
        )

    def test_tokens_post_5(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Token.create(
            person={
                "first_name": "Jane",
                "last_name": "Doe",
                "relationship": {"owner": True},
            },
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/tokens",
            query_string="",
            post_data="person[first_name]=Jane&person[last_name]=Doe&person[relationship][owner]=True",
        )

    def test_tokens_post_6(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Token.create(cvc_update={"cvc": "123"})
        http_client_mock.assert_requested(
            "post",
            path="/v1/tokens",
            query_string="",
            post_data="cvc_update[cvc]=123",
        )

    def test_topups_cancel_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Topup.cancel("tu_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/topups/tu_xxxxxxxxxxxxx/cancel",
            query_string="",
        )

    def test_topups_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Topup.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/topups",
            query_string="limit=3",
        )

    def test_topups_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Topup.retrieve("tu_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/topups/tu_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_topups_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Topup.create(
            amount=2000,
            currency="usd",
            description="Top-up for Jenny Rosen",
            statement_descriptor="Top-up",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/topups",
            query_string="",
            post_data="amount=2000&currency=usd&description=Top-up%20for%20Jenny%20Rosen&statement_descriptor=Top-up",
        )

    def test_topups_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Topup.modify(
            "tu_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/topups/tu_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_transfers_get(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Transfer.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/transfers",
            query_string="limit=3",
        )

    def test_transfers_get_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Transfer.retrieve("tr_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/transfers/tr_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_transfers_post(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Transfer.create(
            amount=400,
            currency="usd",
            destination="acct_xxxxxxxxxxxxx",
            transfer_group="ORDER_95",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/transfers",
            query_string="",
            post_data="amount=400&currency=usd&destination=acct_xxxxxxxxxxxxx&transfer_group=ORDER_95",
        )

    def test_transfers_post_2(self, http_client_mock: HTTPClientMock) -> None:
        stripe.Transfer.modify(
            "tr_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/transfers/tr_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_transfers_reversals_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Transfer.list_reversals(
            "tr_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/transfers/tr_xxxxxxxxxxxxx/reversals",
            query_string="limit=3",
        )

    def test_transfers_reversals_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Transfer.retrieve_reversal(
            "tr_xxxxxxxxxxxxx",
            "trr_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/transfers/tr_xxxxxxxxxxxxx/reversals/trr_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_transfers_reversals_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Transfer.create_reversal(
            "tr_xxxxxxxxxxxxx",
            amount=100,
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/transfers/tr_xxxxxxxxxxxxx/reversals",
            query_string="",
            post_data="amount=100",
        )

    def test_transfers_reversals_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.Transfer.modify_reversal(
            "tr_xxxxxxxxxxxxx",
            "trr_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/transfers/tr_xxxxxxxxxxxxx/reversals/trr_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_treasury_credit_reversals_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.CreditReversal.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/credit_reversals",
            query_string="financial_account=fa_xxxxxxxxxxxxx&limit=3",
        )

    def test_treasury_credit_reversals_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.CreditReversal.retrieve("credrev_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/credit_reversals/credrev_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_treasury_credit_reversals_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.CreditReversal.create(
            received_credit="rc_xxxxxxxxxxxxx",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/treasury/credit_reversals",
            query_string="",
            post_data="received_credit=rc_xxxxxxxxxxxxx",
        )

    def test_treasury_debit_reversals_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.DebitReversal.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/debit_reversals",
            query_string="financial_account=fa_xxxxxxxxxxxxx&limit=3",
        )

    def test_treasury_debit_reversals_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.DebitReversal.retrieve("debrev_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/debit_reversals/debrev_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_treasury_debit_reversals_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.DebitReversal.create(received_debit="rd_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/treasury/debit_reversals",
            query_string="",
            post_data="received_debit=rd_xxxxxxxxxxxxx",
        )

    def test_treasury_financial_accounts_features_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.FinancialAccount.retrieve_features("fa_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/financial_accounts/fa_xxxxxxxxxxxxx/features",
            query_string="",
        )

    def test_treasury_financial_accounts_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.FinancialAccount.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/financial_accounts",
            query_string="limit=3",
        )

    def test_treasury_financial_accounts_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.FinancialAccount.retrieve("fa_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/financial_accounts/fa_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_treasury_financial_accounts_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.FinancialAccount.create(
            supported_currencies=["usd"],
            features={},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/treasury/financial_accounts",
            query_string="",
            post_data="supported_currencies[0]=usd",
        )

    def test_treasury_financial_accounts_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.FinancialAccount.modify(
            "fa_xxxxxxxxxxxxx",
            metadata={"order_id": "6735"},
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/treasury/financial_accounts/fa_xxxxxxxxxxxxx",
            query_string="",
            post_data="metadata[order_id]=6735",
        )

    def test_treasury_inbound_transfers_cancel_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.InboundTransfer.cancel("ibt_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/treasury/inbound_transfers/ibt_xxxxxxxxxxxxx/cancel",
            query_string="",
        )

    def test_treasury_inbound_transfers_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.InboundTransfer.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/inbound_transfers",
            query_string="financial_account=fa_xxxxxxxxxxxxx&limit=3",
        )

    def test_treasury_inbound_transfers_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.InboundTransfer.retrieve("ibt_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/inbound_transfers/ibt_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_treasury_inbound_transfers_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.InboundTransfer.create(
            financial_account="fa_xxxxxxxxxxxxx",
            amount=10000,
            currency="usd",
            origin_payment_method="pm_xxxxxxxxxxxxx",
            description="InboundTransfer from my bank account",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/treasury/inbound_transfers",
            query_string="",
            post_data="financial_account=fa_xxxxxxxxxxxxx&amount=10000&currency=usd&origin_payment_method=pm_xxxxxxxxxxxxx&description=InboundTransfer%20from%20my%20bank%20account",
        )

    def test_treasury_outbound_payments_cancel_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.OutboundPayment.cancel("bot_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/treasury/outbound_payments/bot_xxxxxxxxxxxxx/cancel",
            query_string="",
        )

    def test_treasury_outbound_payments_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.OutboundPayment.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/outbound_payments",
            query_string="financial_account=fa_xxxxxxxxxxxxx&limit=3",
        )

    def test_treasury_outbound_payments_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.OutboundPayment.retrieve("bot_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/outbound_payments/bot_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_treasury_outbound_payments_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.OutboundPayment.create(
            financial_account="fa_xxxxxxxxxxxxx",
            amount=10000,
            currency="usd",
            customer="cus_xxxxxxxxxxxxx",
            destination_payment_method="pm_xxxxxxxxxxxxx",
            description="OutboundPayment to a 3rd party",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/treasury/outbound_payments",
            query_string="",
            post_data="financial_account=fa_xxxxxxxxxxxxx&amount=10000&currency=usd&customer=cus_xxxxxxxxxxxxx&destination_payment_method=pm_xxxxxxxxxxxxx&description=OutboundPayment%20to%20a%203rd%20party",
        )

    def test_treasury_outbound_transfers_cancel_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.OutboundTransfer.cancel("obt_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "post",
            path="/v1/treasury/outbound_transfers/obt_xxxxxxxxxxxxx/cancel",
            query_string="",
        )

    def test_treasury_outbound_transfers_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.OutboundTransfer.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/outbound_transfers",
            query_string="financial_account=fa_xxxxxxxxxxxxx&limit=3",
        )

    def test_treasury_outbound_transfers_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.OutboundTransfer.retrieve("obt_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/outbound_transfers/obt_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_treasury_outbound_transfers_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.OutboundTransfer.create(
            financial_account="fa_xxxxxxxxxxxxx",
            destination_payment_method="pm_xxxxxxxxxxxxx",
            amount=500,
            currency="usd",
            description="OutboundTransfer to my external bank account",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/treasury/outbound_transfers",
            query_string="",
            post_data="financial_account=fa_xxxxxxxxxxxxx&destination_payment_method=pm_xxxxxxxxxxxxx&amount=500&currency=usd&description=OutboundTransfer%20to%20my%20external%20bank%20account",
        )

    def test_treasury_received_credits_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.ReceivedCredit.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/received_credits",
            query_string="financial_account=fa_xxxxxxxxxxxxx&limit=3",
        )

    def test_treasury_received_credits_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.ReceivedCredit.retrieve("rc_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/received_credits/rc_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_treasury_received_debits_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.ReceivedDebit.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/received_debits",
            query_string="financial_account=fa_xxxxxxxxxxxxx&limit=3",
        )

    def test_treasury_received_debits_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.ReceivedDebit.retrieve("rd_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/received_debits/rd_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_treasury_transaction_entries_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.TransactionEntry.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/transaction_entries",
            query_string="financial_account=fa_xxxxxxxxxxxxx&limit=3",
        )

    def test_treasury_transaction_entries_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.TransactionEntry.retrieve("trxne_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/transaction_entries/trxne_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_treasury_transactions_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.Transaction.list(
            financial_account="fa_xxxxxxxxxxxxx",
            limit=3,
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/transactions",
            query_string="financial_account=fa_xxxxxxxxxxxxx&limit=3",
        )

    def test_treasury_transactions_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.treasury.Transaction.retrieve("trxn_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/treasury/transactions/trxn_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_webhook_endpoints_delete(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.WebhookEndpoint.delete("we_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "delete",
            path="/v1/webhook_endpoints/we_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_webhook_endpoints_get(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.WebhookEndpoint.list(limit=3)
        http_client_mock.assert_requested(
            "get",
            path="/v1/webhook_endpoints",
            query_string="limit=3",
        )

    def test_webhook_endpoints_get_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.WebhookEndpoint.retrieve("we_xxxxxxxxxxxxx")
        http_client_mock.assert_requested(
            "get",
            path="/v1/webhook_endpoints/we_xxxxxxxxxxxxx",
            query_string="",
        )

    def test_webhook_endpoints_post(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.WebhookEndpoint.create(
            url="https://example.com/my/webhook/endpoint",
            enabled_events=["charge.failed", "charge.succeeded"],
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/webhook_endpoints",
            query_string="",
            post_data="url=https%3A%2F%2Fexample.com%2Fmy%2Fwebhook%2Fendpoint&enabled_events[0]=charge.failed&enabled_events[1]=charge.succeeded",
        )

    def test_webhook_endpoints_post_2(
        self, http_client_mock: HTTPClientMock
    ) -> None:
        stripe.WebhookEndpoint.modify(
            "we_xxxxxxxxxxxxx",
            url="https://example.com/new_endpoint",
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/webhook_endpoints/we_xxxxxxxxxxxxx",
            query_string="",
            post_data="url=https%3A%2F%2Fexample.com%2Fnew_endpoint",
        )
