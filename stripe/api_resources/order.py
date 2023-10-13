# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.discount import Discount as DiscountResource
    from stripe.api_resources.line_item import LineItem
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.shipping_rate import ShippingRate
    from stripe.api_resources.tax_rate import TaxRate


class Order(
    CreateableAPIResource["Order"],
    ListableAPIResource["Order"],
    UpdateableAPIResource["Order"],
):
    """
    An Order describes a purchase being made by a customer, including the
    products & quantities being purchased, the order status, the payment information,
    and the billing/shipping details.

    Related guide: [Orders overview](https://stripe.com/docs/orders)
    """

    OBJECT_NAME = "order"

    class AutomaticTax(StripeObject):
        enabled: bool
        status: Optional[
            Literal["complete", "failed", "requires_location_inputs"]
        ]

    class BillingDetails(StripeObject):
        class Address(StripeObject):
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
        _inner_class_types = {"address": Address}

    class Credit(StripeObject):
        class GiftCard(StripeObject):
            card: str

        amount: int
        gift_card: Optional[GiftCard]
        ineligible_line_items: Optional[List[str]]
        type: Literal["gift_card"]
        _inner_class_types = {"gift_card": GiftCard}

    class Payment(StripeObject):
        class Settings(StripeObject):
            class AutomaticPaymentMethods(StripeObject):
                enabled: bool

            class PaymentMethodOptions(StripeObject):
                class AcssDebit(StripeObject):
                    class MandateOptions(StripeObject):
                        custom_mandate_url: Optional[str]
                        interval_description: Optional[str]
                        payment_schedule: Optional[
                            Literal["combined", "interval", "sporadic"]
                        ]
                        transaction_type: Optional[
                            Literal["business", "personal"]
                        ]

                    mandate_options: Optional[MandateOptions]
                    setup_future_usage: Optional[
                        Literal["none", "off_session", "on_session"]
                    ]
                    verification_method: Optional[
                        Literal["automatic", "instant", "microdeposits"]
                    ]
                    _inner_class_types = {"mandate_options": MandateOptions}

                class AfterpayClearpay(StripeObject):
                    capture_method: Optional[
                        Literal["automatic", "automatic_async", "manual"]
                    ]
                    reference: Optional[str]
                    setup_future_usage: Optional[Literal["none"]]

                class Alipay(StripeObject):
                    setup_future_usage: Optional[
                        Literal["none", "off_session"]
                    ]

                class Bancontact(StripeObject):
                    preferred_language: Literal["de", "en", "fr", "nl"]
                    setup_future_usage: Optional[
                        Literal["none", "off_session"]
                    ]

                class Card(StripeObject):
                    capture_method: Literal[
                        "automatic", "automatic_async", "manual"
                    ]
                    setup_future_usage: Optional[
                        Literal["none", "off_session", "on_session"]
                    ]

                class CustomerBalance(StripeObject):
                    class BankTransfer(StripeObject):
                        class EuBankTransfer(StripeObject):
                            country: Literal[
                                "BE", "DE", "ES", "FR", "IE", "NL"
                            ]

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
                        _inner_class_types = {
                            "eu_bank_transfer": EuBankTransfer,
                        }

                    bank_transfer: Optional[BankTransfer]
                    funding_type: Optional[Literal["bank_transfer"]]
                    setup_future_usage: Optional[Literal["none"]]
                    _inner_class_types = {"bank_transfer": BankTransfer}

                class Ideal(StripeObject):
                    setup_future_usage: Optional[
                        Literal["none", "off_session"]
                    ]

                class Klarna(StripeObject):
                    capture_method: Optional[Literal["manual"]]
                    preferred_locale: Optional[str]
                    setup_future_usage: Optional[Literal["none"]]

                class Link(StripeObject):
                    capture_method: Optional[Literal["manual"]]
                    persistent_token: Optional[str]
                    setup_future_usage: Optional[
                        Literal["none", "off_session"]
                    ]

                class Oxxo(StripeObject):
                    expires_after_days: int
                    setup_future_usage: Optional[Literal["none"]]

                class P24(StripeObject):
                    setup_future_usage: Optional[Literal["none"]]

                class Paypal(StripeObject):
                    capture_method: Optional[Literal["manual"]]
                    preferred_locale: Optional[str]
                    reference: Optional[str]
                    reference_id: Optional[str]
                    setup_future_usage: Optional[
                        Literal["none", "off_session"]
                    ]

                class SepaDebit(StripeObject):
                    class MandateOptions(StripeObject):
                        pass

                    mandate_options: Optional[MandateOptions]
                    setup_future_usage: Optional[
                        Literal["none", "off_session", "on_session"]
                    ]
                    _inner_class_types = {"mandate_options": MandateOptions}

                class Sofort(StripeObject):
                    preferred_language: Optional[
                        Literal["de", "en", "es", "fr", "it", "nl", "pl"]
                    ]
                    setup_future_usage: Optional[
                        Literal["none", "off_session"]
                    ]

                class WechatPay(StripeObject):
                    app_id: Optional[str]
                    client: Optional[Literal["android", "ios", "web"]]
                    setup_future_usage: Optional[Literal["none"]]

                acss_debit: Optional[AcssDebit]
                afterpay_clearpay: Optional[AfterpayClearpay]
                alipay: Optional[Alipay]
                bancontact: Optional[Bancontact]
                card: Optional[Card]
                customer_balance: Optional[CustomerBalance]
                ideal: Optional[Ideal]
                klarna: Optional[Klarna]
                link: Optional[Link]
                oxxo: Optional[Oxxo]
                p24: Optional[P24]
                paypal: Optional[Paypal]
                sepa_debit: Optional[SepaDebit]
                sofort: Optional[Sofort]
                wechat_pay: Optional[WechatPay]
                _inner_class_types = {
                    "acss_debit": AcssDebit,
                    "afterpay_clearpay": AfterpayClearpay,
                    "alipay": Alipay,
                    "bancontact": Bancontact,
                    "card": Card,
                    "customer_balance": CustomerBalance,
                    "ideal": Ideal,
                    "klarna": Klarna,
                    "link": Link,
                    "oxxo": Oxxo,
                    "p24": P24,
                    "paypal": Paypal,
                    "sepa_debit": SepaDebit,
                    "sofort": Sofort,
                    "wechat_pay": WechatPay,
                }

            class TransferData(StripeObject):
                amount: Optional[int]
                destination: ExpandableField["Account"]

            application_fee_amount: Optional[int]
            automatic_payment_methods: Optional[AutomaticPaymentMethods]
            payment_method_options: Optional[PaymentMethodOptions]
            payment_method_types: Optional[
                List[
                    Literal[
                        "acss_debit",
                        "afterpay_clearpay",
                        "alipay",
                        "au_becs_debit",
                        "bacs_debit",
                        "bancontact",
                        "card",
                        "customer_balance",
                        "eps",
                        "fpx",
                        "giropay",
                        "grabpay",
                        "ideal",
                        "klarna",
                        "link",
                        "oxxo",
                        "p24",
                        "paypal",
                        "sepa_debit",
                        "sofort",
                        "wechat_pay",
                    ]
                ]
            ]
            return_url: Optional[str]
            statement_descriptor: Optional[str]
            statement_descriptor_suffix: Optional[str]
            transfer_data: Optional[TransferData]
            _inner_class_types = {
                "automatic_payment_methods": AutomaticPaymentMethods,
                "payment_method_options": PaymentMethodOptions,
                "transfer_data": TransferData,
            }

        payment_intent: Optional[ExpandableField["PaymentIntent"]]
        settings: Optional[Settings]
        status: Optional[
            Literal[
                "canceled",
                "complete",
                "not_required",
                "processing",
                "requires_action",
                "requires_capture",
                "requires_confirmation",
                "requires_payment_method",
            ]
        ]
        _inner_class_types = {"settings": Settings}

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
        name: Optional[str]
        phone: Optional[str]
        _inner_class_types = {"address": Address}

    class TaxDetails(StripeObject):
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

        tax_exempt: Literal["exempt", "none", "reverse"]
        tax_ids: List[TaxId]
        _inner_class_types = {"tax_ids": TaxId}

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

        amount_credit: Optional[int]
        amount_discount: int
        amount_shipping: Optional[int]
        amount_tax: int
        breakdown: Optional[Breakdown]
        _inner_class_types = {"breakdown": Breakdown}

    if TYPE_CHECKING:

        class CancelParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateParams(RequestOptions):
            automatic_tax: NotRequired["Order.CreateParamsAutomaticTax|None"]
            billing_details: NotRequired[
                "Literal['']|Order.CreateParamsBillingDetails|None"
            ]
            credits: NotRequired[
                "Literal['']|List[Order.CreateParamsCredit]|None"
            ]
            currency: str
            customer: NotRequired["str|None"]
            description: NotRequired["str|None"]
            discounts: NotRequired[
                "Literal['']|List[Order.CreateParamsDiscount]|None"
            ]
            expand: NotRequired["List[str]|None"]
            ip_address: NotRequired["str|None"]
            line_items: List["Order.CreateParamsLineItem"]
            metadata: NotRequired["Dict[str, str]|None"]
            payment: NotRequired["Order.CreateParamsPayment|None"]
            shipping_cost: NotRequired[
                "Literal['']|Order.CreateParamsShippingCost|None"
            ]
            shipping_details: NotRequired[
                "Literal['']|Order.CreateParamsShippingDetails|None"
            ]
            tax_details: NotRequired["Order.CreateParamsTaxDetails|None"]

        class CreateParamsTaxDetails(TypedDict):
            tax_exempt: NotRequired[
                "Literal['']|Literal['exempt', 'none', 'reverse']|None"
            ]
            tax_ids: NotRequired[
                "List[Order.CreateParamsTaxDetailsTaxId]|None"
            ]

        class CreateParamsTaxDetailsTaxId(TypedDict):
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
                "us_ein",
                "uy_ruc",
                "ve_rif",
                "vn_tin",
                "za_vat",
            ]
            value: str

        class CreateParamsShippingDetails(TypedDict):
            address: "Order.CreateParamsShippingDetailsAddress"
            name: str
            phone: NotRequired["Literal['']|str|None"]

        class CreateParamsShippingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsShippingCost(TypedDict):
            shipping_rate: NotRequired["str|None"]
            shipping_rate_data: NotRequired[
                "Order.CreateParamsShippingCostShippingRateData|None"
            ]

        class CreateParamsShippingCostShippingRateData(TypedDict):
            delivery_estimate: NotRequired[
                "Order.CreateParamsShippingCostShippingRateDataDeliveryEstimate|None"
            ]
            display_name: str
            fixed_amount: NotRequired[
                "Order.CreateParamsShippingCostShippingRateDataFixedAmount|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tax_code: NotRequired["str|None"]
            type: NotRequired["Literal['fixed_amount']|None"]

        class CreateParamsShippingCostShippingRateDataFixedAmount(TypedDict):
            amount: int
            currency: str
            currency_options: NotRequired[
                "Dict[str, Order.CreateParamsShippingCostShippingRateDataFixedAmountCurrencyOptions]|None"
            ]

        class CreateParamsShippingCostShippingRateDataFixedAmountCurrencyOptions(
            TypedDict,
        ):
            amount: int
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]

        class CreateParamsShippingCostShippingRateDataDeliveryEstimate(
            TypedDict,
        ):
            maximum: NotRequired[
                "Order.CreateParamsShippingCostShippingRateDataDeliveryEstimateMaximum|None"
            ]
            minimum: NotRequired[
                "Order.CreateParamsShippingCostShippingRateDataDeliveryEstimateMinimum|None"
            ]

        class CreateParamsShippingCostShippingRateDataDeliveryEstimateMinimum(
            TypedDict,
        ):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class CreateParamsShippingCostShippingRateDataDeliveryEstimateMaximum(
            TypedDict,
        ):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class CreateParamsPayment(TypedDict):
            settings: "Order.CreateParamsPaymentSettings"

        class CreateParamsPaymentSettings(TypedDict):
            application_fee_amount: NotRequired["int|None"]
            payment_method_options: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptions|None"
            ]
            payment_method_types: NotRequired[
                "List[Literal['acss_debit', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'card', 'customer_balance', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'link', 'oxxo', 'p24', 'paypal', 'sepa_debit', 'sofort', 'wechat_pay']]|None"
            ]
            return_url: NotRequired["str|None"]
            statement_descriptor: NotRequired["str|None"]
            statement_descriptor_suffix: NotRequired["str|None"]
            transfer_data: NotRequired[
                "Order.CreateParamsPaymentSettingsTransferData|None"
            ]

        class CreateParamsPaymentSettingsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            destination: str

        class CreateParamsPaymentSettingsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit|None"
            ]
            afterpay_clearpay: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsAfterpayClearpay|None"
            ]
            alipay: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsAlipay|None"
            ]
            bancontact: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsBancontact|None"
            ]
            card: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsCard|None"
            ]
            customer_balance: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance|None"
            ]
            ideal: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsIdeal|None"
            ]
            klarna: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsKlarna|None"
            ]
            link: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsLink|None"
            ]
            oxxo: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsOxxo|None"
            ]
            p24: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsP24|None"
            ]
            paypal: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsPaypal|None"
            ]
            sepa_debit: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsSepaDebit|None"
            ]
            sofort: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsSofort|None"
            ]
            wechat_pay: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsWechatPay|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsWechatPay(
            TypedDict,
        ):
            app_id: NotRequired["str|None"]
            client: Literal["android", "ios", "web"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsSofort(TypedDict):
            preferred_language: NotRequired[
                "Literal['']|Literal['de', 'en', 'es', 'fr', 'it', 'nl', 'pl']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsSepaDebit(
            TypedDict,
        ):
            mandate_options: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsSepaDebitMandateOptions|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsSepaDebitMandateOptions(
            TypedDict,
        ):
            pass

        class CreateParamsPaymentSettingsPaymentMethodOptionsPaypal(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            preferred_locale: NotRequired[
                "Literal['cs-CZ', 'da-DK', 'de-AT', 'de-DE', 'de-LU', 'el-GR', 'en-GB', 'en-US', 'es-ES', 'fi-FI', 'fr-BE', 'fr-FR', 'fr-LU', 'hu-HU', 'it-IT', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-PT', 'sk-SK', 'sv-SE']|None"
            ]
            reference: NotRequired["str|None"]
            reference_id: NotRequired["str|None"]
            risk_correlation_id: NotRequired["str|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsP24(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]
            tos_shown_and_accepted: NotRequired["bool|None"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsOxxo(TypedDict):
            expires_after_days: NotRequired["int|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsLink(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            persistent_token: NotRequired["str|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsKlarna(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            preferred_locale: NotRequired[
                "Literal['cs-CZ', 'da-DK', 'de-AT', 'de-CH', 'de-DE', 'el-GR', 'en-AT', 'en-AU', 'en-BE', 'en-CA', 'en-CH', 'en-CZ', 'en-DE', 'en-DK', 'en-ES', 'en-FI', 'en-FR', 'en-GB', 'en-GR', 'en-IE', 'en-IT', 'en-NL', 'en-NO', 'en-NZ', 'en-PL', 'en-PT', 'en-SE', 'en-US', 'es-ES', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-CH', 'fr-FR', 'it-CH', 'it-IT', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-PT', 'sv-FI', 'sv-SE']|None"
            ]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsIdeal(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
            TypedDict,
        ):
            bank_transfer: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer|None"
            ]
            funding_type: NotRequired["Literal['bank_transfer']|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
            TypedDict,
        ):
            eu_bank_transfer: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer|None"
            ]
            requested_address_types: NotRequired[
                "List[Literal['aba', 'iban', 'sepa', 'sort_code', 'spei', 'swift', 'zengin']]|None"
            ]
            type: Literal[
                "eu_bank_transfer",
                "gb_bank_transfer",
                "jp_bank_transfer",
                "mx_bank_transfer",
                "us_bank_transfer",
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
            TypedDict,
        ):
            country: str

        class CreateParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
            capture_method: NotRequired[
                "Literal['automatic', 'automatic_async', 'manual']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['none', 'off_session', 'on_session']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsBancontact(
            TypedDict,
        ):
            preferred_language: NotRequired[
                "Literal['de', 'en', 'fr', 'nl']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsAlipay(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsAfterpayClearpay(
            TypedDict,
        ):
            capture_method: NotRequired[
                "Literal['automatic', 'automatic_async', 'manual']|None"
            ]
            reference: NotRequired["str|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit(
            TypedDict,
        ):
            mandate_options: NotRequired[
                "Order.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            custom_mandate_url: NotRequired["Literal['']|str|None"]
            interval_description: NotRequired["str|None"]
            payment_schedule: NotRequired[
                "Literal['combined', 'interval', 'sporadic']|None"
            ]
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]

        class CreateParamsLineItem(TypedDict):
            description: NotRequired["str|None"]
            discounts: NotRequired[
                "Literal['']|List[Order.CreateParamsLineItemDiscount]|None"
            ]
            price: NotRequired["str|None"]
            price_data: NotRequired["Order.CreateParamsLineItemPriceData|None"]
            product: NotRequired["str|None"]
            product_data: NotRequired[
                "Order.CreateParamsLineItemProductData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class CreateParamsLineItemProductData(TypedDict):
            description: NotRequired["Literal['']|str|None"]
            id: str
            images: NotRequired["Literal['']|List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            name: str
            package_dimensions: NotRequired[
                "Literal['']|Order.CreateParamsLineItemProductDataPackageDimensions|None"
            ]
            shippable: NotRequired["bool|None"]
            tax_code: NotRequired["Literal['']|str|None"]
            url: NotRequired["Literal['']|str|None"]

        class CreateParamsLineItemProductDataPackageDimensions(TypedDict):
            height: float
            length: float
            weight: float
            width: float

        class CreateParamsLineItemPriceData(TypedDict):
            currency: NotRequired["str|None"]
            product: NotRequired["str|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsLineItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class CreateParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            promotion_code: NotRequired["str|None"]

        class CreateParamsCredit(TypedDict):
            gift_card: NotRequired["str|None"]
            type: Literal["gift_card"]

        class CreateParamsBillingDetails(TypedDict):
            address: NotRequired[
                "Order.CreateParamsBillingDetailsAddress|None"
            ]
            email: NotRequired["str|None"]
            name: NotRequired["str|None"]
            phone: NotRequired["str|None"]

        class CreateParamsBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsAutomaticTax(TypedDict):
            enabled: bool

        class ListParams(RequestOptions):
            customer: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListLineItemsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ModifyParams(RequestOptions):
            automatic_tax: NotRequired["Order.ModifyParamsAutomaticTax|None"]
            billing_details: NotRequired[
                "Literal['']|Order.ModifyParamsBillingDetails|None"
            ]
            credits: NotRequired[
                "Literal['']|List[Order.ModifyParamsCredit]|None"
            ]
            currency: NotRequired["str|None"]
            customer: NotRequired["str|None"]
            description: NotRequired["Literal['']|str|None"]
            discounts: NotRequired[
                "Literal['']|List[Order.ModifyParamsDiscount]|None"
            ]
            expand: NotRequired["List[str]|None"]
            ip_address: NotRequired["str|None"]
            line_items: NotRequired["List[Order.ModifyParamsLineItem]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            payment: NotRequired["Order.ModifyParamsPayment|None"]
            shipping_cost: NotRequired[
                "Literal['']|Order.ModifyParamsShippingCost|None"
            ]
            shipping_details: NotRequired[
                "Literal['']|Order.ModifyParamsShippingDetails|None"
            ]
            tax_details: NotRequired["Order.ModifyParamsTaxDetails|None"]

        class ModifyParamsTaxDetails(TypedDict):
            tax_exempt: NotRequired[
                "Literal['']|Literal['exempt', 'none', 'reverse']|None"
            ]
            tax_ids: NotRequired[
                "List[Order.ModifyParamsTaxDetailsTaxId]|None"
            ]

        class ModifyParamsTaxDetailsTaxId(TypedDict):
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
                "us_ein",
                "uy_ruc",
                "ve_rif",
                "vn_tin",
                "za_vat",
            ]
            value: str

        class ModifyParamsShippingDetails(TypedDict):
            address: "Order.ModifyParamsShippingDetailsAddress"
            name: str
            phone: NotRequired["Literal['']|str|None"]

        class ModifyParamsShippingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ModifyParamsShippingCost(TypedDict):
            shipping_rate: NotRequired["str|None"]
            shipping_rate_data: NotRequired[
                "Order.ModifyParamsShippingCostShippingRateData|None"
            ]

        class ModifyParamsShippingCostShippingRateData(TypedDict):
            delivery_estimate: NotRequired[
                "Order.ModifyParamsShippingCostShippingRateDataDeliveryEstimate|None"
            ]
            display_name: str
            fixed_amount: NotRequired[
                "Order.ModifyParamsShippingCostShippingRateDataFixedAmount|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tax_code: NotRequired["str|None"]
            type: NotRequired["Literal['fixed_amount']|None"]

        class ModifyParamsShippingCostShippingRateDataFixedAmount(TypedDict):
            amount: int
            currency: str
            currency_options: NotRequired[
                "Dict[str, Order.ModifyParamsShippingCostShippingRateDataFixedAmountCurrencyOptions]|None"
            ]

        class ModifyParamsShippingCostShippingRateDataFixedAmountCurrencyOptions(
            TypedDict,
        ):
            amount: int
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]

        class ModifyParamsShippingCostShippingRateDataDeliveryEstimate(
            TypedDict,
        ):
            maximum: NotRequired[
                "Order.ModifyParamsShippingCostShippingRateDataDeliveryEstimateMaximum|None"
            ]
            minimum: NotRequired[
                "Order.ModifyParamsShippingCostShippingRateDataDeliveryEstimateMinimum|None"
            ]

        class ModifyParamsShippingCostShippingRateDataDeliveryEstimateMinimum(
            TypedDict,
        ):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class ModifyParamsShippingCostShippingRateDataDeliveryEstimateMaximum(
            TypedDict,
        ):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class ModifyParamsPayment(TypedDict):
            settings: "Order.ModifyParamsPaymentSettings"

        class ModifyParamsPaymentSettings(TypedDict):
            application_fee_amount: NotRequired["Literal['']|int|None"]
            payment_method_options: NotRequired[
                "Order.ModifyParamsPaymentSettingsPaymentMethodOptions|None"
            ]
            payment_method_types: NotRequired[
                "List[Literal['acss_debit', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'card', 'customer_balance', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'link', 'oxxo', 'p24', 'paypal', 'sepa_debit', 'sofort', 'wechat_pay']]|None"
            ]
            return_url: NotRequired["Literal['']|str|None"]
            statement_descriptor: NotRequired["str|None"]
            statement_descriptor_suffix: NotRequired["str|None"]
            transfer_data: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsTransferData|None"
            ]

        class ModifyParamsPaymentSettingsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            destination: str

        class ModifyParamsPaymentSettingsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit|None"
            ]
            afterpay_clearpay: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsAfterpayClearpay|None"
            ]
            alipay: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsAlipay|None"
            ]
            bancontact: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact|None"
            ]
            card: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsCard|None"
            ]
            customer_balance: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance|None"
            ]
            ideal: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsIdeal|None"
            ]
            klarna: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsKlarna|None"
            ]
            link: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsLink|None"
            ]
            oxxo: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsOxxo|None"
            ]
            p24: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsP24|None"
            ]
            paypal: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsPaypal|None"
            ]
            sepa_debit: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsSepaDebit|None"
            ]
            sofort: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsSofort|None"
            ]
            wechat_pay: NotRequired[
                "Literal['']|Order.ModifyParamsPaymentSettingsPaymentMethodOptionsWechatPay|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsWechatPay(
            TypedDict,
        ):
            app_id: NotRequired["str|None"]
            client: Literal["android", "ios", "web"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsSofort(TypedDict):
            preferred_language: NotRequired[
                "Literal['']|Literal['de', 'en', 'es', 'fr', 'it', 'nl', 'pl']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsSepaDebit(
            TypedDict,
        ):
            mandate_options: NotRequired[
                "Order.ModifyParamsPaymentSettingsPaymentMethodOptionsSepaDebitMandateOptions|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsSepaDebitMandateOptions(
            TypedDict,
        ):
            pass

        class ModifyParamsPaymentSettingsPaymentMethodOptionsPaypal(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            preferred_locale: NotRequired[
                "Literal['cs-CZ', 'da-DK', 'de-AT', 'de-DE', 'de-LU', 'el-GR', 'en-GB', 'en-US', 'es-ES', 'fi-FI', 'fr-BE', 'fr-FR', 'fr-LU', 'hu-HU', 'it-IT', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-PT', 'sk-SK', 'sv-SE']|None"
            ]
            reference: NotRequired["str|None"]
            reference_id: NotRequired["str|None"]
            risk_correlation_id: NotRequired["str|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsP24(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]
            tos_shown_and_accepted: NotRequired["bool|None"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsOxxo(TypedDict):
            expires_after_days: NotRequired["int|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsLink(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            persistent_token: NotRequired["str|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsKlarna(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            preferred_locale: NotRequired[
                "Literal['cs-CZ', 'da-DK', 'de-AT', 'de-CH', 'de-DE', 'el-GR', 'en-AT', 'en-AU', 'en-BE', 'en-CA', 'en-CH', 'en-CZ', 'en-DE', 'en-DK', 'en-ES', 'en-FI', 'en-FR', 'en-GB', 'en-GR', 'en-IE', 'en-IT', 'en-NL', 'en-NO', 'en-NZ', 'en-PL', 'en-PT', 'en-SE', 'en-US', 'es-ES', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-CH', 'fr-FR', 'it-CH', 'it-IT', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-PT', 'sv-FI', 'sv-SE']|None"
            ]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsIdeal(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
            TypedDict,
        ):
            bank_transfer: NotRequired[
                "Order.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer|None"
            ]
            funding_type: NotRequired["Literal['bank_transfer']|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
            TypedDict,
        ):
            eu_bank_transfer: NotRequired[
                "Order.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer|None"
            ]
            requested_address_types: NotRequired[
                "List[Literal['aba', 'iban', 'sepa', 'sort_code', 'spei', 'swift', 'zengin']]|None"
            ]
            type: Literal[
                "eu_bank_transfer",
                "gb_bank_transfer",
                "jp_bank_transfer",
                "mx_bank_transfer",
                "us_bank_transfer",
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
            TypedDict,
        ):
            country: str

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
            capture_method: NotRequired[
                "Literal['automatic', 'automatic_async', 'manual']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['none', 'off_session', 'on_session']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact(
            TypedDict,
        ):
            preferred_language: NotRequired[
                "Literal['de', 'en', 'fr', 'nl']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsAlipay(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsAfterpayClearpay(
            TypedDict,
        ):
            capture_method: NotRequired[
                "Literal['automatic', 'automatic_async', 'manual']|None"
            ]
            reference: NotRequired["str|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit(
            TypedDict,
        ):
            mandate_options: NotRequired[
                "Order.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            custom_mandate_url: NotRequired["Literal['']|str|None"]
            interval_description: NotRequired["str|None"]
            payment_schedule: NotRequired[
                "Literal['combined', 'interval', 'sporadic']|None"
            ]
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]

        class ModifyParamsLineItem(TypedDict):
            description: NotRequired["str|None"]
            discounts: NotRequired[
                "Literal['']|List[Order.ModifyParamsLineItemDiscount]|None"
            ]
            id: NotRequired["str|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired["Order.ModifyParamsLineItemPriceData|None"]
            product: NotRequired["str|None"]
            product_data: NotRequired[
                "Order.ModifyParamsLineItemProductData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class ModifyParamsLineItemProductData(TypedDict):
            description: NotRequired["Literal['']|str|None"]
            id: str
            images: NotRequired["Literal['']|List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            name: str
            package_dimensions: NotRequired[
                "Literal['']|Order.ModifyParamsLineItemProductDataPackageDimensions|None"
            ]
            shippable: NotRequired["bool|None"]
            tax_code: NotRequired["Literal['']|str|None"]
            url: NotRequired["Literal['']|str|None"]

        class ModifyParamsLineItemProductDataPackageDimensions(TypedDict):
            height: float
            length: float
            weight: float
            width: float

        class ModifyParamsLineItemPriceData(TypedDict):
            currency: NotRequired["str|None"]
            product: NotRequired["str|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class ModifyParamsLineItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]

        class ModifyParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            promotion_code: NotRequired["str|None"]

        class ModifyParamsCredit(TypedDict):
            gift_card: NotRequired["str|None"]
            type: Literal["gift_card"]

        class ModifyParamsBillingDetails(TypedDict):
            address: NotRequired[
                "Order.ModifyParamsBillingDetailsAddress|None"
            ]
            email: NotRequired["str|None"]
            name: NotRequired["str|None"]
            phone: NotRequired["str|None"]

        class ModifyParamsBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ModifyParamsAutomaticTax(TypedDict):
            enabled: bool

        class ReopenParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class SubmitParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            expected_total: int

    amount_remaining: Optional[int]
    amount_subtotal: int
    amount_total: int
    application: Optional[ExpandableField["Application"]]
    automatic_tax: Optional[AutomaticTax]
    billing_details: Optional[BillingDetails]
    client_secret: Optional[str]
    created: int
    credits: Optional[List[Credit]]
    currency: str
    customer: Optional[ExpandableField["Customer"]]
    description: Optional[str]
    discounts: Optional[List[ExpandableField["DiscountResource"]]]
    id: str
    ip_address: Optional[str]
    line_items: Optional[ListObject["LineItem"]]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["order"]
    payment: Payment
    shipping_cost: Optional[ShippingCost]
    shipping_details: Optional[ShippingDetails]
    status: Literal["canceled", "complete", "open", "processing", "submitted"]
    tax_details: Optional[TaxDetails]
    total_details: TotalDetails

    @classmethod
    def _cls_cancel(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Order.CancelParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/orders/{id}/cancel".format(id=util.sanitize_id(id)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Order.CancelParams"]
    ):
        return self._request(
            "post",
            "/v1/orders/{id}/cancel".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Order.CreateParams"]
    ) -> "Order":
        return cast(
            "Order",
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
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Order.ListParams"]
    ) -> ListObject["Order"]:
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
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Order.ListLineItemsParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/orders/{id}/line_items".format(id=util.sanitize_id(id)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Order.ListLineItemsParams"]
    ):
        return self._request(
            "get",
            "/v1/orders/{id}/line_items".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def modify(cls, id, **params: Unpack["Order.ModifyParams"]) -> "Order":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Order",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def _cls_reopen(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Order.ReopenParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/orders/{id}/reopen".format(id=util.sanitize_id(id)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_reopen")
    def reopen(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Order.ReopenParams"]
    ):
        return self._request(
            "post",
            "/v1/orders/{id}/reopen".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Order.RetrieveParams"]
    ) -> "Order":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_submit(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Order.SubmitParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/orders/{id}/submit".format(id=util.sanitize_id(id)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_submit")
    def submit(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Order.SubmitParams"]
    ):
        return self._request(
            "post",
            "/v1/orders/{id}/submit".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    _inner_class_types = {
        "automatic_tax": AutomaticTax,
        "billing_details": BillingDetails,
        "credits": Credit,
        "payment": Payment,
        "shipping_cost": ShippingCost,
        "shipping_details": ShippingDetails,
        "tax_details": TaxDetails,
        "total_details": TotalDetails,
    }
