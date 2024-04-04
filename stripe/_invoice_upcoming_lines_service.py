# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._invoice_line_item import InvoiceLineItem
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class InvoiceUpcomingLinesService(StripeService):
    class ListParams(TypedDict):
        automatic_tax: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsAutomaticTax"
        ]
        """
        Settings for automatic tax lookup for this invoice preview.
        """
        coupon: NotRequired[str]
        """
        The ID of the coupon to apply to this phase of the subscription schedule. This field has been deprecated and will be removed in a future API version. Use `discounts` instead.
        """
        currency: NotRequired[str]
        """
        The currency to preview this invoice in. Defaults to that of `customer` if not specified.
        """
        customer: NotRequired[str]
        """
        The identifier of the customer whose upcoming invoice you'd like to retrieve. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set.
        """
        customer_details: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsCustomerDetails"
        ]
        """
        Details about the customer you want to invoice or overrides for an existing customer. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set.
        """
        discounts: NotRequired[
            "Literal['']|List[InvoiceUpcomingLinesService.ListParamsDiscount]"
        ]
        """
        The coupons to redeem into discounts for the invoice preview. If not specified, inherits the discount from the subscription or customer. This works for both coupons directly applied to an invoice and coupons applied to a subscription. Pass an empty string to avoid inheriting any discounts.
        """
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        invoice_items: NotRequired[
            List["InvoiceUpcomingLinesService.ListParamsInvoiceItem"]
        ]
        """
        List of invoice items to add or update in the upcoming invoice preview.
        """
        issuer: NotRequired["InvoiceUpcomingLinesService.ListParamsIssuer"]
        """
        The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        on_behalf_of: NotRequired["Literal['']|str"]
        """
        The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details.
        """
        schedule: NotRequired[str]
        """
        The identifier of the schedule whose upcoming invoice you'd like to retrieve. Cannot be used with subscription or subscription fields.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        subscription: NotRequired[str]
        """
        The identifier of the subscription for which you'd like to retrieve the upcoming invoice. If not provided, but a `subscription_items` is provided, you will preview creating a subscription with those items. If neither `subscription` nor `subscription_items` is provided, you will retrieve the next upcoming invoice from among the customer's subscriptions.
        """
        subscription_billing_cycle_anchor: NotRequired[
            "Literal['now', 'unchanged']|int"
        ]
        """
        For new subscriptions, a future timestamp to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). This is used to determine the date of the first full invoice, and, for plans with `month` or `year` intervals, the day of the month for subsequent invoices. For existing subscriptions, the value can only be set to `now` or `unchanged`.
        """
        subscription_cancel_at: NotRequired["Literal['']|int"]
        """
        A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.
        """
        subscription_cancel_at_period_end: NotRequired[bool]
        """
        Boolean indicating whether this subscription should cancel at the end of the current period.
        """
        subscription_cancel_now: NotRequired[bool]
        """
        This simulates the subscription being canceled or expired immediately.
        """
        subscription_default_tax_rates: NotRequired["Literal['']|List[str]"]
        """
        If provided, the invoice returned will preview updating or creating a subscription with these default tax rates. The default tax rates will apply to any line item that does not have `tax_rates` set.
        """
        subscription_items: NotRequired[
            List["InvoiceUpcomingLinesService.ListParamsSubscriptionItem"]
        ]
        """
        A list of up to 20 subscription items, each with an attached price.
        """
        subscription_proration_behavior: NotRequired[
            Literal["always_invoice", "create_prorations", "none"]
        ]
        """
        Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
        """
        subscription_proration_date: NotRequired[int]
        """
        If previewing an update to a subscription, and doing proration, `subscription_proration_date` forces the proration to be calculated as though the update was done at the specified time. The time given must be within the current subscription period and within the current phase of the schedule backing this subscription, if the schedule exists. If set, `subscription`, and one of `subscription_items`, or `subscription_trial_end` are required. Also, `subscription_proration_behavior` cannot be set to 'none'.
        """
        subscription_resume_at: NotRequired[Literal["now"]]
        """
        For paused subscriptions, setting `subscription_resume_at` to `now` will preview the invoice that will be generated if the subscription is resumed.
        """
        subscription_start_date: NotRequired[int]
        """
        Date a subscription is intended to start (can be future or past).
        """
        subscription_trial_end: NotRequired["Literal['now']|int"]
        """
        If provided, the invoice returned will preview updating or creating a subscription with that trial end. If set, one of `subscription_items` or `subscription` is required.
        """
        subscription_trial_from_plan: NotRequired[bool]
        """
        Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `subscription_trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `subscription_trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
        """

    class ListParamsAutomaticTax(TypedDict):
        enabled: bool
        """
        Whether Stripe automatically computes tax on this invoice. Note that incompatible invoice items (invoice items with manually specified [tax rates](https://stripe.com/docs/api/tax_rates), negative amounts, or `tax_behavior=unspecified`) cannot be added to automatic tax invoices.
        """
        liability: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsAutomaticTaxLiability"
        ]
        """
        The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
        """

    class ListParamsAutomaticTaxLiability(TypedDict):
        account: NotRequired[str]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class ListParamsCustomerDetails(TypedDict):
        address: NotRequired[
            "Literal['']|InvoiceUpcomingLinesService.ListParamsCustomerDetailsAddress"
        ]
        """
        The customer's address.
        """
        shipping: NotRequired[
            "Literal['']|InvoiceUpcomingLinesService.ListParamsCustomerDetailsShipping"
        ]
        """
        The customer's shipping information. Appears on invoices emailed to this customer.
        """
        tax: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsCustomerDetailsTax"
        ]
        """
        Tax details about the customer.
        """
        tax_exempt: NotRequired[
            "Literal['']|Literal['exempt', 'none', 'reverse']"
        ]
        """
        The customer's tax exemption. One of `none`, `exempt`, or `reverse`.
        """
        tax_ids: NotRequired[
            List["InvoiceUpcomingLinesService.ListParamsCustomerDetailsTaxId"]
        ]
        """
        The customer's tax IDs.
        """

    class ListParamsCustomerDetailsAddress(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[str]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[str]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[str]
        """
        ZIP or postal code.
        """
        state: NotRequired[str]
        """
        State, county, province, or region.
        """

    class ListParamsCustomerDetailsShipping(TypedDict):
        address: "InvoiceUpcomingLinesService.ListParamsCustomerDetailsShippingAddress"
        """
        Customer shipping address.
        """
        name: str
        """
        Customer name.
        """
        phone: NotRequired[str]
        """
        Customer phone (including extension).
        """

    class ListParamsCustomerDetailsShippingAddress(TypedDict):
        city: NotRequired[str]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired[str]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired[str]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired[str]
        """
        ZIP or postal code.
        """
        state: NotRequired[str]
        """
        State, county, province, or region.
        """

    class ListParamsCustomerDetailsTax(TypedDict):
        ip_address: NotRequired["Literal['']|str"]
        """
        A recent IP address of the customer used for tax reporting and tax location inference. Stripe recommends updating the IP address when a new PaymentMethod is attached or the address field on the customer is updated. We recommend against updating this field more frequently since it could result in unexpected tax location/reporting outcomes.
        """

    class ListParamsCustomerDetailsTaxId(TypedDict):
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
            "no_voec",
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
        Type of the tax ID, one of `ad_nrt`, `ae_trn`, `ar_cuit`, `au_abn`, `au_arn`, `bg_uic`, `bo_tin`, `br_cnpj`, `br_cpf`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `ch_vat`, `cl_tin`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `hk_br`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kr_brn`, `li_uid`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `no_vat`, `no_voec`, `nz_gst`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sv_nit`, `th_vat`, `tr_tin`, `tw_vat`, `ua_vat`, `us_ein`, `uy_ruc`, `ve_rif`, `vn_tin`, or `za_vat`
        """
        value: str
        """
        Value of the tax ID.
        """

    class ListParamsDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired[str]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        promotion_code: NotRequired[str]
        """
        ID of the promotion code to create a new discount for.
        """

    class ListParamsInvoiceItem(TypedDict):
        amount: NotRequired[int]
        """
        The integer amount in cents (or local equivalent) of previewed invoice item.
        """
        currency: NotRequired[str]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Only applicable to new invoice items.
        """
        description: NotRequired[str]
        """
        An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.
        """
        discountable: NotRequired[bool]
        """
        Explicitly controls whether discounts apply to this invoice item. Defaults to true, except for negative invoice items.
        """
        discounts: NotRequired[
            "Literal['']|List[InvoiceUpcomingLinesService.ListParamsInvoiceItemDiscount]"
        ]
        """
        The coupons to redeem into discounts for the invoice item in the preview.
        """
        invoiceitem: NotRequired[str]
        """
        The ID of the invoice item to update in preview. If not specified, a new invoice item will be added to the preview of the upcoming invoice.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        period: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsInvoiceItemPeriod"
        ]
        """
        The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
        """
        price: NotRequired[str]
        """
        The ID of the price object.
        """
        price_data: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsInvoiceItemPriceData"
        ]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
        """
        quantity: NotRequired[int]
        """
        Non-negative integer. The quantity of units for the invoice item.
        """
        tax_behavior: NotRequired[
            Literal["exclusive", "inclusive", "unspecified"]
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        tax_code: NotRequired["Literal['']|str"]
        """
        A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        The tax rates that apply to the item. When set, any `default_tax_rates` do not apply to this item.
        """
        unit_amount: NotRequired[int]
        """
        The integer unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This unit_amount will be multiplied by the quantity to get the full amount. If you want to apply a credit to the customer's account, pass a negative unit_amount.
        """
        unit_amount_decimal: NotRequired[str]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class ListParamsInvoiceItemDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired[str]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        promotion_code: NotRequired[str]
        """
        ID of the promotion code to create a new discount for.
        """

    class ListParamsInvoiceItemPeriod(TypedDict):
        end: int
        """
        The end of the period, which must be greater than or equal to the start. This value is inclusive.
        """
        start: int
        """
        The start of the period. This value is inclusive.
        """

    class ListParamsInvoiceItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        tax_behavior: NotRequired[
            Literal["exclusive", "inclusive", "unspecified"]
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired[int]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired[str]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class ListParamsIssuer(TypedDict):
        account: NotRequired[str]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced in the request.
        """

    class ListParamsSubscriptionItem(TypedDict):
        billing_thresholds: NotRequired[
            "Literal['']|InvoiceUpcomingLinesService.ListParamsSubscriptionItemBillingThresholds"
        ]
        """
        Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.
        """
        clear_usage: NotRequired[bool]
        """
        Delete all usage for a given subscription item. Allowed only when `deleted` is set to `true` and the current plan's `usage_type` is `metered`.
        """
        deleted: NotRequired[bool]
        """
        A flag that, if set to `true`, will delete the specified item.
        """
        discounts: NotRequired[
            "Literal['']|List[InvoiceUpcomingLinesService.ListParamsSubscriptionItemDiscount]"
        ]
        """
        The coupons to redeem into discounts for the subscription item.
        """
        id: NotRequired[str]
        """
        Subscription item to update.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        plan: NotRequired[str]
        """
        Plan ID for this item, as a string.
        """
        price: NotRequired[str]
        """
        The ID of the price object. When changing a subscription item's price, `quantity` is set to 1 unless a `quantity` parameter is provided.
        """
        price_data: NotRequired[
            "InvoiceUpcomingLinesService.ListParamsSubscriptionItemPriceData"
        ]
        """
        Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
        """
        quantity: NotRequired[int]
        """
        Quantity for this item.
        """
        tax_rates: NotRequired["Literal['']|List[str]"]
        """
        A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates.
        """

    class ListParamsSubscriptionItemBillingThresholds(TypedDict):
        usage_gte: int
        """
        Number of units that meets the billing threshold to advance the subscription to a new billing period (e.g., it takes 10 $5 units to meet a $50 [monetary threshold](https://stripe.com/docs/api/subscriptions/update#update_subscription-billing_thresholds-amount_gte))
        """

    class ListParamsSubscriptionItemDiscount(TypedDict):
        coupon: NotRequired[str]
        """
        ID of the coupon to create a new discount for.
        """
        discount: NotRequired[str]
        """
        ID of an existing discount on the object (or one of its ancestors) to reuse.
        """
        promotion_code: NotRequired[str]
        """
        ID of the promotion code to create a new discount for.
        """

    class ListParamsSubscriptionItemPriceData(TypedDict):
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        product: str
        """
        The ID of the product that this price will belong to.
        """
        recurring: "InvoiceUpcomingLinesService.ListParamsSubscriptionItemPriceDataRecurring"
        """
        The recurring components of a price such as `interval` and `interval_count`.
        """
        tax_behavior: NotRequired[
            Literal["exclusive", "inclusive", "unspecified"]
        ]
        """
        Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
        """
        unit_amount: NotRequired[int]
        """
        A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge.
        """
        unit_amount_decimal: NotRequired[str]
        """
        Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set.
        """

    class ListParamsSubscriptionItemPriceDataRecurring(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        Specifies billing frequency. Either `day`, `week`, `month` or `year`.
        """
        interval_count: NotRequired[int]
        """
        The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
        """

    def list(
        self,
        params: "InvoiceUpcomingLinesService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[InvoiceLineItem]:
        """
        When retrieving an upcoming invoice, you'll get a lines property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject[InvoiceLineItem],
            self._request(
                "get",
                "/v1/invoices/upcoming/lines",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "InvoiceUpcomingLinesService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[InvoiceLineItem]:
        """
        When retrieving an upcoming invoice, you'll get a lines property containing the total count of line items and the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        return cast(
            ListObject[InvoiceLineItem],
            await self._request_async(
                "get",
                "/v1/invoices/upcoming/lines",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
