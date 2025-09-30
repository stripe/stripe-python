# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._charge import Charge
    from stripe._customer import Customer
    from stripe._setup_attempt import SetupAttempt
    from stripe.params._payment_method_attach_params import (
        PaymentMethodAttachParams,
    )
    from stripe.params._payment_method_create_params import (
        PaymentMethodCreateParams,
    )
    from stripe.params._payment_method_detach_params import (
        PaymentMethodDetachParams,
    )
    from stripe.params._payment_method_list_params import (
        PaymentMethodListParams,
    )
    from stripe.params._payment_method_modify_params import (
        PaymentMethodModifyParams,
    )
    from stripe.params._payment_method_retrieve_params import (
        PaymentMethodRetrieveParams,
    )


class PaymentMethod(
    CreateableAPIResource["PaymentMethod"],
    ListableAPIResource["PaymentMethod"],
    UpdateableAPIResource["PaymentMethod"],
):
    """
    PaymentMethod objects represent your customer's payment instruments.
    You can use them with [PaymentIntents](https://stripe.com/docs/payments/payment-intents) to collect payments or save them to
    Customer objects to store instrument details for future payments.

    Related guides: [Payment Methods](https://stripe.com/docs/payments/payment-methods) and [More Payment Scenarios](https://stripe.com/docs/payments/more-payment-scenarios).
    """

    OBJECT_NAME: ClassVar[Literal["payment_method"]] = "payment_method"

    class AcssDebit(StripeObject):
        bank_name: Optional[str]
        """
        Name of the bank associated with the bank account.
        """
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
        """
        institution_number: Optional[str]
        """
        Institution number of the bank account.
        """
        last4: Optional[str]
        """
        Last four digits of the bank account number.
        """
        transit_number: Optional[str]
        """
        Transit number of the bank account.
        """

    class Affirm(StripeObject):
        pass

    class AfterpayClearpay(StripeObject):
        pass

    class Alipay(StripeObject):
        pass

    class Alma(StripeObject):
        pass

    class AmazonPay(StripeObject):
        pass

    class AuBecsDebit(StripeObject):
        bsb_number: Optional[str]
        """
        Six-digit number identifying bank and branch associated with this bank account.
        """
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
        """
        last4: Optional[str]
        """
        Last four digits of the bank account number.
        """

    class BacsDebit(StripeObject):
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
        """
        last4: Optional[str]
        """
        Last four digits of the bank account number.
        """
        sort_code: Optional[str]
        """
        Sort code of the bank account. (e.g., `10-20-30`)
        """

    class Bancontact(StripeObject):
        pass

    class Billie(StripeObject):
        pass

    class BillingDetails(StripeObject):
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
            Address line 1, such as the street, PO Box, or company name.
            """
            line2: Optional[str]
            """
            Address line 2, such as the apartment, suite, unit, or building.
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
        """
        Billing address.
        """
        email: Optional[str]
        """
        Email address.
        """
        name: Optional[str]
        """
        Full name.
        """
        phone: Optional[str]
        """
        Billing phone number (including extension).
        """
        tax_id: Optional[str]
        """
        Taxpayer identification number. Used only for transactions between LATAM buyers and non-LATAM sellers.
        """
        _inner_class_types = {"address": Address}

    class Blik(StripeObject):
        pass

    class Boleto(StripeObject):
        tax_id: str
        """
        Uniquely identifies the customer tax id (CNPJ or CPF)
        """

    class Card(StripeObject):
        class Checks(StripeObject):
            address_line1_check: Optional[str]
            """
            If a address line1 was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.
            """
            address_postal_code_check: Optional[str]
            """
            If a address postal code was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.
            """
            cvc_check: Optional[str]
            """
            If a CVC was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.
            """

        class GeneratedFrom(StripeObject):
            class PaymentMethodDetails(StripeObject):
                class CardPresent(StripeObject):
                    class Offline(StripeObject):
                        stored_at: Optional[int]
                        """
                        Time at which the payment was collected while offline
                        """
                        type: Optional[Literal["deferred"]]
                        """
                        The method used to process this payment method offline. Only deferred is allowed.
                        """

                    class Receipt(StripeObject):
                        account_type: Optional[
                            Literal["checking", "credit", "prepaid", "unknown"]
                        ]
                        """
                        The type of account being debited or credited
                        """
                        application_cryptogram: Optional[str]
                        """
                        The Application Cryptogram, a unique value generated by the card to authenticate the transaction with issuers.
                        """
                        application_preferred_name: Optional[str]
                        """
                        The Application Identifier (AID) on the card used to determine which networks are eligible to process the transaction. Referenced from EMV tag 9F12, data encoded on the card's chip.
                        """
                        authorization_code: Optional[str]
                        """
                        Identifier for this transaction.
                        """
                        authorization_response_code: Optional[str]
                        """
                        EMV tag 8A. A code returned by the card issuer.
                        """
                        cardholder_verification_method: Optional[str]
                        """
                        Describes the method used by the cardholder to verify ownership of the card. One of the following: `approval`, `failure`, `none`, `offline_pin`, `offline_pin_and_signature`, `online_pin`, or `signature`.
                        """
                        dedicated_file_name: Optional[str]
                        """
                        Similar to the application_preferred_name, identifying the applications (AIDs) available on the card. Referenced from EMV tag 84.
                        """
                        terminal_verification_results: Optional[str]
                        """
                        A 5-byte string that records the checks and validations that occur between the card and the terminal. These checks determine how the terminal processes the transaction and what risk tolerance is acceptable. Referenced from EMV Tag 95.
                        """
                        transaction_status_information: Optional[str]
                        """
                        An indication of which steps were completed during the card read process. Referenced from EMV Tag 9B.
                        """

                    class Wallet(StripeObject):
                        type: Literal[
                            "apple_pay", "google_pay", "samsung_pay", "unknown"
                        ]
                        """
                        The type of mobile wallet, one of `apple_pay`, `google_pay`, `samsung_pay`, or `unknown`.
                        """

                    amount_authorized: Optional[int]
                    """
                    The authorized amount
                    """
                    brand: Optional[str]
                    """
                    Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.
                    """
                    brand_product: Optional[str]
                    """
                    The [product code](https://stripe.com/docs/card-product-codes) that identifies the specific program or product associated with a card.
                    """
                    capture_before: Optional[int]
                    """
                    When using manual capture, a future timestamp after which the charge will be automatically refunded if uncaptured.
                    """
                    cardholder_name: Optional[str]
                    """
                    The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.
                    """
                    country: Optional[str]
                    """
                    Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
                    """
                    description: Optional[str]
                    """
                    A high-level description of the type of cards issued in this range. (For internal use only and not typically available in standard API requests.)
                    """
                    emv_auth_data: Optional[str]
                    """
                    Authorization response cryptogram.
                    """
                    exp_month: int
                    """
                    Two-digit number representing the card's expiration month.
                    """
                    exp_year: int
                    """
                    Four-digit number representing the card's expiration year.
                    """
                    fingerprint: Optional[str]
                    """
                    Uniquely identifies this particular card number. You can use this attribute to check whether two customers who've signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

                    *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.*
                    """
                    funding: Optional[str]
                    """
                    Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
                    """
                    generated_card: Optional[str]
                    """
                    ID of a card PaymentMethod generated from the card_present PaymentMethod that may be attached to a Customer for future transactions. Only present if it was possible to generate a card PaymentMethod.
                    """
                    iin: Optional[str]
                    """
                    Issuer identification number of the card. (For internal use only and not typically available in standard API requests.)
                    """
                    incremental_authorization_supported: bool
                    """
                    Whether this [PaymentIntent](https://stripe.com/docs/api/payment_intents) is eligible for incremental authorizations. Request support using [request_incremental_authorization_support](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-payment_method_options-card_present-request_incremental_authorization_support).
                    """
                    issuer: Optional[str]
                    """
                    The name of the card's issuing bank. (For internal use only and not typically available in standard API requests.)
                    """
                    last4: Optional[str]
                    """
                    The last four digits of the card.
                    """
                    network: Optional[str]
                    """
                    Identifies which network this charge was processed on. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `interac`, `jcb`, `link`, `mastercard`, `unionpay`, `visa`, or `unknown`.
                    """
                    network_transaction_id: Optional[str]
                    """
                    This is used by the financial networks to identify a transaction. Visa calls this the Transaction ID, Mastercard calls this the Trace ID, and American Express calls this the Acquirer Reference Data. This value will be present if it is returned by the financial network in the authorization response, and null otherwise.
                    """
                    offline: Optional[Offline]
                    """
                    Details about payments collected offline.
                    """
                    overcapture_supported: bool
                    """
                    Defines whether the authorized amount can be over-captured or not
                    """
                    preferred_locales: Optional[List[str]]
                    """
                    The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card's chip.
                    """
                    read_method: Optional[
                        Literal[
                            "contact_emv",
                            "contactless_emv",
                            "contactless_magstripe_mode",
                            "magnetic_stripe_fallback",
                            "magnetic_stripe_track2",
                        ]
                    ]
                    """
                    How card details were read in this transaction.
                    """
                    receipt: Optional[Receipt]
                    """
                    A collection of fields required to be displayed on receipts. Only required for EMV transactions.
                    """
                    wallet: Optional[Wallet]
                    _inner_class_types = {
                        "offline": Offline,
                        "receipt": Receipt,
                        "wallet": Wallet,
                    }

                card_present: Optional[CardPresent]
                type: str
                """
                The type of payment method transaction-specific details from the transaction that generated this `card` payment method. Always `card_present`.
                """
                _inner_class_types = {"card_present": CardPresent}

            charge: Optional[str]
            """
            The charge that created this object.
            """
            payment_method_details: Optional[PaymentMethodDetails]
            """
            Transaction-specific details of the payment method used in the payment.
            """
            setup_attempt: Optional[ExpandableField["SetupAttempt"]]
            """
            The ID of the SetupAttempt that generated this PaymentMethod, if any.
            """
            _inner_class_types = {
                "payment_method_details": PaymentMethodDetails,
            }

        class Networks(StripeObject):
            available: List[str]
            """
            All networks available for selection via [payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-network).
            """
            preferred: Optional[str]
            """
            The preferred network for co-branded cards. Can be `cartes_bancaires`, `mastercard`, `visa` or `invalid_preference` if requested network is not valid for the card.
            """

        class ThreeDSecureUsage(StripeObject):
            supported: bool
            """
            Whether 3D Secure is supported on this card.
            """

        class Wallet(StripeObject):
            class AmexExpressCheckout(StripeObject):
                pass

            class ApplePay(StripeObject):
                pass

            class GooglePay(StripeObject):
                pass

            class Link(StripeObject):
                pass

            class Masterpass(StripeObject):
                class BillingAddress(StripeObject):
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
                    Address line 1, such as the street, PO Box, or company name.
                    """
                    line2: Optional[str]
                    """
                    Address line 2, such as the apartment, suite, unit, or building.
                    """
                    postal_code: Optional[str]
                    """
                    ZIP or postal code.
                    """
                    state: Optional[str]
                    """
                    State, county, province, or region.
                    """

                class ShippingAddress(StripeObject):
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
                    Address line 1, such as the street, PO Box, or company name.
                    """
                    line2: Optional[str]
                    """
                    Address line 2, such as the apartment, suite, unit, or building.
                    """
                    postal_code: Optional[str]
                    """
                    ZIP or postal code.
                    """
                    state: Optional[str]
                    """
                    State, county, province, or region.
                    """

                billing_address: Optional[BillingAddress]
                """
                Owner's verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                email: Optional[str]
                """
                Owner's verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                name: Optional[str]
                """
                Owner's verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                shipping_address: Optional[ShippingAddress]
                """
                Owner's verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                _inner_class_types = {
                    "billing_address": BillingAddress,
                    "shipping_address": ShippingAddress,
                }

            class SamsungPay(StripeObject):
                pass

            class VisaCheckout(StripeObject):
                class BillingAddress(StripeObject):
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
                    Address line 1, such as the street, PO Box, or company name.
                    """
                    line2: Optional[str]
                    """
                    Address line 2, such as the apartment, suite, unit, or building.
                    """
                    postal_code: Optional[str]
                    """
                    ZIP or postal code.
                    """
                    state: Optional[str]
                    """
                    State, county, province, or region.
                    """

                class ShippingAddress(StripeObject):
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
                    Address line 1, such as the street, PO Box, or company name.
                    """
                    line2: Optional[str]
                    """
                    Address line 2, such as the apartment, suite, unit, or building.
                    """
                    postal_code: Optional[str]
                    """
                    ZIP or postal code.
                    """
                    state: Optional[str]
                    """
                    State, county, province, or region.
                    """

                billing_address: Optional[BillingAddress]
                """
                Owner's verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                email: Optional[str]
                """
                Owner's verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                name: Optional[str]
                """
                Owner's verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                shipping_address: Optional[ShippingAddress]
                """
                Owner's verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                _inner_class_types = {
                    "billing_address": BillingAddress,
                    "shipping_address": ShippingAddress,
                }

            amex_express_checkout: Optional[AmexExpressCheckout]
            apple_pay: Optional[ApplePay]
            dynamic_last4: Optional[str]
            """
            (For tokenized numbers only.) The last four digits of the device account number.
            """
            google_pay: Optional[GooglePay]
            link: Optional[Link]
            masterpass: Optional[Masterpass]
            samsung_pay: Optional[SamsungPay]
            type: Literal[
                "amex_express_checkout",
                "apple_pay",
                "google_pay",
                "link",
                "masterpass",
                "samsung_pay",
                "visa_checkout",
            ]
            """
            The type of the card wallet, one of `amex_express_checkout`, `apple_pay`, `google_pay`, `masterpass`, `samsung_pay`, `visa_checkout`, or `link`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type.
            """
            visa_checkout: Optional[VisaCheckout]
            _inner_class_types = {
                "amex_express_checkout": AmexExpressCheckout,
                "apple_pay": ApplePay,
                "google_pay": GooglePay,
                "link": Link,
                "masterpass": Masterpass,
                "samsung_pay": SamsungPay,
                "visa_checkout": VisaCheckout,
            }

        brand: str
        """
        Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.
        """
        checks: Optional[Checks]
        """
        Checks on Card address and CVC if provided.
        """
        country: Optional[str]
        """
        Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
        """
        description: Optional[str]
        """
        A high-level description of the type of cards issued in this range. (For internal use only and not typically available in standard API requests.)
        """
        display_brand: Optional[str]
        """
        The brand to use when displaying the card, this accounts for customer's brand choice on dual-branded cards. Can be `american_express`, `cartes_bancaires`, `diners_club`, `discover`, `eftpos_australia`, `interac`, `jcb`, `mastercard`, `union_pay`, `visa`, or `other` and may contain more values in the future.
        """
        exp_month: int
        """
        Two-digit number representing the card's expiration month.
        """
        exp_year: int
        """
        Four-digit number representing the card's expiration year.
        """
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular card number. You can use this attribute to check whether two customers who've signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

        *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.*
        """
        funding: str
        """
        Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
        """
        generated_from: Optional[GeneratedFrom]
        """
        Details of the original PaymentMethod that created this object.
        """
        iin: Optional[str]
        """
        Issuer identification number of the card. (For internal use only and not typically available in standard API requests.)
        """
        issuer: Optional[str]
        """
        The name of the card's issuing bank. (For internal use only and not typically available in standard API requests.)
        """
        last4: str
        """
        The last four digits of the card.
        """
        networks: Optional[Networks]
        """
        Contains information about card networks that can be used to process the payment.
        """
        regulated_status: Optional[Literal["regulated", "unregulated"]]
        """
        Status of a card based on the card issuer.
        """
        three_d_secure_usage: Optional[ThreeDSecureUsage]
        """
        Contains details on how this Card may be used for 3D Secure authentication.
        """
        wallet: Optional[Wallet]
        """
        If this Card is part of a card wallet, this contains the details of the card wallet.
        """
        _inner_class_types = {
            "checks": Checks,
            "generated_from": GeneratedFrom,
            "networks": Networks,
            "three_d_secure_usage": ThreeDSecureUsage,
            "wallet": Wallet,
        }

    class CardPresent(StripeObject):
        class Networks(StripeObject):
            available: List[str]
            """
            All networks available for selection via [payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-network).
            """
            preferred: Optional[str]
            """
            The preferred network for the card.
            """

        class Offline(StripeObject):
            stored_at: Optional[int]
            """
            Time at which the payment was collected while offline
            """
            type: Optional[Literal["deferred"]]
            """
            The method used to process this payment method offline. Only deferred is allowed.
            """

        class Wallet(StripeObject):
            type: Literal["apple_pay", "google_pay", "samsung_pay", "unknown"]
            """
            The type of mobile wallet, one of `apple_pay`, `google_pay`, `samsung_pay`, or `unknown`.
            """

        brand: Optional[str]
        """
        Card brand. Can be `amex`, `cartes_bancaires`, `diners`, `discover`, `eftpos_au`, `jcb`, `link`, `mastercard`, `unionpay`, `visa` or `unknown`.
        """
        brand_product: Optional[str]
        """
        The [product code](https://stripe.com/docs/card-product-codes) that identifies the specific program or product associated with a card.
        """
        cardholder_name: Optional[str]
        """
        The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.
        """
        country: Optional[str]
        """
        Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
        """
        description: Optional[str]
        """
        A high-level description of the type of cards issued in this range. (For internal use only and not typically available in standard API requests.)
        """
        exp_month: int
        """
        Two-digit number representing the card's expiration month.
        """
        exp_year: int
        """
        Four-digit number representing the card's expiration year.
        """
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular card number. You can use this attribute to check whether two customers who've signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

        *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.*
        """
        funding: Optional[str]
        """
        Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
        """
        iin: Optional[str]
        """
        Issuer identification number of the card. (For internal use only and not typically available in standard API requests.)
        """
        issuer: Optional[str]
        """
        The name of the card's issuing bank. (For internal use only and not typically available in standard API requests.)
        """
        last4: Optional[str]
        """
        The last four digits of the card.
        """
        networks: Optional[Networks]
        """
        Contains information about card networks that can be used to process the payment.
        """
        offline: Optional[Offline]
        """
        Details about payment methods collected offline.
        """
        preferred_locales: Optional[List[str]]
        """
        The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card's chip.
        """
        read_method: Optional[
            Literal[
                "contact_emv",
                "contactless_emv",
                "contactless_magstripe_mode",
                "magnetic_stripe_fallback",
                "magnetic_stripe_track2",
            ]
        ]
        """
        How card details were read in this transaction.
        """
        wallet: Optional[Wallet]
        _inner_class_types = {
            "networks": Networks,
            "offline": Offline,
            "wallet": Wallet,
        }

    class Cashapp(StripeObject):
        buyer_id: Optional[str]
        """
        A unique and immutable identifier assigned by Cash App to every buyer.
        """
        cashtag: Optional[str]
        """
        A public identifier for buyers using Cash App.
        """

    class Crypto(StripeObject):
        pass

    class CustomerBalance(StripeObject):
        pass

    class Eps(StripeObject):
        bank: Optional[
            Literal[
                "arzte_und_apotheker_bank",
                "austrian_anadi_bank_ag",
                "bank_austria",
                "bankhaus_carl_spangler",
                "bankhaus_schelhammer_und_schattera_ag",
                "bawag_psk_ag",
                "bks_bank_ag",
                "brull_kallmus_bank_ag",
                "btv_vier_lander_bank",
                "capital_bank_grawe_gruppe_ag",
                "deutsche_bank_ag",
                "dolomitenbank",
                "easybank_ag",
                "erste_bank_und_sparkassen",
                "hypo_alpeadriabank_international_ag",
                "hypo_bank_burgenland_aktiengesellschaft",
                "hypo_noe_lb_fur_niederosterreich_u_wien",
                "hypo_oberosterreich_salzburg_steiermark",
                "hypo_tirol_bank_ag",
                "hypo_vorarlberg_bank_ag",
                "marchfelder_bank",
                "oberbank_ag",
                "raiffeisen_bankengruppe_osterreich",
                "schoellerbank_ag",
                "sparda_bank_wien",
                "volksbank_gruppe",
                "volkskreditbank_ag",
                "vr_bank_braunau",
            ]
        ]
        """
        The customer's bank. Should be one of `arzte_und_apotheker_bank`, `austrian_anadi_bank_ag`, `bank_austria`, `bankhaus_carl_spangler`, `bankhaus_schelhammer_und_schattera_ag`, `bawag_psk_ag`, `bks_bank_ag`, `brull_kallmus_bank_ag`, `btv_vier_lander_bank`, `capital_bank_grawe_gruppe_ag`, `deutsche_bank_ag`, `dolomitenbank`, `easybank_ag`, `erste_bank_und_sparkassen`, `hypo_alpeadriabank_international_ag`, `hypo_noe_lb_fur_niederosterreich_u_wien`, `hypo_oberosterreich_salzburg_steiermark`, `hypo_tirol_bank_ag`, `hypo_vorarlberg_bank_ag`, `hypo_bank_burgenland_aktiengesellschaft`, `marchfelder_bank`, `oberbank_ag`, `raiffeisen_bankengruppe_osterreich`, `schoellerbank_ag`, `sparda_bank_wien`, `volksbank_gruppe`, `volkskreditbank_ag`, or `vr_bank_braunau`.
        """

    class Fpx(StripeObject):
        account_holder_type: Optional[Literal["company", "individual"]]
        """
        Account holder type, if provided. Can be one of `individual` or `company`.
        """
        bank: Literal[
            "affin_bank",
            "agrobank",
            "alliance_bank",
            "ambank",
            "bank_islam",
            "bank_muamalat",
            "bank_of_china",
            "bank_rakyat",
            "bsn",
            "cimb",
            "deutsche_bank",
            "hong_leong_bank",
            "hsbc",
            "kfh",
            "maybank2e",
            "maybank2u",
            "ocbc",
            "pb_enterprise",
            "public_bank",
            "rhb",
            "standard_chartered",
            "uob",
        ]
        """
        The customer's bank, if provided. Can be one of `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_rakyat`, `bsn`, `cimb`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2u`, `ocbc`, `public_bank`, `rhb`, `standard_chartered`, `uob`, `deutsche_bank`, `maybank2e`, `pb_enterprise`, or `bank_of_china`.
        """

    class Giropay(StripeObject):
        pass

    class Grabpay(StripeObject):
        pass

    class Ideal(StripeObject):
        bank: Optional[
            Literal[
                "abn_amro",
                "asn_bank",
                "bunq",
                "buut",
                "handelsbanken",
                "ing",
                "knab",
                "moneyou",
                "n26",
                "nn",
                "rabobank",
                "regiobank",
                "revolut",
                "sns_bank",
                "triodos_bank",
                "van_lanschot",
                "yoursafe",
            ]
        ]
        """
        The customer's bank, if provided. Can be one of `abn_amro`, `asn_bank`, `bunq`, `buut`, `handelsbanken`, `ing`, `knab`, `moneyou`, `n26`, `nn`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, or `yoursafe`.
        """
        bic: Optional[
            Literal[
                "ABNANL2A",
                "ASNBNL21",
                "BITSNL2A",
                "BUNQNL2A",
                "BUUTNL2A",
                "FVLBNL22",
                "HANDNL2A",
                "INGBNL2A",
                "KNABNL2H",
                "MOYONL21",
                "NNBANL2G",
                "NTSBDEB1",
                "RABONL2U",
                "RBRBNL21",
                "REVOIE23",
                "REVOLT21",
                "SNSBNL2A",
                "TRIONL2U",
            ]
        ]
        """
        The Bank Identifier Code of the customer's bank, if the bank was provided.
        """

    class InteracPresent(StripeObject):
        class Networks(StripeObject):
            available: List[str]
            """
            All networks available for selection via [payment_method_options.card.network](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-payment_method_options-card-network).
            """
            preferred: Optional[str]
            """
            The preferred network for the card.
            """

        brand: Optional[str]
        """
        Card brand. Can be `interac`, `mastercard` or `visa`.
        """
        cardholder_name: Optional[str]
        """
        The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.
        """
        country: Optional[str]
        """
        Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
        """
        description: Optional[str]
        """
        A high-level description of the type of cards issued in this range. (For internal use only and not typically available in standard API requests.)
        """
        exp_month: int
        """
        Two-digit number representing the card's expiration month.
        """
        exp_year: int
        """
        Four-digit number representing the card's expiration year.
        """
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular card number. You can use this attribute to check whether two customers who've signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

        *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.*
        """
        funding: Optional[str]
        """
        Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
        """
        iin: Optional[str]
        """
        Issuer identification number of the card. (For internal use only and not typically available in standard API requests.)
        """
        issuer: Optional[str]
        """
        The name of the card's issuing bank. (For internal use only and not typically available in standard API requests.)
        """
        last4: Optional[str]
        """
        The last four digits of the card.
        """
        networks: Optional[Networks]
        """
        Contains information about card networks that can be used to process the payment.
        """
        preferred_locales: Optional[List[str]]
        """
        The languages that the issuing bank recommends using for localizing any customer-facing text, as read from the card. Referenced from EMV tag 5F2D, data encoded on the card's chip.
        """
        read_method: Optional[
            Literal[
                "contact_emv",
                "contactless_emv",
                "contactless_magstripe_mode",
                "magnetic_stripe_fallback",
                "magnetic_stripe_track2",
            ]
        ]
        """
        How card details were read in this transaction.
        """
        _inner_class_types = {"networks": Networks}

    class KakaoPay(StripeObject):
        pass

    class Klarna(StripeObject):
        class Dob(StripeObject):
            day: Optional[int]
            """
            The day of birth, between 1 and 31.
            """
            month: Optional[int]
            """
            The month of birth, between 1 and 12.
            """
            year: Optional[int]
            """
            The four-digit year of birth.
            """

        dob: Optional[Dob]
        """
        The customer's date of birth, if provided.
        """
        _inner_class_types = {"dob": Dob}

    class Konbini(StripeObject):
        pass

    class KrCard(StripeObject):
        brand: Optional[
            Literal[
                "bc",
                "citi",
                "hana",
                "hyundai",
                "jeju",
                "jeonbuk",
                "kakaobank",
                "kbank",
                "kdbbank",
                "kookmin",
                "kwangju",
                "lotte",
                "mg",
                "nh",
                "post",
                "samsung",
                "savingsbank",
                "shinhan",
                "shinhyup",
                "suhyup",
                "tossbank",
                "woori",
            ]
        ]
        """
        The local credit or debit card brand.
        """
        last4: Optional[str]
        """
        The last four digits of the card. This may not be present for American Express cards.
        """

    class Link(StripeObject):
        email: Optional[str]
        """
        Account owner's email address.
        """
        persistent_token: Optional[str]
        """
        [Deprecated] This is a legacy parameter that no longer has any function.
        """

    class MbWay(StripeObject):
        pass

    class Mobilepay(StripeObject):
        pass

    class Multibanco(StripeObject):
        pass

    class NaverPay(StripeObject):
        buyer_id: Optional[str]
        """
        Uniquely identifies this particular Naver Pay account. You can use this attribute to check whether two Naver Pay accounts are the same.
        """
        funding: Literal["card", "points"]
        """
        Whether to fund this transaction with Naver Pay points or a card.
        """

    class NzBankAccount(StripeObject):
        account_holder_name: Optional[str]
        """
        The name on the bank account. Only present if the account holder name is different from the name of the authorized signatory collected in the PaymentMethod's billing details.
        """
        bank_code: str
        """
        The numeric code for the bank account's bank.
        """
        bank_name: str
        """
        The name of the bank.
        """
        branch_code: str
        """
        The numeric code for the bank account's bank branch.
        """
        last4: str
        """
        Last four digits of the bank account number.
        """
        suffix: Optional[str]
        """
        The suffix of the bank account number.
        """

    class Oxxo(StripeObject):
        pass

    class P24(StripeObject):
        bank: Optional[
            Literal[
                "alior_bank",
                "bank_millennium",
                "bank_nowy_bfg_sa",
                "bank_pekao_sa",
                "banki_spbdzielcze",
                "blik",
                "bnp_paribas",
                "boz",
                "citi_handlowy",
                "credit_agricole",
                "envelobank",
                "etransfer_pocztowy24",
                "getin_bank",
                "ideabank",
                "ing",
                "inteligo",
                "mbank_mtransfer",
                "nest_przelew",
                "noble_pay",
                "pbac_z_ipko",
                "plus_bank",
                "santander_przelew24",
                "tmobile_usbugi_bankowe",
                "toyota_bank",
                "velobank",
                "volkswagen_bank",
            ]
        ]
        """
        The customer's bank, if provided.
        """

    class PayByBank(StripeObject):
        pass

    class Payco(StripeObject):
        pass

    class Paynow(StripeObject):
        pass

    class Paypal(StripeObject):
        country: Optional[str]
        """
        Two-letter ISO code representing the buyer's country. Values are provided by PayPal directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
        """
        payer_email: Optional[str]
        """
        Owner's email. Values are provided by PayPal directly
        (if supported) at the time of authorization or settlement. They cannot be set or mutated.
        """
        payer_id: Optional[str]
        """
        PayPal account PayerID. This identifier uniquely identifies the PayPal customer.
        """

    class Pix(StripeObject):
        pass

    class Promptpay(StripeObject):
        pass

    class RadarOptions(StripeObject):
        session: Optional[str]
        """
        A [Radar Session](https://stripe.com/docs/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
        """

    class RevolutPay(StripeObject):
        pass

    class SamsungPay(StripeObject):
        pass

    class Satispay(StripeObject):
        pass

    class SepaDebit(StripeObject):
        class GeneratedFrom(StripeObject):
            charge: Optional[ExpandableField["Charge"]]
            """
            The ID of the Charge that generated this PaymentMethod, if any.
            """
            setup_attempt: Optional[ExpandableField["SetupAttempt"]]
            """
            The ID of the SetupAttempt that generated this PaymentMethod, if any.
            """

        bank_code: Optional[str]
        """
        Bank code of bank associated with the bank account.
        """
        branch_code: Optional[str]
        """
        Branch code of bank associated with the bank account.
        """
        country: Optional[str]
        """
        Two-letter ISO code representing the country the bank account is located in.
        """
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
        """
        generated_from: Optional[GeneratedFrom]
        """
        Information about the object that generated this PaymentMethod.
        """
        last4: Optional[str]
        """
        Last four characters of the IBAN.
        """
        _inner_class_types = {"generated_from": GeneratedFrom}

    class Sofort(StripeObject):
        country: Optional[str]
        """
        Two-letter ISO code representing the country the bank account is located in.
        """

    class Swish(StripeObject):
        pass

    class Twint(StripeObject):
        pass

    class UsBankAccount(StripeObject):
        class Networks(StripeObject):
            preferred: Optional[str]
            """
            The preferred network.
            """
            supported: List[Literal["ach", "us_domestic_wire"]]
            """
            All supported networks.
            """

        class StatusDetails(StripeObject):
            class Blocked(StripeObject):
                network_code: Optional[
                    Literal[
                        "R02",
                        "R03",
                        "R04",
                        "R05",
                        "R07",
                        "R08",
                        "R10",
                        "R11",
                        "R16",
                        "R20",
                        "R29",
                        "R31",
                    ]
                ]
                """
                The ACH network code that resulted in this block.
                """
                reason: Optional[
                    Literal[
                        "bank_account_closed",
                        "bank_account_frozen",
                        "bank_account_invalid_details",
                        "bank_account_restricted",
                        "bank_account_unusable",
                        "debit_not_authorized",
                    ]
                ]
                """
                The reason why this PaymentMethod's fingerprint has been blocked
                """

            blocked: Optional[Blocked]
            _inner_class_types = {"blocked": Blocked}

        account_holder_type: Optional[Literal["company", "individual"]]
        """
        Account holder type: individual or company.
        """
        account_type: Optional[Literal["checking", "savings"]]
        """
        Account type: checkings or savings. Defaults to checking if omitted.
        """
        bank_name: Optional[str]
        """
        The name of the bank.
        """
        financial_connections_account: Optional[str]
        """
        The ID of the Financial Connections Account used to create the payment method.
        """
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
        """
        last4: Optional[str]
        """
        Last four digits of the bank account number.
        """
        networks: Optional[Networks]
        """
        Contains information about US bank account networks that can be used.
        """
        routing_number: Optional[str]
        """
        Routing number of the bank account.
        """
        status_details: Optional[StatusDetails]
        """
        Contains information about the future reusability of this PaymentMethod.
        """
        _inner_class_types = {
            "networks": Networks,
            "status_details": StatusDetails,
        }

    class WechatPay(StripeObject):
        pass

    class Zip(StripeObject):
        pass

    acss_debit: Optional[AcssDebit]
    affirm: Optional[Affirm]
    afterpay_clearpay: Optional[AfterpayClearpay]
    alipay: Optional[Alipay]
    allow_redisplay: Optional[Literal["always", "limited", "unspecified"]]
    """
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to “unspecified”.
    """
    alma: Optional[Alma]
    amazon_pay: Optional[AmazonPay]
    au_becs_debit: Optional[AuBecsDebit]
    bacs_debit: Optional[BacsDebit]
    bancontact: Optional[Bancontact]
    billie: Optional[Billie]
    billing_details: BillingDetails
    blik: Optional[Blik]
    boleto: Optional[Boleto]
    card: Optional[Card]
    card_present: Optional[CardPresent]
    cashapp: Optional[Cashapp]
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    crypto: Optional[Crypto]
    customer: Optional[ExpandableField["Customer"]]
    """
    The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.
    """
    customer_balance: Optional[CustomerBalance]
    eps: Optional[Eps]
    fpx: Optional[Fpx]
    giropay: Optional[Giropay]
    grabpay: Optional[Grabpay]
    id: str
    """
    Unique identifier for the object.
    """
    ideal: Optional[Ideal]
    interac_present: Optional[InteracPresent]
    kakao_pay: Optional[KakaoPay]
    klarna: Optional[Klarna]
    konbini: Optional[Konbini]
    kr_card: Optional[KrCard]
    link: Optional[Link]
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    mb_way: Optional[MbWay]
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    mobilepay: Optional[Mobilepay]
    multibanco: Optional[Multibanco]
    naver_pay: Optional[NaverPay]
    nz_bank_account: Optional[NzBankAccount]
    object: Literal["payment_method"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    oxxo: Optional[Oxxo]
    p24: Optional[P24]
    pay_by_bank: Optional[PayByBank]
    payco: Optional[Payco]
    paynow: Optional[Paynow]
    paypal: Optional[Paypal]
    pix: Optional[Pix]
    promptpay: Optional[Promptpay]
    radar_options: Optional[RadarOptions]
    """
    Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
    """
    revolut_pay: Optional[RevolutPay]
    samsung_pay: Optional[SamsungPay]
    satispay: Optional[Satispay]
    sepa_debit: Optional[SepaDebit]
    sofort: Optional[Sofort]
    swish: Optional[Swish]
    twint: Optional[Twint]
    type: Literal[
        "acss_debit",
        "affirm",
        "afterpay_clearpay",
        "alipay",
        "alma",
        "amazon_pay",
        "au_becs_debit",
        "bacs_debit",
        "bancontact",
        "billie",
        "blik",
        "boleto",
        "card",
        "card_present",
        "cashapp",
        "crypto",
        "customer_balance",
        "eps",
        "fpx",
        "giropay",
        "grabpay",
        "ideal",
        "interac_present",
        "kakao_pay",
        "klarna",
        "konbini",
        "kr_card",
        "link",
        "mb_way",
        "mobilepay",
        "multibanco",
        "naver_pay",
        "nz_bank_account",
        "oxxo",
        "p24",
        "pay_by_bank",
        "payco",
        "paynow",
        "paypal",
        "pix",
        "promptpay",
        "revolut_pay",
        "samsung_pay",
        "satispay",
        "sepa_debit",
        "sofort",
        "swish",
        "twint",
        "us_bank_account",
        "wechat_pay",
        "zip",
    ]
    """
    The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
    """
    us_bank_account: Optional[UsBankAccount]
    wechat_pay: Optional[WechatPay]
    zip: Optional[Zip]

    @classmethod
    def _cls_attach(
        cls, payment_method: str, **params: Unpack["PaymentMethodAttachParams"]
    ) -> "PaymentMethod":
        """
        Attaches a PaymentMethod object to a Customer.

        To attach a new PaymentMethod to a customer for future payments, we recommend you use a [SetupIntent](https://docs.stripe.com/docs/api/setup_intents)
        or a PaymentIntent with [setup_future_usage](https://docs.stripe.com/docs/api/payment_intents/create#create_payment_intent-setup_future_usage).
        These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the /v1/payment_methods/:id/attach
        endpoint without first using a SetupIntent or PaymentIntent with setup_future_usage does not optimize the PaymentMethod for
        future use, which makes later declines and payment friction more likely.
        See [Optimizing cards for future payments](https://docs.stripe.com/docs/payments/payment-intents#future-usage) for more information about setting up
        future payments.

        To use this PaymentMethod as the default for invoice or subscription payments,
        set [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method),
        on the Customer to the PaymentMethod's ID.
        """
        return cast(
            "PaymentMethod",
            cls._static_request(
                "post",
                "/v1/payment_methods/{payment_method}/attach".format(
                    payment_method=sanitize_id(payment_method)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def attach(
        payment_method: str, **params: Unpack["PaymentMethodAttachParams"]
    ) -> "PaymentMethod":
        """
        Attaches a PaymentMethod object to a Customer.

        To attach a new PaymentMethod to a customer for future payments, we recommend you use a [SetupIntent](https://docs.stripe.com/docs/api/setup_intents)
        or a PaymentIntent with [setup_future_usage](https://docs.stripe.com/docs/api/payment_intents/create#create_payment_intent-setup_future_usage).
        These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the /v1/payment_methods/:id/attach
        endpoint without first using a SetupIntent or PaymentIntent with setup_future_usage does not optimize the PaymentMethod for
        future use, which makes later declines and payment friction more likely.
        See [Optimizing cards for future payments](https://docs.stripe.com/docs/payments/payment-intents#future-usage) for more information about setting up
        future payments.

        To use this PaymentMethod as the default for invoice or subscription payments,
        set [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method),
        on the Customer to the PaymentMethod's ID.
        """
        ...

    @overload
    def attach(
        self, **params: Unpack["PaymentMethodAttachParams"]
    ) -> "PaymentMethod":
        """
        Attaches a PaymentMethod object to a Customer.

        To attach a new PaymentMethod to a customer for future payments, we recommend you use a [SetupIntent](https://docs.stripe.com/docs/api/setup_intents)
        or a PaymentIntent with [setup_future_usage](https://docs.stripe.com/docs/api/payment_intents/create#create_payment_intent-setup_future_usage).
        These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the /v1/payment_methods/:id/attach
        endpoint without first using a SetupIntent or PaymentIntent with setup_future_usage does not optimize the PaymentMethod for
        future use, which makes later declines and payment friction more likely.
        See [Optimizing cards for future payments](https://docs.stripe.com/docs/payments/payment-intents#future-usage) for more information about setting up
        future payments.

        To use this PaymentMethod as the default for invoice or subscription payments,
        set [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method),
        on the Customer to the PaymentMethod's ID.
        """
        ...

    @class_method_variant("_cls_attach")
    def attach(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["PaymentMethodAttachParams"]
    ) -> "PaymentMethod":
        """
        Attaches a PaymentMethod object to a Customer.

        To attach a new PaymentMethod to a customer for future payments, we recommend you use a [SetupIntent](https://docs.stripe.com/docs/api/setup_intents)
        or a PaymentIntent with [setup_future_usage](https://docs.stripe.com/docs/api/payment_intents/create#create_payment_intent-setup_future_usage).
        These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the /v1/payment_methods/:id/attach
        endpoint without first using a SetupIntent or PaymentIntent with setup_future_usage does not optimize the PaymentMethod for
        future use, which makes later declines and payment friction more likely.
        See [Optimizing cards for future payments](https://docs.stripe.com/docs/payments/payment-intents#future-usage) for more information about setting up
        future payments.

        To use this PaymentMethod as the default for invoice or subscription payments,
        set [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method),
        on the Customer to the PaymentMethod's ID.
        """
        return cast(
            "PaymentMethod",
            self._request(
                "post",
                "/v1/payment_methods/{payment_method}/attach".format(
                    payment_method=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_attach_async(
        cls, payment_method: str, **params: Unpack["PaymentMethodAttachParams"]
    ) -> "PaymentMethod":
        """
        Attaches a PaymentMethod object to a Customer.

        To attach a new PaymentMethod to a customer for future payments, we recommend you use a [SetupIntent](https://docs.stripe.com/docs/api/setup_intents)
        or a PaymentIntent with [setup_future_usage](https://docs.stripe.com/docs/api/payment_intents/create#create_payment_intent-setup_future_usage).
        These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the /v1/payment_methods/:id/attach
        endpoint without first using a SetupIntent or PaymentIntent with setup_future_usage does not optimize the PaymentMethod for
        future use, which makes later declines and payment friction more likely.
        See [Optimizing cards for future payments](https://docs.stripe.com/docs/payments/payment-intents#future-usage) for more information about setting up
        future payments.

        To use this PaymentMethod as the default for invoice or subscription payments,
        set [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method),
        on the Customer to the PaymentMethod's ID.
        """
        return cast(
            "PaymentMethod",
            await cls._static_request_async(
                "post",
                "/v1/payment_methods/{payment_method}/attach".format(
                    payment_method=sanitize_id(payment_method)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def attach_async(
        payment_method: str, **params: Unpack["PaymentMethodAttachParams"]
    ) -> "PaymentMethod":
        """
        Attaches a PaymentMethod object to a Customer.

        To attach a new PaymentMethod to a customer for future payments, we recommend you use a [SetupIntent](https://docs.stripe.com/docs/api/setup_intents)
        or a PaymentIntent with [setup_future_usage](https://docs.stripe.com/docs/api/payment_intents/create#create_payment_intent-setup_future_usage).
        These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the /v1/payment_methods/:id/attach
        endpoint without first using a SetupIntent or PaymentIntent with setup_future_usage does not optimize the PaymentMethod for
        future use, which makes later declines and payment friction more likely.
        See [Optimizing cards for future payments](https://docs.stripe.com/docs/payments/payment-intents#future-usage) for more information about setting up
        future payments.

        To use this PaymentMethod as the default for invoice or subscription payments,
        set [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method),
        on the Customer to the PaymentMethod's ID.
        """
        ...

    @overload
    async def attach_async(
        self, **params: Unpack["PaymentMethodAttachParams"]
    ) -> "PaymentMethod":
        """
        Attaches a PaymentMethod object to a Customer.

        To attach a new PaymentMethod to a customer for future payments, we recommend you use a [SetupIntent](https://docs.stripe.com/docs/api/setup_intents)
        or a PaymentIntent with [setup_future_usage](https://docs.stripe.com/docs/api/payment_intents/create#create_payment_intent-setup_future_usage).
        These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the /v1/payment_methods/:id/attach
        endpoint without first using a SetupIntent or PaymentIntent with setup_future_usage does not optimize the PaymentMethod for
        future use, which makes later declines and payment friction more likely.
        See [Optimizing cards for future payments](https://docs.stripe.com/docs/payments/payment-intents#future-usage) for more information about setting up
        future payments.

        To use this PaymentMethod as the default for invoice or subscription payments,
        set [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method),
        on the Customer to the PaymentMethod's ID.
        """
        ...

    @class_method_variant("_cls_attach_async")
    async def attach_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["PaymentMethodAttachParams"]
    ) -> "PaymentMethod":
        """
        Attaches a PaymentMethod object to a Customer.

        To attach a new PaymentMethod to a customer for future payments, we recommend you use a [SetupIntent](https://docs.stripe.com/docs/api/setup_intents)
        or a PaymentIntent with [setup_future_usage](https://docs.stripe.com/docs/api/payment_intents/create#create_payment_intent-setup_future_usage).
        These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the /v1/payment_methods/:id/attach
        endpoint without first using a SetupIntent or PaymentIntent with setup_future_usage does not optimize the PaymentMethod for
        future use, which makes later declines and payment friction more likely.
        See [Optimizing cards for future payments](https://docs.stripe.com/docs/payments/payment-intents#future-usage) for more information about setting up
        future payments.

        To use this PaymentMethod as the default for invoice or subscription payments,
        set [invoice_settings.default_payment_method](https://docs.stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method),
        on the Customer to the PaymentMethod's ID.
        """
        return cast(
            "PaymentMethod",
            await self._request_async(
                "post",
                "/v1/payment_methods/{payment_method}/attach".format(
                    payment_method=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def create(
        cls, **params: Unpack["PaymentMethodCreateParams"]
    ) -> "PaymentMethod":
        """
        Creates a PaymentMethod object. Read the [Stripe.js reference](https://docs.stripe.com/docs/stripe-js/reference#stripe-create-payment-method) to learn how to create PaymentMethods via Stripe.js.

        Instead of creating a PaymentMethod directly, we recommend using the [PaymentIntents API to accept a payment immediately or the <a href="/docs/payments/save-and-reuse">SetupIntent](https://docs.stripe.com/docs/payments/accept-a-payment) API to collect payment method details ahead of a future payment.
        """
        return cast(
            "PaymentMethod",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["PaymentMethodCreateParams"]
    ) -> "PaymentMethod":
        """
        Creates a PaymentMethod object. Read the [Stripe.js reference](https://docs.stripe.com/docs/stripe-js/reference#stripe-create-payment-method) to learn how to create PaymentMethods via Stripe.js.

        Instead of creating a PaymentMethod directly, we recommend using the [PaymentIntents API to accept a payment immediately or the <a href="/docs/payments/save-and-reuse">SetupIntent](https://docs.stripe.com/docs/payments/accept-a-payment) API to collect payment method details ahead of a future payment.
        """
        return cast(
            "PaymentMethod",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def _cls_detach(
        cls, payment_method: str, **params: Unpack["PaymentMethodDetachParams"]
    ) -> "PaymentMethod":
        """
        Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.
        """
        return cast(
            "PaymentMethod",
            cls._static_request(
                "post",
                "/v1/payment_methods/{payment_method}/detach".format(
                    payment_method=sanitize_id(payment_method)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def detach(
        payment_method: str, **params: Unpack["PaymentMethodDetachParams"]
    ) -> "PaymentMethod":
        """
        Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.
        """
        ...

    @overload
    def detach(
        self, **params: Unpack["PaymentMethodDetachParams"]
    ) -> "PaymentMethod":
        """
        Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.
        """
        ...

    @class_method_variant("_cls_detach")
    def detach(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["PaymentMethodDetachParams"]
    ) -> "PaymentMethod":
        """
        Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.
        """
        return cast(
            "PaymentMethod",
            self._request(
                "post",
                "/v1/payment_methods/{payment_method}/detach".format(
                    payment_method=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_detach_async(
        cls, payment_method: str, **params: Unpack["PaymentMethodDetachParams"]
    ) -> "PaymentMethod":
        """
        Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.
        """
        return cast(
            "PaymentMethod",
            await cls._static_request_async(
                "post",
                "/v1/payment_methods/{payment_method}/detach".format(
                    payment_method=sanitize_id(payment_method)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def detach_async(
        payment_method: str, **params: Unpack["PaymentMethodDetachParams"]
    ) -> "PaymentMethod":
        """
        Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.
        """
        ...

    @overload
    async def detach_async(
        self, **params: Unpack["PaymentMethodDetachParams"]
    ) -> "PaymentMethod":
        """
        Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.
        """
        ...

    @class_method_variant("_cls_detach_async")
    async def detach_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["PaymentMethodDetachParams"]
    ) -> "PaymentMethod":
        """
        Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.
        """
        return cast(
            "PaymentMethod",
            await self._request_async(
                "post",
                "/v1/payment_methods/{payment_method}/detach".format(
                    payment_method=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["PaymentMethodListParams"]
    ) -> ListObject["PaymentMethod"]:
        """
        Returns a list of PaymentMethods for Treasury flows. If you want to list the PaymentMethods attached to a Customer for payments, you should use the [List a Customer's PaymentMethods](https://docs.stripe.com/docs/api/payment_methods/customer_list) API instead.
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["PaymentMethodListParams"]
    ) -> ListObject["PaymentMethod"]:
        """
        Returns a list of PaymentMethods for Treasury flows. If you want to list the PaymentMethods attached to a Customer for payments, you should use the [List a Customer's PaymentMethods](https://docs.stripe.com/docs/api/payment_methods/customer_list) API instead.
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["PaymentMethodModifyParams"]
    ) -> "PaymentMethod":
        """
        Updates a PaymentMethod object. A PaymentMethod must be attached to a customer to be updated.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "PaymentMethod",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["PaymentMethodModifyParams"]
    ) -> "PaymentMethod":
        """
        Updates a PaymentMethod object. A PaymentMethod must be attached to a customer to be updated.
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "PaymentMethod",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PaymentMethodRetrieveParams"]
    ) -> "PaymentMethod":
        """
        Retrieves a PaymentMethod object attached to the StripeAccount. To retrieve a payment method attached to a Customer, you should use [Retrieve a Customer's PaymentMethods](https://docs.stripe.com/docs/api/payment_methods/customer)
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["PaymentMethodRetrieveParams"]
    ) -> "PaymentMethod":
        """
        Retrieves a PaymentMethod object attached to the StripeAccount. To retrieve a payment method attached to a Customer, you should use [Retrieve a Customer's PaymentMethods](https://docs.stripe.com/docs/api/payment_methods/customer)
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {
        "acss_debit": AcssDebit,
        "affirm": Affirm,
        "afterpay_clearpay": AfterpayClearpay,
        "alipay": Alipay,
        "alma": Alma,
        "amazon_pay": AmazonPay,
        "au_becs_debit": AuBecsDebit,
        "bacs_debit": BacsDebit,
        "bancontact": Bancontact,
        "billie": Billie,
        "billing_details": BillingDetails,
        "blik": Blik,
        "boleto": Boleto,
        "card": Card,
        "card_present": CardPresent,
        "cashapp": Cashapp,
        "crypto": Crypto,
        "customer_balance": CustomerBalance,
        "eps": Eps,
        "fpx": Fpx,
        "giropay": Giropay,
        "grabpay": Grabpay,
        "ideal": Ideal,
        "interac_present": InteracPresent,
        "kakao_pay": KakaoPay,
        "klarna": Klarna,
        "konbini": Konbini,
        "kr_card": KrCard,
        "link": Link,
        "mb_way": MbWay,
        "mobilepay": Mobilepay,
        "multibanco": Multibanco,
        "naver_pay": NaverPay,
        "nz_bank_account": NzBankAccount,
        "oxxo": Oxxo,
        "p24": P24,
        "pay_by_bank": PayByBank,
        "payco": Payco,
        "paynow": Paynow,
        "paypal": Paypal,
        "pix": Pix,
        "promptpay": Promptpay,
        "radar_options": RadarOptions,
        "revolut_pay": RevolutPay,
        "samsung_pay": SamsungPay,
        "satispay": Satispay,
        "sepa_debit": SepaDebit,
        "sofort": Sofort,
        "swish": Swish,
        "twint": Twint,
        "us_bank_account": UsBankAccount,
        "wechat_pay": WechatPay,
        "zip": Zip,
    }
