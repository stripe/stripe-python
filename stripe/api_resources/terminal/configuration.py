# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus


class Configuration(
    CreateableAPIResource["Configuration"],
    DeletableAPIResource["Configuration"],
    ListableAPIResource["Configuration"],
    UpdateableAPIResource["Configuration"],
):
    """
    A Configurations object represents how features should be configured for terminal readers.
    """

    OBJECT_NAME = "terminal.configuration"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            bbpos_wisepos_e: NotRequired[
                "Configuration.CreateParamsBbposWiseposE|None"
            ]
            expand: NotRequired["List[str]|None"]
            offline: NotRequired[
                "Literal['']|Configuration.CreateParamsOffline|None"
            ]
            tipping: NotRequired[
                "Literal['']|Configuration.CreateParamsTipping|None"
            ]
            verifone_p400: NotRequired[
                "Configuration.CreateParamsVerifoneP400|None"
            ]

        class CreateParamsVerifoneP400(TypedDict):
            splashscreen: NotRequired["Literal['']|str|None"]

        class CreateParamsTipping(TypedDict):
            aud: NotRequired["Configuration.CreateParamsTippingAud|None"]
            cad: NotRequired["Configuration.CreateParamsTippingCad|None"]
            chf: NotRequired["Configuration.CreateParamsTippingChf|None"]
            czk: NotRequired["Configuration.CreateParamsTippingCzk|None"]
            dkk: NotRequired["Configuration.CreateParamsTippingDkk|None"]
            eur: NotRequired["Configuration.CreateParamsTippingEur|None"]
            gbp: NotRequired["Configuration.CreateParamsTippingGbp|None"]
            hkd: NotRequired["Configuration.CreateParamsTippingHkd|None"]
            myr: NotRequired["Configuration.CreateParamsTippingMyr|None"]
            nok: NotRequired["Configuration.CreateParamsTippingNok|None"]
            nzd: NotRequired["Configuration.CreateParamsTippingNzd|None"]
            sek: NotRequired["Configuration.CreateParamsTippingSek|None"]
            sgd: NotRequired["Configuration.CreateParamsTippingSgd|None"]
            usd: NotRequired["Configuration.CreateParamsTippingUsd|None"]

        class CreateParamsTippingUsd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class CreateParamsTippingSgd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class CreateParamsTippingSek(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class CreateParamsTippingNzd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class CreateParamsTippingNok(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class CreateParamsTippingMyr(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class CreateParamsTippingHkd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class CreateParamsTippingGbp(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class CreateParamsTippingEur(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class CreateParamsTippingDkk(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class CreateParamsTippingCzk(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class CreateParamsTippingChf(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class CreateParamsTippingCad(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class CreateParamsTippingAud(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class CreateParamsOffline(TypedDict):
            enabled: bool

        class CreateParamsBbposWiseposE(TypedDict):
            splashscreen: NotRequired["Literal['']|str|None"]

        class DeleteParams(RequestOptions):
            pass

        class ListParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            is_account_default: NotRequired["bool|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ModifyParams(RequestOptions):
            bbpos_wisepos_e: NotRequired[
                "Literal['']|Configuration.ModifyParamsBbposWiseposE|None"
            ]
            expand: NotRequired["List[str]|None"]
            offline: NotRequired[
                "Literal['']|Configuration.ModifyParamsOffline|None"
            ]
            tipping: NotRequired[
                "Literal['']|Configuration.ModifyParamsTipping|None"
            ]
            verifone_p400: NotRequired[
                "Literal['']|Configuration.ModifyParamsVerifoneP400|None"
            ]

        class ModifyParamsVerifoneP400(TypedDict):
            splashscreen: NotRequired["Literal['']|str|None"]

        class ModifyParamsTipping(TypedDict):
            aud: NotRequired["Configuration.ModifyParamsTippingAud|None"]
            cad: NotRequired["Configuration.ModifyParamsTippingCad|None"]
            chf: NotRequired["Configuration.ModifyParamsTippingChf|None"]
            czk: NotRequired["Configuration.ModifyParamsTippingCzk|None"]
            dkk: NotRequired["Configuration.ModifyParamsTippingDkk|None"]
            eur: NotRequired["Configuration.ModifyParamsTippingEur|None"]
            gbp: NotRequired["Configuration.ModifyParamsTippingGbp|None"]
            hkd: NotRequired["Configuration.ModifyParamsTippingHkd|None"]
            myr: NotRequired["Configuration.ModifyParamsTippingMyr|None"]
            nok: NotRequired["Configuration.ModifyParamsTippingNok|None"]
            nzd: NotRequired["Configuration.ModifyParamsTippingNzd|None"]
            sek: NotRequired["Configuration.ModifyParamsTippingSek|None"]
            sgd: NotRequired["Configuration.ModifyParamsTippingSgd|None"]
            usd: NotRequired["Configuration.ModifyParamsTippingUsd|None"]

        class ModifyParamsTippingUsd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class ModifyParamsTippingSgd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class ModifyParamsTippingSek(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class ModifyParamsTippingNzd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class ModifyParamsTippingNok(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class ModifyParamsTippingMyr(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class ModifyParamsTippingHkd(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class ModifyParamsTippingGbp(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class ModifyParamsTippingEur(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class ModifyParamsTippingDkk(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class ModifyParamsTippingCzk(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class ModifyParamsTippingChf(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class ModifyParamsTippingCad(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class ModifyParamsTippingAud(TypedDict):
            fixed_amounts: NotRequired["List[int]|None"]
            percentages: NotRequired["List[int]|None"]
            smart_tip_threshold: NotRequired["int|None"]

        class ModifyParamsOffline(TypedDict):
            enabled: bool

        class ModifyParamsBbposWiseposE(TypedDict):
            splashscreen: NotRequired["Literal['']|str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    bbpos_wisepos_e: Optional[StripeObject]
    id: str
    is_account_default: Optional[bool]
    livemode: bool
    object: Literal["terminal.configuration"]
    offline: Optional[StripeObject]
    tipping: Optional[StripeObject]
    verifone_p400: Optional[StripeObject]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Configuration.CreateParams"]
    ) -> "Configuration":
        return cast(
            "Configuration",
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
    def _cls_delete(
        cls, sid: str, **params: Unpack["Configuration.DeleteParams"]
    ) -> "Configuration":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Configuration",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(
        self, **params: Unpack["Configuration.DeleteParams"]
    ) -> "Configuration":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Configuration.ListParams"]
    ) -> ListObject["Configuration"]:
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
        cls, id, **params: Unpack["Configuration.ModifyParams"]
    ) -> "Configuration":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Configuration",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Configuration.RetrieveParams"]
    ) -> "Configuration":
        instance = cls(id, **params)
        instance.refresh()
        return instance
