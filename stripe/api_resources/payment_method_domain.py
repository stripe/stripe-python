# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from stripe.util import class_method_variant
from typing import ClassVar, List, Optional, cast, overload
from typing_extensions import Literal, NotRequired, Unpack, TYPE_CHECKING
from urllib.parse import quote_plus


class PaymentMethodDomain(
    CreateableAPIResource["PaymentMethodDomain"],
    ListableAPIResource["PaymentMethodDomain"],
    UpdateableAPIResource["PaymentMethodDomain"],
):
    """
    A payment method domain represents a web domain that you have registered with Stripe.
    Stripe Elements use registered payment method domains to control where certain payment methods are shown.

    Related guides: [Payment method domains](https://stripe.com/docs/payments/payment-methods/pmd-registration).
    """

    OBJECT_NAME: ClassVar[
        Literal["payment_method_domain"]
    ] = "payment_method_domain"

    class ApplePay(StripeObject):
        class StatusDetails(StripeObject):
            error_message: str
            """
            The error message associated with the status of the payment method on the domain.
            """

        status: Literal["active", "inactive"]
        """
        The status of the payment method on the domain.
        """
        status_details: Optional[StatusDetails]
        """
        Contains additional details about the status of a payment method for a specific payment method domain.
        """
        _inner_class_types = {"status_details": StatusDetails}

    class GooglePay(StripeObject):
        class StatusDetails(StripeObject):
            error_message: str
            """
            The error message associated with the status of the payment method on the domain.
            """

        status: Literal["active", "inactive"]
        """
        The status of the payment method on the domain.
        """
        status_details: Optional[StatusDetails]
        """
        Contains additional details about the status of a payment method for a specific payment method domain.
        """
        _inner_class_types = {"status_details": StatusDetails}

    class Link(StripeObject):
        class StatusDetails(StripeObject):
            error_message: str
            """
            The error message associated with the status of the payment method on the domain.
            """

        status: Literal["active", "inactive"]
        """
        The status of the payment method on the domain.
        """
        status_details: Optional[StatusDetails]
        """
        Contains additional details about the status of a payment method for a specific payment method domain.
        """
        _inner_class_types = {"status_details": StatusDetails}

    class Paypal(StripeObject):
        class StatusDetails(StripeObject):
            error_message: str
            """
            The error message associated with the status of the payment method on the domain.
            """

        status: Literal["active", "inactive"]
        """
        The status of the payment method on the domain.
        """
        status_details: Optional[StatusDetails]
        """
        Contains additional details about the status of a payment method for a specific payment method domain.
        """
        _inner_class_types = {"status_details": StatusDetails}

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            domain_name: str
            """
            The domain name that this payment method domain object represents.
            """
            enabled: NotRequired["bool|None"]
            """
            Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ListParams(RequestOptions):
            domain_name: NotRequired["str|None"]
            """
            The domain name that this payment method domain object represents.
            """
            enabled: NotRequired["bool|None"]
            """
            Whether this payment method domain is enabled. If the domain is not enabled, payment methods will not appear in Elements
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

        class ModifyParams(RequestOptions):
            enabled: NotRequired["bool|None"]
            """
            Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ValidateParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    apple_pay: ApplePay
    """
    Indicates the status of a specific payment method on a payment method domain.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    domain_name: str
    """
    The domain name that this payment method domain object represents.
    """
    enabled: bool
    """
    Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements.
    """
    google_pay: GooglePay
    """
    Indicates the status of a specific payment method on a payment method domain.
    """
    id: str
    """
    Unique identifier for the object.
    """
    link: Link
    """
    Indicates the status of a specific payment method on a payment method domain.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["payment_method_domain"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    paypal: Paypal
    """
    Indicates the status of a specific payment method on a payment method domain.
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentMethodDomain.CreateParams"]
    ) -> "PaymentMethodDomain":
        """
        Creates a payment method domain.
        """
        return cast(
            "PaymentMethodDomain",
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
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentMethodDomain.ListParams"]
    ) -> ListObject["PaymentMethodDomain"]:
        """
        Lists the details of existing payment method domains.
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
    def modify(
        cls, id: str, **params: Unpack["PaymentMethodDomain.ModifyParams"]
    ) -> "PaymentMethodDomain":
        """
        Updates an existing payment method domain.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentMethodDomain",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PaymentMethodDomain.RetrieveParams"]
    ) -> "PaymentMethodDomain":
        """
        Retrieves the details of an existing payment method domain.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_validate(
        cls,
        payment_method_domain: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentMethodDomain.ValidateParams"]
    ) -> "PaymentMethodDomain":
        """
        Some payment methods such as Apple Pay require additional steps to verify a domain. If the requirements weren't satisfied when the domain was created, the payment method will be inactive on the domain.
        The payment method doesn't appear in Elements for this domain until it is active.

        To activate a payment method on an existing payment method domain, complete the required validation steps specific to the payment method, and then validate the payment method domain with this endpoint.

        Related guides: [Payment method domains](https://stripe.com/docs/payments/payment-methods/pmd-registration).
        """
        return cast(
            "PaymentMethodDomain",
            cls._static_request(
                "post",
                "/v1/payment_method_domains/{payment_method_domain}/validate".format(
                    payment_method_domain=util.sanitize_id(
                        payment_method_domain
                    )
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def validate(
        payment_method_domain: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentMethodDomain.ValidateParams"]
    ) -> "PaymentMethodDomain":
        """
        Some payment methods such as Apple Pay require additional steps to verify a domain. If the requirements weren't satisfied when the domain was created, the payment method will be inactive on the domain.
        The payment method doesn't appear in Elements for this domain until it is active.

        To activate a payment method on an existing payment method domain, complete the required validation steps specific to the payment method, and then validate the payment method domain with this endpoint.

        Related guides: [Payment method domains](https://stripe.com/docs/payments/payment-methods/pmd-registration).
        """
        ...

    @overload
    def validate(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentMethodDomain.ValidateParams"]
    ) -> "PaymentMethodDomain":
        """
        Some payment methods such as Apple Pay require additional steps to verify a domain. If the requirements weren't satisfied when the domain was created, the payment method will be inactive on the domain.
        The payment method doesn't appear in Elements for this domain until it is active.

        To activate a payment method on an existing payment method domain, complete the required validation steps specific to the payment method, and then validate the payment method domain with this endpoint.

        Related guides: [Payment method domains](https://stripe.com/docs/payments/payment-methods/pmd-registration).
        """
        ...

    @class_method_variant("_cls_validate")
    def validate(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentMethodDomain.ValidateParams"]
    ) -> "PaymentMethodDomain":
        """
        Some payment methods such as Apple Pay require additional steps to verify a domain. If the requirements weren't satisfied when the domain was created, the payment method will be inactive on the domain.
        The payment method doesn't appear in Elements for this domain until it is active.

        To activate a payment method on an existing payment method domain, complete the required validation steps specific to the payment method, and then validate the payment method domain with this endpoint.

        Related guides: [Payment method domains](https://stripe.com/docs/payments/payment-methods/pmd-registration).
        """
        return cast(
            "PaymentMethodDomain",
            self._request(
                "post",
                "/v1/payment_method_domains/{payment_method_domain}/validate".format(
                    payment_method_domain=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    _inner_class_types = {
        "apple_pay": ApplePay,
        "google_pay": GooglePay,
        "link": Link,
        "paypal": Paypal,
    }
