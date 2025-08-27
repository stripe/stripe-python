# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._collection_setting import CollectionSetting
from stripe.v2.billing.collection_settings._version_service import (
    VersionService,
)
from typing import List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict


class CollectionSettingService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.versions = VersionService(self._requestor)

    class CreateParams(TypedDict):
        collection_method: NotRequired[Literal["automatic", "send_invoice"]]
        """
        Either automatic, or send_invoice. When charging automatically, Stripe will attempt to pay this
        bill at the end of the period using the payment method attached to the payer profile. When sending an invoice,
        Stripe will email your payer profile an invoice with payment instructions.
        Defaults to automatic.
        """
        display_name: NotRequired[str]
        """
        An optional customer-facing display name for the CollectionSetting object.
        Maximum length of 250 characters.
        """
        email_delivery: NotRequired[
            "CollectionSettingService.CreateParamsEmailDelivery"
        ]
        """
        Email delivery setting.
        """
        lookup_key: NotRequired[str]
        """
        A lookup key used to retrieve settings dynamically from a static string.
        This may be up to 200 characters.
        """
        payment_method_configuration: NotRequired[str]
        """
        The ID of the PaymentMethodConfiguration object, which controls which payment methods are displayed to your customers.
        """
        payment_method_options: NotRequired[
            "CollectionSettingService.CreateParamsPaymentMethodOptions"
        ]
        """
        Payment Method specific configuration to be stored on the object.
        """

    class CreateParamsEmailDelivery(TypedDict):
        payment_due: NotRequired[
            "CollectionSettingService.CreateParamsEmailDeliveryPaymentDue"
        ]
        """
        Controls emails for when the payment is due. For example after the invoice is finilized and transition to Open state.
        """

    class CreateParamsEmailDeliveryPaymentDue(TypedDict):
        enabled: bool
        """
        If true an email for the invoice would be generated and sent out.
        """
        include_payment_link: bool
        """
        If true the payment link to hosted invocie page would be included in email and PDF of the invoice.
        """

    class CreateParamsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            "CollectionSettingService.CreateParamsPaymentMethodOptionsAcssDebit"
        ]
        """
        This sub-hash contains details about the Canadian pre-authorized debit payment method options.
        """
        bancontact: NotRequired[
            "CollectionSettingService.CreateParamsPaymentMethodOptionsBancontact"
        ]
        """
        This sub-hash contains details about the Bancontact payment method.
        """
        card: NotRequired[
            "CollectionSettingService.CreateParamsPaymentMethodOptionsCard"
        ]
        """
        This sub-hash contains details about the Card payment method options.
        """
        customer_balance: NotRequired[
            "CollectionSettingService.CreateParamsPaymentMethodOptionsCustomerBalance"
        ]
        """
        This sub-hash contains details about the Bank transfer payment method options.
        """
        konbini: NotRequired[
            "CollectionSettingService.CreateParamsPaymentMethodOptionsKonbini"
        ]
        """
        This sub-hash contains details about the Konbini payment method options.
        """
        sepa_debit: NotRequired[
            "CollectionSettingService.CreateParamsPaymentMethodOptionsSepaDebit"
        ]
        """
        This sub-hash contains details about the SEPA Direct Debit payment method options.
        """
        us_bank_account: NotRequired[
            "CollectionSettingService.CreateParamsPaymentMethodOptionsUsBankAccount"
        ]
        """
        This sub-hash contains details about the ACH direct debit payment method options.
        """

    class CreateParamsPaymentMethodOptionsAcssDebit(TypedDict):
        mandate_options: NotRequired[
            "CollectionSettingService.CreateParamsPaymentMethodOptionsAcssDebitMandateOptions"
        ]
        """
        Additional fields for Mandate creation.
        """
        verification_method: NotRequired[
            Literal["automatic", "instant", "microdeposits"]
        ]
        """
        Verification method.
        """

    class CreateParamsPaymentMethodOptionsAcssDebitMandateOptions(TypedDict):
        transaction_type: NotRequired[Literal["business", "personal"]]
        """
        Transaction type of the mandate.
        """

    class CreateParamsPaymentMethodOptionsBancontact(TypedDict):
        preferred_language: NotRequired[Literal["de", "en", "fr", "nl"]]
        """
        Preferred language of the Bancontact authorization page that the customer is redirected to.
        """

    class CreateParamsPaymentMethodOptionsCard(TypedDict):
        mandate_options: NotRequired[
            "CollectionSettingService.CreateParamsPaymentMethodOptionsCardMandateOptions"
        ]
        """
        Configuration options for setting up an eMandate for cards issued in India.
        """
        network: NotRequired[str]
        """
        Selected network to process the payment on. Depends on the available networks of the card.
        """
        request_three_d_secure: NotRequired[
            Literal["any", "automatic", "challenge"]
        ]
        """
        An advanced option 3D Secure. We strongly recommend that you rely on our SCA Engine to automatically prompt your customers
        for authentication based on risk level and [other requirements](https://docs.corp.stripe.com/strong-customer-authentication).
        However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option.
        Read our guide on [manually requesting 3D Secure](https://docs.corp.stripe.com/payments/3d-secure/authentication-flow#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
        """

    class CreateParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
        amount: NotRequired[int]
        """
        Amount to be charged for future payments.
        """
        amount_type: NotRequired[Literal["fixed", "maximum"]]
        """
        The AmountType for the mandate. One of `fixed` or `maximum`.
        """
        description: NotRequired[str]
        """
        A description of the mandate that is meant to be displayed to the customer.
        """

    class CreateParamsPaymentMethodOptionsCustomerBalance(TypedDict):
        bank_transfer: NotRequired[
            "CollectionSettingService.CreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer"
        ]
        """
        Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.
        """
        funding_type: NotRequired[Literal["bank_transfer"]]
        """
        The funding method type to be used when there are not enough funds in the customer balance. Currently the only supported value is `bank_transfer`.
        """

    class CreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            "CollectionSettingService.CreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
        ]
        """
        Configuration for `eu_bank_transfer` funding type. Required if `type` is `eu_bank_transfer`.
        """
        type: NotRequired[
            Literal[
                "eu_bank_transfer",
                "gb_bank_transfer",
                "jp_bank_transfer",
                "mx_bank_transfer",
                "us_bank_transfer",
            ]
        ]
        """
        The bank transfer type that can be used for funding.
        """

    class CreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
        TypedDict,
    ):
        country: Literal["BE", "DE", "ES", "FR", "IE", "NL"]
        """
        The desired country code of the bank account information.
        """

    class CreateParamsPaymentMethodOptionsKonbini(TypedDict):
        pass

    class CreateParamsPaymentMethodOptionsSepaDebit(TypedDict):
        pass

    class CreateParamsPaymentMethodOptionsUsBankAccount(TypedDict):
        financial_connections: "CollectionSettingService.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections"
        """
        Additional fields for Financial Connections Session creation.
        """
        verification_method: Literal["automatic", "instant", "microdeposits"]
        """
        Verification method.
        """

    class CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
        TypedDict,
    ):
        filters: NotRequired[
            "CollectionSettingService.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters"
        ]
        """
        Provide filters for the linked accounts that the customer can select for the payment method.
        """
        permissions: NotRequired[
            List[
                Literal[
                    "balances", "ownership", "payment_method", "transactions"
                ]
            ]
        ]
        """
        The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included.
        """
        prefetch: NotRequired[
            List[Literal["balances", "ownership", "transactions"]]
        ]
        """
        List of data features that you would like to retrieve upon account creation.
        """

    class CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters(
        TypedDict,
    ):
        account_subcategories: NotRequired[
            List[Literal["checking", "savings"]]
        ]
        """
        The account subcategories to use to filter for selectable accounts.
        """

    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 20.
        """
        lookup_keys: NotRequired[List[str]]
        """
        Only return the settings with these lookup_keys, if any exist.
        You can specify up to 10 lookup_keys.
        """

    class RetrieveParams(TypedDict):
        pass

    class UpdateParams(TypedDict):
        collection_method: NotRequired[Literal["automatic", "send_invoice"]]
        """
        Either automatic, or send_invoice. When charging automatically, Stripe will attempt to pay this
        bill at the end of the period using the payment method attached to the payer profile. When sending an invoice,
        Stripe will email your payer profile an invoice with payment instructions.
        """
        display_name: NotRequired[str]
        """
        An optional customer-facing display name for the CollectionSetting object.
        To remove the display name, set it to an empty string in the request.
        Maximum length of 250 characters.
        """
        email_delivery: NotRequired[
            Optional["CollectionSettingService.UpdateParamsEmailDelivery"]
        ]
        """
        Email delivery settings.
        """
        live_version: NotRequired[str]
        """
        Optionally change the live version of the CollectionSetting. Billing Cadences and other objects that refer to this
        CollectionSetting will use this version when no overrides are set. Providing `live_version = "latest"` will set the
        CollectionSetting's `live_version` to its latest version.
        """
        lookup_key: NotRequired[str]
        """
        A lookup key used to retrieve settings dynamically from a static string.
        This may be up to 200 characters.
        """
        payment_method_configuration: NotRequired[str]
        """
        The ID of the PaymentMethodConfiguration object, which controls which payment methods are displayed to your customers.
        """
        payment_method_options: NotRequired[
            "CollectionSettingService.UpdateParamsPaymentMethodOptions"
        ]
        """
        Payment Method specific configuration to be stored on the object.
        """

    class UpdateParamsEmailDelivery(TypedDict):
        payment_due: NotRequired[
            "CollectionSettingService.UpdateParamsEmailDeliveryPaymentDue"
        ]
        """
        Controls emails for when the payment is due. For example after the invoice is finilized and transition to Open state.
        """

    class UpdateParamsEmailDeliveryPaymentDue(TypedDict):
        enabled: bool
        """
        If true an email for the invoice would be generated and sent out.
        """
        include_payment_link: bool
        """
        If true the payment link to hosted invocie page would be included in email and PDF of the invoice.
        """

    class UpdateParamsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            "CollectionSettingService.UpdateParamsPaymentMethodOptionsAcssDebit"
        ]
        """
        This sub-hash contains details about the Canadian pre-authorized debit payment method options.
        """
        bancontact: NotRequired[
            "CollectionSettingService.UpdateParamsPaymentMethodOptionsBancontact"
        ]
        """
        This sub-hash contains details about the Bancontact payment method.
        """
        card: NotRequired[
            "CollectionSettingService.UpdateParamsPaymentMethodOptionsCard"
        ]
        """
        This sub-hash contains details about the Card payment method options.
        """
        customer_balance: NotRequired[
            "CollectionSettingService.UpdateParamsPaymentMethodOptionsCustomerBalance"
        ]
        """
        This sub-hash contains details about the Bank transfer payment method options.
        """
        konbini: NotRequired[
            "CollectionSettingService.UpdateParamsPaymentMethodOptionsKonbini"
        ]
        """
        This sub-hash contains details about the Konbini payment method options.
        """
        sepa_debit: NotRequired[
            "CollectionSettingService.UpdateParamsPaymentMethodOptionsSepaDebit"
        ]
        """
        This sub-hash contains details about the SEPA Direct Debit payment method options.
        """
        us_bank_account: NotRequired[
            "CollectionSettingService.UpdateParamsPaymentMethodOptionsUsBankAccount"
        ]
        """
        This sub-hash contains details about the ACH direct debit payment method options.
        """

    class UpdateParamsPaymentMethodOptionsAcssDebit(TypedDict):
        mandate_options: NotRequired[
            "CollectionSettingService.UpdateParamsPaymentMethodOptionsAcssDebitMandateOptions"
        ]
        """
        Additional fields for Mandate creation.
        """
        verification_method: NotRequired[
            Literal["automatic", "instant", "microdeposits"]
        ]
        """
        Verification method.
        """

    class UpdateParamsPaymentMethodOptionsAcssDebitMandateOptions(TypedDict):
        transaction_type: NotRequired[Literal["business", "personal"]]
        """
        Transaction type of the mandate.
        """

    class UpdateParamsPaymentMethodOptionsBancontact(TypedDict):
        preferred_language: NotRequired[Literal["de", "en", "fr", "nl"]]
        """
        Preferred language of the Bancontact authorization page that the customer is redirected to.
        """

    class UpdateParamsPaymentMethodOptionsCard(TypedDict):
        mandate_options: NotRequired[
            "CollectionSettingService.UpdateParamsPaymentMethodOptionsCardMandateOptions"
        ]
        """
        Configuration options for setting up an eMandate for cards issued in India.
        """
        network: NotRequired[str]
        """
        Selected network to process the payment on. Depends on the available networks of the card.
        """
        request_three_d_secure: NotRequired[
            Literal["any", "automatic", "challenge"]
        ]
        """
        An advanced option 3D Secure. We strongly recommend that you rely on our SCA Engine to automatically prompt your customers
        for authentication based on risk level and [other requirements](https://docs.corp.stripe.com/strong-customer-authentication).
        However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option.
        Read our guide on [manually requesting 3D Secure](https://docs.corp.stripe.com/payments/3d-secure/authentication-flow#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
        """

    class UpdateParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
        amount: NotRequired[int]
        """
        Amount to be charged for future payments.
        """
        amount_type: NotRequired[Literal["fixed", "maximum"]]
        """
        The AmountType for the mandate. One of `fixed` or `maximum`.
        """
        description: NotRequired[str]
        """
        A description of the mandate that is meant to be displayed to the customer.
        """

    class UpdateParamsPaymentMethodOptionsCustomerBalance(TypedDict):
        bank_transfer: NotRequired[
            "CollectionSettingService.UpdateParamsPaymentMethodOptionsCustomerBalanceBankTransfer"
        ]
        """
        Configuration for the bank transfer funding type, if the `funding_type` is set to `bank_transfer`.
        """
        funding_type: NotRequired[Literal["bank_transfer"]]
        """
        The funding method type to be used when there are not enough funds in the customer balance. Currently the only supported value is `bank_transfer`.
        """

    class UpdateParamsPaymentMethodOptionsCustomerBalanceBankTransfer(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            "CollectionSettingService.UpdateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
        ]
        """
        Configuration for `eu_bank_transfer` funding type. Required if `type` is `eu_bank_transfer`.
        """
        type: NotRequired[
            Literal[
                "eu_bank_transfer",
                "gb_bank_transfer",
                "jp_bank_transfer",
                "mx_bank_transfer",
                "us_bank_transfer",
            ]
        ]
        """
        The bank transfer type that can be used for funding.
        """

    class UpdateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
        TypedDict,
    ):
        country: Literal["BE", "DE", "ES", "FR", "IE", "NL"]
        """
        The desired country code of the bank account information.
        """

    class UpdateParamsPaymentMethodOptionsKonbini(TypedDict):
        pass

    class UpdateParamsPaymentMethodOptionsSepaDebit(TypedDict):
        pass

    class UpdateParamsPaymentMethodOptionsUsBankAccount(TypedDict):
        financial_connections: "CollectionSettingService.UpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnections"
        """
        Additional fields for Financial Connections Session creation.
        """
        verification_method: Literal["automatic", "instant", "microdeposits"]
        """
        Verification method.
        """

    class UpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
        TypedDict,
    ):
        filters: NotRequired[
            "CollectionSettingService.UpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters"
        ]
        """
        Provide filters for the linked accounts that the customer can select for the payment method.
        """
        permissions: NotRequired[
            List[
                Literal[
                    "balances", "ownership", "payment_method", "transactions"
                ]
            ]
        ]
        """
        The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included.
        """
        prefetch: NotRequired[
            List[Literal["balances", "ownership", "transactions"]]
        ]
        """
        List of data features that you would like to retrieve upon account creation.
        """

    class UpdateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters(
        TypedDict,
    ):
        account_subcategories: NotRequired[
            List[Literal["checking", "savings"]]
        ]
        """
        The account subcategories to use to filter for selectable accounts.
        """

    def list(
        self,
        params: "CollectionSettingService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[CollectionSetting]:
        """
        List all CollectionSetting objects.
        """
        return cast(
            ListObject[CollectionSetting],
            self._request(
                "get",
                "/v2/billing/collection_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "CollectionSettingService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[CollectionSetting]:
        """
        List all CollectionSetting objects.
        """
        return cast(
            ListObject[CollectionSetting],
            await self._request_async(
                "get",
                "/v2/billing/collection_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "CollectionSettingService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> CollectionSetting:
        """
        Create a CollectionSetting object.
        """
        return cast(
            CollectionSetting,
            self._request(
                "post",
                "/v2/billing/collection_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "CollectionSettingService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> CollectionSetting:
        """
        Create a CollectionSetting object.
        """
        return cast(
            CollectionSetting,
            await self._request_async(
                "post",
                "/v2/billing/collection_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "CollectionSettingService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CollectionSetting:
        """
        Retrieve a CollectionSetting by ID.
        """
        return cast(
            CollectionSetting,
            self._request(
                "get",
                "/v2/billing/collection_settings/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "CollectionSettingService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> CollectionSetting:
        """
        Retrieve a CollectionSetting by ID.
        """
        return cast(
            CollectionSetting,
            await self._request_async(
                "get",
                "/v2/billing/collection_settings/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "CollectionSettingService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> CollectionSetting:
        """
        Update fields on an existing CollectionSetting.
        """
        return cast(
            CollectionSetting,
            self._request(
                "post",
                "/v2/billing/collection_settings/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "CollectionSettingService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> CollectionSetting:
        """
        Update fields on an existing CollectionSetting.
        """
        return cast(
            CollectionSetting,
            await self._request_async(
                "post",
                "/v2/billing/collection_settings/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
