# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.terminal._configuration_create_params import (
        ConfigurationCreateParams as ConfigurationCreateParams,
        ConfigurationCreateParamsBbposWisepad3 as ConfigurationCreateParamsBbposWisepad3,
        ConfigurationCreateParamsBbposWiseposE as ConfigurationCreateParamsBbposWiseposE,
        ConfigurationCreateParamsOffline as ConfigurationCreateParamsOffline,
        ConfigurationCreateParamsRebootWindow as ConfigurationCreateParamsRebootWindow,
        ConfigurationCreateParamsStripeS700 as ConfigurationCreateParamsStripeS700,
        ConfigurationCreateParamsTipping as ConfigurationCreateParamsTipping,
        ConfigurationCreateParamsTippingAed as ConfigurationCreateParamsTippingAed,
        ConfigurationCreateParamsTippingAud as ConfigurationCreateParamsTippingAud,
        ConfigurationCreateParamsTippingBgn as ConfigurationCreateParamsTippingBgn,
        ConfigurationCreateParamsTippingCad as ConfigurationCreateParamsTippingCad,
        ConfigurationCreateParamsTippingChf as ConfigurationCreateParamsTippingChf,
        ConfigurationCreateParamsTippingCzk as ConfigurationCreateParamsTippingCzk,
        ConfigurationCreateParamsTippingDkk as ConfigurationCreateParamsTippingDkk,
        ConfigurationCreateParamsTippingEur as ConfigurationCreateParamsTippingEur,
        ConfigurationCreateParamsTippingGbp as ConfigurationCreateParamsTippingGbp,
        ConfigurationCreateParamsTippingHkd as ConfigurationCreateParamsTippingHkd,
        ConfigurationCreateParamsTippingHuf as ConfigurationCreateParamsTippingHuf,
        ConfigurationCreateParamsTippingJpy as ConfigurationCreateParamsTippingJpy,
        ConfigurationCreateParamsTippingMxn as ConfigurationCreateParamsTippingMxn,
        ConfigurationCreateParamsTippingMyr as ConfigurationCreateParamsTippingMyr,
        ConfigurationCreateParamsTippingNok as ConfigurationCreateParamsTippingNok,
        ConfigurationCreateParamsTippingNzd as ConfigurationCreateParamsTippingNzd,
        ConfigurationCreateParamsTippingPln as ConfigurationCreateParamsTippingPln,
        ConfigurationCreateParamsTippingRon as ConfigurationCreateParamsTippingRon,
        ConfigurationCreateParamsTippingSek as ConfigurationCreateParamsTippingSek,
        ConfigurationCreateParamsTippingSgd as ConfigurationCreateParamsTippingSgd,
        ConfigurationCreateParamsTippingUsd as ConfigurationCreateParamsTippingUsd,
        ConfigurationCreateParamsVerifoneP400 as ConfigurationCreateParamsVerifoneP400,
        ConfigurationCreateParamsWifi as ConfigurationCreateParamsWifi,
        ConfigurationCreateParamsWifiEnterpriseEapPeap as ConfigurationCreateParamsWifiEnterpriseEapPeap,
        ConfigurationCreateParamsWifiEnterpriseEapTls as ConfigurationCreateParamsWifiEnterpriseEapTls,
        ConfigurationCreateParamsWifiPersonalPsk as ConfigurationCreateParamsWifiPersonalPsk,
    )
    from stripe.params.terminal._configuration_delete_params import (
        ConfigurationDeleteParams as ConfigurationDeleteParams,
    )
    from stripe.params.terminal._configuration_list_params import (
        ConfigurationListParams as ConfigurationListParams,
    )
    from stripe.params.terminal._configuration_modify_params import (
        ConfigurationModifyParams as ConfigurationModifyParams,
        ConfigurationModifyParamsBbposWisepad3 as ConfigurationModifyParamsBbposWisepad3,
        ConfigurationModifyParamsBbposWiseposE as ConfigurationModifyParamsBbposWiseposE,
        ConfigurationModifyParamsOffline as ConfigurationModifyParamsOffline,
        ConfigurationModifyParamsRebootWindow as ConfigurationModifyParamsRebootWindow,
        ConfigurationModifyParamsStripeS700 as ConfigurationModifyParamsStripeS700,
        ConfigurationModifyParamsTipping as ConfigurationModifyParamsTipping,
        ConfigurationModifyParamsTippingAed as ConfigurationModifyParamsTippingAed,
        ConfigurationModifyParamsTippingAud as ConfigurationModifyParamsTippingAud,
        ConfigurationModifyParamsTippingBgn as ConfigurationModifyParamsTippingBgn,
        ConfigurationModifyParamsTippingCad as ConfigurationModifyParamsTippingCad,
        ConfigurationModifyParamsTippingChf as ConfigurationModifyParamsTippingChf,
        ConfigurationModifyParamsTippingCzk as ConfigurationModifyParamsTippingCzk,
        ConfigurationModifyParamsTippingDkk as ConfigurationModifyParamsTippingDkk,
        ConfigurationModifyParamsTippingEur as ConfigurationModifyParamsTippingEur,
        ConfigurationModifyParamsTippingGbp as ConfigurationModifyParamsTippingGbp,
        ConfigurationModifyParamsTippingHkd as ConfigurationModifyParamsTippingHkd,
        ConfigurationModifyParamsTippingHuf as ConfigurationModifyParamsTippingHuf,
        ConfigurationModifyParamsTippingJpy as ConfigurationModifyParamsTippingJpy,
        ConfigurationModifyParamsTippingMxn as ConfigurationModifyParamsTippingMxn,
        ConfigurationModifyParamsTippingMyr as ConfigurationModifyParamsTippingMyr,
        ConfigurationModifyParamsTippingNok as ConfigurationModifyParamsTippingNok,
        ConfigurationModifyParamsTippingNzd as ConfigurationModifyParamsTippingNzd,
        ConfigurationModifyParamsTippingPln as ConfigurationModifyParamsTippingPln,
        ConfigurationModifyParamsTippingRon as ConfigurationModifyParamsTippingRon,
        ConfigurationModifyParamsTippingSek as ConfigurationModifyParamsTippingSek,
        ConfigurationModifyParamsTippingSgd as ConfigurationModifyParamsTippingSgd,
        ConfigurationModifyParamsTippingUsd as ConfigurationModifyParamsTippingUsd,
        ConfigurationModifyParamsVerifoneP400 as ConfigurationModifyParamsVerifoneP400,
        ConfigurationModifyParamsWifi as ConfigurationModifyParamsWifi,
        ConfigurationModifyParamsWifiEnterpriseEapPeap as ConfigurationModifyParamsWifiEnterpriseEapPeap,
        ConfigurationModifyParamsWifiEnterpriseEapTls as ConfigurationModifyParamsWifiEnterpriseEapTls,
        ConfigurationModifyParamsWifiPersonalPsk as ConfigurationModifyParamsWifiPersonalPsk,
    )
    from stripe.params.terminal._configuration_retrieve_params import (
        ConfigurationRetrieveParams as ConfigurationRetrieveParams,
    )
    from stripe.params.terminal._configuration_update_params import (
        ConfigurationUpdateParams as ConfigurationUpdateParams,
        ConfigurationUpdateParamsBbposWisepad3 as ConfigurationUpdateParamsBbposWisepad3,
        ConfigurationUpdateParamsBbposWiseposE as ConfigurationUpdateParamsBbposWiseposE,
        ConfigurationUpdateParamsOffline as ConfigurationUpdateParamsOffline,
        ConfigurationUpdateParamsRebootWindow as ConfigurationUpdateParamsRebootWindow,
        ConfigurationUpdateParamsStripeS700 as ConfigurationUpdateParamsStripeS700,
        ConfigurationUpdateParamsTipping as ConfigurationUpdateParamsTipping,
        ConfigurationUpdateParamsTippingAed as ConfigurationUpdateParamsTippingAed,
        ConfigurationUpdateParamsTippingAud as ConfigurationUpdateParamsTippingAud,
        ConfigurationUpdateParamsTippingBgn as ConfigurationUpdateParamsTippingBgn,
        ConfigurationUpdateParamsTippingCad as ConfigurationUpdateParamsTippingCad,
        ConfigurationUpdateParamsTippingChf as ConfigurationUpdateParamsTippingChf,
        ConfigurationUpdateParamsTippingCzk as ConfigurationUpdateParamsTippingCzk,
        ConfigurationUpdateParamsTippingDkk as ConfigurationUpdateParamsTippingDkk,
        ConfigurationUpdateParamsTippingEur as ConfigurationUpdateParamsTippingEur,
        ConfigurationUpdateParamsTippingGbp as ConfigurationUpdateParamsTippingGbp,
        ConfigurationUpdateParamsTippingHkd as ConfigurationUpdateParamsTippingHkd,
        ConfigurationUpdateParamsTippingHuf as ConfigurationUpdateParamsTippingHuf,
        ConfigurationUpdateParamsTippingJpy as ConfigurationUpdateParamsTippingJpy,
        ConfigurationUpdateParamsTippingMxn as ConfigurationUpdateParamsTippingMxn,
        ConfigurationUpdateParamsTippingMyr as ConfigurationUpdateParamsTippingMyr,
        ConfigurationUpdateParamsTippingNok as ConfigurationUpdateParamsTippingNok,
        ConfigurationUpdateParamsTippingNzd as ConfigurationUpdateParamsTippingNzd,
        ConfigurationUpdateParamsTippingPln as ConfigurationUpdateParamsTippingPln,
        ConfigurationUpdateParamsTippingRon as ConfigurationUpdateParamsTippingRon,
        ConfigurationUpdateParamsTippingSek as ConfigurationUpdateParamsTippingSek,
        ConfigurationUpdateParamsTippingSgd as ConfigurationUpdateParamsTippingSgd,
        ConfigurationUpdateParamsTippingUsd as ConfigurationUpdateParamsTippingUsd,
        ConfigurationUpdateParamsVerifoneP400 as ConfigurationUpdateParamsVerifoneP400,
        ConfigurationUpdateParamsWifi as ConfigurationUpdateParamsWifi,
        ConfigurationUpdateParamsWifiEnterpriseEapPeap as ConfigurationUpdateParamsWifiEnterpriseEapPeap,
        ConfigurationUpdateParamsWifiEnterpriseEapTls as ConfigurationUpdateParamsWifiEnterpriseEapTls,
        ConfigurationUpdateParamsWifiPersonalPsk as ConfigurationUpdateParamsWifiPersonalPsk,
    )
    from stripe.params.terminal._connection_token_create_params import (
        ConnectionTokenCreateParams as ConnectionTokenCreateParams,
    )
    from stripe.params.terminal._location_create_params import (
        LocationCreateParams as LocationCreateParams,
        LocationCreateParamsAddress as LocationCreateParamsAddress,
        LocationCreateParamsAddressKana as LocationCreateParamsAddressKana,
        LocationCreateParamsAddressKanji as LocationCreateParamsAddressKanji,
    )
    from stripe.params.terminal._location_delete_params import (
        LocationDeleteParams as LocationDeleteParams,
    )
    from stripe.params.terminal._location_list_params import (
        LocationListParams as LocationListParams,
    )
    from stripe.params.terminal._location_modify_params import (
        LocationModifyParams as LocationModifyParams,
        LocationModifyParamsAddress as LocationModifyParamsAddress,
        LocationModifyParamsAddressKana as LocationModifyParamsAddressKana,
        LocationModifyParamsAddressKanji as LocationModifyParamsAddressKanji,
    )
    from stripe.params.terminal._location_retrieve_params import (
        LocationRetrieveParams as LocationRetrieveParams,
    )
    from stripe.params.terminal._location_update_params import (
        LocationUpdateParams as LocationUpdateParams,
        LocationUpdateParamsAddress as LocationUpdateParamsAddress,
        LocationUpdateParamsAddressKana as LocationUpdateParamsAddressKana,
        LocationUpdateParamsAddressKanji as LocationUpdateParamsAddressKanji,
    )
    from stripe.params.terminal._reader_cancel_action_params import (
        ReaderCancelActionParams as ReaderCancelActionParams,
    )
    from stripe.params.terminal._reader_collect_inputs_params import (
        ReaderCollectInputsParams as ReaderCollectInputsParams,
        ReaderCollectInputsParamsInput as ReaderCollectInputsParamsInput,
        ReaderCollectInputsParamsInputCustomText as ReaderCollectInputsParamsInputCustomText,
        ReaderCollectInputsParamsInputSelection as ReaderCollectInputsParamsInputSelection,
        ReaderCollectInputsParamsInputSelectionChoice as ReaderCollectInputsParamsInputSelectionChoice,
        ReaderCollectInputsParamsInputToggle as ReaderCollectInputsParamsInputToggle,
    )
    from stripe.params.terminal._reader_collect_payment_method_params import (
        ReaderCollectPaymentMethodParams as ReaderCollectPaymentMethodParams,
        ReaderCollectPaymentMethodParamsCollectConfig as ReaderCollectPaymentMethodParamsCollectConfig,
        ReaderCollectPaymentMethodParamsCollectConfigTipping as ReaderCollectPaymentMethodParamsCollectConfigTipping,
    )
    from stripe.params.terminal._reader_confirm_payment_intent_params import (
        ReaderConfirmPaymentIntentParams as ReaderConfirmPaymentIntentParams,
        ReaderConfirmPaymentIntentParamsConfirmConfig as ReaderConfirmPaymentIntentParamsConfirmConfig,
    )
    from stripe.params.terminal._reader_create_params import (
        ReaderCreateParams as ReaderCreateParams,
    )
    from stripe.params.terminal._reader_delete_params import (
        ReaderDeleteParams as ReaderDeleteParams,
    )
    from stripe.params.terminal._reader_list_params import (
        ReaderListParams as ReaderListParams,
    )
    from stripe.params.terminal._reader_modify_params import (
        ReaderModifyParams as ReaderModifyParams,
    )
    from stripe.params.terminal._reader_present_payment_method_params import (
        ReaderPresentPaymentMethodParams as ReaderPresentPaymentMethodParams,
        ReaderPresentPaymentMethodParamsCard as ReaderPresentPaymentMethodParamsCard,
        ReaderPresentPaymentMethodParamsCardPresent as ReaderPresentPaymentMethodParamsCardPresent,
        ReaderPresentPaymentMethodParamsInteracPresent as ReaderPresentPaymentMethodParamsInteracPresent,
    )
    from stripe.params.terminal._reader_process_payment_intent_params import (
        ReaderProcessPaymentIntentParams as ReaderProcessPaymentIntentParams,
        ReaderProcessPaymentIntentParamsProcessConfig as ReaderProcessPaymentIntentParamsProcessConfig,
        ReaderProcessPaymentIntentParamsProcessConfigTipping as ReaderProcessPaymentIntentParamsProcessConfigTipping,
    )
    from stripe.params.terminal._reader_process_setup_intent_params import (
        ReaderProcessSetupIntentParams as ReaderProcessSetupIntentParams,
        ReaderProcessSetupIntentParamsProcessConfig as ReaderProcessSetupIntentParamsProcessConfig,
    )
    from stripe.params.terminal._reader_refund_payment_params import (
        ReaderRefundPaymentParams as ReaderRefundPaymentParams,
        ReaderRefundPaymentParamsRefundPaymentConfig as ReaderRefundPaymentParamsRefundPaymentConfig,
    )
    from stripe.params.terminal._reader_retrieve_params import (
        ReaderRetrieveParams as ReaderRetrieveParams,
    )
    from stripe.params.terminal._reader_set_reader_display_params import (
        ReaderSetReaderDisplayParams as ReaderSetReaderDisplayParams,
        ReaderSetReaderDisplayParamsCart as ReaderSetReaderDisplayParamsCart,
        ReaderSetReaderDisplayParamsCartLineItem as ReaderSetReaderDisplayParamsCartLineItem,
    )
    from stripe.params.terminal._reader_succeed_input_collection_params import (
        ReaderSucceedInputCollectionParams as ReaderSucceedInputCollectionParams,
    )
    from stripe.params.terminal._reader_timeout_input_collection_params import (
        ReaderTimeoutInputCollectionParams as ReaderTimeoutInputCollectionParams,
    )
    from stripe.params.terminal._reader_update_params import (
        ReaderUpdateParams as ReaderUpdateParams,
    )

