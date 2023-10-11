# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import error, util
from stripe.api_resources import Customer
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    UpdateableAPIResource,
)
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus


class Source(CreateableAPIResource["Source"], UpdateableAPIResource["Source"]):
    """
    `Source` objects allow you to accept a variety of payment methods. They
    represent a customer's payment instrument, and can be used with the Stripe API
    just like a `Card` object: once chargeable, they can be charged, or can be
    attached to customers.

    Stripe doesn't recommend using the deprecated [Sources API](https://stripe.com/docs/api/sources).
    We recommend that you adopt the [PaymentMethods API](https://stripe.com/docs/api/payment_methods).
    This newer API provides access to our latest features and payment method types.

    Related guides: [Sources API](https://stripe.com/docs/sources) and [Sources & Customers](https://stripe.com/docs/sources/customers).
    """

    OBJECT_NAME = "source"

    class AchCreditTransfer(StripeObject):
        account_number: Optional[str]
        bank_name: Optional[str]
        fingerprint: Optional[str]
        refund_account_holder_name: Optional[str]
        refund_account_holder_type: Optional[str]
        refund_routing_number: Optional[str]
        routing_number: Optional[str]
        swift_code: Optional[str]

    class AchDebit(StripeObject):
        bank_name: Optional[str]
        country: Optional[str]
        fingerprint: Optional[str]
        last4: Optional[str]
        routing_number: Optional[str]
        type: Optional[str]

    class AcssDebit(StripeObject):
        bank_address_city: Optional[str]
        bank_address_line_1: Optional[str]
        bank_address_line_2: Optional[str]
        bank_address_postal_code: Optional[str]
        bank_name: Optional[str]
        category: Optional[str]
        country: Optional[str]
        fingerprint: Optional[str]
        last4: Optional[str]
        routing_number: Optional[str]

    class Alipay(StripeObject):
        data_string: Optional[str]
        native_url: Optional[str]
        statement_descriptor: Optional[str]

    class AuBecsDebit(StripeObject):
        bsb_number: Optional[str]
        fingerprint: Optional[str]
        last4: Optional[str]

    class Bancontact(StripeObject):
        bank_code: Optional[str]
        bank_name: Optional[str]
        bic: Optional[str]
        iban_last4: Optional[str]
        preferred_language: Optional[str]
        statement_descriptor: Optional[str]

    class Card(StripeObject):
        address_line1_check: Optional[str]
        address_zip_check: Optional[str]
        brand: Optional[str]
        country: Optional[str]
        cvc_check: Optional[str]
        description: Optional[str]
        dynamic_last4: Optional[str]
        exp_month: Optional[int]
        exp_year: Optional[int]
        fingerprint: Optional[str]
        funding: Optional[str]
        iin: Optional[str]
        issuer: Optional[str]
        last4: Optional[str]
        name: Optional[str]
        three_d_secure: Optional[str]
        tokenization_method: Optional[str]

    class CardPresent(StripeObject):
        application_cryptogram: Optional[str]
        application_preferred_name: Optional[str]
        authorization_code: Optional[str]
        authorization_response_code: Optional[str]
        brand: Optional[str]
        country: Optional[str]
        cvm_type: Optional[str]
        data_type: Optional[str]
        dedicated_file_name: Optional[str]
        description: Optional[str]
        emv_auth_data: Optional[str]
        evidence_customer_signature: Optional[str]
        evidence_transaction_certificate: Optional[str]
        exp_month: Optional[int]
        exp_year: Optional[int]
        fingerprint: Optional[str]
        funding: Optional[str]
        iin: Optional[str]
        issuer: Optional[str]
        last4: Optional[str]
        pos_device_id: Optional[str]
        pos_entry_mode: Optional[str]
        read_method: Optional[str]
        reader: Optional[str]
        terminal_verification_results: Optional[str]
        transaction_status_information: Optional[str]

    class CodeVerification(StripeObject):
        attempts_remaining: int
        status: str

    class Eps(StripeObject):
        reference: Optional[str]
        statement_descriptor: Optional[str]

    class Giropay(StripeObject):
        bank_code: Optional[str]
        bank_name: Optional[str]
        bic: Optional[str]
        statement_descriptor: Optional[str]

    class Ideal(StripeObject):
        bank: Optional[str]
        bic: Optional[str]
        iban_last4: Optional[str]
        statement_descriptor: Optional[str]

    class Klarna(StripeObject):
        background_image_url: Optional[str]
        client_token: Optional[str]
        first_name: Optional[str]
        last_name: Optional[str]
        locale: Optional[str]
        logo_url: Optional[str]
        page_title: Optional[str]
        pay_later_asset_urls_descriptive: Optional[str]
        pay_later_asset_urls_standard: Optional[str]
        pay_later_name: Optional[str]
        pay_later_redirect_url: Optional[str]
        pay_now_asset_urls_descriptive: Optional[str]
        pay_now_asset_urls_standard: Optional[str]
        pay_now_name: Optional[str]
        pay_now_redirect_url: Optional[str]
        pay_over_time_asset_urls_descriptive: Optional[str]
        pay_over_time_asset_urls_standard: Optional[str]
        pay_over_time_name: Optional[str]
        pay_over_time_redirect_url: Optional[str]
        payment_method_categories: Optional[str]
        purchase_country: Optional[str]
        purchase_type: Optional[str]
        redirect_url: Optional[str]
        shipping_delay: Optional[int]
        shipping_first_name: Optional[str]
        shipping_last_name: Optional[str]

    class Multibanco(StripeObject):
        entity: Optional[str]
        reference: Optional[str]
        refund_account_holder_address_city: Optional[str]
        refund_account_holder_address_country: Optional[str]
        refund_account_holder_address_line1: Optional[str]
        refund_account_holder_address_line2: Optional[str]
        refund_account_holder_address_postal_code: Optional[str]
        refund_account_holder_address_state: Optional[str]
        refund_account_holder_name: Optional[str]
        refund_iban: Optional[str]

    class Owner(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            country: Optional[str]
            line1: Optional[str]
            line2: Optional[str]
            postal_code: Optional[str]
            state: Optional[str]

        class VerifiedAddress(StripeObject):
            city: Optional[str]
            country: Optional[str]
            line1: Optional[str]
            line2: Optional[str]
            postal_code: Optional[str]
            state: Optional[str]

        address: Optional[Address]
        email: Optional[str]
        name: Optional[str]
        phone: Optional[str]
        verified_address: Optional[VerifiedAddress]
        verified_email: Optional[str]
        verified_name: Optional[str]
        verified_phone: Optional[str]
        _inner_class_types = {
            "address": Address,
            "verified_address": VerifiedAddress,
        }

    class P24(StripeObject):
        reference: Optional[str]

    class Paypal(StripeObject):
        billing_agreement: Optional[str]
        fingerprint: Optional[str]
        payer_id: Optional[str]
        reference_id: Optional[str]
        reference_transaction_amount: Optional[str]
        reference_transaction_charged: Optional[bool]
        statement_descriptor: Optional[str]
        transaction_id: Optional[str]
        verified_email: Optional[str]

    class Receiver(StripeObject):
        address: Optional[str]
        amount_charged: int
        amount_received: int
        amount_returned: int
        refund_attributes_method: str
        refund_attributes_status: str

    class Redirect(StripeObject):
        failure_reason: Optional[str]
        return_url: str
        status: str
        url: str

    class SepaCreditTransfer(StripeObject):
        bank_name: Optional[str]
        bic: Optional[str]
        iban: Optional[str]
        refund_account_holder_address_city: Optional[str]
        refund_account_holder_address_country: Optional[str]
        refund_account_holder_address_line1: Optional[str]
        refund_account_holder_address_line2: Optional[str]
        refund_account_holder_address_postal_code: Optional[str]
        refund_account_holder_address_state: Optional[str]
        refund_account_holder_name: Optional[str]
        refund_iban: Optional[str]

    class SepaDebit(StripeObject):
        bank_code: Optional[str]
        branch_code: Optional[str]
        country: Optional[str]
        fingerprint: Optional[str]
        last4: Optional[str]
        mandate_reference: Optional[str]
        mandate_url: Optional[str]

    class Sofort(StripeObject):
        bank_code: Optional[str]
        bank_name: Optional[str]
        bic: Optional[str]
        country: Optional[str]
        iban_last4: Optional[str]
        preferred_language: Optional[str]
        statement_descriptor: Optional[str]

    class SourceOrder(StripeObject):
        class Item(StripeObject):
            amount: Optional[int]
            currency: Optional[str]
            description: Optional[str]
            parent: Optional[str]
            quantity: Optional[int]
            type: Optional[str]

        class Shipping(StripeObject):
            class Address(StripeObject):
                city: Optional[str]
                country: Optional[str]
                line1: Optional[str]
                line2: Optional[str]
                postal_code: Optional[str]
                state: Optional[str]

            address: Optional[Address]
            carrier: Optional[str]
            name: Optional[str]
            phone: Optional[str]
            tracking_number: Optional[str]
            _inner_class_types = {"address": Address}

        amount: int
        currency: str
        email: Optional[str]
        items: Optional[List[Item]]
        shipping: Optional[Shipping]
        _inner_class_types = {"items": Item, "shipping": Shipping}

    class ThreeDSecure(StripeObject):
        address_line1_check: Optional[str]
        address_zip_check: Optional[str]
        authenticated: Optional[bool]
        brand: Optional[str]
        card: Optional[str]
        country: Optional[str]
        customer: Optional[str]
        cvc_check: Optional[str]
        description: Optional[str]
        dynamic_last4: Optional[str]
        exp_month: Optional[int]
        exp_year: Optional[int]
        fingerprint: Optional[str]
        funding: Optional[str]
        iin: Optional[str]
        issuer: Optional[str]
        last4: Optional[str]
        name: Optional[str]
        three_d_secure: Optional[str]
        tokenization_method: Optional[str]

    class Wechat(StripeObject):
        prepay_id: Optional[str]
        qr_code_url: Optional[str]
        statement_descriptor: Optional[str]

    ach_credit_transfer: Optional[AchCreditTransfer]
    ach_debit: Optional[AchDebit]
    acss_debit: Optional[AcssDebit]
    alipay: Optional[Alipay]
    amount: Optional[int]
    au_becs_debit: Optional[AuBecsDebit]
    bancontact: Optional[Bancontact]
    card: Optional[Card]
    card_present: Optional[CardPresent]
    client_secret: str
    code_verification: Optional[CodeVerification]
    created: int
    currency: Optional[str]
    customer: Optional[str]
    eps: Optional[Eps]
    flow: str
    giropay: Optional[Giropay]
    id: str
    ideal: Optional[Ideal]
    klarna: Optional[Klarna]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    multibanco: Optional[Multibanco]
    object: Literal["source"]
    owner: Optional[Owner]
    p24: Optional[P24]
    paypal: Optional[Paypal]
    receiver: Optional[Receiver]
    redirect: Optional[Redirect]
    sepa_credit_transfer: Optional[SepaCreditTransfer]
    sepa_debit: Optional[SepaDebit]
    sofort: Optional[Sofort]
    source_order: Optional[SourceOrder]
    statement_descriptor: Optional[str]
    status: str
    three_d_secure: Optional[ThreeDSecure]
    type: Literal[
        "ach_credit_transfer",
        "ach_debit",
        "acss_debit",
        "alipay",
        "au_becs_debit",
        "bancontact",
        "card",
        "card_present",
        "eps",
        "giropay",
        "ideal",
        "klarna",
        "multibanco",
        "p24",
        "paypal",
        "sepa_credit_transfer",
        "sepa_debit",
        "sofort",
        "three_d_secure",
        "wechat",
    ]
    usage: Optional[str]
    wechat: Optional[Wechat]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Source":
        return cast(
            "Source",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def _cls_list_source_transactions(
        cls,
        source: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/sources/{source}/source_transactions".format(
                source=util.sanitize_id(source)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_source_transactions")
    def list_source_transactions(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "get",
            "/v1/sources/{source}/source_transactions".format(
                source=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def modify(cls, id, **params: Any) -> "Source":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Source",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Source":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_verify(
        cls,
        source: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/sources/{source}/verify".format(
                source=util.sanitize_id(source)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_verify")
    def verify(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/sources/{source}/verify".format(
                source=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def detach(self, idempotency_key=None, **params):
        token = self.id

        if hasattr(self, "customer") and self.customer:
            extn = quote_plus(token)
            customer = self.customer
            base = Customer.class_url()
            owner_extn = quote_plus(customer)
            url = "%s/%s/sources/%s" % (base, owner_extn, extn)
            headers = util.populate_headers(idempotency_key)

            self.refresh_from(self.request("delete", url, params, headers))
            return self

        else:
            raise error.InvalidRequestError(
                "Source %s does not appear to be currently attached "
                "to a customer object." % token,
                "id",
            )

    _inner_class_types = {
        "ach_credit_transfer": AchCreditTransfer,
        "ach_debit": AchDebit,
        "acss_debit": AcssDebit,
        "alipay": Alipay,
        "au_becs_debit": AuBecsDebit,
        "bancontact": Bancontact,
        "card": Card,
        "card_present": CardPresent,
        "code_verification": CodeVerification,
        "eps": Eps,
        "giropay": Giropay,
        "ideal": Ideal,
        "klarna": Klarna,
        "multibanco": Multibanco,
        "owner": Owner,
        "p24": P24,
        "paypal": Paypal,
        "receiver": Receiver,
        "redirect": Redirect,
        "sepa_credit_transfer": SepaCreditTransfer,
        "sepa_debit": SepaDebit,
        "sofort": Sofort,
        "source_order": SourceOrder,
        "three_d_secure": ThreeDSecure,
        "wechat": Wechat,
    }
