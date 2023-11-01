# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    APIResourceTestHelpers,
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.api_resources.search_result_object import SearchResultObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import (
    ClassVar,
    Dict,
    Iterator,
    List,
    Optional,
    Union,
    cast,
    overload,
)
from typing_extensions import (
    Literal,
    NotRequired,
    Type,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.bank_account import BankAccount
    from stripe.api_resources.card import Card
    from stripe.api_resources.cash_balance import CashBalance
    from stripe.api_resources.customer_balance_transaction import (
        CustomerBalanceTransaction,
    )
    from stripe.api_resources.customer_cash_balance_transaction import (
        CustomerCashBalanceTransaction,
    )
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.funding_instructions import FundingInstructions
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.source import Source
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.tax_id import TaxId
    from stripe.api_resources.test_helpers.test_clock import TestClock


@nested_resource_class_methods("balance_transaction")
@nested_resource_class_methods("cash_balance_transaction")
@nested_resource_class_methods("source")
@nested_resource_class_methods("tax_id")
class Customer(
    CreateableAPIResource["Customer"],
    DeletableAPIResource["Customer"],
    ListableAPIResource["Customer"],
    SearchableAPIResource["Customer"],
    UpdateableAPIResource["Customer"],
):
    """
    This object represents a customer of your business. Use it to create recurring charges and track payments that belong to the same customer.

    Related guide: [Save a card during payment](https://stripe.com/docs/payments/save-during-payment)
    """

    OBJECT_NAME: ClassVar[Literal["customer"]] = "customer"

    class Address(StripeObject):
        city: Optional[str]
        """
        City, district, suburb, town, or village.
        """
        country: Optional[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: Optional[str]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: Optional[str]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: Optional[str]
        """
        ZIP or postal code.
        """
        state: Optional[str]
        """
        State, county, province, or region.
        """

    class InvoiceSettings(StripeObject):
        class CustomField(StripeObject):
            name: str
            """
            The name of the custom field.
            """
            value: str
            """
            The value of the custom field.
            """

        class RenderingOptions(StripeObject):
            amount_tax_display: Optional[str]
            """
            How line-item prices and amounts will be displayed with respect to tax on invoice PDFs.
            """

        custom_fields: Optional[List[CustomField]]
        """
        Default custom fields to be displayed on invoices for this customer.
        """
        default_payment_method: Optional[ExpandableField["PaymentMethod"]]
        """
        ID of a payment method that's attached to the customer, to be used as the customer's default payment method for subscriptions and invoices.
        """
        footer: Optional[str]
        """
        Default footer to be displayed on invoices for this customer.
        """
        rendering_options: Optional[RenderingOptions]
        """
        Default options for invoice PDF rendering for this customer.
        """
        _inner_class_types = {
            "custom_fields": CustomField,
            "rendering_options": RenderingOptions,
        }

    class Shipping(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            """
            City, district, suburb, town, or village.
            """
            country: Optional[str]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: Optional[str]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State, county, province, or region.
            """

        address: Optional[Address]
        carrier: Optional[str]
        """
        The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.
        """
        name: Optional[str]
        """
        Recipient name.
        """
        phone: Optional[str]
        """
        Recipient phone (including extension).
        """
        tracking_number: Optional[str]
        """
        The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.
        """
        _inner_class_types = {"address": Address}

    class Tax(StripeObject):
        class Location(StripeObject):
            country: str
            """
            The customer's country as identified by Stripe Tax.
            """
            source: Literal[
                "billing_address",
                "ip_address",
                "payment_method",
                "shipping_destination",
            ]
            """
            The data source used to infer the customer's location.
            """
            state: Optional[str]
            """
            The customer's state, county, province, or region as identified by Stripe Tax.
            """

        automatic_tax: Literal[
            "failed", "not_collecting", "supported", "unrecognized_location"
        ]
        """
        Surfaces if automatic tax computation is possible given the current customer location information.
        """
        ip_address: Optional[str]
        """
        A recent IP address of the customer used for tax reporting and tax location inference.
        """
        location: Optional[Location]
        """
        The customer's location as identified by Stripe Tax.
        """
        _inner_class_types = {"location": Location}

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            address: NotRequired[
                "Literal['']|Customer.CreateParamsAddress|None"
            ]
            """
            The customer's address.
            """
            balance: NotRequired["int|None"]
            """
            An integer amount in cents (or local equivalent) that represents the customer's current balance, which affect the customer's future invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice.
            """
            cash_balance: NotRequired["Customer.CreateParamsCashBalance|None"]
            """
            Balance information and default balance settings for this customer.
            """
            coupon: NotRequired["str|None"]
            description: NotRequired["str|None"]
            """
            An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.
            """
            email: NotRequired["str|None"]
            """
            Customer's email address. It's displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to *512 characters*.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            invoice_prefix: NotRequired["str|None"]
            """
            The prefix for the customer used to generate unique invoice numbers. Must be 3–12 uppercase letters or numbers.
            """
            invoice_settings: NotRequired[
                "Customer.CreateParamsInvoiceSettings|None"
            ]
            """
            Default invoice settings for this customer.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            name: NotRequired["str|None"]
            """
            The customer's full name or business name.
            """
            next_invoice_sequence: NotRequired["int|None"]
            """
            The sequence to be used on the customer's next invoice. Defaults to 1.
            """
            payment_method: NotRequired["str|None"]
            phone: NotRequired["str|None"]
            """
            The customer's phone number.
            """
            preferred_locales: NotRequired["List[str]|None"]
            """
            Customer's preferred languages, ordered by preference.
            """
            promotion_code: NotRequired["str|None"]
            """
            The API ID of a promotion code to apply to the customer. The customer will have a discount applied on all recurring payments. Charges you create through the API will not have the discount.
            """
            shipping: NotRequired[
                "Literal['']|Customer.CreateParamsShipping|None"
            ]
            """
            The customer's shipping information. Appears on invoices emailed to this customer.
            """
            source: NotRequired["str|None"]
            tax: NotRequired["Customer.CreateParamsTax|None"]
            """
            Tax details about the customer.
            """
            tax_exempt: NotRequired[
                "Literal['']|Literal['exempt', 'none', 'reverse']|None"
            ]
            """
            The customer's tax exemption. One of `none`, `exempt`, or `reverse`.
            """
            tax_id_data: NotRequired[
                "List[Customer.CreateParamsTaxIdDatum]|None"
            ]
            """
            The customer's tax IDs.
            """
            test_clock: NotRequired["str|None"]
            """
            ID of the test clock to attach to the customer.
            """
            validate: NotRequired["bool|None"]

        class CreateParamsTaxIdDatum(TypedDict):
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
            """
            Type of the tax ID, one of `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, or `za_vat`
            """
            value: str
            """
            Value of the tax ID.
            """

        class CreateParamsTax(TypedDict):
            ip_address: NotRequired["Literal['']|str|None"]
            """
            A recent IP address of the customer used for tax reporting and tax location inference. Stripe recommends updating the IP address when a new PaymentMethod is attached or the address field on the customer is updated. We recommend against updating this field more frequently since it could result in unexpected tax location/reporting outcomes.
            """

        class CreateParamsShipping(TypedDict):
            address: "Customer.CreateParamsShippingAddress"
            """
            Customer shipping address.
            """
            name: str
            """
            Customer name.
            """
            phone: NotRequired["str|None"]
            """
            Customer phone (including extension).
            """

        class CreateParamsShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class CreateParamsInvoiceSettings(TypedDict):
            custom_fields: NotRequired[
                "Literal['']|List[Customer.CreateParamsInvoiceSettingsCustomField]|None"
            ]
            """
            Default custom fields to be displayed on invoices for this customer. When updating, pass an empty string to remove previously-defined fields.
            """
            default_payment_method: NotRequired["str|None"]
            """
            ID of a payment method that's attached to the customer, to be used as the customer's default payment method for subscriptions and invoices.
            """
            footer: NotRequired["str|None"]
            """
            Default footer to be displayed on invoices for this customer.
            """
            rendering_options: NotRequired[
                "Literal['']|Customer.CreateParamsInvoiceSettingsRenderingOptions|None"
            ]
            """
            Default options for invoice PDF rendering for this customer.
            """

        class CreateParamsInvoiceSettingsRenderingOptions(TypedDict):
            amount_tax_display: NotRequired[
                "Literal['']|Literal['exclude_tax', 'include_inclusive_tax']|None"
            ]
            """
            How line-item prices and amounts will be displayed with respect to tax on invoice PDFs. One of `exclude_tax` or `include_inclusive_tax`. `include_inclusive_tax` will include inclusive tax (and exclude exclusive tax) in invoice PDF amounts. `exclude_tax` will exclude all tax (inclusive and exclusive alike) from invoice PDF amounts.
            """

        class CreateParamsInvoiceSettingsCustomField(TypedDict):
            name: str
            """
            The name of the custom field. This may be up to 30 characters.
            """
            value: str
            """
            The value of the custom field. This may be up to 30 characters.
            """

        class CreateParamsCashBalance(TypedDict):
            settings: NotRequired[
                "Customer.CreateParamsCashBalanceSettings|None"
            ]
            """
            Settings controlling the behavior of the customer's cash balance,
            such as reconciliation of funds received.
            """

        class CreateParamsCashBalanceSettings(TypedDict):
            reconciliation_mode: NotRequired[
                "Literal['automatic', 'manual', 'merchant_default']|None"
            ]
            """
            Controls how funds transferred by the customer are applied to payment intents and invoices. Valid options are `automatic`, `manual`, or `merchant_default`. For more information about these reconciliation modes, see [Reconciliation](https://stripe.com/docs/payments/customer-balance/reconciliation).
            """

        class CreateParamsAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class CreateFundingInstructionsParams(RequestOptions):
            bank_transfer: "Customer.CreateFundingInstructionsParamsBankTransfer"
            """
            Additional parameters for `bank_transfer` funding types
            """
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            funding_type: Literal["bank_transfer"]
            """
            The `funding_type` to get the instructions for.
            """

        class CreateFundingInstructionsParamsBankTransfer(TypedDict):
            eu_bank_transfer: NotRequired[
                "Customer.CreateFundingInstructionsParamsBankTransferEuBankTransfer|None"
            ]
            """
            Configuration for eu_bank_transfer funding type.
            """
            requested_address_types: NotRequired[
                "List[Literal['iban', 'sort_code', 'spei', 'zengin']]|None"
            ]
            """
            List of address types that should be returned in the financial_addresses response. If not specified, all valid types will be returned.

            Permitted values include: `sort_code`, `zengin`, `iban`, or `spei`.
            """
            type: Literal[
                "eu_bank_transfer",
                "gb_bank_transfer",
                "jp_bank_transfer",
                "mx_bank_transfer",
                "us_bank_transfer",
            ]
            """
            The type of the `bank_transfer`
            """

        class CreateFundingInstructionsParamsBankTransferEuBankTransfer(
            TypedDict,
        ):
            country: str
            """
            The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.
            """

        class DeleteParams(RequestOptions):
            pass

        class DeleteDiscountParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            created: NotRequired["Customer.ListParamsCreated|int|None"]
            email: NotRequired["str|None"]
            """
            A case-sensitive filter on the list based on the customer's `email` field. The value must be a string.
            """
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            test_clock: NotRequired["str|None"]
            """
            Provides a list of customers that are associated with the specified test clock. The response will not include customers with test clocks if this parameter is not set.
            """

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class ListPaymentMethodsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            type: NotRequired[
                "Literal['acss_debit', 'affirm', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'blik', 'boleto', 'card', 'cashapp', 'customer_balance', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'konbini', 'link', 'oxxo', 'p24', 'paynow', 'paypal', 'pix', 'promptpay', 'revolut_pay', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay', 'zip']|None"
            ]
            """
            An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.
            """

        class ModifyParams(RequestOptions):
            address: NotRequired[
                "Literal['']|Customer.ModifyParamsAddress|None"
            ]
            """
            The customer's address.
            """
            balance: NotRequired["int|None"]
            """
            An integer amount in cents (or local equivalent) that represents the customer's current balance, which affect the customer's future invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice.
            """
            cash_balance: NotRequired["Customer.ModifyParamsCashBalance|None"]
            """
            Balance information and default balance settings for this customer.
            """
            coupon: NotRequired["str|None"]
            default_source: NotRequired["str|None"]
            """
            If you are using payment methods created via the PaymentMethods API, see the [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method) parameter.

            Provide the ID of a payment source already attached to this customer to make it this customer's default payment source.

            If you want to add a new payment source and make it the default, see the [source](https://stripe.com/docs/api/customers/update#update_customer-source) property.
            """
            description: NotRequired["str|None"]
            """
            An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.
            """
            email: NotRequired["str|None"]
            """
            Customer's email address. It's displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to *512 characters*.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            invoice_prefix: NotRequired["str|None"]
            """
            The prefix for the customer used to generate unique invoice numbers. Must be 3–12 uppercase letters or numbers.
            """
            invoice_settings: NotRequired[
                "Customer.ModifyParamsInvoiceSettings|None"
            ]
            """
            Default invoice settings for this customer.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            name: NotRequired["str|None"]
            """
            The customer's full name or business name.
            """
            next_invoice_sequence: NotRequired["int|None"]
            """
            The sequence to be used on the customer's next invoice. Defaults to 1.
            """
            phone: NotRequired["str|None"]
            """
            The customer's phone number.
            """
            preferred_locales: NotRequired["List[str]|None"]
            """
            Customer's preferred languages, ordered by preference.
            """
            promotion_code: NotRequired["str|None"]
            """
            The API ID of a promotion code to apply to the customer. The customer will have a discount applied on all recurring payments. Charges you create through the API will not have the discount.
            """
            shipping: NotRequired[
                "Literal['']|Customer.ModifyParamsShipping|None"
            ]
            """
            The customer's shipping information. Appears on invoices emailed to this customer.
            """
            source: NotRequired["str|None"]
            tax: NotRequired["Customer.ModifyParamsTax|None"]
            """
            Tax details about the customer.
            """
            tax_exempt: NotRequired[
                "Literal['']|Literal['exempt', 'none', 'reverse']|None"
            ]
            """
            The customer's tax exemption. One of `none`, `exempt`, or `reverse`.
            """
            validate: NotRequired["bool|None"]

        class ModifyParamsTax(TypedDict):
            ip_address: NotRequired["Literal['']|str|None"]
            """
            A recent IP address of the customer used for tax reporting and tax location inference. Stripe recommends updating the IP address when a new PaymentMethod is attached or the address field on the customer is updated. We recommend against updating this field more frequently since it could result in unexpected tax location/reporting outcomes.
            """

        class ModifyParamsShipping(TypedDict):
            address: "Customer.ModifyParamsShippingAddress"
            """
            Customer shipping address.
            """
            name: str
            """
            Customer name.
            """
            phone: NotRequired["str|None"]
            """
            Customer phone (including extension).
            """

        class ModifyParamsShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class ModifyParamsInvoiceSettings(TypedDict):
            custom_fields: NotRequired[
                "Literal['']|List[Customer.ModifyParamsInvoiceSettingsCustomField]|None"
            ]
            """
            Default custom fields to be displayed on invoices for this customer. When updating, pass an empty string to remove previously-defined fields.
            """
            default_payment_method: NotRequired["str|None"]
            """
            ID of a payment method that's attached to the customer, to be used as the customer's default payment method for subscriptions and invoices.
            """
            footer: NotRequired["str|None"]
            """
            Default footer to be displayed on invoices for this customer.
            """
            rendering_options: NotRequired[
                "Literal['']|Customer.ModifyParamsInvoiceSettingsRenderingOptions|None"
            ]
            """
            Default options for invoice PDF rendering for this customer.
            """

        class ModifyParamsInvoiceSettingsRenderingOptions(TypedDict):
            amount_tax_display: NotRequired[
                "Literal['']|Literal['exclude_tax', 'include_inclusive_tax']|None"
            ]
            """
            How line-item prices and amounts will be displayed with respect to tax on invoice PDFs. One of `exclude_tax` or `include_inclusive_tax`. `include_inclusive_tax` will include inclusive tax (and exclude exclusive tax) in invoice PDF amounts. `exclude_tax` will exclude all tax (inclusive and exclusive alike) from invoice PDF amounts.
            """

        class ModifyParamsInvoiceSettingsCustomField(TypedDict):
            name: str
            """
            The name of the custom field. This may be up to 30 characters.
            """
            value: str
            """
            The value of the custom field. This may be up to 30 characters.
            """

        class ModifyParamsCashBalance(TypedDict):
            settings: NotRequired[
                "Customer.ModifyParamsCashBalanceSettings|None"
            ]
            """
            Settings controlling the behavior of the customer's cash balance,
            such as reconciliation of funds received.
            """

        class ModifyParamsCashBalanceSettings(TypedDict):
            reconciliation_mode: NotRequired[
                "Literal['automatic', 'manual', 'merchant_default']|None"
            ]
            """
            Controls how funds transferred by the customer are applied to payment intents and invoices. Valid options are `automatic`, `manual`, or `merchant_default`. For more information about these reconciliation modes, see [Reconciliation](https://stripe.com/docs/payments/customer-balance/reconciliation).
            """

        class ModifyParamsAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class RetrievePaymentMethodParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class SearchParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            page: NotRequired["str|None"]
            """
            A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
            """
            query: str
            """
            The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for customers](https://stripe.com/docs/search#query-fields-for-customers).
            """

        class ModifyCashBalanceParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            settings: NotRequired[
                "Customer.ModifyCashBalanceParamsSettings|None"
            ]
            """
            A hash of settings for this cash balance.
            """

        class ModifyCashBalanceParamsSettings(TypedDict):
            reconciliation_mode: NotRequired[
                "Literal['automatic', 'manual', 'merchant_default']|None"
            ]
            """
            Controls how funds transferred by the customer are applied to payment intents and invoices. Valid options are `automatic`, `manual`, or `merchant_default`. For more information about these reconciliation modes, see [Reconciliation](https://stripe.com/docs/payments/customer-balance/reconciliation).
            """

        class RetrieveCashBalanceParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class FundCashBalanceParams(RequestOptions):
            amount: int
            """
            Amount to be used for this test cash balance transaction. A positive integer representing how much to fund in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to fund $1.00 or 100 to fund ¥100, a zero-decimal currency).
            """
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            reference: NotRequired["str|None"]
            """
            A description of the test funding. This simulates free-text references supplied by customers when making bank transfers to their cash balance. You can use this to test how Stripe's [reconciliation algorithm](https://stripe.com/docs/payments/customer-balance/reconciliation) applies to different user inputs.
            """

        class CreateBalanceTransactionParams(RequestOptions):
            amount: int
            """
            The integer amount in **cents (or local equivalent)** to apply to the customer's credit balance.
            """
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Specifies the [`invoice_credit_balance`](https://stripe.com/docs/api/customers/object#customer_object-invoice_credit_balance) that this transaction will apply to. If the customer's `currency` is not set, it will be updated to this value.
            """
            description: NotRequired["str|None"]
            """
            An arbitrary string attached to the object. Often useful for displaying to users.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """

        class RetrieveBalanceTransactionParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ModifyBalanceTransactionParams(RequestOptions):
            description: NotRequired["str|None"]
            """
            An arbitrary string attached to the object. Often useful for displaying to users.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """

        class ListBalanceTransactionsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class RetrieveCashBalanceTransactionParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ListCashBalanceTransactionsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class CreateSourceParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            source: str
            """
            Please refer to full [documentation](https://stripe.com/docs/api) instead.
            """
            validate: NotRequired["bool|None"]

        class RetrieveSourceParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ModifySourceParams(RequestOptions):
            account_holder_name: NotRequired["str|None"]
            """
            The name of the person or business that owns the bank account.
            """
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            """
            The type of entity that holds the account. This can be either `individual` or `company`.
            """
            address_city: NotRequired["str|None"]
            """
            City/District/Suburb/Town/Village.
            """
            address_country: NotRequired["str|None"]
            """
            Billing address country, if provided when creating card.
            """
            address_line1: NotRequired["str|None"]
            """
            Address line 1 (Street address/PO Box/Company name).
            """
            address_line2: NotRequired["str|None"]
            """
            Address line 2 (Apartment/Suite/Unit/Building).
            """
            address_state: NotRequired["str|None"]
            """
            State/County/Province/Region.
            """
            address_zip: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            exp_month: NotRequired["str|None"]
            """
            Two digit number representing the card's expiration month.
            """
            exp_year: NotRequired["str|None"]
            """
            Four digit number representing the card's expiration year.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            name: NotRequired["str|None"]
            """
            Cardholder name.
            """
            owner: NotRequired["Customer.ModifySourceParamsOwner|None"]

        class ModifySourceParamsOwner(TypedDict):
            address: NotRequired[
                "Customer.ModifySourceParamsOwnerAddress|None"
            ]
            """
            Owner's address.
            """
            email: NotRequired["str|None"]
            """
            Owner's email address.
            """
            name: NotRequired["str|None"]
            """
            Owner's full name.
            """
            phone: NotRequired["str|None"]
            """
            Owner's phone number.
            """

        class ModifySourceParamsOwnerAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class DeleteSourceParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ListSourcesParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            object: NotRequired["str|None"]
            """
            Filter sources according to a particular object type.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class CreateTaxIdParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
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
            """
            Type of the tax ID, one of `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, or `za_vat`
            """
            value: str
            """
            Value of the tax ID.
            """

        class RetrieveTaxIdParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class DeleteTaxIdParams(RequestOptions):
            pass

        class ListTaxIdsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

    address: Optional[Address]
    """
    The customer's address.
    """
    balance: Optional[int]
    """
    The current balance, if any, that's stored on the customer. If negative, the customer has credit to apply to their next invoice. If positive, the customer has an amount owed that's added to their next invoice. The balance only considers amounts that Stripe hasn't successfully applied to any invoice. It doesn't reflect unpaid invoices. This balance is only taken into account after invoices finalize.
    """
    cash_balance: Optional["CashBalance"]
    """
    The current funds being held by Stripe on behalf of the customer. You can apply these funds towards payment intents when the source is "cash_balance". The `settings[reconciliation_mode]` field describes if these funds apply to these payment intents manually or automatically.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: Optional[str]
    """
    Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) the customer can be charged in for recurring billing purposes.
    """
    default_source: Optional[
        ExpandableField[Union["Account", "BankAccount", "Card", "Source"]]
    ]
    """
    ID of the default payment source for the customer.

    If you use payment methods created through the PaymentMethods API, see the [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) field instead.
    """
    delinquent: Optional[bool]
    """
    Tracks the most recent state change on any invoice belonging to the customer. Paying an invoice or marking it uncollectible via the API will set this field to false. An automatic payment failure or passing the `invoice.due_date` will set this field to `true`.

    If an invoice becomes uncollectible by [dunning](https://stripe.com/docs/billing/automatic-collection), `delinquent` doesn't reset to `false`.

    If you care whether the customer has paid their most recent subscription invoice, use `subscription.status` instead. Paying or marking uncollectible any customer invoice regardless of whether it is the latest invoice for a subscription will always set this field to `false`.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    discount: Optional["Discount"]
    """
    Describes the current discount active on the customer, if there is one.
    """
    email: Optional[str]
    """
    The customer's email address.
    """
    id: str
    """
    Unique identifier for the object.
    """
    invoice_credit_balance: Optional[Dict[str, int]]
    """
    The current multi-currency balances, if any, that's stored on the customer. If positive in a currency, the customer has a credit to apply to their next invoice denominated in that currency. If negative, the customer has an amount owed that's added to their next invoice denominated in that currency. These balances don't apply to unpaid invoices. They solely track amounts that Stripe hasn't successfully applied to any invoice. Stripe only applies a balance in a specific currency to an invoice after that invoice (which is in the same currency) finalizes.
    """
    invoice_prefix: Optional[str]
    """
    The prefix for the customer used to generate unique invoice numbers.
    """
    invoice_settings: Optional[InvoiceSettings]
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    name: Optional[str]
    """
    The customer's full name or business name.
    """
    next_invoice_sequence: Optional[int]
    """
    The suffix of the customer's next invoice number (for example, 0001).
    """
    object: Literal["customer"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    phone: Optional[str]
    """
    The customer's phone number.
    """
    preferred_locales: Optional[List[str]]
    """
    The customer's preferred locales (languages), ordered by preference.
    """
    shipping: Optional[Shipping]
    """
    Mailing and shipping address for the customer. Appears on invoices emailed to this customer.
    """
    sources: Optional[
        ListObject[Union["Account", "BankAccount", "Card", "Source"]]
    ]
    """
    The customer's payment sources, if any.
    """
    subscriptions: Optional[ListObject["Subscription"]]
    """
    The customer's current subscriptions, if any.
    """
    tax: Optional[Tax]
    tax_exempt: Optional[Literal["exempt", "none", "reverse"]]
    """
    Describes the customer's tax exemption status, which is `none`, `exempt`, or `reverse`. When set to `reverse`, invoice and receipt PDFs include the following text: **"Reverse charge"**.
    """
    tax_ids: Optional[ListObject["TaxId"]]
    """
    The customer's tax IDs.
    """
    test_clock: Optional[ExpandableField["TestClock"]]
    """
    ID of the test clock that this customer belongs to.
    """
    deleted: Optional[Literal[True]]
    """
    Always true for a deleted object
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.CreateParams"]
    ) -> "Customer":
        """
        Creates a new customer object.
        """
        return cast(
            "Customer",
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
    def _cls_create_funding_instructions(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.CreateFundingInstructionsParams"]
    ) -> "FundingInstructions":
        """
        Retrieve funding instructions for a customer cash balance. If funding instructions do not yet exist for the customer, new
        funding instructions will be created. If funding instructions have already been created for a given customer, the same
        funding instructions will be retrieved. In other words, we will return the same funding instructions each time.
        """
        return cast(
            "FundingInstructions",
            cls._static_request(
                "post",
                "/v1/customers/{customer}/funding_instructions".format(
                    customer=util.sanitize_id(customer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def create_funding_instructions(
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.CreateFundingInstructionsParams"]
    ) -> "FundingInstructions":
        """
        Retrieve funding instructions for a customer cash balance. If funding instructions do not yet exist for the customer, new
        funding instructions will be created. If funding instructions have already been created for a given customer, the same
        funding instructions will be retrieved. In other words, we will return the same funding instructions each time.
        """
        ...

    @overload
    def create_funding_instructions(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Customer.CreateFundingInstructionsParams"]
    ) -> "FundingInstructions":
        """
        Retrieve funding instructions for a customer cash balance. If funding instructions do not yet exist for the customer, new
        funding instructions will be created. If funding instructions have already been created for a given customer, the same
        funding instructions will be retrieved. In other words, we will return the same funding instructions each time.
        """
        ...

    @class_method_variant("_cls_create_funding_instructions")
    def create_funding_instructions(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Customer.CreateFundingInstructionsParams"]
    ) -> "FundingInstructions":
        """
        Retrieve funding instructions for a customer cash balance. If funding instructions do not yet exist for the customer, new
        funding instructions will be created. If funding instructions have already been created for a given customer, the same
        funding instructions will be retrieved. In other words, we will return the same funding instructions each time.
        """
        return cast(
            "FundingInstructions",
            self._request(
                "post",
                "/v1/customers/{customer}/funding_instructions".format(
                    customer=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def _cls_delete(
        cls, sid: str, **params: Unpack["Customer.DeleteParams"]
    ) -> "Customer":
        """
        Permanently deletes a customer. It cannot be undone. Also immediately cancels any active subscriptions on the customer.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Customer",
            cls._static_request("delete", url, params=params),
        )

    @overload
    @staticmethod
    def delete(
        sid: str, **params: Unpack["Customer.DeleteParams"]
    ) -> "Customer":
        """
        Permanently deletes a customer. It cannot be undone. Also immediately cancels any active subscriptions on the customer.
        """
        ...

    @overload
    def delete(self, **params: Unpack["Customer.DeleteParams"]) -> "Customer":
        """
        Permanently deletes a customer. It cannot be undone. Also immediately cancels any active subscriptions on the customer.
        """
        ...

    @class_method_variant("_cls_delete")
    def delete(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["Customer.DeleteParams"]
    ) -> "Customer":
        """
        Permanently deletes a customer. It cannot be undone. Also immediately cancels any active subscriptions on the customer.
        """
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def _cls_delete_discount(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.DeleteDiscountParams"]
    ) -> "Discount":
        """
        Removes the currently applied discount on a customer.
        """
        return cast(
            "Discount",
            cls._static_request(
                "delete",
                "/v1/customers/{customer}/discount".format(
                    customer=util.sanitize_id(customer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def delete_discount(
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.DeleteDiscountParams"]
    ) -> "Discount":
        """
        Removes the currently applied discount on a customer.
        """
        ...

    @overload
    def delete_discount(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Customer.DeleteDiscountParams"]
    ) -> "Discount":
        """
        Removes the currently applied discount on a customer.
        """
        ...

    @class_method_variant("_cls_delete_discount")
    def delete_discount(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Customer.DeleteDiscountParams"]
    ) -> "Discount":
        """
        Removes the currently applied discount on a customer.
        """
        return cast(
            "Discount",
            self._request(
                "delete",
                "/v1/customers/{customer}/discount".format(
                    customer=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ListParams"]
    ) -> ListObject["Customer"]:
        """
        Returns a list of your customers. The customers are returned sorted by creation date, with the most recent customers appearing first.
        """
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
    def _cls_list_payment_methods(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ListPaymentMethodsParams"]
    ) -> ListObject["PaymentMethod"]:
        """
        Returns a list of PaymentMethods for a given Customer
        """
        return cast(
            ListObject["PaymentMethod"],
            cls._static_request(
                "get",
                "/v1/customers/{customer}/payment_methods".format(
                    customer=util.sanitize_id(customer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def list_payment_methods(
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ListPaymentMethodsParams"]
    ) -> ListObject["PaymentMethod"]:
        """
        Returns a list of PaymentMethods for a given Customer
        """
        ...

    @overload
    def list_payment_methods(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Customer.ListPaymentMethodsParams"]
    ) -> ListObject["PaymentMethod"]:
        """
        Returns a list of PaymentMethods for a given Customer
        """
        ...

    @class_method_variant("_cls_list_payment_methods")
    def list_payment_methods(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Customer.ListPaymentMethodsParams"]
    ) -> ListObject["PaymentMethod"]:
        """
        Returns a list of PaymentMethods for a given Customer
        """
        return cast(
            ListObject["PaymentMethod"],
            self._request(
                "get",
                "/v1/customers/{customer}/payment_methods".format(
                    customer=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["Customer.ModifyParams"]
    ) -> "Customer":
        """
        Updates the specified customer by setting the values of the parameters passed. Any parameters not provided will be left unchanged. For example, if you pass the source parameter, that becomes the customer's active source (e.g., a card) to be used for all charges in the future. When you update a customer to a new valid card source by passing the source parameter: for each of the customer's current subscriptions, if the subscription bills automatically and is in the past_due state, then the latest open invoice for the subscription with automatic collection enabled will be retried. This retry will not count as an automatic retry, and will not affect the next regularly scheduled payment for the invoice. Changing the default_source for a customer will not trigger this behavior.

        This request accepts mostly the same arguments as the customer creation call.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Customer",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Customer.RetrieveParams"]
    ) -> "Customer":
        """
        Retrieves a Customer object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_retrieve_payment_method(
        cls,
        customer: str,
        payment_method: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.RetrievePaymentMethodParams"]
    ) -> "PaymentMethod":
        """
        Retrieves a PaymentMethod object for a given Customer.
        """
        return cast(
            "PaymentMethod",
            cls._static_request(
                "get",
                "/v1/customers/{customer}/payment_methods/{payment_method}".format(
                    customer=util.sanitize_id(customer),
                    payment_method=util.sanitize_id(payment_method),
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def retrieve_payment_method(
        customer: str,
        payment_method: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.RetrievePaymentMethodParams"]
    ) -> "PaymentMethod":
        """
        Retrieves a PaymentMethod object for a given Customer.
        """
        ...

    @overload
    def retrieve_payment_method(
        self,
        payment_method: str,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Customer.RetrievePaymentMethodParams"]
    ) -> "PaymentMethod":
        """
        Retrieves a PaymentMethod object for a given Customer.
        """
        ...

    @class_method_variant("_cls_retrieve_payment_method")
    def retrieve_payment_method(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        payment_method: str,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Customer.RetrievePaymentMethodParams"]
    ) -> "PaymentMethod":
        """
        Retrieves a PaymentMethod object for a given Customer.
        """
        return cast(
            "PaymentMethod",
            self._request(
                "get",
                "/v1/customers/{customer}/payment_methods/{payment_method}".format(
                    customer=util.sanitize_id(self.get("id")),
                    payment_method=util.sanitize_id(payment_method),
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def search(
        cls, *args, **kwargs: Unpack["Customer.SearchParams"]
    ) -> SearchResultObject["Customer"]:
        """
        Search for customers you've previously created using Stripe's [Search Query Language](https://stripe.com/docs/search#search-query-language).
        Don't use search in read-after-write flows where strict consistency is necessary. Under normal operating
        conditions, data is searchable in less than a minute. Occasionally, propagation of new or updated data can be up
        to an hour behind during outages. Search functionality is not available to merchants in India.
        """
        return cls._search(search_url="/v1/customers/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(
        cls, *args, **kwargs: Unpack["Customer.SearchParams"]
    ) -> Iterator["Customer"]:
        return cls.search(*args, **kwargs).auto_paging_iter()

    @classmethod
    def create_balance_transaction(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.CreateBalanceTransactionParams"]
    ) -> "CustomerBalanceTransaction":
        """
        Creates an immutable transaction that updates the customer's credit [balance](https://stripe.com/docs/billing/customer/balance).
        """
        return cast(
            "CustomerBalanceTransaction",
            cls._static_request(
                "post",
                "/v1/customers/{customer}/balance_transactions".format(
                    customer=util.sanitize_id(customer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def retrieve_balance_transaction(
        cls,
        customer: str,
        transaction: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.RetrieveBalanceTransactionParams"]
    ) -> "CustomerBalanceTransaction":
        """
        Retrieves a specific customer balance transaction that updated the customer's [balances](https://stripe.com/docs/billing/customer/balance).
        """
        return cast(
            "CustomerBalanceTransaction",
            cls._static_request(
                "get",
                "/v1/customers/{customer}/balance_transactions/{transaction}".format(
                    customer=util.sanitize_id(customer),
                    transaction=util.sanitize_id(transaction),
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def modify_balance_transaction(
        cls,
        customer: str,
        transaction: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ModifyBalanceTransactionParams"]
    ) -> "CustomerBalanceTransaction":
        """
        Most credit balance transaction fields are immutable, but you may update its description and metadata.
        """
        return cast(
            "CustomerBalanceTransaction",
            cls._static_request(
                "post",
                "/v1/customers/{customer}/balance_transactions/{transaction}".format(
                    customer=util.sanitize_id(customer),
                    transaction=util.sanitize_id(transaction),
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def list_balance_transactions(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ListBalanceTransactionsParams"]
    ) -> ListObject["CustomerBalanceTransaction"]:
        """
        Returns a list of transactions that updated the customer's [balances](https://stripe.com/docs/billing/customer/balance).
        """
        return cast(
            ListObject["CustomerBalanceTransaction"],
            cls._static_request(
                "get",
                "/v1/customers/{customer}/balance_transactions".format(
                    customer=util.sanitize_id(customer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def retrieve_cash_balance_transaction(
        cls,
        customer: str,
        transaction: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.RetrieveCashBalanceTransactionParams"]
    ) -> "CustomerCashBalanceTransaction":
        """
        Retrieves a specific cash balance transaction, which updated the customer's [cash balance](https://stripe.com/docs/payments/customer-balance).
        """
        return cast(
            "CustomerCashBalanceTransaction",
            cls._static_request(
                "get",
                "/v1/customers/{customer}/cash_balance_transactions/{transaction}".format(
                    customer=util.sanitize_id(customer),
                    transaction=util.sanitize_id(transaction),
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def list_cash_balance_transactions(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ListCashBalanceTransactionsParams"]
    ) -> ListObject["CustomerCashBalanceTransaction"]:
        """
        Returns a list of transactions that modified the customer's [cash balance](https://stripe.com/docs/payments/customer-balance).
        """
        return cast(
            ListObject["CustomerCashBalanceTransaction"],
            cls._static_request(
                "get",
                "/v1/customers/{customer}/cash_balance_transactions".format(
                    customer=util.sanitize_id(customer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def create_source(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.CreateSourceParams"]
    ) -> Union["Account", "BankAccount", "Card", "Source"]:
        """
        When you create a new credit card, you must specify a customer or recipient on which to create it.

        If the card's owner has no default card, then the new card will become the default.
        However, if the owner already has a default, then it will not change.
        To change the default, you should [update the customer](https://stripe.com/docs/api#update_customer) to have a new default_source.
        """
        return cast(
            Union["Account", "BankAccount", "Card", "Source"],
            cls._static_request(
                "post",
                "/v1/customers/{customer}/sources".format(
                    customer=util.sanitize_id(customer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def retrieve_source(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.RetrieveSourceParams"]
    ) -> Union["Account", "BankAccount", "Card", "Source"]:
        """
        Retrieve a specified source for a given customer.
        """
        return cast(
            Union["Account", "BankAccount", "Card", "Source"],
            cls._static_request(
                "get",
                "/v1/customers/{customer}/sources/{id}".format(
                    customer=util.sanitize_id(customer),
                    id=util.sanitize_id(id),
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def modify_source(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ModifySourceParams"]
    ) -> Union["Account", "BankAccount", "Card", "Source"]:
        """
        Update a specified source for a given customer.
        """
        return cast(
            Union["Account", "BankAccount", "Card", "Source"],
            cls._static_request(
                "post",
                "/v1/customers/{customer}/sources/{id}".format(
                    customer=util.sanitize_id(customer),
                    id=util.sanitize_id(id),
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def delete_source(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.DeleteSourceParams"]
    ) -> Union["Account", "BankAccount", "Card", "Source"]:
        """
        Delete a specified source for a given customer.
        """
        return cast(
            Union["Account", "BankAccount", "Card", "Source"],
            cls._static_request(
                "delete",
                "/v1/customers/{customer}/sources/{id}".format(
                    customer=util.sanitize_id(customer),
                    id=util.sanitize_id(id),
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def list_sources(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ListSourcesParams"]
    ) -> ListObject[Union["Account", "BankAccount", "Card", "Source"]]:
        """
        List sources for a specified customer.
        """
        return cast(
            ListObject[Union["Account", "BankAccount", "Card", "Source"]],
            cls._static_request(
                "get",
                "/v1/customers/{customer}/sources".format(
                    customer=util.sanitize_id(customer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def create_tax_id(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.CreateTaxIdParams"]
    ) -> "TaxId":
        """
        Creates a new tax_id object for a customer.
        """
        return cast(
            "TaxId",
            cls._static_request(
                "post",
                "/v1/customers/{customer}/tax_ids".format(
                    customer=util.sanitize_id(customer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def retrieve_tax_id(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.RetrieveTaxIdParams"]
    ) -> "TaxId":
        """
        Retrieves the tax_id object with the given identifier.
        """
        return cast(
            "TaxId",
            cls._static_request(
                "get",
                "/v1/customers/{customer}/tax_ids/{id}".format(
                    customer=util.sanitize_id(customer),
                    id=util.sanitize_id(id),
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def delete_tax_id(
        cls,
        customer: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.DeleteTaxIdParams"]
    ) -> "TaxId":
        """
        Deletes an existing tax_id object.
        """
        return cast(
            "TaxId",
            cls._static_request(
                "delete",
                "/v1/customers/{customer}/tax_ids/{id}".format(
                    customer=util.sanitize_id(customer),
                    id=util.sanitize_id(id),
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def list_tax_ids(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ListTaxIdsParams"]
    ) -> ListObject["TaxId"]:
        """
        Returns a list of tax IDs for a customer.
        """
        return cast(
            ListObject["TaxId"],
            cls._static_request(
                "get",
                "/v1/customers/{customer}/tax_ids".format(
                    customer=util.sanitize_id(customer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def modify_cash_balance(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.ModifyCashBalanceParams"]
    ) -> "CashBalance":
        """
        Changes the settings on a customer's cash balance.
        """
        return cast(
            "CashBalance",
            cls._static_request(
                "post",
                "/v1/customers/{customer}/cash_balance".format(
                    customer=util.sanitize_id(customer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @classmethod
    def retrieve_cash_balance(
        cls,
        customer: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Customer.RetrieveCashBalanceParams"]
    ) -> "CashBalance":
        """
        Retrieves a customer's cash balance.
        """
        return cast(
            "CashBalance",
            cls._static_request(
                "get",
                "/v1/customers/{customer}/cash_balance".format(
                    customer=util.sanitize_id(customer)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    class TestHelpers(APIResourceTestHelpers["Customer"]):
        _resource_cls: Type["Customer"]

        @classmethod
        def _cls_fund_cash_balance(
            cls,
            customer: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["Customer.FundCashBalanceParams"]
        ) -> "CustomerCashBalanceTransaction":
            """
            Create an incoming testmode bank transfer
            """
            return cast(
                "CustomerCashBalanceTransaction",
                cls._static_request(
                    "post",
                    "/v1/test_helpers/customers/{customer}/fund_cash_balance".format(
                        customer=util.sanitize_id(customer)
                    ),
                    api_key=api_key,
                    stripe_version=stripe_version,
                    stripe_account=stripe_account,
                    params=params,
                ),
            )

        @overload
        @staticmethod
        def fund_cash_balance(
            customer: str,
            api_key: Optional[str] = None,
            stripe_version: Optional[str] = None,
            stripe_account: Optional[str] = None,
            **params: Unpack["Customer.FundCashBalanceParams"]
        ) -> "CustomerCashBalanceTransaction":
            """
            Create an incoming testmode bank transfer
            """
            ...

        @overload
        def fund_cash_balance(
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["Customer.FundCashBalanceParams"]
        ) -> "CustomerCashBalanceTransaction":
            """
            Create an incoming testmode bank transfer
            """
            ...

        @class_method_variant("_cls_fund_cash_balance")
        def fund_cash_balance(  # pyright: ignore[reportGeneralTypeIssues]
            self,
            idempotency_key: Optional[str] = None,
            **params: Unpack["Customer.FundCashBalanceParams"]
        ) -> "CustomerCashBalanceTransaction":
            """
            Create an incoming testmode bank transfer
            """
            return cast(
                "CustomerCashBalanceTransaction",
                self.resource._request(
                    "post",
                    "/v1/test_helpers/customers/{customer}/fund_cash_balance".format(
                        customer=util.sanitize_id(self.resource.get("id"))
                    ),
                    idempotency_key=idempotency_key,
                    params=params,
                ),
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)

    _inner_class_types = {
        "address": Address,
        "invoice_settings": InvoiceSettings,
        "shipping": Shipping,
        "tax": Tax,
    }


Customer.TestHelpers._resource_cls = Customer