_submodules = {
    "ConfigurationCreateParams": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsBbposWisepad3": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsBbposWiseposE": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsOffline": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsRebootWindow": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsStripeS700": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTipping": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingAed": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingAud": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingBgn": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingCad": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingChf": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingCzk": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingDkk": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingEur": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingGbp": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingHkd": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingHuf": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingJpy": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingMxn": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingMyr": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingNok": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingNzd": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingPln": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingRon": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingSek": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingSgd": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsTippingUsd": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsVerifoneP400": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsWifi": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsWifiEnterpriseEapPeap": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsWifiEnterpriseEapTls": "stripe.params.terminal._configuration_create_params",
    "ConfigurationCreateParamsWifiPersonalPsk": "stripe.params.terminal._configuration_create_params",
    "ConfigurationDeleteParams": "stripe.params.terminal._configuration_delete_params",
    "ConfigurationListParams": "stripe.params.terminal._configuration_list_params",
    "ConfigurationModifyParams": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsBbposWisepad3": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsBbposWiseposE": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsOffline": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsRebootWindow": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsStripeS700": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTipping": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingAed": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingAud": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingBgn": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingCad": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingChf": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingCzk": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingDkk": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingEur": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingGbp": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingHkd": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingHuf": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingJpy": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingMxn": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingMyr": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingNok": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingNzd": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingPln": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingRon": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingSek": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingSgd": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsTippingUsd": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsVerifoneP400": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsWifi": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsWifiEnterpriseEapPeap": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsWifiEnterpriseEapTls": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationModifyParamsWifiPersonalPsk": "stripe.params.terminal._configuration_modify_params",
    "ConfigurationRetrieveParams": "stripe.params.terminal._configuration_retrieve_params",
    "ConfigurationUpdateParams": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsBbposWisepad3": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsBbposWiseposE": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsOffline": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsRebootWindow": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsStripeS700": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTipping": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingAed": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingAud": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingBgn": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingCad": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingChf": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingCzk": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingDkk": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingEur": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingGbp": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingHkd": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingHuf": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingJpy": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingMxn": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingMyr": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingNok": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingNzd": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingPln": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingRon": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingSek": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingSgd": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsTippingUsd": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsVerifoneP400": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsWifi": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsWifiEnterpriseEapPeap": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsWifiEnterpriseEapTls": "stripe.params.terminal._configuration_update_params",
    "ConfigurationUpdateParamsWifiPersonalPsk": "stripe.params.terminal._configuration_update_params",
    "ConnectionTokenCreateParams": "stripe.params.terminal._connection_token_create_params",
    "LocationCreateParams": "stripe.params.terminal._location_create_params",
    "LocationCreateParamsAddress": "stripe.params.terminal._location_create_params",
    "LocationCreateParamsAddressKana": "stripe.params.terminal._location_create_params",
    "LocationCreateParamsAddressKanji": "stripe.params.terminal._location_create_params",
    "LocationDeleteParams": "stripe.params.terminal._location_delete_params",
    "LocationListParams": "stripe.params.terminal._location_list_params",
    "LocationModifyParams": "stripe.params.terminal._location_modify_params",
    "LocationModifyParamsAddress": "stripe.params.terminal._location_modify_params",
    "LocationModifyParamsAddressKana": "stripe.params.terminal._location_modify_params",
    "LocationModifyParamsAddressKanji": "stripe.params.terminal._location_modify_params",
    "LocationRetrieveParams": "stripe.params.terminal._location_retrieve_params",
    "LocationUpdateParams": "stripe.params.terminal._location_update_params",
    "LocationUpdateParamsAddress": "stripe.params.terminal._location_update_params",
    "LocationUpdateParamsAddressKana": "stripe.params.terminal._location_update_params",
    "LocationUpdateParamsAddressKanji": "stripe.params.terminal._location_update_params",
    "ReaderCancelActionParams": "stripe.params.terminal._reader_cancel_action_params",
    "ReaderCollectInputsParams": "stripe.params.terminal._reader_collect_inputs_params",
    "ReaderCollectInputsParamsInput": "stripe.params.terminal._reader_collect_inputs_params",
    "ReaderCollectInputsParamsInputCustomText": "stripe.params.terminal._reader_collect_inputs_params",
    "ReaderCollectInputsParamsInputSelection": "stripe.params.terminal._reader_collect_inputs_params",
    "ReaderCollectInputsParamsInputSelectionChoice": "stripe.params.terminal._reader_collect_inputs_params",
    "ReaderCollectInputsParamsInputToggle": "stripe.params.terminal._reader_collect_inputs_params",
    "ReaderCollectPaymentMethodParams": "stripe.params.terminal._reader_collect_payment_method_params",
    "ReaderCollectPaymentMethodParamsCollectConfig": "stripe.params.terminal._reader_collect_payment_method_params",
    "ReaderCollectPaymentMethodParamsCollectConfigTipping": "stripe.params.terminal._reader_collect_payment_method_params",
    "ReaderConfirmPaymentIntentParams": "stripe.params.terminal._reader_confirm_payment_intent_params",
    "ReaderConfirmPaymentIntentParamsConfirmConfig": "stripe.params.terminal._reader_confirm_payment_intent_params",
    "ReaderCreateParams": "stripe.params.terminal._reader_create_params",
    "ReaderDeleteParams": "stripe.params.terminal._reader_delete_params",
    "ReaderListParams": "stripe.params.terminal._reader_list_params",
    "ReaderModifyParams": "stripe.params.terminal._reader_modify_params",
    "ReaderPresentPaymentMethodParams": "stripe.params.terminal._reader_present_payment_method_params",
    "ReaderPresentPaymentMethodParamsCard": "stripe.params.terminal._reader_present_payment_method_params",
    "ReaderPresentPaymentMethodParamsCardPresent": "stripe.params.terminal._reader_present_payment_method_params",
    "ReaderPresentPaymentMethodParamsInteracPresent": "stripe.params.terminal._reader_present_payment_method_params",
    "ReaderProcessPaymentIntentParams": "stripe.params.terminal._reader_process_payment_intent_params",
    "ReaderProcessPaymentIntentParamsProcessConfig": "stripe.params.terminal._reader_process_payment_intent_params",
    "ReaderProcessPaymentIntentParamsProcessConfigTipping": "stripe.params.terminal._reader_process_payment_intent_params",
    "ReaderProcessSetupIntentParams": "stripe.params.terminal._reader_process_setup_intent_params",
    "ReaderProcessSetupIntentParamsProcessConfig": "stripe.params.terminal._reader_process_setup_intent_params",
    "ReaderRefundPaymentParams": "stripe.params.terminal._reader_refund_payment_params",
    "ReaderRefundPaymentParamsRefundPaymentConfig": "stripe.params.terminal._reader_refund_payment_params",
    "ReaderRetrieveParams": "stripe.params.terminal._reader_retrieve_params",
    "ReaderSetReaderDisplayParams": "stripe.params.terminal._reader_set_reader_display_params",
    "ReaderSetReaderDisplayParamsCart": "stripe.params.terminal._reader_set_reader_display_params",
    "ReaderSetReaderDisplayParamsCartLineItem": "stripe.params.terminal._reader_set_reader_display_params",
    "ReaderSucceedInputCollectionParams": "stripe.params.terminal._reader_succeed_input_collection_params",
    "ReaderTimeoutInputCollectionParams": "stripe.params.terminal._reader_timeout_input_collection_params",
    "ReaderUpdateParams": "stripe.params.terminal._reader_update_params",
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            return getattr(
                import_module(_submodules[name]),
                name,
            )
        except KeyError:
            raise AttributeError(f"cannot import '{name}' from '{__name__}'")
