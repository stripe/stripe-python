---
title: Update generated code for private-preview
pr_url: https://github.com/stripe/stripe-python/pull/1674
is_stripe_api_change: true
released_in_version: 14.1.0a1
---

* Add support for new resources `BalanceTransfer` and `radar.AccountEvaluation`
* Add support for `create` method on resource `BalanceTransfer`
* Add support for `create`, `modify`, and `retrieve` methods on resource `radar.AccountEvaluation`
* Change `Tax.Association.tax_transaction_attempts` to be required
* Add support for `specified_commercial_transactions_act_url` on `Account.BusinessProfile`, `AccountCreateParamsBusinessProfile`, and `AccountModifyParamsBusinessProfile`
* Add support for `paypay_payments` on `Account.Setting`, `AccountCreateParamsSetting`, and `AccountModifyParamsSetting`
* Change type of `billing.analytics.MeterUsageRetrieveParamsMeter.dimension_filters` from `string` to `array(string)`
* Change type of `billing.analytics.MeterUsageRetrieveParamsMeter.tenant_filters` from `string` to `array(string)`
* Add support for `payment_method_configuration` on `BillingPortal.Configuration.Feature.PaymentMethodUpdate`
* Add support for `car_rental_data`, `flight_data`, and `lodging_data` on `ChargeCaptureParamsPaymentDetail`, `ChargeModifyParamsPaymentDetail`, `PaymentIntentCaptureParamsPaymentDetail`, `PaymentIntentConfirmParamsPaymentDetail`, `PaymentIntentCreateParamsPaymentDetail`, and `PaymentIntentModifyParamsPaymentDetail`
* Add support for `transaction_id` on `Charge.PaymentMethodDetail.Ideal`, `PaymentAttemptRecord.PaymentMethodDetail.Ideal`, and `PaymentRecord.PaymentMethodDetail.Ideal`
* Add support for new value `finom` on enums `Charge.PaymentMethodDetail.Ideal.bank`, `ConfirmationToken.PaymentMethodPreview.Ideal.bank`, `ConfirmationTokenCreateParamsPaymentMethodDatumIdeal.bank`, `PaymentAttemptRecord.PaymentMethodDetail.Ideal.bank`, `PaymentIntentConfirmParamsPaymentMethodDatumIdeal.bank`, `PaymentIntentCreateParamsPaymentMethodDatumIdeal.bank`, `PaymentIntentModifyParamsPaymentMethodDatumIdeal.bank`, `PaymentMethod.Ideal.bank`, `PaymentMethodCreateParamsIdeal.bank`, `PaymentRecord.PaymentMethodDetail.Ideal.bank`, `SetupAttempt.PaymentMethodDetail.Ideal.bank`, `SetupIntentConfirmParamsPaymentMethodDatumIdeal.bank`, `SetupIntentCreateParamsPaymentMethodDatumIdeal.bank`, and `SetupIntentModifyParamsPaymentMethodDatumIdeal.bank`
* Add support for new value `FNOMNL22` on enums `Charge.PaymentMethodDetail.Ideal.bic`, `ConfirmationToken.PaymentMethodPreview.Ideal.bic`, `PaymentAttemptRecord.PaymentMethodDetail.Ideal.bic`, `PaymentMethod.Ideal.bic`, `PaymentRecord.PaymentMethodDetail.Ideal.bic`, and `SetupAttempt.PaymentMethodDetail.Ideal.bic`
* Add support for new value `tokenized_account_number_deactivated` on enums `ConfirmationToken.PaymentMethodPreview.UsBankAccount.StatusDetail.Blocked.reason` and `PaymentMethod.UsBankAccount.StatusDetail.Blocked.reason`
* Add support for `created` on `CustomerListCustomerBalanceTransactionParams` and `InvoicePaymentListParams`
* Add support for new values `capital.financing_offer.accepted_other_offer`, `financial_connections.account.account_numbers_updated`, and `financial_connections.account.upcoming_account_number_expiry` on enum `Event.type`
* Add support for `account_numbers` on `FinancialConnections.Account`
* Change type of `FinancialConnections.Session.client_secret` from `string` to `nullable(string)`
* Add support for `fraud_risk` on `issuing.AuthorizationCreateParamsRiskAssessment`
* Add support for `latest_fraud_warning` on `Issuing.Card`
* Add support for `supplementary_purchase_data` on `OrderCreateParamsPaymentSettingPaymentMethodOptionKlarna`, `OrderModifyParamsPaymentSettingPaymentMethodOptionKlarna`, `PaymentIntentConfirmParamsPaymentMethodOptionKlarna`, `PaymentIntentCreateParamsPaymentMethodOptionKlarna`, and `PaymentIntentModifyParamsPaymentMethodOptionKlarna`
* Add support for `capture_method` on `PaymentIntent.PaymentMethodOption.CardPresent`, `PaymentIntentConfirmParamsPaymentMethodOptionCardPresent`, `PaymentIntentCreateParamsPaymentMethodOptionCardPresent`, and `PaymentIntentModifyParamsPaymentMethodOptionCardPresent`
* Add support for `allow_redisplay` and `customer_account` on `PaymentMethodListParams`
* Add support for `mb_way` and `twint` on `Refund.DestinationDetail`
* Change type of `SubscriptionScheduleModifyParams.billing_schedules` from `array(billing_schedules_update_params)` to `emptyable(array(billing_schedules_update_params))`
* Add support for new values `capital.financing_offer.accepted_other_offer`, `financial_connections.account.account_numbers_updated`, and `financial_connections.account.upcoming_account_number_expiry` on enums `WebhookEndpointCreateParams.enabled_events` and `WebhookEndpointModifyParams.enabled_events`
* Add support for new value `2025-11-17.clover` on enum `WebhookEndpointCreateParams.api_version`
* Add support for snapshot events `financial_connections.account.account_numbers_updated` and `financial_connections.account.upcoming_account_number_expiry` with resource `financial_connections.Account`
