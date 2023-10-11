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
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

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
        **params: Any
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
    def cancel(self, idempotency_key: Optional[str] = None, **params: Any):
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
        **params: Any
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
        **params: Any
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
        **params: Any
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
        self, idempotency_key: Optional[str] = None, **params: Any
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
    def modify(cls, id, **params: Any) -> "Order":
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
        **params: Any
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
    def reopen(self, idempotency_key: Optional[str] = None, **params: Any):
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
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Order":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_submit(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def submit(self, idempotency_key: Optional[str] = None, **params: Any):
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
