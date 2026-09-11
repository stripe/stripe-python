---
title: Update generated code for private-preview
pr_link: https://github.com/stripe/stripe-python/pull/1726
is_stripe_api_change: true
released_in_version: 14.4.0a1
---

* Add support for new resources `FrMealVouchersOnboarding`, `reserve.Hold`, `reserve.Plan`, and `reserve.Release`
* Add support for `create`, `list`, `modify`, and `retrieve` methods on resource `FrMealVouchersOnboarding`
* Add support for `list` and `retrieve` methods on resources `reserve.Hold` and `reserve.Release`
* Add support for `retrieve` method on resource `reserve.Plan`
* Add support for `pause` method on resource `Subscription`
* Add support for `service_period_details` on `Discount`
* Add support for `agentic_commerce_settings` on `AccountSession.Component`
* Add support for new value `risk_reserved` on enum `BalanceTransaction.balance_type`
* Add support for new value `service_period` on enums `Coupon.duration`, `CouponCreateParams.duration`, `checkout.SessionCreateParamsDiscountCouponDatum.duration`, and `checkout.SessionModifyParamsDiscountCouponDatum.duration`
* Add support for `service_period` on `CouponCreateParams` and `Coupon`
* Change type of `InvoiceItem.Pricing.PriceDetail.price` and `InvoiceLineItem.Pricing.PriceDetail.price` from `string` to `expandable($Price)`
* Add support for `settings` on `InvoiceCreatePreviewParamsDiscount`, `InvoiceCreatePreviewParamsScheduleDetailAmendmentDiscountActionAdd`, `InvoiceCreatePreviewParamsScheduleDetailAmendmentDiscountActionSet`, `InvoiceCreatePreviewParamsScheduleDetailAmendmentItemActionAddDiscount`, `InvoiceCreatePreviewParamsScheduleDetailAmendmentItemActionSetDiscount`, `InvoiceCreatePreviewParamsScheduleDetailPhaseDiscount`, `InvoiceCreatePreviewParamsScheduleDetailPhaseItemDiscount`, `InvoiceCreatePreviewParamsSubscriptionDetailItemDiscount`, `QuoteCreateParamsLineActionAddDiscount`, `QuoteCreateParamsLineActionAddItemDiscount`, `QuoteCreateParamsLineActionSetDiscount`, `QuoteCreateParamsLineActionSetItemDiscount`, `QuoteModifyParamsLineActionAddDiscount`, `QuoteModifyParamsLineActionAddItemDiscount`, `QuoteModifyParamsLineActionSetDiscount`, `QuoteModifyParamsLineActionSetItemDiscount`, `SubscriptionCreateParamsDiscount`, `SubscriptionCreateParamsItemDiscount`, `SubscriptionItemCreateParamsDiscount`, `SubscriptionItemModifyParamsDiscount`, `SubscriptionModifyParamsDiscount`, `SubscriptionModifyParamsItemDiscount`, `SubscriptionScheduleAmendParamsAmendmentDiscountActionAdd`, `SubscriptionScheduleAmendParamsAmendmentDiscountActionSet`, `SubscriptionScheduleAmendParamsAmendmentItemActionAddDiscount`, `SubscriptionScheduleAmendParamsAmendmentItemActionSetDiscount`, `SubscriptionScheduleCreateParamsPhaseDiscount`, `SubscriptionScheduleCreateParamsPhaseItemDiscount`, `SubscriptionScheduleModifyParamsPhaseDiscount`, and `SubscriptionScheduleModifyParamsPhaseItemDiscount`
* Add support for `subtotal` on `InvoiceLineItem`
* Add support for `billing_cadence` on `SubscriptionListParams`
