# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.discount import Discount as DiscountResource
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.line_item import LineItem
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.payment_link import PaymentLink
    from stripe.api_resources.setup_intent import SetupIntent
    from stripe.api_resources.shipping_rate import ShippingRate
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.tax_id import TaxId as TaxIdResource
    from stripe.api_resources.tax_rate import TaxRate


class Session(
    CreateableAPIResource["Session"], ListableAPIResource["Session"]
):
    """
    A Checkout Session represents your customer's session as they pay for
    one-time purchases or subscriptions through [Checkout](https://stripe.com/docs/payments/checkout)
    or [Payment Links](https://stripe.com/docs/payments/payment-links). We recommend creating a
    new Session each time your customer attempts to pay.

    Once payment is successful, the Checkout Session will contain a reference
    to the [Customer](https://stripe.com/docs/api/customers), and either the successful
    [PaymentIntent](https://stripe.com/docs/api/payment_intents) or an active
    [Subscription](https://stripe.com/docs/api/subscriptions).

    You can create a Checkout Session on your server and redirect to its URL
    to begin Checkout.

    Related guide: [Checkout quickstart](https://stripe.com/docs/checkout/quickstart)
    """

    OBJECT_NAME = "checkout.session"

    class AfterExpiration(StripeObject):
        class Recovery(StripeObject):
            allow_promotion_codes: bool
            enabled: bool
            expires_at: Optional[int]
            url: Optional[str]

        recovery: Optional[Recovery]
        _inner_class_types = {"recovery": Recovery}

    class AutomaticTax(StripeObject):
        class Liability(StripeObject):
            account: Optional[ExpandableField["Account"]]
            type: Literal["account", "self"]

        enabled: bool
        liability: Optional[Liability]
        status: Optional[
            Literal["complete", "failed", "requires_location_inputs"]
        ]
        _inner_class_types = {"liability": Liability}

    class Consent(StripeObject):
        promotions: Optional[Literal["opt_in", "opt_out"]]
        terms_of_service: Optional[Literal["accepted"]]

    class ConsentCollection(StripeObject):
        promotions: Optional[Literal["auto", "none"]]
        terms_of_service: Optional[Literal["none", "required"]]

    class CurrencyConversion(StripeObject):
        amount_subtotal: int
        amount_total: int
        fx_rate: float
        source_currency: str

    class CustomField(StripeObject):
        class Dropdown(StripeObject):
            class Option(StripeObject):
                label: str
                value: str

            options: List[Option]
            value: Optional[str]
            _inner_class_types = {"options": Option}

        class Label(StripeObject):
            custom: Optional[str]
            type: Literal["custom"]

        class Numeric(StripeObject):
            maximum_length: Optional[int]
            minimum_length: Optional[int]
            value: Optional[str]

        class Text(StripeObject):
            maximum_length: Optional[int]
            minimum_length: Optional[int]
            value: Optional[str]

        dropdown: Optional[Dropdown]
        key: str
        label: Label
        numeric: Optional[Numeric]
        optional: bool
        text: Optional[Text]
        type: Literal["dropdown", "numeric", "text"]
        _inner_class_types = {
            "dropdown": Dropdown,
            "label": Label,
            "numeric": Numeric,
            "text": Text,
        }

    class CustomText(StripeObject):
        class ShippingAddress(StripeObject):
            message: str

        class Submit(StripeObject):
            message: str

        class TermsOfServiceAcceptance(StripeObject):
            message: str

        shipping_address: Optional[ShippingAddress]
        submit: Optional[Submit]
        terms_of_service_acceptance: Optional[TermsOfServiceAcceptance]
        _inner_class_types = {
            "shipping_address": ShippingAddress,
            "submit": Submit,
            "terms_of_service_acceptance": TermsOfServiceAcceptance,
        }

    class CustomerDetails(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            country: Optional[str]
            line1: Optional[str]
            line2: Optional[str]
            postal_code: Optional[str]
            state: Optional[str]

        class TaxId(StripeObject):
            type: Literal[
                "ad_nrt",
                "ae_trn",
                "ar_cuit",
                "au_abn",
                "au_arn",
                "bg_uic",
                "bo_tin",
                "br_cnpj",
                "br_cpf",
                "ca_bn",
                "ca_gst_hst",
                "ca_pst_bc",
                "ca_pst_mb",
                "ca_pst_sk",
                "ca_qst",
                "ch_vat",
                "cl_tin",
                "cn_tin",
                "co_nit",
                "cr_tin",
                "do_rcn",
                "ec_ruc",
                "eg_tin",
                "es_cif",
                "eu_oss_vat",
                "eu_vat",
                "gb_vat",
                "ge_vat",
                "hk_br",
                "hu_tin",
                "id_npwp",
                "il_vat",
                "in_gst",
                "is_vat",
                "jp_cn",
                "jp_rn",
                "jp_trn",
                "ke_pin",
                "kr_brn",
                "li_uid",
                "mx_rfc",
                "my_frp",
                "my_itn",
                "my_sst",
                "no_vat",
                "nz_gst",
                "pe_ruc",
                "ph_tin",
                "ro_tin",
                "rs_pib",
                "ru_inn",
                "ru_kpp",
                "sa_vat",
                "sg_gst",
                "sg_uen",
                "si_tin",
                "sv_nit",
                "th_vat",
                "tr_tin",
                "tw_vat",
                "ua_vat",
                "unknown",
                "us_ein",
                "uy_ruc",
                "ve_rif",
                "vn_tin",
                "za_vat",
            ]
            value: Optional[str]

        address: Optional[Address]
        email: Optional[str]
        name: Optional[str]
        phone: Optional[str]
        tax_exempt: Optional[Literal["exempt", "none", "reverse"]]
        tax_ids: Optional[List[TaxId]]
        _inner_class_types = {"address": Address, "tax_ids": TaxId}

    class InvoiceCreation(StripeObject):
        class InvoiceData(StripeObject):
            class CustomField(StripeObject):
                name: str
                value: str

            class Issuer(StripeObject):
                account: Optional[ExpandableField["Account"]]
                type: Literal["account", "self"]

            class RenderingOptions(StripeObject):
                amount_tax_display: Optional[str]

            account_tax_ids: Optional[List[ExpandableField["TaxIdResource"]]]
            custom_fields: Optional[List[CustomField]]
            description: Optional[str]
            footer: Optional[str]
            issuer: Optional[Issuer]
            metadata: Optional[Dict[str, str]]
            rendering_options: Optional[RenderingOptions]
            _inner_class_types = {
                "custom_fields": CustomField,
                "issuer": Issuer,
                "rendering_options": RenderingOptions,
            }

        enabled: bool
        invoice_data: InvoiceData
        _inner_class_types = {"invoice_data": InvoiceData}

    class PaymentMethodConfigurationDetails(StripeObject):
        id: str
        parent: Optional[str]

    class PaymentMethodOptions(StripeObject):
        class AcssDebit(StripeObject):
            class MandateOptions(StripeObject):
                custom_mandate_url: Optional[str]
                default_for: Optional[List[Literal["invoice", "subscription"]]]
                interval_description: Optional[str]
                payment_schedule: Optional[
                    Literal["combined", "interval", "sporadic"]
                ]
                transaction_type: Optional[Literal["business", "personal"]]

            currency: Optional[Literal["cad", "usd"]]
            mandate_options: Optional[MandateOptions]
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]
            verification_method: Optional[
                Literal["automatic", "instant", "microdeposits"]
            ]
            _inner_class_types = {"mandate_options": MandateOptions}

        class Affirm(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class AfterpayClearpay(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Alipay(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class AuBecsDebit(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class BacsDebit(StripeObject):
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]

        class Bancontact(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Boleto(StripeObject):
            expires_after_days: int
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]

        class Card(StripeObject):
            class Installments(StripeObject):
                enabled: Optional[bool]

            installments: Optional[Installments]
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]
            statement_descriptor_suffix_kana: Optional[str]
            statement_descriptor_suffix_kanji: Optional[str]
            _inner_class_types = {"installments": Installments}

        class Cashapp(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class CustomerBalance(StripeObject):
            class BankTransfer(StripeObject):
                class EuBankTransfer(StripeObject):
                    country: Literal["BE", "DE", "ES", "FR", "IE", "NL"]

                eu_bank_transfer: Optional[EuBankTransfer]
                requested_address_types: Optional[
                    List[
                        Literal[
                            "aba",
                            "iban",
                            "sepa",
                            "sort_code",
                            "spei",
                            "swift",
                            "zengin",
                        ]
                    ]
                ]
                type: Optional[
                    Literal[
                        "eu_bank_transfer",
                        "gb_bank_transfer",
                        "jp_bank_transfer",
                        "mx_bank_transfer",
                        "us_bank_transfer",
                    ]
                ]
                _inner_class_types = {"eu_bank_transfer": EuBankTransfer}

            bank_transfer: Optional[BankTransfer]
            funding_type: Optional[Literal["bank_transfer"]]
            setup_future_usage: Optional[Literal["none"]]
            _inner_class_types = {"bank_transfer": BankTransfer}

        class Eps(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Fpx(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Giropay(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Grabpay(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Ideal(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Klarna(StripeObject):
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]

        class Konbini(StripeObject):
            expires_after_days: Optional[int]
            setup_future_usage: Optional[Literal["none"]]

        class Link(StripeObject):
            setup_future_usage: Optional[Literal["none", "off_session"]]

        class Oxxo(StripeObject):
            expires_after_days: int
            setup_future_usage: Optional[Literal["none"]]

        class P24(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Paynow(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Pix(StripeObject):
            expires_after_seconds: Optional[int]

        class SepaDebit(StripeObject):
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]

        class Sofort(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class UsBankAccount(StripeObject):
            class FinancialConnections(StripeObject):
                class ManualEntry(StripeObject):
                    mode: Optional[Literal["automatic", "custom"]]

                manual_entry: Optional[ManualEntry]
                permissions: Optional[
                    List[
                        Literal[
                            "balances",
                            "ownership",
                            "payment_method",
                            "transactions",
                        ]
                    ]
                ]
                prefetch: Optional[
                    List[
                        Literal[
                            "balances",
                            "inferred_balances",
                            "ownership",
                            "transactions",
                        ]
                    ]
                ]
                return_url: Optional[str]
                _inner_class_types = {"manual_entry": ManualEntry}

            financial_connections: Optional[FinancialConnections]
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]
            verification_method: Optional[Literal["automatic", "instant"]]
            _inner_class_types = {
                "financial_connections": FinancialConnections
            }

        acss_debit: Optional[AcssDebit]
        affirm: Optional[Affirm]
        afterpay_clearpay: Optional[AfterpayClearpay]
        alipay: Optional[Alipay]
        au_becs_debit: Optional[AuBecsDebit]
        bacs_debit: Optional[BacsDebit]
        bancontact: Optional[Bancontact]
        boleto: Optional[Boleto]
        card: Optional[Card]
        cashapp: Optional[Cashapp]
        customer_balance: Optional[CustomerBalance]
        eps: Optional[Eps]
        fpx: Optional[Fpx]
        giropay: Optional[Giropay]
        grabpay: Optional[Grabpay]
        ideal: Optional[Ideal]
        klarna: Optional[Klarna]
        konbini: Optional[Konbini]
        link: Optional[Link]
        oxxo: Optional[Oxxo]
        p24: Optional[P24]
        paynow: Optional[Paynow]
        pix: Optional[Pix]
        sepa_debit: Optional[SepaDebit]
        sofort: Optional[Sofort]
        us_bank_account: Optional[UsBankAccount]
        _inner_class_types = {
            "acss_debit": AcssDebit,
            "affirm": Affirm,
            "afterpay_clearpay": AfterpayClearpay,
            "alipay": Alipay,
            "au_becs_debit": AuBecsDebit,
            "bacs_debit": BacsDebit,
            "bancontact": Bancontact,
            "boleto": Boleto,
            "card": Card,
            "cashapp": Cashapp,
            "customer_balance": CustomerBalance,
            "eps": Eps,
            "fpx": Fpx,
            "giropay": Giropay,
            "grabpay": Grabpay,
            "ideal": Ideal,
            "klarna": Klarna,
            "konbini": Konbini,
            "link": Link,
            "oxxo": Oxxo,
            "p24": P24,
            "paynow": Paynow,
            "pix": Pix,
            "sepa_debit": SepaDebit,
            "sofort": Sofort,
            "us_bank_account": UsBankAccount,
        }

    class PhoneNumberCollection(StripeObject):
        enabled: bool

    class ShippingAddressCollection(StripeObject):
        allowed_countries: List[
            Literal[
                "AC",
                "AD",
                "AE",
                "AF",
                "AG",
                "AI",
                "AL",
                "AM",
                "AO",
                "AQ",
                "AR",
                "AT",
                "AU",
                "AW",
                "AX",
                "AZ",
                "BA",
                "BB",
                "BD",
                "BE",
                "BF",
                "BG",
                "BH",
                "BI",
                "BJ",
                "BL",
                "BM",
                "BN",
                "BO",
                "BQ",
                "BR",
                "BS",
                "BT",
                "BV",
                "BW",
                "BY",
                "BZ",
                "CA",
                "CD",
                "CF",
                "CG",
                "CH",
                "CI",
                "CK",
                "CL",
                "CM",
                "CN",
                "CO",
                "CR",
                "CV",
                "CW",
                "CY",
                "CZ",
                "DE",
                "DJ",
                "DK",
                "DM",
                "DO",
                "DZ",
                "EC",
                "EE",
                "EG",
                "EH",
                "ER",
                "ES",
                "ET",
                "FI",
                "FJ",
                "FK",
                "FO",
                "FR",
                "GA",
                "GB",
                "GD",
                "GE",
                "GF",
                "GG",
                "GH",
                "GI",
                "GL",
                "GM",
                "GN",
                "GP",
                "GQ",
                "GR",
                "GS",
                "GT",
                "GU",
                "GW",
                "GY",
                "HK",
                "HN",
                "HR",
                "HT",
                "HU",
                "ID",
                "IE",
                "IL",
                "IM",
                "IN",
                "IO",
                "IQ",
                "IS",
                "IT",
                "JE",
                "JM",
                "JO",
                "JP",
                "KE",
                "KG",
                "KH",
                "KI",
                "KM",
                "KN",
                "KR",
                "KW",
                "KY",
                "KZ",
                "LA",
                "LB",
                "LC",
                "LI",
                "LK",
                "LR",
                "LS",
                "LT",
                "LU",
                "LV",
                "LY",
                "MA",
                "MC",
                "MD",
                "ME",
                "MF",
                "MG",
                "MK",
                "ML",
                "MM",
                "MN",
                "MO",
                "MQ",
                "MR",
                "MS",
                "MT",
                "MU",
                "MV",
                "MW",
                "MX",
                "MY",
                "MZ",
                "NA",
                "NC",
                "NE",
                "NG",
                "NI",
                "NL",
                "NO",
                "NP",
                "NR",
                "NU",
                "NZ",
                "OM",
                "PA",
                "PE",
                "PF",
                "PG",
                "PH",
                "PK",
                "PL",
                "PM",
                "PN",
                "PR",
                "PS",
                "PT",
                "PY",
                "QA",
                "RE",
                "RO",
                "RS",
                "RU",
                "RW",
                "SA",
                "SB",
                "SC",
                "SE",
                "SG",
                "SH",
                "SI",
                "SJ",
                "SK",
                "SL",
                "SM",
                "SN",
                "SO",
                "SR",
                "SS",
                "ST",
                "SV",
                "SX",
                "SZ",
                "TA",
                "TC",
                "TD",
                "TF",
                "TG",
                "TH",
                "TJ",
                "TK",
                "TL",
                "TM",
                "TN",
                "TO",
                "TR",
                "TT",
                "TV",
                "TW",
                "TZ",
                "UA",
                "UG",
                "US",
                "UY",
                "UZ",
                "VA",
                "VC",
                "VE",
                "VG",
                "VN",
                "VU",
                "WF",
                "WS",
                "XK",
                "YE",
                "YT",
                "ZA",
                "ZM",
                "ZW",
                "ZZ",
            ]
        ]

    class ShippingCost(StripeObject):
        class Tax(StripeObject):
            amount: int
            rate: "TaxRate"
            taxability_reason: Optional[
                Literal[
                    "customer_exempt",
                    "not_collecting",
                    "not_subject_to_tax",
                    "not_supported",
                    "portion_product_exempt",
                    "portion_reduced_rated",
                    "portion_standard_rated",
                    "product_exempt",
                    "product_exempt_holiday",
                    "proportionally_rated",
                    "reduced_rated",
                    "reverse_charge",
                    "standard_rated",
                    "taxable_basis_reduced",
                    "zero_rated",
                ]
            ]
            taxable_amount: Optional[int]

        amount_subtotal: int
        amount_tax: int
        amount_total: int
        shipping_rate: Optional[ExpandableField["ShippingRate"]]
        taxes: Optional[List[Tax]]
        _inner_class_types = {"taxes": Tax}

    class ShippingDetails(StripeObject):
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

    class ShippingOption(StripeObject):
        shipping_amount: int
        shipping_rate: ExpandableField["ShippingRate"]

    class TaxIdCollection(StripeObject):
        enabled: bool

    class TotalDetails(StripeObject):
        class Breakdown(StripeObject):
            class Discount(StripeObject):
                amount: int
                discount: "DiscountResource"

            class Tax(StripeObject):
                amount: int
                rate: "TaxRate"
                taxability_reason: Optional[
                    Literal[
                        "customer_exempt",
                        "not_collecting",
                        "not_subject_to_tax",
                        "not_supported",
                        "portion_product_exempt",
                        "portion_reduced_rated",
                        "portion_standard_rated",
                        "product_exempt",
                        "product_exempt_holiday",
                        "proportionally_rated",
                        "reduced_rated",
                        "reverse_charge",
                        "standard_rated",
                        "taxable_basis_reduced",
                        "zero_rated",
                    ]
                ]
                taxable_amount: Optional[int]

            discounts: List[Discount]
            taxes: List[Tax]
            _inner_class_types = {"discounts": Discount, "taxes": Tax}

        amount_discount: int
        amount_shipping: Optional[int]
        amount_tax: int
        breakdown: Optional[Breakdown]
        _inner_class_types = {"breakdown": Breakdown}

    after_expiration: Optional[AfterExpiration]
    allow_promotion_codes: Optional[bool]
    amount_subtotal: Optional[int]
    amount_total: Optional[int]
    automatic_tax: AutomaticTax
    billing_address_collection: Optional[Literal["auto", "required"]]
    cancel_url: Optional[str]
    client_reference_id: Optional[str]
    client_secret: Optional[str]
    consent: Optional[Consent]
    consent_collection: Optional[ConsentCollection]
    created: int
    currency: Optional[str]
    currency_conversion: Optional[CurrencyConversion]
    custom_fields: List[CustomField]
    custom_text: CustomText
    customer: Optional[ExpandableField["Customer"]]
    customer_creation: Optional[Literal["always", "if_required"]]
    customer_details: Optional[CustomerDetails]
    customer_email: Optional[str]
    expires_at: int
    id: str
    invoice: Optional[ExpandableField["Invoice"]]
    invoice_creation: Optional[InvoiceCreation]
    line_items: Optional[ListObject["LineItem"]]
    livemode: bool
    locale: Optional[
        Literal[
            "auto",
            "bg",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "en-GB",
            "es",
            "es-419",
            "et",
            "fi",
            "fil",
            "fr",
            "fr-CA",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ko",
            "lt",
            "lv",
            "ms",
            "mt",
            "nb",
            "nl",
            "pl",
            "pt",
            "pt-BR",
            "ro",
            "ru",
            "sk",
            "sl",
            "sv",
            "th",
            "tr",
            "vi",
            "zh",
            "zh-HK",
            "zh-TW",
        ]
    ]
    metadata: Optional[Dict[str, str]]
    mode: Literal["payment", "setup", "subscription"]
    object: Literal["checkout.session"]
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    payment_link: Optional[ExpandableField["PaymentLink"]]
    payment_method_collection: Optional[Literal["always", "if_required"]]
    payment_method_configuration_details: Optional[
        PaymentMethodConfigurationDetails
    ]
    payment_method_options: Optional[PaymentMethodOptions]
    payment_method_types: List[str]
    payment_status: Literal["no_payment_required", "paid", "unpaid"]
    phone_number_collection: Optional[PhoneNumberCollection]
    recovered_from: Optional[str]
    redirect_on_completion: Optional[Literal["always", "if_required", "never"]]
    return_url: Optional[str]
    setup_intent: Optional[ExpandableField["SetupIntent"]]
    shipping_address_collection: Optional[ShippingAddressCollection]
    shipping_cost: Optional[ShippingCost]
    shipping_details: Optional[ShippingDetails]
    shipping_options: List[ShippingOption]
    status: Optional[Literal["complete", "expired", "open"]]
    submit_type: Optional[Literal["auto", "book", "donate", "pay"]]
    subscription: Optional[ExpandableField["Subscription"]]
    success_url: Optional[str]
    tax_id_collection: Optional[TaxIdCollection]
    total_details: Optional[TotalDetails]
    ui_mode: Optional[Literal["embedded", "hosted"]]
    url: Optional[str]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Session":
        return cast(
            "Session",
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
    def _cls_expire(
        cls,
        session: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/checkout/sessions/{session}/expire".format(
                session=util.sanitize_id(session)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_expire")
    def expire(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/checkout/sessions/{session}/expire".format(
                session=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["Session"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def _cls_list_line_items(
        cls,
        session: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/checkout/sessions/{session}/line_items".format(
                session=util.sanitize_id(session)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "get",
            "/v1/checkout/sessions/{session}/line_items".format(
                session=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Session":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "after_expiration": AfterExpiration,
        "automatic_tax": AutomaticTax,
        "consent": Consent,
        "consent_collection": ConsentCollection,
        "currency_conversion": CurrencyConversion,
        "custom_fields": CustomField,
        "custom_text": CustomText,
        "customer_details": CustomerDetails,
        "invoice_creation": InvoiceCreation,
        "payment_method_configuration_details": PaymentMethodConfigurationDetails,
        "payment_method_options": PaymentMethodOptions,
        "phone_number_collection": PhoneNumberCollection,
        "shipping_address_collection": ShippingAddressCollection,
        "shipping_cost": ShippingCost,
        "shipping_details": ShippingDetails,
        "shipping_options": ShippingOption,
        "tax_id_collection": TaxIdCollection,
        "total_details": TotalDetails,
    }
