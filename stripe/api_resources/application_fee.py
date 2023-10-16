# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    ListableAPIResource,
    nested_resource_class_methods,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from typing import Dict, List, Optional
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.application_fee_refund import (
        ApplicationFeeRefund,
    )
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.charge import Charge


@nested_resource_class_methods("refund")
class ApplicationFee(ListableAPIResource["ApplicationFee"]):
    OBJECT_NAME = "application_fee"
    if TYPE_CHECKING:

        class ListParams(RequestOptions):
            charge: NotRequired["str|None"]
            created: NotRequired["ApplicationFee.ListParamsCreated|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class RefundParams(RequestOptions):
            amount: NotRequired["int|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class CreateRefundParams(RequestOptions):
            amount: NotRequired["int|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]

        class RetrieveRefundParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ModifyRefundParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

        class ListRefundsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

    account: ExpandableField["Account"]
    amount: int
    amount_refunded: int
    application: ExpandableField["Application"]
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    charge: ExpandableField["Charge"]
    created: int
    currency: str
    id: str
    livemode: bool
    object: Literal["application_fee"]
    originating_transaction: Optional[ExpandableField["Charge"]]
    refunded: bool
    refunds: ListObject["ApplicationFeeRefund"]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ApplicationFee.ListParams"]
    ) -> ListObject["ApplicationFee"]:
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
    def _cls_refund(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ApplicationFee.RefundParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/application_fees/{id}/refunds".format(
                id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_refund")
    def refund(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["ApplicationFee.RefundParams"]
    ):
        return self._request(
            "post",
            "/v1/application_fees/{id}/refunds".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["ApplicationFee.RetrieveParams"]
    ) -> "ApplicationFee":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def create_refund(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ApplicationFee.CreateRefundParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/application_fees/{id}/refunds".format(
                id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_refund(
        cls,
        fee: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ApplicationFee.RetrieveRefundParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/application_fees/{fee}/refunds/{id}".format(
                fee=util.sanitize_id(fee), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def modify_refund(
        cls,
        fee: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ApplicationFee.ModifyRefundParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/application_fees/{fee}/refunds/{id}".format(
                fee=util.sanitize_id(fee), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_refunds(
        cls,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["ApplicationFee.ListRefundsParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/application_fees/{id}/refunds".format(
                id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
