# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Optional, Union, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._payment_method import PaymentMethod
    from stripe.params.three_d_secure._authentication_cancel_params import (
        AuthenticationCancelParams,
    )
    from stripe.params.three_d_secure._authentication_create_params import (
        AuthenticationCreateParams,
    )
    from stripe.params.three_d_secure._authentication_list_params import (
        AuthenticationListParams,
    )
    from stripe.params.three_d_secure._authentication_retrieve_params import (
        AuthenticationRetrieveParams,
    )
    from stripe.params.three_d_secure._authentication_submit_params import (
        AuthenticationSubmitParams,
    )


class Authentication(
    CreateableAPIResource["Authentication"],
    ListableAPIResource["Authentication"],
):
    """
    The Standalone 3DS API allows you to run EMV 3D Secure (3DS) authentication using Stripe while authorizing the payment with any PSP.

    Related guide: [Standalone 3DS](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure)
    """

    OBJECT_NAME: ClassVar[Literal["three_d_secure.authentication"]] = (
        "three_d_secure.authentication"
    )

    class AcquirerDetails(StripeObject):
        acquirer_bin: Optional[str]
        """
        The Acquirer BIN (specific to the directory_server).
        """
        acquirer_country: Optional[str]
        """
        The two-letter country code of the acquirer ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        acquirer_merchant_id: Optional[str]
        """
        The Merchant ID (or Card Acceptor ID) that your acquirer assigned you (specific to the directory_server).
        """
        mcc: Optional[str]
        """
        The [merchant category code](https://en.wikipedia.org/wiki/Merchant_category_code) as defined by each payment system or directory server.
        """
        merchant_name: Optional[str]
        """
        The merchant name assigned by the acquirer or payment system. Same name used in the authorization message as defined in [ISO 8583](https://en.wikipedia.org/wiki/ISO_8583).
        """
        requestor_id: Optional[str]
        """
        Requestor ID if you're enrolled in the card network's 3DS program. Otherwise, you can omit this field because Stripe assigns a Requestor ID with the card networks.
        """

    class Channel(StripeObject):
        class Browser(StripeObject):
            accept_header: str
            """
            The HTTP accept headers from the cardholder's browser.
            """
            color_depth: Optional[int]
            """
            The color depth of the cardholder's screen.
            """
            ip_address: str
            """
            The IP address of the browser.
            """
            java_enabled: Optional[bool]
            """
            The cardholder browser's ability to execute Java.
            """
            javascript_enabled: bool
            """
            The cardholder browser's ability to execute JavaScript.
            """
            language: str
            """
            An IETF BCP 47 language tag representing the browser language.
            """
            screen_height: Optional[int]
            """
            The total height of the cardholder's screen in pixels.
            """
            screen_width: Optional[int]
            """
            The total width of the cardholder's screen in pixels.
            """
            timezone_offset: Optional[int]
            """
            The time difference between UTC time and the local time of the cardholder's browser, in minutes.
            """
            user_agent: str
            """
            The browser user agent.
            """

        class ThreeRI(StripeObject):
            previous_authentication: str
            """
            ID of the previous initial authenticated 3DS Authentication object.
            """
            type: Union[
                Literal[
                    "delayed_shipment",
                    "other_payment",
                    "recurring",
                    "split_shipment",
                ],
                str,
            ]
            """
            Type of the 3RI Authentication.
            """

        browser: Optional[Browser]
        """
        Contains details on the browser for a standalone 3DS Authentication.
        """
        three_r_i: Optional[ThreeRI]
        """
        Contains details for a 3RI standalone 3DS Authentication.
        """
        type: Union[Literal["browser", "three_r_i"], str]
        """
        Type of channel you would prefer to use for this 3DS Authentication. Only browser.
        """
        _inner_class_types = {"browser": Browser, "three_r_i": ThreeRI}

    class FlowPreference(StripeObject):
        class Challenge(StripeObject):
            type: Union[Literal["mandated", "preferred"], str]
            """
            Type of challenge flow you requested for this 3DS Authentication.
            """

        class DataShare(StripeObject):
            type: Union[Literal["ds_specific", "emv_standard"], str]
            """
            Type of data share flow you requested for this 3DS Authentication.
            """

        class Frictionless(StripeObject):
            type: Union[Literal["low_risk", "none"], str]
            """
            Type of frictionless flow you requested for this 3DS Authentication.
            """

        challenge: Optional[Challenge]
        data_share: Optional[DataShare]
        frictionless: Optional[Frictionless]
        type: Union[Literal["challenge", "data_share", "frictionless"], str]
        """
        Type of flow you requested for this 3DS Authentication.
        """
        _inner_class_types = {
            "challenge": Challenge,
            "data_share": DataShare,
            "frictionless": Frictionless,
        }

    class FutureUsage(StripeObject):
        class Installment(StripeObject):
            class Expiry(StripeObject):
                date: Optional[str]
                type: Union[Literal["date", "never"], str]

            amount: Optional[int]
            """
            A non-negative integer representing the amount in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
            """
            expiry: Expiry
            """
            Information about recurring payment expiry
            """
            interval: Literal["day"]
            """
            The unit of time for `interval_count`.
            """
            interval_count: int
            """
            The minimum number of time intervals between authorizations.
            """
            number: int
            """
            The maximum number of installments.
            """
            _inner_class_types = {"expiry": Expiry}

        class Recurring(StripeObject):
            class Expiry(StripeObject):
                date: Optional[str]
                type: Union[Literal["date", "never"], str]

            amount: Optional[int]
            """
            A non-negative integer representing the amount in the [smallest currency unit](https://docs.stripe.com/currencies#zero-decimal).
            """
            expiry: Expiry
            """
            Information about recurring payment expiry
            """
            interval: Literal["day"]
            """
            The unit of time for `interval_count`.
            """
            interval_count: int
            """
            The minimum number of time intervals between authorizations.
            """
            _inner_class_types = {"expiry": Expiry}

        installment: Optional[Installment]
        """
        Details about installment payments
        """
        recurring: Optional[Recurring]
        """
        Details about recurring payments
        """
        type: Union[Literal["card_on_file", "installment", "recurring"], str]
        """
        The type of future usage declared for this 3DS Authentication.
        """
        _inner_class_types = {
            "installment": Installment,
            "recurring": Recurring,
        }

    class OutcomeDetails(StripeObject):
        class NetworkDetails(StripeObject):
            class CartesBancaires(StripeObject):
                avalgo: str
                """
                The cryptogram calculation algorithm used by the card Issuer's ACS to calculate the Authentication cryptogram. Also known as cavvAlgorithm. ARes/RReq messageExtension: `CB-AVALGO`
                """
                cb_exemption: Optional[str]
                """
                The exemption indicator returned from Cartes Bancaires in the ARes. This is a 3 byte bitmap (lowest significant byte first and most significant bit first) that has been Base64 encoded. String (4 characters). ARes message extension: `CB-EXEMPTION`
                """
                cb_score: Optional[str]
                """
                The risk score returned from Cartes Bancaires in the ARes. Numeric value 0-99. ARes/RReq message extension: `CB-SCORE`
                """

            cartes_bancaires: Optional[CartesBancaires]
            """
            Contains details for Cartes Bancaires specific fields in the authentication outcomes.
            """
            _inner_class_types = {"cartes_bancaires": CartesBancaires}

        acs_transaction_id: Optional[str]
        """
        Universally unique transaction identifier assigned by the issuer to identify the transaction.
        """
        ares: Optional[str]
        """
        The Authentication Response Message (ARes) is the issuer's response to the AReq message.
        """
        ares_trans_status: Optional[
            Union[Literal["A", "C", "D", "I", "N", "R", "S", "U", "Y"], str]
        ]
        """
        TransStatus field on the ARes
        """
        cryptogram: Optional[str]
        """
        A 28-character Base64 string proving that 3DS was completed. Store this value securely, and don't reuse it for multiple authorizations.
        """
        ds_transaction_id: Optional[str]
        """
        The 3DS2 Directory Server Transaction ID.
        """
        eci: Optional[str]
        """
        Electronic Commerce Indicator provided by the issuer to indicate the result of this 3DS Authentication.
        """
        network_details: Optional[NetworkDetails]
        """
        Contains details specific to the individual network.
        """
        protocol_version: Union[Literal["2.1.0", "2.2.0", "2.3.1"], str]
        """
        The 3DS protocol version used for this 3DS Authentication.
        """
        requestor_challenge_indicator: Optional[
            Union[Literal["01", "02", "03", "04", "05", "06"], str]
        ]
        """
        The indicator provided to the issuer by Stripe in the AReq that indicates whether a challenge is requested for this Authentication. This indicator should match the flow_preference you specified but may be overridden (for compliance reasons for example).
        """
        rreq: Optional[str]
        """
        The Results Request Message (RReq) communicates the results of the authentication or verification.
        """
        rreq_trans_status: Optional[
            Union[Literal["A", "C", "D", "I", "N", "R", "S", "U", "Y"], str]
        ]
        """
        TransStatus field on the RReq
        """
        three_ds_server_transaction_id: str
        """
        Universally unique transaction identifier assigned by Stripe to identify the transaction.
        """
        _inner_class_types = {"network_details": NetworkDetails}

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
        State, county, province, or region ([ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)).
        """

    acquirer_details: Optional[AcquirerDetails]
    """
    Contains additional details about the acquirer for a 3DS Authentication.
    """
    amount: Optional[int]
    """
    The amount for this 3DS Authentication.
    """
    challenge_url: Optional[str]
    """
    The URL for presenting a challenge to your cardholder, present if status is requires_challenge.
    """
    channel: Channel
    """
    Contains details on the channel used (browser, 3RI) for a standalone 3DS Authentication.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: Optional[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    directory_server: Union[
        Literal[
            "american_express",
            "cartes_bancaires",
            "discover",
            "mastercard",
            "visa",
        ],
        str,
    ]
    """
    The 3DS directory server with which this 3DS Authentication was processed.
    """
    fingerprinting_url: Optional[str]
    """
    The URL for performing issuer fingerprinting, present if fingerprinting is supported for the given payment method.
    """
    flow_preference: Optional[FlowPreference]
    """
    Contains details of the flow preference used for a standalone 3DS Authentication.
    """
    future_usage: Optional[FutureUsage]
    """
    Contains information about the future authorisations related to this authentication
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    message_category: Union[
        Literal["non_payment_authentication", "payment_authentication"], str
    ]
    """
    Indicates whether this 3DS Authentication is being performed for a payment or non-payment use case.
    """
    metadata: Optional[UntypedStripeObject[str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["three_d_secure.authentication"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    outcome: Optional[
        Union[
            Literal[
                "abandoned",
                "attempt_acknowledged",
                "authenticated",
                "canceled",
                "denied",
                "informational",
                "internal_error",
                "not_supported",
                "not_triggered",
                "processing_error",
                "rejected",
            ],
            str,
        ]
    ]
    """
    The outcome of this 3DS Authentication.
    """
    outcome_details: Optional[OutcomeDetails]
    """
    Contains details on the result for a standalone 3DS Authentication.
    """
    payment_method: ExpandableField["PaymentMethod"]
    """
    ID of the payment method (a PaymentMethod object) to attach to this 3DS Authentication.
    """
    reason: Optional[
        Union[
            Literal[
                "cardholder_authentication",
                "issuer_requested",
                "liability_shift",
                "processing_costs",
                "regulatory_compliance",
            ],
            str,
        ]
    ]
    """
    The reason for invoking this 3DS Authentication.
    """
    shipping_address: Optional[ShippingAddress]
    """
    Contains details about the shipping address for a 3DS Authentication.
    """
    status: Union[
        Literal[
            "canceled",
            "error",
            "failed",
            "requires_challenge",
            "requires_submission",
            "succeeded",
        ],
        str,
    ]
    """
    Status of this Authentication.
    """

    @classmethod
    def _cls_cancel(
        cls,
        authentication: str,
        **params: Unpack["AuthenticationCancelParams"],
    ) -> "Authentication":
        """
        This endpoint cancels a 3DS Authentication. You can cancel a 3DS Authentication object when it's in a non-final status:
        requires_submission or requires_challenge.
        """
        return cast(
            "Authentication",
            cls._static_request(
                "post",
                "/v1/three_d_secure/authentications/{authentication}/cancel".format(
                    authentication=sanitize_id(authentication)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def cancel(
        authentication: str, **params: Unpack["AuthenticationCancelParams"]
    ) -> "Authentication":
        """
        This endpoint cancels a 3DS Authentication. You can cancel a 3DS Authentication object when it's in a non-final status:
        requires_submission or requires_challenge.
        """
        ...

    @overload
    def cancel(
        self, **params: Unpack["AuthenticationCancelParams"]
    ) -> "Authentication":
        """
        This endpoint cancels a 3DS Authentication. You can cancel a 3DS Authentication object when it's in a non-final status:
        requires_submission or requires_challenge.
        """
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["AuthenticationCancelParams"]
    ) -> "Authentication":
        """
        This endpoint cancels a 3DS Authentication. You can cancel a 3DS Authentication object when it's in a non-final status:
        requires_submission or requires_challenge.
        """
        return cast(
            "Authentication",
            self._request(
                "post",
                "/v1/three_d_secure/authentications/{authentication}/cancel".format(
                    authentication=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_cancel_async(
        cls,
        authentication: str,
        **params: Unpack["AuthenticationCancelParams"],
    ) -> "Authentication":
        """
        This endpoint cancels a 3DS Authentication. You can cancel a 3DS Authentication object when it's in a non-final status:
        requires_submission or requires_challenge.
        """
        return cast(
            "Authentication",
            await cls._static_request_async(
                "post",
                "/v1/three_d_secure/authentications/{authentication}/cancel".format(
                    authentication=sanitize_id(authentication)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def cancel_async(
        authentication: str, **params: Unpack["AuthenticationCancelParams"]
    ) -> "Authentication":
        """
        This endpoint cancels a 3DS Authentication. You can cancel a 3DS Authentication object when it's in a non-final status:
        requires_submission or requires_challenge.
        """
        ...

    @overload
    async def cancel_async(
        self, **params: Unpack["AuthenticationCancelParams"]
    ) -> "Authentication":
        """
        This endpoint cancels a 3DS Authentication. You can cancel a 3DS Authentication object when it's in a non-final status:
        requires_submission or requires_challenge.
        """
        ...

    @class_method_variant("_cls_cancel_async")
    async def cancel_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["AuthenticationCancelParams"]
    ) -> "Authentication":
        """
        This endpoint cancels a 3DS Authentication. You can cancel a 3DS Authentication object when it's in a non-final status:
        requires_submission or requires_challenge.
        """
        return cast(
            "Authentication",
            await self._request_async(
                "post",
                "/v1/three_d_secure/authentications/{authentication}/cancel".format(
                    authentication=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def create(
        cls, **params: Unpack["AuthenticationCreateParams"]
    ) -> "Authentication":
        """
        This endpoint creates a 3DS Authentication. Refer to the [Create a 3DS Authentication object section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#create-a-3ds-authentication-object) for more information.

        You can pass the submit parameter to automatically submit the 3DS Authentication object when you create it. Refer to the [Submit at creation section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-at-creation) for more information.
        """
        return cast(
            "Authentication",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["AuthenticationCreateParams"]
    ) -> "Authentication":
        """
        This endpoint creates a 3DS Authentication. Refer to the [Create a 3DS Authentication object section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#create-a-3ds-authentication-object) for more information.

        You can pass the submit parameter to automatically submit the 3DS Authentication object when you create it. Refer to the [Submit at creation section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-at-creation) for more information.
        """
        return cast(
            "Authentication",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["AuthenticationListParams"]
    ) -> ListObject["Authentication"]:
        """
        Returns a list of 3D Secure Authentications.
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
        cls, **params: Unpack["AuthenticationListParams"]
    ) -> ListObject["Authentication"]:
        """
        Returns a list of 3D Secure Authentications.
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
    def retrieve(
        cls, id: str, **params: Unpack["AuthenticationRetrieveParams"]
    ) -> "Authentication":
        """
        This endpoint retrieves a 3DS Authentication.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["AuthenticationRetrieveParams"]
    ) -> "Authentication":
        """
        This endpoint retrieves a 3DS Authentication.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def _cls_submit(
        cls,
        authentication: str,
        **params: Unpack["AuthenticationSubmitParams"],
    ) -> "Authentication":
        """
        This endpoint submits a 3DS Authentication. You can submit a 3DS Authentication object when it has status requires_submission. Refer to the [Submit the 3DS Authentication object section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-the-3ds-authentication-object) for more information.
        """
        return cast(
            "Authentication",
            cls._static_request(
                "post",
                "/v1/three_d_secure/authentications/{authentication}/submit".format(
                    authentication=sanitize_id(authentication)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def submit(
        authentication: str, **params: Unpack["AuthenticationSubmitParams"]
    ) -> "Authentication":
        """
        This endpoint submits a 3DS Authentication. You can submit a 3DS Authentication object when it has status requires_submission. Refer to the [Submit the 3DS Authentication object section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-the-3ds-authentication-object) for more information.
        """
        ...

    @overload
    def submit(
        self, **params: Unpack["AuthenticationSubmitParams"]
    ) -> "Authentication":
        """
        This endpoint submits a 3DS Authentication. You can submit a 3DS Authentication object when it has status requires_submission. Refer to the [Submit the 3DS Authentication object section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-the-3ds-authentication-object) for more information.
        """
        ...

    @class_method_variant("_cls_submit")
    def submit(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["AuthenticationSubmitParams"]
    ) -> "Authentication":
        """
        This endpoint submits a 3DS Authentication. You can submit a 3DS Authentication object when it has status requires_submission. Refer to the [Submit the 3DS Authentication object section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-the-3ds-authentication-object) for more information.
        """
        return cast(
            "Authentication",
            self._request(
                "post",
                "/v1/three_d_secure/authentications/{authentication}/submit".format(
                    authentication=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_submit_async(
        cls,
        authentication: str,
        **params: Unpack["AuthenticationSubmitParams"],
    ) -> "Authentication":
        """
        This endpoint submits a 3DS Authentication. You can submit a 3DS Authentication object when it has status requires_submission. Refer to the [Submit the 3DS Authentication object section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-the-3ds-authentication-object) for more information.
        """
        return cast(
            "Authentication",
            await cls._static_request_async(
                "post",
                "/v1/three_d_secure/authentications/{authentication}/submit".format(
                    authentication=sanitize_id(authentication)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def submit_async(
        authentication: str, **params: Unpack["AuthenticationSubmitParams"]
    ) -> "Authentication":
        """
        This endpoint submits a 3DS Authentication. You can submit a 3DS Authentication object when it has status requires_submission. Refer to the [Submit the 3DS Authentication object section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-the-3ds-authentication-object) for more information.
        """
        ...

    @overload
    async def submit_async(
        self, **params: Unpack["AuthenticationSubmitParams"]
    ) -> "Authentication":
        """
        This endpoint submits a 3DS Authentication. You can submit a 3DS Authentication object when it has status requires_submission. Refer to the [Submit the 3DS Authentication object section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-the-3ds-authentication-object) for more information.
        """
        ...

    @class_method_variant("_cls_submit_async")
    async def submit_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["AuthenticationSubmitParams"]
    ) -> "Authentication":
        """
        This endpoint submits a 3DS Authentication. You can submit a 3DS Authentication object when it has status requires_submission. Refer to the [Submit the 3DS Authentication object section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-the-3ds-authentication-object) for more information.
        """
        return cast(
            "Authentication",
            await self._request_async(
                "post",
                "/v1/three_d_secure/authentications/{authentication}/submit".format(
                    authentication=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    _inner_class_types = {
        "acquirer_details": AcquirerDetails,
        "channel": Channel,
        "flow_preference": FlowPreference,
        "future_usage": FutureUsage,
        "outcome_details": OutcomeDetails,
        "shipping_address": ShippingAddress,
    }
