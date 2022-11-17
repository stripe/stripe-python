# Changelog

## 5.0.0 - 2022-11-16

Breaking changes that arose during code generation of the library that we postponed for the next major version. For changes to the Stripe products, read more at https://stripe.com/docs/upgrades#2022-11-15.

"⚠️" symbol highlights breaking changes.

* [#895](https://github.com/stripe/stripe-python/pull/895) Next major release changes
* [#889](https://github.com/stripe/stripe-python/pull/889) API Updates

* [#888](https://github.com/stripe/stripe-python/pull/888) Do not run Coveralls if secret token is not available
* [#875](https://github.com/stripe/stripe-python/pull/875) hide misleading ssl security warning in python>=2.7.9

### ⚠️ Changed
- Dropped support for Python version 3.4 and 3.5 (#881). We now support Python 2.7 or 3.6+.
- Fixed mistyped names for two OAuth exceptions: `UnsupportedGrantTypError`->`UnsupportedGrantTypeError` and `UnsupportedResponseTypError`->`UnsupportedResponseTypeError` (#872).

### Deprecated
- Deprecate `save` method on resources (#887). Use `modify` instead.
   ```python
  # Before
  customer = stripe.Customer.retrieve("cus_123")
  customer.email = "example@test.com"
  customer.save()

  # After
  stripe.Customer.modify("cus_123", email="example@test.com")
   ```

### ⚠️ Removed
- Removed `Orders` resource (#882).
- Removed `SKU` resource (#883).

## 4.2.0 - 2022-09-23
* [#877](https://github.com/stripe/stripe-python/pull/877) API Updates
  * Add `upcoming_lines` method to the `Invoice` resource.
* [#873](https://github.com/stripe/stripe-python/pull/873) Add abstract methods for SearchableAPIResource
* [#867](https://github.com/stripe/stripe-python/pull/867) API Updates
  * Update links in documentation to be absolute.

## 4.1.0 - 2022-08-19
* [#861](https://github.com/stripe/stripe-python/pull/861) API Updates
  * Add support for new resource `CustomerCashBalanceTransaction`
* [#860](https://github.com/stripe/stripe-python/pull/860) Add a support section to the readme
* [#717](https://github.com/stripe/stripe-python/pull/717) Fix test TestCharge.test_is_saveable().

## 4.0.2 - 2022-08-03
* [#855](https://github.com/stripe/stripe-python/pull/855) Fix issue where auto_paging_iter failed on nested list objects.

## 4.0.1 - 2022-08-02
* [#850](https://github.com/stripe/stripe-python/pull/850) Fix incorrect handling of additional request parameters
  * Fixes issue where using special parameter like `api_key`, `idempotency_key`, `stripe_version`, `stripe_account`, `headers` can cause a `Received unknown parameter error`.

## 4.0.0 - 2022-08-02

Breaking changes that arose during code generation of the library that we postponed for the next major version. For changes to the SDK, read more detailed description at https://github.com/stripe/stripe-python/wiki/Migration-guide-for-v4. For changes to the Stripe products, read more at https://stripe.com/docs/upgrades#2022-08-01.

"⚠️" symbol highlights breaking changes.

* [#847](https://github.com/stripe/stripe-python/pull/847) API Updates
* [#845](https://github.com/stripe/stripe-python/pull/845) Next major release changes
* [#836](https://github.com/stripe/stripe-python/pull/836) API Updates. Add Price.create tests.
* [#835](https://github.com/stripe/stripe-python/pull/835) API Updates. Use auto-generation for credit_note and invoice methods.

### ⚠️ Removed
- Removed deprecated `AlipayAccount`, `BitcoinReceiver`, `BitcoinTransaction`, `IssuerFraudRecord`, `Recipient`, `RecipientTransfer`, and  `ThreeDSecure` classes.
- Removed deprecated `Charge.update_dispute` and `Charge.close_dispute` methods that were using legacy REST API endpoint. Prefer [Dispute.modify](https://stripe.com/docs/api/disputes/update?lang=python) and [Dispute.close](https://stripe.com/docs/api/disputes/close?lang=python)
- Removed deprecated `Card.details` method and `CardDetails` resource. The REST API endpoint is not longer supported.
- Removed the deprecated `Source.source_transactions` method. Prefer `SubscriptionItem.list_source_transactions`
- Removed the deprecated `SubscriptionItem.usage_record_summaries` method. Prefer `SubscriptionItem.list_usage_record_summaries`
- Removed the deprecated `Charge.refund` method. Prefer [Refund.create](https://stripe.com/docs/api/refunds/create)

### ⚠️ Changed
- To be consistent with other resource methods, `ApplicationFee.refund` returns an instance of `ApplicationFee` and doesn't mutate the instance of `ApplicationFee`.
- To be consistent with other resource methods, the `Customer.delete_discount` no longer resets the `discount` property to `None` and returns the deleted discount instead. If you were relying on this behavior, reset the discount property manually:
- The `LineItem` resource now inherits from `StripeObject` as it has no methods of it's own.
- To be consistent with other resource methods, the `Subscription.delete_discount` returns an instance of deleted discount and doesn't mutate the instance of `Subscription`.
- Update the CA certificate bundle.
- Request sending logic unified across standard and custom methods (https://github.com/stripe/stripe-python/pull/832)

## 3.5.0 - 2022-06-30
* [#831](https://github.com/stripe/stripe-python/pull/831) API Updates
  * Add support for `deliver_card`, `fail_card`, `return_card`, and `ship_card` test helper methods on resource `Issuing.Card`
  * Switch from using `instance_url` to computing method path in place for custom methods.
  * Switch from using explicit class methods for test helpers instead of using meta-programming.

## 3.4.0 - 2022-06-17
* [#824](https://github.com/stripe/stripe-python/pull/824) API Updates
  * Add support for `fund_cash_balance` test helper method on resource `Customer`
* [#823](https://github.com/stripe/stripe-python/pull/823) Trigger workflows on beta branches

## 3.3.0 - 2022-06-08
* [#818](https://github.com/stripe/stripe-python/pull/818) fix: Update cash balance methods to no longer require nested ID.

## 3.2.0 - 2022-05-23
* [#812](https://github.com/stripe/stripe-python/pull/812) API Updates
  * Add support for new resource `Apps.Secret`

## 3.1.0 - 2022-05-19
* [#810](https://github.com/stripe/stripe-python/pull/810) API Updates
  * Add support for new resources `Treasury.CreditReversal`, `Treasury.DebitReversal`, `Treasury.FinancialAccountFeatures`, `Treasury.FinancialAccount`, `Treasury.FlowDetails`, `Treasury.InboundTransfer`, `Treasury.OutboundPayment`, `Treasury.OutboundTransfer`, `Treasury.ReceivedCredit`, `Treasury.ReceivedDebit`, `Treasury.TransactionEntry`, and `Treasury.Transaction`
  * Add support for `retrieve_payment_method` method on resource `Customer`
  * Add support for `list_owners` and `list` methods on resource `FinancialConnections.Account`
* [#719](https://github.com/stripe/stripe-python/pull/719) Set daemon attribute instead of using setDaemon method that was deprecated in Python 3.10
* [#767](https://github.com/stripe/stripe-python/pull/767) Bump vendored six to 1.16.0
* [#806](https://github.com/stripe/stripe-python/pull/806) Start testing on pypy-3.8
* [#811](https://github.com/stripe/stripe-python/pull/811) Add sanitize_id method


## 3.0.0 - 2022-05-09
* [#809](https://github.com/stripe/stripe-python/pull/809) Release of major version v3.0.0. The [migration guide](https://github.com/stripe/stripe-python/wiki/Migration-Guide-for-v3) contains more information.
  (⚠️ = breaking changes):
  * ⚠️ Replace the legacy `Order` API with the new `Order` API.
    * New methods: `cancel`, `list_line_items`, `reopen`, and `submit`
    * Removed methods: `pay` and `return_order`
    * Removed resources: `OrderItem` and `OrderReturn`
  * ⚠️ Rename `financial_connections.account.refresh` to `financial_connections.refresh_account`
  * Add support for `amount_discount`, `amount_tax`, and `product` on `LineItem`

## 2.76.0 - 2022-05-05
* [#808](https://github.com/stripe/stripe-python/pull/808) API Updates
  * Add support for new resources `FinancialConnections.AccountOwner`, `FinancialConnections.AccountOwnership`, `FinancialConnections.Account`, and `FinancialConnections.Session`

## 2.75.0 - 2022-05-03
* [#805](https://github.com/stripe/stripe-python/pull/805) API Updates
  * Add support for new resource `CashBalance`

## 2.74.0 - 2022-04-21
* [#796](https://github.com/stripe/stripe-python/pull/796) API Updates
  * Add support for `expire` test helper method on resource `Refund`

## 2.73.0 - 2022-04-18
* [#792](https://github.com/stripe/stripe-python/pull/792) [#794](https://github.com/stripe/stripe-python/pull/794) [#795](https://github.com/stripe/stripe-python/pull/795) API Updates
  * Add support for new resources `FundingInstructions` and `Terminal.Configuration`

## 2.72.0 - 2022-04-13
* [#791](https://github.com/stripe/stripe-python/pull/791) API Updates
  * Add support for `increment_authorization` method on resource `PaymentIntent`

## 2.71.0 - 2022-04-08
* [#788](https://github.com/stripe/stripe-python/pull/788) API Updates
  * Add support for `apply_customer_balance` method on resource `PaymentIntent`

## 2.70.0 - 2022-03-30
* [#785](https://github.com/stripe/stripe-python/pull/785) API Updates
  * Add support for `cancel_action`, `process_payment_intent`, `process_setup_intent`, and `set_reader_display` methods on resource `Terminal.Reader`

## 2.69.0 - 2022-03-29
* [#783](https://github.com/stripe/stripe-python/pull/783) API Updates
  * Add support for Search API
    * Add support for `search` method on resources `Charge`, `Customer`, `Invoice`, `PaymentIntent`, `Price`, `Product`, and `Subscription`
* [#784](https://github.com/stripe/stripe-python/pull/784) Pin click dependency to 8.0.4 to avoid breakage in black
* [#773](https://github.com/stripe/stripe-python/pull/773) Add infrastructure for test-helper methods
* [#782](https://github.com/stripe/stripe-python/pull/782) Revert Orders to use qualified name for upload_api_base

## 2.68.0 - 2022-03-23
* [#781](https://github.com/stripe/stripe-python/pull/781) API Updates
  * Add support for `cancel` method on resource `Refund`
* [#777](https://github.com/stripe/stripe-python/pull/777) Add support for SearchResult.

## 2.67.0 - 2022-03-01
* [#774](https://github.com/stripe/stripe-python/pull/774) API Updates
  * Add support for new resource `TestHelpers.TestClock`

## 2.66.0 - 2022-02-16
* [#771](https://github.com/stripe/stripe-python/pull/771) API Updates
  * Add support for `verify_microdeposits` method on resources `PaymentIntent` and `SetupIntent`

## 2.65.0 - 2022-01-20
* [#766](https://github.com/stripe/stripe-python/pull/766) API Updates
  * Add support for new resource `PaymentLink`
* [#763](https://github.com/stripe/stripe-python/pull/763) Start testing Python 3.10

## 2.64.0 - 2021-12-21
* [#757](https://github.com/stripe/stripe-python/pull/757) Update class custom methods to save list object parameters.
* [#756](https://github.com/stripe/stripe-python/pull/756) Introduce custom listing methods on objects.
* [#754](https://github.com/stripe/stripe-python/pull/754) Clarify metadata deletion message.

## 2.63.0 - 2021-11-16
* [#748](https://github.com/stripe/stripe-python/pull/748) API Updates
  * Add support for new resource `ShippingRate`

## 2.62.0 - 2021-11-11
* [#745](https://github.com/stripe/stripe-python/pull/745) API Updates
  * Add support for `expire` method on resource `Checkout.Session`

## 2.61.0 - 2021-10-11
* [#738](https://github.com/stripe/stripe-python/pull/738) API Updates
  * Add support for `list_payment_methods` method on resource `Customer`
* [#736](https://github.com/stripe/stripe-python/pull/736) Stop sending raw exception message as part of Stripe user agent.

## 2.60.0 - 2021-07-14
* [#728](https://github.com/stripe/stripe-python/pull/728) API Updates
  * Add support for `list_computed_upfront_line_items` method on resource `Quote`

## 2.59.0 - 2021-07-09
* [#727](https://github.com/stripe/stripe-python/pull/727) [#725](https://github.com/stripe/stripe-python/pull/725) Add support for new `Quote` API.

## 2.58.0 - 2021-06-04
* [#722](https://github.com/stripe/stripe-python/pull/722) API Updates
  * Add support for new `TaxCode` API.

## 2.57.0 - 2021-05-19
* [#720](https://github.com/stripe/stripe-python/pull/720) Add support for Identity VerificationSession and VerificationReport APIs

## 2.56.0 - 2021-02-22
* [#713](https://github.com/stripe/stripe-python/pull/713) Add support for the Billing Portal Configuration API

## 2.55.2 - 2021-02-05
* [#704](https://github.com/stripe/stripe-python/pull/704) Fix CA bundle path issue

## 2.55.1 - 2020-12-01
* [#698](https://github.com/stripe/stripe-python/pull/698) Fix issue where StripeObjects in lists would not be converted to dicts
* [#699](https://github.com/stripe/stripe-python/pull/699) Start testing Python 3.9
* [#691](https://github.com/stripe/stripe-python/pull/691) Include the examples in the built sources

## 2.55.0 - 2020-10-14
* [#684](https://github.com/stripe/stripe-python/pull/684) Add support for the Payout Reverse API

## 2.54.0 - 2020-09-29
* [#681](https://github.com/stripe/stripe-python/pull/681) Add support for the `SetupAttempt` resource and List API
* 2.52.0 and 2.53.0 were empty releases that contained no additional changes.

## 2.51.0 - 2020-09-02
* [#676](https://github.com/stripe/stripe-python/pull/676) Add support for the Issuing Dispute Submit API

## 2.50.0 - 2020-08-05
* [#669](https://github.com/stripe/stripe-python/pull/669) Add support for the `PromotionCode` resource and APIs

## 2.49.0 - 2020-07-17
* [#665](https://github.com/stripe/stripe-python/pull/665) Support stripe.File.create(stripe_version='...')

## 2.48.0 - 2020-05-11
* [#655](https://github.com/stripe/stripe-python/pull/655) Add support for the `LineItem` resource and APIs

## 2.47.0 - 2020-04-29
* [#652](https://github.com/stripe/stripe-python/pull/652) Add support for the `Price` resource and APIs

## 2.46.0 - 2020-04-22
* [#651](https://github.com/stripe/stripe-python/pull/651) Add support for `billing_portal` namespace and `Session` resource and APIs

## 2.45.0 - 2020-04-06
* [#648](https://github.com/stripe/stripe-python/pull/648) Add support for Express links in `authorize_url` for `OAuth`

## 2.44.0 - 2020-03-23
* [#646](https://github.com/stripe/stripe-python/pull/646) Allow overriding API key in OAuth methods

## 2.43.0 - 2020-02-26
* [#644](https://github.com/stripe/stripe-python/pull/644) Add support for listing Checkout `Session`

## 2.42.0 - 2020-01-14
* [#640](https://github.com/stripe/stripe-python/pull/640) Add support for `CreditNoteLineItem`
* [#639](https://github.com/stripe/stripe-python/pull/639) Pin black version
* [#637](https://github.com/stripe/stripe-python/pull/637) Start testing Python 3.8

## 2.41.1 - 2019-12-30
* [#636](https://github.com/stripe/stripe-python/pull/636) Fix uploading files with Unicode names (Python 2.7)
* [#635](https://github.com/stripe/stripe-python/pull/635) Update Python API docs inline link
* [#631](https://github.com/stripe/stripe-python/pull/631) Update `proxy.py`

## 2.41.0 - 2019-11-26
* [#630](https://github.com/stripe/stripe-python/pull/630) Add support for `CreditNote` preview

## 2.40.0 - 2019-11-08
* [#627](https://github.com/stripe/stripe-python/pull/627) Add list_usage_record_summaries and list_source_transactions

## 2.39.0 - 2019-11-06
* [#625](https://github.com/stripe/stripe-python/pull/625) Add support for `Mandate`

## 2.38.0 - 2019-10-29
* [#623](https://github.com/stripe/stripe-python/pull/623) Add support for reverse pagination
* [#624](https://github.com/stripe/stripe-python/pull/624) Contributor Convenant

## 2.37.2 - 2019-10-04
* [#621](https://github.com/stripe/stripe-python/pull/621) Implement support for stripe-should-retry and retry-after headers

## 2.37.1 - 2019-09-26
* [#620](https://github.com/stripe/stripe-python/pull/620) Check that `error` is a dict before trying to use it to create a `StripeError`

## 2.37.0 - 2019-09-26
* [#619](https://github.com/stripe/stripe-python/pull/619) Add `ErrorObject` to `StripeError` exceptions
* [#616](https://github.com/stripe/stripe-python/pull/616) Pass `CFLAGS` and `LDFLAGS` when running tests

## 2.36.2 - 2019-09-12
* [#614](https://github.com/stripe/stripe-python/pull/614) Use `OrderedDict` to maintain key order in API requests and responses

## 2.36.1 - 2019-09-11
* [#612](https://github.com/stripe/stripe-python/pull/612) Use `ListObject` properties as default values in request methods

## 2.36.0 - 2019-09-10
* [#610](https://github.com/stripe/stripe-python/pull/610) Add support for header parameters in `ListObject` request methods

## 2.35.1 - 2019-08-20
* [#605](https://github.com/stripe/stripe-python/pull/605) Fix automatic retries of failed requests
* [#606](https://github.com/stripe/stripe-python/pull/606) Clarify what `max_network_retries` does

## 2.35.0 - 2019-08-12
* [#607](https://github.com/stripe/stripe-python/pull/607) Add `SubscriptionItem.create_usage_record` method

## 2.34.0 - 2019-08-09
* [#604](https://github.com/stripe/stripe-python/pull/604) Remove subscription schedule revisions
  - This is technically a breaking change. We've chosen to release it as a minor vesion bump because the associated API is unused.

## 2.33.2 - 2019-08-06
* [#601](https://github.com/stripe/stripe-python/pull/601) Add support for passing full objects instead of IDs to custom methods
* [#603](https://github.com/stripe/stripe-python/pull/603) Bump vendored six to latest version

## 2.33.1 - 2019-08-06
* [#599](https://github.com/stripe/stripe-python/pull/599) Fix `del` statement to not raise `KeyError`

## 2.33.0 - 2019-07-30
* [#595](https://github.com/stripe/stripe-python/pull/595) Listing `BalanceTransaction` objects now uses `/v1/balance_transactions` instead of `/v1/balance/history`

## 2.32.1 - 2019-07-08
* [#592](https://github.com/stripe/stripe-python/pull/592) Fix argument name conflict

## 2.32.0 - 2019-06-27
* [#590](https://github.com/stripe/stripe-python/pull/590) Add support for the `SetupIntent` resource and APIs

## 2.31.0 - 2019-06-24
* [#587](https://github.com/stripe/stripe-python/pull/587) Enable request latency telemetry by default

## 2.30.1 - 2019-06-20
* [#589](https://github.com/stripe/stripe-python/pull/589) Fix support for `CustomerBalanceTransaction`

## 2.30.0 - 2019-06-17
* [#564](https://github.com/stripe/stripe-python/pull/564) Add support for `CustomerBalanceTransaction` resource and APIs

## 2.29.4 - 2019-06-03
* [#583](https://github.com/stripe/stripe-python/pull/583) Remove Poetry and reinstate `setup.py`

## 2.29.3 - 2019-05-31
Version 2.29.2 was non-functional due to a bugged `version.py` file. This release is identical to 2.29.2 save for the version number.

## 2.29.2 - 2019-05-31
* [#561](https://github.com/stripe/stripe-python/pull/561) Replace pipenv with poetry

## 2.29.1 - 2019-05-31
* [#578](https://github.com/stripe/stripe-python/pull/578) Verify signatures before deserializing events

## 2.29.0 - 2019-05-23
* [#575](https://github.com/stripe/stripe-python/pull/575) Add support for `radar.early_fraud_warning` resource

## 2.28.2 - 2019-05-23
* [#574](https://github.com/stripe/stripe-python/pull/574) Fix a few more code quality issues

## 2.28.1 - 2019-05-20
* [#572](https://github.com/stripe/stripe-python/pull/572) Fix a few code quality issues

## 2.28.0 - 2019-05-14
* [#566](https://github.com/stripe/stripe-python/pull/566) Add support for the `Capability` resource and APIs

## 2.27.0 - 2019-04-24
* [#554](https://github.com/stripe/stripe-python/pull/554) Add support for the `TaxRate` resource and APIs

## 2.26.0 - 2019-04-22
* [#555](https://github.com/stripe/stripe-python/pull/555) Add support for the `TaxId` resource and APIs

## 2.25.0 - 2019-04-18
* [#551](https://github.com/stripe/stripe-python/pull/551) Add support for the `CreditNote` resource and APIs

## 2.24.1 - 2019-04-08
* [#550](https://github.com/stripe/stripe-python/pull/550) Fix encoding of nested parameters in multipart requests

## 2.24.0 - 2019-04-03
* [#543](https://github.com/stripe/stripe-python/pull/543) Add `delete` class method on deletable API resources
* [#547](https://github.com/stripe/stripe-python/pull/547) Add class methods for all custom API requests (e.g. `Charge.capture`)

## 2.23.0 - 2019-03-18
* [#537](https://github.com/stripe/stripe-python/pull/537) Add support for the `PaymentMethod` resource and APIs
* [#540](https://github.com/stripe/stripe-python/pull/540) Add support for retrieving a Checkout `Session`
* [#542](https://github.com/stripe/stripe-python/pull/542) Add support for deleting a Terminal `Location` and `Reader`

## 2.22.0 - 2019-03-14
* [#541](https://github.com/stripe/stripe-python/pull/541) Add `stripe.util.convert_to_dict` method for converting `StripeObject` instances to regular `dict`s

## 2.21.0 - 2019-02-12
* [#532](https://github.com/stripe/stripe-python/pull/532) Add support for subscription schedules

## 2.20.3 - 2019-01-30
* [#530](https://github.com/stripe/stripe-python/pull/530) Fix client telemetry implementation

## 2.20.2 - 2019-01-30
* [#534](https://github.com/stripe/stripe-python/pull/534) Fix session initialization for multi-threaded environments

## 2.20.1 - 2019-01-30
* [#531](https://github.com/stripe/stripe-python/pull/531) Make `RequestsClient` thread-safe

## 2.20.0 - 2019-01-29
* [#526](https://github.com/stripe/stripe-python/pull/526) Reuse the default HTTP client by default

## 2.19.0 - 2019-01-23
* [#524](https://github.com/stripe/stripe-python/pull/524) Rename `CheckoutSession` to `Session` and move it under the `checkout` namespace. This is a breaking change, but we've reached out to affected merchants and all new merchants would use the new approach.

## 2.18.1 - 2019-01-21
* [#525](https://github.com/stripe/stripe-python/pull/525) Properly serialize `individual` on `Account` objects

## 2.18.0 - 2019-01-15
* [#518](https://github.com/stripe/stripe-python/pull/518) Add configurable telemetry to gather information on client-side request latency

## 2.17.0 - 2018-12-21
* [#510](https://github.com/stripe/stripe-python/pull/510) Add support for Checkout sessions

## 2.16.0 - 2018-12-10
* [#507](https://github.com/stripe/stripe-python/pull/507) Add support for account links

## 2.15.0 - 2018-11-30
* [#503](https://github.com/stripe/stripe-python/pull/503) Add support for providing custom CA certificate bundle

## 2.14.0 - 2018-11-28
* [#500](https://github.com/stripe/stripe-python/pull/500) Add support for `Review` for Radar

## 2.13.0 - 2018-11-27
* [#489](https://github.com/stripe/stripe-python/pull/489) Add support for `ValueList` and `ValueListItem` for Radar

## 2.12.1 - 2018-11-22
* [#495](https://github.com/stripe/stripe-python/pull/495) Make `StripeResponse` a new-style class

## 2.12.0 - 2018-11-08
* [#483](https://github.com/stripe/stripe-python/pull/483) Add new API endpoints for the `Invoice` resource.

## 2.11.1 - 2018-11-08
* [#491](https://github.com/stripe/stripe-python/pull/491) Bump minimum requests version to 2.20.0 (for [CVE-2018-18074](https://nvd.nist.gov/vuln/detail/CVE-2018-18074))

## 2.11.0 - 2018-10-30
* [#482](https://github.com/stripe/stripe-python/pull/482) Add support for the `Person` resource
* [#484](https://github.com/stripe/stripe-python/pull/484) Add support for the `WebhookEndpoint` resource

## 2.10.1 - 2018-10-02
* [#481](https://github.com/stripe/stripe-python/pull/481) Correct behavior of `stripe.max_network_retries` if it's reset after initial use

## 2.10.0 - 2018-09-24
* [#478](https://github.com/stripe/stripe-python/pull/478) Add support for Stripe Terminal

## 2.9.0 - 2018-09-24
* [#477](https://github.com/stripe/stripe-python/pull/477) Rename `FileUpload` to `File`

## 2.8.1 - 2018-09-13
* [#474](https://github.com/stripe/stripe-python/pull/474) Don't URL-encode square brackets
* [#473](https://github.com/stripe/stripe-python/pull/473) Integer-index encode all arrays

## 2.8.0 - 2018-09-10
* [#470](https://github.com/stripe/stripe-python/pull/470) Add support for automatic network retries

## 2.7.0 - 2018-09-05
* [#469](https://github.com/stripe/stripe-python/pull/469) Add support for reporting resources

## 2.6.0 - 2018-08-23
* [#467](https://github.com/stripe/stripe-python/pull/467) Add support for usage record summaries

## 2.5.0 - 2018-08-16
* [#463](https://github.com/stripe/stripe-python/pull/463) Remove unsupported Bitcoin endpoints (this is technically a breaking change, but we're releasing as a minor version because none of these APIs were usable anyway)

## 2.4.0 - 2018-08-03
* [#460](https://github.com/stripe/stripe-python/pull/460) Add cancel support for topups
* [#461](https://github.com/stripe/stripe-python/pull/461) Add support for file links

## 2.3.0 - 2018-07-27
* [#456](https://github.com/stripe/stripe-python/pull/456) Add support for Sigma scheduled query run objects

## 2.2.0 - 2018-07-26
* [#455](https://github.com/stripe/stripe-python/pull/455) Add support for Stripe Issuing

## 2.1.0 - 2018-07-25
* [#452](https://github.com/stripe/stripe-python/pull/452) Add `InvoiceLineItem` class

## 2.0.3 - 2018-07-19
* [#450](https://github.com/stripe/stripe-python/pull/450) Internal improvements to `ApiResource.class_url`

## 2.0.2 - 2018-07-18
* [#448](https://github.com/stripe/stripe-python/pull/448) Avoid duplicate dependency on `requests` with Python 2.7

## 2.0.1 - 2018-07-10
* [#445](https://github.com/stripe/stripe-python/pull/445) Fix `setup.py`

## 2.0.0 - 2018-07-10
Major version release. List of backwards incompatible changes to watch out for:
* The minimum Python versions are now 2.7 / 3.4. If you're using Python 2.6 or 3.3, consider upgrading to a more recent version.
* Stripe exception classes should now be accessed via `stripe.error` rather than just `stripe`
* Some older deprecated methods have been removed
* Trying to detach an unattached source will now raise a `stripe.error.InvalidRequestError` exception instead of a `NotImplementedError` exception

For more information, check out the [migration guide for v2](https://github.com/stripe/stripe-python/wiki/Migration-guide-for-v2)

Pull requests included in this release:
* [#385](https://github.com/stripe/stripe-python/pull/385) Drop support for Python 2.6 and 3.3
* [#384](https://github.com/stripe/stripe-python/pull/384) Use py.test for tests
* [#399](https://github.com/stripe/stripe-python/pull/399) Remove deprecated code
* [#402](https://github.com/stripe/stripe-python/pull/402) Remove `util.json` and use `json` module directly everywhere
* [#403](https://github.com/stripe/stripe-python/pull/403) Update setup.py and test flow
* [#410](https://github.com/stripe/stripe-python/pull/410) Use pipenv
* [#415](https://github.com/stripe/stripe-python/pull/415) Change exception when detaching unattached sources from `NotImplementedError` to `stripe.error.InvalidRequestError`

## 1.84.2 - 2018-07-06
* [#441](https://github.com/stripe/stripe-python/pull/441) Better (hopefully) fix for serialization of empty `ListObject`s

## 1.84.1 - 2018-07-04
* [#439](https://github.com/stripe/stripe-python/pull/439) Fix serialization of empty `ListObject`s

## 1.84.0 - 2018-06-29
* [#436](https://github.com/stripe/stripe-python/pull/436) Add support for payment intents

## 1.83.0 - 2018-06-28
* [#437](https://github.com/stripe/stripe-python/pull/437) Add support for `partner_id` in `stripe.set_app_info()`

## 1.82.2 - 2018-06-19
* [#365](https://github.com/stripe/stripe-python/pull/365) Add `__repr__` methods to `StripeError` exception classes

## 1.82.1 - 2018-05-14
* [#430](https://github.com/stripe/stripe-python/pull/430) Handle the case where request ID is `None` when formatting errors

## 1.82.0 - 2018-05-13
* [#422](https://github.com/stripe/stripe-python/pull/422) Add `user_mesage` to `StripeError` for a way in Python 3 to avoid the "Request req_...:" string normally appended to error messages

## 1.81.0 - 2018-05-10
* [#425](https://github.com/stripe/stripe-python/pull/425) Add support for issuer fraud records

## 1.80.0 - 2018-04-24
* [#421](https://github.com/stripe/stripe-python/pull/421) Add support for flexible billing and usage records

## 1.79.1 - 2018-02-27
* [#401](https://github.com/stripe/stripe-python/pull/401) Drop conditional dependencies that incorrectly led to an added `simplejson` dependency in Python 3+ after switching to universal wheel

## 1.79.0 - 2018-02-23
* [#397](https://github.com/stripe/stripe-python/pull/397) Build universal wheels by default
* [#398](https://github.com/stripe/stripe-python/pull/398) Add support for `code` attribute on all Stripe exceptions

## 1.78.0 - 2018-02-21
* [#396](https://github.com/stripe/stripe-python/pull/396) Add support for topups

## 1.77.2 - 2018-02-08
* [#394](https://github.com/stripe/stripe-python/pull/394) Make `last_response` available after calling `save()`

## 1.77.1 - 2018-01-12
* [#389](https://github.com/stripe/stripe-python/pull/389) Register unsaved attributes on assignment regardless of new value

## 1.77.0 - 2017-12-21
* [#371](https://github.com/stripe/stripe-python/pull/371) Add accessor `last_response` on `StripeObject` for accessing request ID and other metadata

## 1.76.0 - 2017-12-21
* [#382](https://github.com/stripe/stripe-python/pull/382) Add new `IdempotencyError` type

## 1.75.3 - 2017-12-05
* [#378](https://github.com/stripe/stripe-python/pull/378) Log encoded version of parameters instead of raw POST data

## 1.75.2 - 2017-12-05
* (Accidental no-op release. See 1.75.3.)

## 1.75.1 - 2017-11-29
* [#372](https://github.com/stripe/stripe-python/pull/372) Add only changed values to `_unsaved_values` in `StripeObject`
* [#375](https://github.com/stripe/stripe-python/pull/375) Use a custom JSON encoder to handle `datetime` objects when serializing `StripeObject`s

## 1.75.0 - 2017-11-08
* [#369](https://github.com/stripe/stripe-python/pull/369) Make custom actions on various resources (e.g. `Account.reject`) more consistent with other APIs

## 1.74.0 - 2017-11-07
* [#368](https://github.com/stripe/stripe-python/pull/368) Remove API that allowed the creation of new disputes (this was an erroneous addition; it never worked because the API would not allow it)

## 1.73.0 - 2017-11-02
* [#364](https://github.com/stripe/stripe-python/pull/364) Switch to vendored version of the `six` package for compatibility between Python 2 and 3

## 1.72.0 - 2017-10-31
* [#361](https://github.com/stripe/stripe-python/pull/361) Support for exchange rates APIs

## 1.71.2 - 2017-10-31
* [#362](https://github.com/stripe/stripe-python/pull/362) Fix balance transaction and invoice item conversion into `StripeObject`s

## 1.71.1 - 2017-10-27
* [#360](https://github.com/stripe/stripe-python/pull/360) Fix `BytesWarning` being issued on logging in Python 3

## 1.71.0 - 2017-10-26
* [#359](https://github.com/stripe/stripe-python/pull/359) Support for listing source transactions

## 1.70.0 - 2017-10-23
* [#356](https://github.com/stripe/stripe-python/pull/356) Support uploading files with `StringIO` in addition to a file on disk

## 1.69.0 - 2017-10-20
* [#351](https://github.com/stripe/stripe-python/pull/351) Break resource.py module into separate ones for each type of resource
    * Classes are still into resource.py for backwards compatibility
* [#353](https://github.com/stripe/stripe-python/pull/353) Fix unpickling `StripeObject` in Python 3

## 1.68.0 - 2017-10-19
* [#350](https://github.com/stripe/stripe-python/pull/350) Add static methods to manipulate resources from parent
    * `Account` gains methods for external accounts and login links (e.g. `.create_account`, `create_login_link`)
    * `ApplicationFee` gains methods for refunds
    * `Customer` gains methods for sources
    * `Transfer` gains methods for reversals

## 1.67.0 - 2017-10-11
* [#349](https://github.com/stripe/stripe-python/pull/349) Rename source `delete` to `detach` (and deprecate the former)

## 1.66.0 - 2017-09-29
* Support length reads on list objects

## 1.65.1 - 2017-09-21
* Handle `bytearray` and `bytes` (in addition to string) in `Webhook.construct_event`

## 1.65.0 - 2017-09-07
* Add support for passing a `stripe_version` argument to all API requests

## 1.64.0 - 2017-09-01
* Error when an invalid type (i.e. non-string) passed as an API method argument

## 1.63.1 - 2017-09-01
* Fix serialization of `items` on Relay order creation and order return

## 1.63.0 - 2017-08-29
* Add support for `InvalidClientError` OAuth error

## 1.62.1 - 2017-08-07
* Change serialization of subscription items on update to encoded as an integer-indexed map

## 1.62.0 - 2017-06-27
* `pay` on invoice can now take parameter

## 1.61.0 - 2017-06-24
* Expose `code` on `InvalidRequestError`

## 1.60.0 - 2017-06-19
* Add support for ephemeral keys

## 1.59.0 - 2017-06-07
* Refactor OAuth implementation to have dedicated classes for errors

## 1.58.0 - 2017-06-02
* Re-use connections with Pycurl

## 1.57.1 - 2017-05-31
* Fix the pycurl client

## 1.57.0 - 2017-05-26
* Add `api_key` parameter to webhook's `construct_event`

## 1.56.0 - 2017-05-25
* Add support for account login links

## 1.55.2 - 2017-05-11
* Remove Requests constraint from 1.55.1 now that they've patched (as of 2.14.2)

## 1.55.1 - 2017-05-10
* Constrain Requests to < 2.13.0 if on setuptools < 18.0.0

## 1.55.0 - 2017-04-28
* Support for checking webhook signatures

## 1.54.0 - 2017-04-28
* Add `stripe.set_app_info` for use by plugin creators

## 1.53.0 - 2017-04-06
* Add support for payouts and recipient transfers

## 1.52.0 - 2017-04-06
* No-op release: peg test suite to a specific API version

## 1.51.0 - 2017-03-20
* Support OAuth operations (getting a token and deauthorizing)

## 1.50.0 - 2017-03-17
* Support for detaching sources from customers

## 1.49.0 - 2017-03-13
* Accept `session` argument for `RequestsClient`

## 1.48.1 - 2017-02-21
* Fix encoding of parameters when fetching upcoming invoices

## 1.48.0 - 2017-02-21
* Add `Account.modify_external_account` to modify an account in one API call
* Add `Customer.modify_source` to modify a source in one API call

## 1.47.0 - 2017-01-18
* Allow sources to be updated

## 1.46.0 - 2017-01-06
* Use internal session for Requests for connection pooling

## 1.45.0 - 2017-01-06
* request logging goes to stderr now
* Logs properly handle unicode
* Format is now the same between logging logs, and console logs

## 1.44.0 - 2016-12-16
* Add request logging and some mechanisms to enable it when debugging

## 1.43.0 - 2016-11-30
* Add support for verifying sources

## 1.42.0 - 2016-11-21
* Add retrieve method for 3-D Secure resources

## 1.41.1 - 2016-10-26
* Implement __copy__ and __deepcopy__ on StripeObject to fix these operations

## 1.41.0 - 2016-10-12
* Add `Source` model for generic payment sources

## 1.40.1 - 2016-10-10
* Return subscription model instance on subscription create/modify

## 1.40.0 - 2016-10-07
* Add configurable timeout for Requests HTTP library

## 1.39.0 - 2016-10-06
* Add support for subscription items
* Add proxy support for pycurl, Requests, urlfetch, and urllib2 libraries

## 1.38.0 - 2016-09-15
* Add support for Apple Pay domains

## 1.37.0 - 2016-07-12
* Add `ThreeDSecure` model for 3-D secure payments

## 1.36.0 - 2016-06-29
* Add `update` class method to resources that can be updated

## 1.35.0 - 2016-05-24
* Add support for returning Relay orders

## 1.34.0 - 2016-05-20
* Add support for Alipay accounts

## 1.33.0 - 2016-05-04
* Add support for the new `/v1/subscriptions` endpoint
  * `stripe.Subscription.retrieve`
  * `stripe.Subscription.update`
  * `stripe.Subscription.create`
  * `stripe.Subscription.list`

## 1.32.2 - 2016-04-12
* Fix bug where file uploads could not be properly listed

## 1.32.1 - 2016-04-11
* Fix bug where request parameters were not passed between pages with `auto_paging_iter`

## 1.32.0 - 2016-03-31
* Update CA cert bundle for compatibility with OpenSSL versions below 1.0.1

## 1.31.1 - 2016-03-24
* Fix uploading of binary files in Python 3

## 1.31.0 - 2016-03-15
* Add `reject` on `Account` to support the new API feature

## 1.30.0 - 2016-02-27
* Add `CountrySpec` model for looking up country payment information

## 1.29.1 - 2016-02-01
* Update bundled CA certs

## 1.29.0 - 2016-01-26
* Add support for deleting Relay products and SKUs

## 1.28.0 - 2016-01-04
* Add an automatic paginating iterator to lists available via `auto_paging_iter`
* List objects are now iterable
* Error messages set to `None` are now handled properly
* The `all` method on list objects has been deprecated in favor of `list`
* Calls to `instance_url` are now side effect free

## 1.27.1 - 2015-10-02
* Official Python 3.4 & 3.5 compatibility
* Add configurable HTTP client
* Add ability to delete attributes

## 1.27.0 - 2015-09-14
* Products, SKUs, Orders resources

## 1.26.0 - 2015-09-11
* Add support for new 429 rate limit response

## 1.25.0 - 2015-08-17
* Added refund listing, creation and retrieval

## 1.24.1 - 2015-08-05
* Fix error handling for Python 2.6

## 1.24.0 - 2015-08-03
* Managed accounts can now be deleted
* Added dispute listing and retrieval

## 1.23.0 - 2015-07-06
* Include response headers in exceptions

## 1.22.3 - 2015-06-04
* Fix saving `additional_owners` on managed accounts

## 1.22.2 - 2015-04-08
* Fix saving manage accounts

## 1.22.1 - 2015-03-30
* Pass `stripe_account` to Balance.retrieve

## 1.22.0 - 2015-03-22
* Added methods for updating and saving arrays of objects

## 1.21.0 - 2015-02-19
* Added Bitcoin Receiver update and delete methods

## 1.20.2 - 2015-01-21
* Remove support for top-level bitcoin transactions

## 1.20.1 - 2015-01-07
* Adding bitcoin receiver and transaction objects

## 1.20.0 - 2014-12-23
* Adding support for file uploads resource

## 1.19.1 - 2014-10-23
* Remove redundant manual SSL blacklist preflight check

## 1.19.0 - 2014-07-26
* Application Fee refunds now a list instead of array

## 1.18.0 - 2014-06-17
* Add metadata for disputes and refunds

## 1.17.0 - 2014-06-10
* Remove official support for Python 2.5

## 1.16.0 - 2014-05-28
* Support for canceling transfers

## 1.15.1 - 2014-05-21
* Support cards for recipients.

## 1.14.1 - 2014-05-19
* Disable loading the ssl module on the Google App Engine dev server.

## 1.14.0 - 2014-04-09
* Use DER encoded certificate for checksumming
* Don't rely on SNI support in integration tests

## 1.13.0 - 2014-04-09
* Update bundled ca-certificates
* Add certificate blacklist for CVE-2014-0160 mitigation

## 1.12.2 - 2014-03-13
* Fix syntax errors in setup.py metadata

## 1.12.1 - 2014-03-13
* Added license and other metadata in setup.py
* Fix `__repr__` in Python 3
* Support pickling of responses

## 1.12.0 - 2014-01-29
* Added support for multiple subscriptions per customer

## 1.11.0 - 2013-12-05
* Added extensive unit tests
* Extended functional test coverage
* Refactored code into modules and out of stripe/__init__.py
* Abstracted http library selection and use from the `APIRequestor` into `stripe.http_client`
* Refactored `StripeObject` to inherit from `dict` and avoid direct access of `__dict__`.
* PEP8ified the codebase and enforced with a test.
* Proper encoding of timezone aware datetimes

### Backwards incompatible changes
* The `to_dict` and `values` methods on resources no longer recursively convert objects to plain `dict`s.  All resources now inherit from `dict` but are functionally different in that you cannot set a value to an empty string and cannot delete items.
* The `previous_metadata` attribute on resources is now protected.
* Timezone aware `datetime` objects passed to the API will now be encoded in a way that does not depend on the local system time.  If you are passing timezone-aware datetimes to our API and your server time is not already in UTC, this will change the value passed to our API.

## 1.10.8 - 2013-12-02
* Add stripe.ApplicationFee resource

## 1.9.8 - 2013-10-17
* Removed incorrect test.

## 1.9.7 - 2013-10-10
* Add support for metadata.

## 1.9.6 - 2013-10-08
* Fix issue with support for closing disputes.

## 1.9.5 - 2013-09-18
* Add support for closing disputes.

## 1.9.4 - 2013-08-13
* Add stripe.Balance and stripe.BalanceTransaction resources

## 1.9.3 - 2013-08-12
* Add support for unsetting attributes by setting to None.
  Setting properties to a blank string is now an error.

## 1.9.2 - 2013-07-12
* Add support for multiple cards API

## 1.9.1 - 2013-05-03
* Remove 'id' from the list of permanent attributes

## 1.9.0 - 2013-04-25
* Support for Python 3 (github issue #32)

## 1.8.0 - 2013-04-11
* Allow transfers to be creatable
* Add new stripe.Recipient resource

## 1.7.10 - 2013-02-21
* Add 'id' to the list of permanent attributes

## 1.7.9 - 2013-02-01
* Add support for passing options when retrieving Stripe objects; e.g., stripe.Charge.retrieve("foo", params={"expand":["customer"]})

## 1.7.8 - 2013-01-15
* Add support for setting a Stripe API version override

## 1.7.7 - 2012-12-18
* Update requests version check to work with requests 1.x.x (github issue #24)

## 1.7.6 - 2012-11-08
* Add support for updating charge disputes

## 1.7.5 - 2012-10-30
* Add support for creating invoices
* Add support for new invoice lines return format
* Add support for new List objects

## 1.7.4 - 2012-08-31
* Add update and pay methods for Invoice resource

## 1.7.3 - 2012-08-15
* Add new stripe.Account resource
* Remove uncaptured_charge tests (this has been deprecated from the API).

## 1.7.2 - 2012-05-31
* Fix a bug that would cause nested objects to be mis-rendered in __str__ and __repr__ methods (github issues #17, #18)

## 1.7.1 - 2012-05-21
* Prefer App Engine's urlfetch over requests, as that's the only thing that will work in App Engine's environment. Previously, if requests was available in the App Engine environment, we would attempt to use it.

## 1.7.0 - 2012-05-17
* Add new delete_discount method to stripe.Customer
* Add new stripe.Transfer resource
* Switch from using HTTP Basic auth to Bearer auth. (Note: Stripe will support Basic auth for the indefinite future, but recommends Bearer auth when possible going forward)
* Numerous test suite improvements

## 1.6.1 - 2011-09-14
* Parameters with value None are no longer included in API requests
