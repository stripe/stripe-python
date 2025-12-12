# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.checkout._session_create_params import (
        SessionCreateParams as SessionCreateParams,
        SessionCreateParamsAdaptivePricing as SessionCreateParamsAdaptivePricing,
        SessionCreateParamsAfterExpiration as SessionCreateParamsAfterExpiration,
        SessionCreateParamsAfterExpirationRecovery as SessionCreateParamsAfterExpirationRecovery,
        SessionCreateParamsAutomaticTax as SessionCreateParamsAutomaticTax,
        SessionCreateParamsAutomaticTaxLiability as SessionCreateParamsAutomaticTaxLiability,
        SessionCreateParamsBrandingSettings as SessionCreateParamsBrandingSettings,
        SessionCreateParamsBrandingSettingsIcon as SessionCreateParamsBrandingSettingsIcon,
        SessionCreateParamsBrandingSettingsLogo as SessionCreateParamsBrandingSettingsLogo,
        SessionCreateParamsCheckoutItem as SessionCreateParamsCheckoutItem,
        SessionCreateParamsCheckoutItemPricingPlanSubscriptionItem as SessionCreateParamsCheckoutItemPricingPlanSubscriptionItem,
        SessionCreateParamsCheckoutItemPricingPlanSubscriptionItemComponentConfigurations as SessionCreateParamsCheckoutItemPricingPlanSubscriptionItemComponentConfigurations,
        SessionCreateParamsCheckoutItemPricingPlanSubscriptionItemComponentConfigurationsLicenseFeeComponent as SessionCreateParamsCheckoutItemPricingPlanSubscriptionItemComponentConfigurationsLicenseFeeComponent,
        SessionCreateParamsCheckoutItemRateCardSubscriptionItem as SessionCreateParamsCheckoutItemRateCardSubscriptionItem,
        SessionCreateParamsConsentCollection as SessionCreateParamsConsentCollection,
        SessionCreateParamsConsentCollectionPaymentMethodReuseAgreement as SessionCreateParamsConsentCollectionPaymentMethodReuseAgreement,
        SessionCreateParamsCustomField as SessionCreateParamsCustomField,
        SessionCreateParamsCustomFieldDropdown as SessionCreateParamsCustomFieldDropdown,
        SessionCreateParamsCustomFieldDropdownOption as SessionCreateParamsCustomFieldDropdownOption,
        SessionCreateParamsCustomFieldLabel as SessionCreateParamsCustomFieldLabel,
        SessionCreateParamsCustomFieldNumeric as SessionCreateParamsCustomFieldNumeric,
        SessionCreateParamsCustomFieldText as SessionCreateParamsCustomFieldText,
        SessionCreateParamsCustomText as SessionCreateParamsCustomText,
        SessionCreateParamsCustomTextAfterSubmit as SessionCreateParamsCustomTextAfterSubmit,
        SessionCreateParamsCustomTextShippingAddress as SessionCreateParamsCustomTextShippingAddress,
        SessionCreateParamsCustomTextSubmit as SessionCreateParamsCustomTextSubmit,
        SessionCreateParamsCustomTextTermsOfServiceAcceptance as SessionCreateParamsCustomTextTermsOfServiceAcceptance,
        SessionCreateParamsCustomerUpdate as SessionCreateParamsCustomerUpdate,
        SessionCreateParamsDiscount as SessionCreateParamsDiscount,
        SessionCreateParamsDiscountCouponData as SessionCreateParamsDiscountCouponData,
        SessionCreateParamsInvoiceCreation as SessionCreateParamsInvoiceCreation,
        SessionCreateParamsInvoiceCreationInvoiceData as SessionCreateParamsInvoiceCreationInvoiceData,
        SessionCreateParamsInvoiceCreationInvoiceDataCustomField as SessionCreateParamsInvoiceCreationInvoiceDataCustomField,
        SessionCreateParamsInvoiceCreationInvoiceDataIssuer as SessionCreateParamsInvoiceCreationInvoiceDataIssuer,
        SessionCreateParamsInvoiceCreationInvoiceDataRenderingOptions as SessionCreateParamsInvoiceCreationInvoiceDataRenderingOptions,
        SessionCreateParamsLineItem as SessionCreateParamsLineItem,
        SessionCreateParamsLineItemAdjustableQuantity as SessionCreateParamsLineItemAdjustableQuantity,
        SessionCreateParamsLineItemPriceData as SessionCreateParamsLineItemPriceData,
        SessionCreateParamsLineItemPriceDataProductData as SessionCreateParamsLineItemPriceDataProductData,
        SessionCreateParamsLineItemPriceDataProductDataTaxDetails as SessionCreateParamsLineItemPriceDataProductDataTaxDetails,
        SessionCreateParamsLineItemPriceDataRecurring as SessionCreateParamsLineItemPriceDataRecurring,
        SessionCreateParamsNameCollection as SessionCreateParamsNameCollection,
        SessionCreateParamsNameCollectionBusiness as SessionCreateParamsNameCollectionBusiness,
        SessionCreateParamsNameCollectionIndividual as SessionCreateParamsNameCollectionIndividual,
        SessionCreateParamsOptionalItem as SessionCreateParamsOptionalItem,
        SessionCreateParamsOptionalItemAdjustableQuantity as SessionCreateParamsOptionalItemAdjustableQuantity,
        SessionCreateParamsPaymentIntentData as SessionCreateParamsPaymentIntentData,
        SessionCreateParamsPaymentIntentDataShipping as SessionCreateParamsPaymentIntentDataShipping,
        SessionCreateParamsPaymentIntentDataShippingAddress as SessionCreateParamsPaymentIntentDataShippingAddress,
        SessionCreateParamsPaymentIntentDataTransferData as SessionCreateParamsPaymentIntentDataTransferData,
        SessionCreateParamsPaymentMethodData as SessionCreateParamsPaymentMethodData,
        SessionCreateParamsPaymentMethodOptions as SessionCreateParamsPaymentMethodOptions,
        SessionCreateParamsPaymentMethodOptionsAcssDebit as SessionCreateParamsPaymentMethodOptionsAcssDebit,
        SessionCreateParamsPaymentMethodOptionsAcssDebitMandateOptions as SessionCreateParamsPaymentMethodOptionsAcssDebitMandateOptions,
        SessionCreateParamsPaymentMethodOptionsAffirm as SessionCreateParamsPaymentMethodOptionsAffirm,
        SessionCreateParamsPaymentMethodOptionsAfterpayClearpay as SessionCreateParamsPaymentMethodOptionsAfterpayClearpay,
        SessionCreateParamsPaymentMethodOptionsAlipay as SessionCreateParamsPaymentMethodOptionsAlipay,
        SessionCreateParamsPaymentMethodOptionsAlma as SessionCreateParamsPaymentMethodOptionsAlma,
        SessionCreateParamsPaymentMethodOptionsAmazonPay as SessionCreateParamsPaymentMethodOptionsAmazonPay,
        SessionCreateParamsPaymentMethodOptionsAuBecsDebit as SessionCreateParamsPaymentMethodOptionsAuBecsDebit,
        SessionCreateParamsPaymentMethodOptionsBacsDebit as SessionCreateParamsPaymentMethodOptionsBacsDebit,
        SessionCreateParamsPaymentMethodOptionsBacsDebitMandateOptions as SessionCreateParamsPaymentMethodOptionsBacsDebitMandateOptions,
        SessionCreateParamsPaymentMethodOptionsBancontact as SessionCreateParamsPaymentMethodOptionsBancontact,
        SessionCreateParamsPaymentMethodOptionsBillie as SessionCreateParamsPaymentMethodOptionsBillie,
        SessionCreateParamsPaymentMethodOptionsBoleto as SessionCreateParamsPaymentMethodOptionsBoleto,
        SessionCreateParamsPaymentMethodOptionsCard as SessionCreateParamsPaymentMethodOptionsCard,
        SessionCreateParamsPaymentMethodOptionsCardInstallments as SessionCreateParamsPaymentMethodOptionsCardInstallments,
        SessionCreateParamsPaymentMethodOptionsCardRestrictions as SessionCreateParamsPaymentMethodOptionsCardRestrictions,
        SessionCreateParamsPaymentMethodOptionsCashapp as SessionCreateParamsPaymentMethodOptionsCashapp,
        SessionCreateParamsPaymentMethodOptionsCustomerBalance as SessionCreateParamsPaymentMethodOptionsCustomerBalance,
        SessionCreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer as SessionCreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer,
        SessionCreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer as SessionCreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer,
        SessionCreateParamsPaymentMethodOptionsDemoPay as SessionCreateParamsPaymentMethodOptionsDemoPay,
        SessionCreateParamsPaymentMethodOptionsEps as SessionCreateParamsPaymentMethodOptionsEps,
        SessionCreateParamsPaymentMethodOptionsFpx as SessionCreateParamsPaymentMethodOptionsFpx,
        SessionCreateParamsPaymentMethodOptionsGiropay as SessionCreateParamsPaymentMethodOptionsGiropay,
        SessionCreateParamsPaymentMethodOptionsGrabpay as SessionCreateParamsPaymentMethodOptionsGrabpay,
        SessionCreateParamsPaymentMethodOptionsIdeal as SessionCreateParamsPaymentMethodOptionsIdeal,
        SessionCreateParamsPaymentMethodOptionsKakaoPay as SessionCreateParamsPaymentMethodOptionsKakaoPay,
        SessionCreateParamsPaymentMethodOptionsKlarna as SessionCreateParamsPaymentMethodOptionsKlarna,
        SessionCreateParamsPaymentMethodOptionsKlarnaSubscription as SessionCreateParamsPaymentMethodOptionsKlarnaSubscription,
        SessionCreateParamsPaymentMethodOptionsKlarnaSubscriptionNextBilling as SessionCreateParamsPaymentMethodOptionsKlarnaSubscriptionNextBilling,
        SessionCreateParamsPaymentMethodOptionsKonbini as SessionCreateParamsPaymentMethodOptionsKonbini,
        SessionCreateParamsPaymentMethodOptionsKrCard as SessionCreateParamsPaymentMethodOptionsKrCard,
        SessionCreateParamsPaymentMethodOptionsLink as SessionCreateParamsPaymentMethodOptionsLink,
        SessionCreateParamsPaymentMethodOptionsMobilepay as SessionCreateParamsPaymentMethodOptionsMobilepay,
        SessionCreateParamsPaymentMethodOptionsMultibanco as SessionCreateParamsPaymentMethodOptionsMultibanco,
        SessionCreateParamsPaymentMethodOptionsNaverPay as SessionCreateParamsPaymentMethodOptionsNaverPay,
        SessionCreateParamsPaymentMethodOptionsOxxo as SessionCreateParamsPaymentMethodOptionsOxxo,
        SessionCreateParamsPaymentMethodOptionsP24 as SessionCreateParamsPaymentMethodOptionsP24,
        SessionCreateParamsPaymentMethodOptionsPayByBank as SessionCreateParamsPaymentMethodOptionsPayByBank,
        SessionCreateParamsPaymentMethodOptionsPayco as SessionCreateParamsPaymentMethodOptionsPayco,
        SessionCreateParamsPaymentMethodOptionsPaynow as SessionCreateParamsPaymentMethodOptionsPaynow,
        SessionCreateParamsPaymentMethodOptionsPaypal as SessionCreateParamsPaymentMethodOptionsPaypal,
        SessionCreateParamsPaymentMethodOptionsPayto as SessionCreateParamsPaymentMethodOptionsPayto,
        SessionCreateParamsPaymentMethodOptionsPaytoMandateOptions as SessionCreateParamsPaymentMethodOptionsPaytoMandateOptions,
        SessionCreateParamsPaymentMethodOptionsPix as SessionCreateParamsPaymentMethodOptionsPix,
        SessionCreateParamsPaymentMethodOptionsPixMandateOptions as SessionCreateParamsPaymentMethodOptionsPixMandateOptions,
        SessionCreateParamsPaymentMethodOptionsRevolutPay as SessionCreateParamsPaymentMethodOptionsRevolutPay,
        SessionCreateParamsPaymentMethodOptionsSamsungPay as SessionCreateParamsPaymentMethodOptionsSamsungPay,
        SessionCreateParamsPaymentMethodOptionsSatispay as SessionCreateParamsPaymentMethodOptionsSatispay,
        SessionCreateParamsPaymentMethodOptionsSepaDebit as SessionCreateParamsPaymentMethodOptionsSepaDebit,
        SessionCreateParamsPaymentMethodOptionsSepaDebitMandateOptions as SessionCreateParamsPaymentMethodOptionsSepaDebitMandateOptions,
        SessionCreateParamsPaymentMethodOptionsSofort as SessionCreateParamsPaymentMethodOptionsSofort,
        SessionCreateParamsPaymentMethodOptionsSwish as SessionCreateParamsPaymentMethodOptionsSwish,
        SessionCreateParamsPaymentMethodOptionsTwint as SessionCreateParamsPaymentMethodOptionsTwint,
        SessionCreateParamsPaymentMethodOptionsUsBankAccount as SessionCreateParamsPaymentMethodOptionsUsBankAccount,
        SessionCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections as SessionCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections,
        SessionCreateParamsPaymentMethodOptionsWechatPay as SessionCreateParamsPaymentMethodOptionsWechatPay,
        SessionCreateParamsPermissions as SessionCreateParamsPermissions,
        SessionCreateParamsPermissionsUpdate as SessionCreateParamsPermissionsUpdate,
        SessionCreateParamsPhoneNumberCollection as SessionCreateParamsPhoneNumberCollection,
        SessionCreateParamsSavedPaymentMethodOptions as SessionCreateParamsSavedPaymentMethodOptions,
        SessionCreateParamsSetupIntentData as SessionCreateParamsSetupIntentData,
        SessionCreateParamsShippingAddressCollection as SessionCreateParamsShippingAddressCollection,
        SessionCreateParamsShippingOption as SessionCreateParamsShippingOption,
        SessionCreateParamsShippingOptionShippingRateData as SessionCreateParamsShippingOptionShippingRateData,
        SessionCreateParamsShippingOptionShippingRateDataDeliveryEstimate as SessionCreateParamsShippingOptionShippingRateDataDeliveryEstimate,
        SessionCreateParamsShippingOptionShippingRateDataDeliveryEstimateMaximum as SessionCreateParamsShippingOptionShippingRateDataDeliveryEstimateMaximum,
        SessionCreateParamsShippingOptionShippingRateDataDeliveryEstimateMinimum as SessionCreateParamsShippingOptionShippingRateDataDeliveryEstimateMinimum,
        SessionCreateParamsShippingOptionShippingRateDataFixedAmount as SessionCreateParamsShippingOptionShippingRateDataFixedAmount,
        SessionCreateParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions as SessionCreateParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions,
        SessionCreateParamsSubscriptionData as SessionCreateParamsSubscriptionData,
        SessionCreateParamsSubscriptionDataBillingMode as SessionCreateParamsSubscriptionDataBillingMode,
        SessionCreateParamsSubscriptionDataBillingModeFlexible as SessionCreateParamsSubscriptionDataBillingModeFlexible,
        SessionCreateParamsSubscriptionDataInvoiceSettings as SessionCreateParamsSubscriptionDataInvoiceSettings,
        SessionCreateParamsSubscriptionDataInvoiceSettingsIssuer as SessionCreateParamsSubscriptionDataInvoiceSettingsIssuer,
        SessionCreateParamsSubscriptionDataTransferData as SessionCreateParamsSubscriptionDataTransferData,
        SessionCreateParamsSubscriptionDataTrialSettings as SessionCreateParamsSubscriptionDataTrialSettings,
        SessionCreateParamsSubscriptionDataTrialSettingsEndBehavior as SessionCreateParamsSubscriptionDataTrialSettingsEndBehavior,
        SessionCreateParamsTaxIdCollection as SessionCreateParamsTaxIdCollection,
        SessionCreateParamsWalletOptions as SessionCreateParamsWalletOptions,
        SessionCreateParamsWalletOptionsLink as SessionCreateParamsWalletOptionsLink,
    )
    from stripe.params.checkout._session_expire_params import (
        SessionExpireParams as SessionExpireParams,
    )
    from stripe.params.checkout._session_line_item_list_params import (
        SessionLineItemListParams as SessionLineItemListParams,
    )
    from stripe.params.checkout._session_list_line_items_params import (
        SessionListLineItemsParams as SessionListLineItemsParams,
    )
    from stripe.params.checkout._session_list_params import (
        SessionListParams as SessionListParams,
        SessionListParamsCreated as SessionListParamsCreated,
        SessionListParamsCustomerDetails as SessionListParamsCustomerDetails,
    )
    from stripe.params.checkout._session_modify_params import (
        SessionModifyParams as SessionModifyParams,
        SessionModifyParamsAutomaticTax as SessionModifyParamsAutomaticTax,
        SessionModifyParamsAutomaticTaxLiability as SessionModifyParamsAutomaticTaxLiability,
        SessionModifyParamsCollectedInformation as SessionModifyParamsCollectedInformation,
        SessionModifyParamsCollectedInformationShippingDetails as SessionModifyParamsCollectedInformationShippingDetails,
        SessionModifyParamsCollectedInformationShippingDetailsAddress as SessionModifyParamsCollectedInformationShippingDetailsAddress,
        SessionModifyParamsDiscount as SessionModifyParamsDiscount,
        SessionModifyParamsDiscountCouponData as SessionModifyParamsDiscountCouponData,
        SessionModifyParamsInvoiceCreation as SessionModifyParamsInvoiceCreation,
        SessionModifyParamsInvoiceCreationInvoiceData as SessionModifyParamsInvoiceCreationInvoiceData,
        SessionModifyParamsInvoiceCreationInvoiceDataIssuer as SessionModifyParamsInvoiceCreationInvoiceDataIssuer,
        SessionModifyParamsLineItem as SessionModifyParamsLineItem,
        SessionModifyParamsLineItemAdjustableQuantity as SessionModifyParamsLineItemAdjustableQuantity,
        SessionModifyParamsLineItemPriceData as SessionModifyParamsLineItemPriceData,
        SessionModifyParamsLineItemPriceDataProductData as SessionModifyParamsLineItemPriceDataProductData,
        SessionModifyParamsLineItemPriceDataProductDataTaxDetails as SessionModifyParamsLineItemPriceDataProductDataTaxDetails,
        SessionModifyParamsLineItemPriceDataRecurring as SessionModifyParamsLineItemPriceDataRecurring,
        SessionModifyParamsShippingOption as SessionModifyParamsShippingOption,
        SessionModifyParamsShippingOptionShippingRateData as SessionModifyParamsShippingOptionShippingRateData,
        SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimate as SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimate,
        SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimateMaximum as SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimateMaximum,
        SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimateMinimum as SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimateMinimum,
        SessionModifyParamsShippingOptionShippingRateDataFixedAmount as SessionModifyParamsShippingOptionShippingRateDataFixedAmount,
        SessionModifyParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions as SessionModifyParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions,
        SessionModifyParamsSubscriptionData as SessionModifyParamsSubscriptionData,
        SessionModifyParamsSubscriptionDataInvoiceSettings as SessionModifyParamsSubscriptionDataInvoiceSettings,
        SessionModifyParamsSubscriptionDataInvoiceSettingsIssuer as SessionModifyParamsSubscriptionDataInvoiceSettingsIssuer,
    )
    from stripe.params.checkout._session_retrieve_params import (
        SessionRetrieveParams as SessionRetrieveParams,
    )
    from stripe.params.checkout._session_update_params import (
        SessionUpdateParams as SessionUpdateParams,
        SessionUpdateParamsAutomaticTax as SessionUpdateParamsAutomaticTax,
        SessionUpdateParamsAutomaticTaxLiability as SessionUpdateParamsAutomaticTaxLiability,
        SessionUpdateParamsCollectedInformation as SessionUpdateParamsCollectedInformation,
        SessionUpdateParamsCollectedInformationShippingDetails as SessionUpdateParamsCollectedInformationShippingDetails,
        SessionUpdateParamsCollectedInformationShippingDetailsAddress as SessionUpdateParamsCollectedInformationShippingDetailsAddress,
        SessionUpdateParamsDiscount as SessionUpdateParamsDiscount,
        SessionUpdateParamsDiscountCouponData as SessionUpdateParamsDiscountCouponData,
        SessionUpdateParamsInvoiceCreation as SessionUpdateParamsInvoiceCreation,
        SessionUpdateParamsInvoiceCreationInvoiceData as SessionUpdateParamsInvoiceCreationInvoiceData,
        SessionUpdateParamsInvoiceCreationInvoiceDataIssuer as SessionUpdateParamsInvoiceCreationInvoiceDataIssuer,
        SessionUpdateParamsLineItem as SessionUpdateParamsLineItem,
        SessionUpdateParamsLineItemAdjustableQuantity as SessionUpdateParamsLineItemAdjustableQuantity,
        SessionUpdateParamsLineItemPriceData as SessionUpdateParamsLineItemPriceData,
        SessionUpdateParamsLineItemPriceDataProductData as SessionUpdateParamsLineItemPriceDataProductData,
        SessionUpdateParamsLineItemPriceDataProductDataTaxDetails as SessionUpdateParamsLineItemPriceDataProductDataTaxDetails,
        SessionUpdateParamsLineItemPriceDataRecurring as SessionUpdateParamsLineItemPriceDataRecurring,
        SessionUpdateParamsShippingOption as SessionUpdateParamsShippingOption,
        SessionUpdateParamsShippingOptionShippingRateData as SessionUpdateParamsShippingOptionShippingRateData,
        SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimate as SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimate,
        SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimateMaximum as SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimateMaximum,
        SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimateMinimum as SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimateMinimum,
        SessionUpdateParamsShippingOptionShippingRateDataFixedAmount as SessionUpdateParamsShippingOptionShippingRateDataFixedAmount,
        SessionUpdateParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions as SessionUpdateParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions,
        SessionUpdateParamsSubscriptionData as SessionUpdateParamsSubscriptionData,
        SessionUpdateParamsSubscriptionDataInvoiceSettings as SessionUpdateParamsSubscriptionDataInvoiceSettings,
        SessionUpdateParamsSubscriptionDataInvoiceSettingsIssuer as SessionUpdateParamsSubscriptionDataInvoiceSettingsIssuer,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "SessionCreateParams": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsAdaptivePricing": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsAfterExpiration": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsAfterExpirationRecovery": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsAutomaticTax": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsAutomaticTaxLiability": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsBrandingSettings": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsBrandingSettingsIcon": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsBrandingSettingsLogo": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCheckoutItem": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCheckoutItemPricingPlanSubscriptionItem": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCheckoutItemPricingPlanSubscriptionItemComponentConfigurations": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCheckoutItemPricingPlanSubscriptionItemComponentConfigurationsLicenseFeeComponent": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCheckoutItemRateCardSubscriptionItem": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsConsentCollection": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsConsentCollectionPaymentMethodReuseAgreement": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCustomField": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCustomFieldDropdown": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCustomFieldDropdownOption": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCustomFieldLabel": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCustomFieldNumeric": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCustomFieldText": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCustomText": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCustomTextAfterSubmit": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCustomTextShippingAddress": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCustomTextSubmit": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCustomTextTermsOfServiceAcceptance": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsCustomerUpdate": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsDiscount": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsDiscountCouponData": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsInvoiceCreation": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsInvoiceCreationInvoiceData": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsInvoiceCreationInvoiceDataCustomField": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsInvoiceCreationInvoiceDataIssuer": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsInvoiceCreationInvoiceDataRenderingOptions": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsLineItem": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsLineItemAdjustableQuantity": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsLineItemPriceData": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsLineItemPriceDataProductData": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsLineItemPriceDataProductDataTaxDetails": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsLineItemPriceDataRecurring": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsNameCollection": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsNameCollectionBusiness": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsNameCollectionIndividual": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsOptionalItem": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsOptionalItemAdjustableQuantity": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentIntentData": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentIntentDataShipping": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentIntentDataShippingAddress": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentIntentDataTransferData": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodData": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptions": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsAcssDebit": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsAcssDebitMandateOptions": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsAffirm": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsAfterpayClearpay": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsAlipay": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsAlma": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsAmazonPay": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsAuBecsDebit": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsBacsDebit": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsBacsDebitMandateOptions": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsBancontact": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsBillie": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsBoleto": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsCard": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsCardInstallments": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsCardRestrictions": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsCashapp": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsCustomerBalance": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsDemoPay": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsEps": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsFpx": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsGiropay": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsGrabpay": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsIdeal": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsKakaoPay": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsKlarna": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsKlarnaSubscription": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsKlarnaSubscriptionNextBilling": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsKonbini": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsKrCard": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsLink": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsMobilepay": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsMultibanco": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsNaverPay": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsOxxo": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsP24": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsPayByBank": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsPayco": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsPaynow": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsPaypal": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsPayto": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsPaytoMandateOptions": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsPix": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsPixMandateOptions": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsRevolutPay": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsSamsungPay": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsSatispay": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsSepaDebit": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsSepaDebitMandateOptions": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsSofort": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsSwish": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsTwint": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsUsBankAccount": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPaymentMethodOptionsWechatPay": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPermissions": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPermissionsUpdate": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsPhoneNumberCollection": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsSavedPaymentMethodOptions": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsSetupIntentData": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsShippingAddressCollection": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsShippingOption": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsShippingOptionShippingRateData": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsShippingOptionShippingRateDataDeliveryEstimate": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsShippingOptionShippingRateDataDeliveryEstimateMaximum": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsShippingOptionShippingRateDataDeliveryEstimateMinimum": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsShippingOptionShippingRateDataFixedAmount": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsSubscriptionData": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsSubscriptionDataBillingMode": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsSubscriptionDataBillingModeFlexible": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsSubscriptionDataInvoiceSettings": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsSubscriptionDataInvoiceSettingsIssuer": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsSubscriptionDataTransferData": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsSubscriptionDataTrialSettings": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsSubscriptionDataTrialSettingsEndBehavior": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsTaxIdCollection": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsWalletOptions": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionCreateParamsWalletOptionsLink": (
        "stripe.params.checkout._session_create_params",
        False,
    ),
    "SessionExpireParams": (
        "stripe.params.checkout._session_expire_params",
        False,
    ),
    "SessionLineItemListParams": (
        "stripe.params.checkout._session_line_item_list_params",
        False,
    ),
    "SessionListLineItemsParams": (
        "stripe.params.checkout._session_list_line_items_params",
        False,
    ),
    "SessionListParams": (
        "stripe.params.checkout._session_list_params",
        False,
    ),
    "SessionListParamsCreated": (
        "stripe.params.checkout._session_list_params",
        False,
    ),
    "SessionListParamsCustomerDetails": (
        "stripe.params.checkout._session_list_params",
        False,
    ),
    "SessionModifyParams": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsAutomaticTax": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsAutomaticTaxLiability": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsCollectedInformation": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsCollectedInformationShippingDetails": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsCollectedInformationShippingDetailsAddress": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsDiscount": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsDiscountCouponData": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsInvoiceCreation": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsInvoiceCreationInvoiceData": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsInvoiceCreationInvoiceDataIssuer": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsLineItem": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsLineItemAdjustableQuantity": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsLineItemPriceData": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsLineItemPriceDataProductData": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsLineItemPriceDataProductDataTaxDetails": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsLineItemPriceDataRecurring": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsShippingOption": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsShippingOptionShippingRateData": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimate": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimateMaximum": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsShippingOptionShippingRateDataDeliveryEstimateMinimum": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsShippingOptionShippingRateDataFixedAmount": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsSubscriptionData": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsSubscriptionDataInvoiceSettings": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionModifyParamsSubscriptionDataInvoiceSettingsIssuer": (
        "stripe.params.checkout._session_modify_params",
        False,
    ),
    "SessionRetrieveParams": (
        "stripe.params.checkout._session_retrieve_params",
        False,
    ),
    "SessionUpdateParams": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsAutomaticTax": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsAutomaticTaxLiability": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsCollectedInformation": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsCollectedInformationShippingDetails": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsCollectedInformationShippingDetailsAddress": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsDiscount": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsDiscountCouponData": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsInvoiceCreation": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsInvoiceCreationInvoiceData": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsInvoiceCreationInvoiceDataIssuer": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsLineItem": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsLineItemAdjustableQuantity": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsLineItemPriceData": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsLineItemPriceDataProductData": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsLineItemPriceDataProductDataTaxDetails": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsLineItemPriceDataRecurring": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsShippingOption": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsShippingOptionShippingRateData": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimate": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimateMaximum": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsShippingOptionShippingRateDataDeliveryEstimateMinimum": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsShippingOptionShippingRateDataFixedAmount": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsSubscriptionData": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsSubscriptionDataInvoiceSettings": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
    "SessionUpdateParamsSubscriptionDataInvoiceSettingsIssuer": (
        "stripe.params.checkout._session_update_params",
        False,
    ),
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            target, is_submodule = _import_map[name]
            module = import_module(target)
            if is_submodule:
                return module

            return getattr(
                module,
                name,
            )
        except KeyError:
            raise AttributeError()
