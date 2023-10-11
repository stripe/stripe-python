# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

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
from typing import List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
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

    class CreateParams(RequestOptions):
        bbpos_wisepos_e: NotRequired[
            Optional["Configuration.CreateParamsBbposWiseposE"]
        ]
        expand: NotRequired[Optional[List[str]]]
        tipping: NotRequired[
            Optional[Union[Literal[""], "Configuration.CreateParamsTipping"]]
        ]
        verifone_p400: NotRequired[
            Optional["Configuration.CreateParamsVerifoneP400"]
        ]

    class CreateParamsVerifoneP400(TypedDict):
        splashscreen: NotRequired[Optional[Union[Literal[""], str]]]

    class CreateParamsTipping(TypedDict):
        aud: NotRequired[Optional["Configuration.CreateParamsTippingAud"]]
        cad: NotRequired[Optional["Configuration.CreateParamsTippingCad"]]
        chf: NotRequired[Optional["Configuration.CreateParamsTippingChf"]]
        czk: NotRequired[Optional["Configuration.CreateParamsTippingCzk"]]
        dkk: NotRequired[Optional["Configuration.CreateParamsTippingDkk"]]
        eur: NotRequired[Optional["Configuration.CreateParamsTippingEur"]]
        gbp: NotRequired[Optional["Configuration.CreateParamsTippingGbp"]]
        hkd: NotRequired[Optional["Configuration.CreateParamsTippingHkd"]]
        myr: NotRequired[Optional["Configuration.CreateParamsTippingMyr"]]
        nok: NotRequired[Optional["Configuration.CreateParamsTippingNok"]]
        nzd: NotRequired[Optional["Configuration.CreateParamsTippingNzd"]]
        sek: NotRequired[Optional["Configuration.CreateParamsTippingSek"]]
        sgd: NotRequired[Optional["Configuration.CreateParamsTippingSgd"]]
        usd: NotRequired[Optional["Configuration.CreateParamsTippingUsd"]]

    class CreateParamsTippingUsd(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateParamsTippingSgd(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateParamsTippingSek(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateParamsTippingNzd(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateParamsTippingNok(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateParamsTippingMyr(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateParamsTippingHkd(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateParamsTippingGbp(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateParamsTippingEur(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateParamsTippingDkk(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateParamsTippingCzk(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateParamsTippingChf(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateParamsTippingCad(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateParamsTippingAud(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateParamsBbposWiseposE(TypedDict):
        splashscreen: NotRequired[Optional[Union[Literal[""], str]]]

    class DeleteParams(RequestOptions):
        pass

    class ListParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        is_account_default: NotRequired[Optional[bool]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ModifyParams(RequestOptions):
        bbpos_wisepos_e: NotRequired[
            Optional[
                Union[Literal[""], "Configuration.ModifyParamsBbposWiseposE"]
            ]
        ]
        expand: NotRequired[Optional[List[str]]]
        tipping: NotRequired[
            Optional[Union[Literal[""], "Configuration.ModifyParamsTipping"]]
        ]
        verifone_p400: NotRequired[
            Optional[
                Union[Literal[""], "Configuration.ModifyParamsVerifoneP400"]
            ]
        ]

    class ModifyParamsVerifoneP400(TypedDict):
        splashscreen: NotRequired[Optional[Union[Literal[""], str]]]

    class ModifyParamsTipping(TypedDict):
        aud: NotRequired[Optional["Configuration.ModifyParamsTippingAud"]]
        cad: NotRequired[Optional["Configuration.ModifyParamsTippingCad"]]
        chf: NotRequired[Optional["Configuration.ModifyParamsTippingChf"]]
        czk: NotRequired[Optional["Configuration.ModifyParamsTippingCzk"]]
        dkk: NotRequired[Optional["Configuration.ModifyParamsTippingDkk"]]
        eur: NotRequired[Optional["Configuration.ModifyParamsTippingEur"]]
        gbp: NotRequired[Optional["Configuration.ModifyParamsTippingGbp"]]
        hkd: NotRequired[Optional["Configuration.ModifyParamsTippingHkd"]]
        myr: NotRequired[Optional["Configuration.ModifyParamsTippingMyr"]]
        nok: NotRequired[Optional["Configuration.ModifyParamsTippingNok"]]
        nzd: NotRequired[Optional["Configuration.ModifyParamsTippingNzd"]]
        sek: NotRequired[Optional["Configuration.ModifyParamsTippingSek"]]
        sgd: NotRequired[Optional["Configuration.ModifyParamsTippingSgd"]]
        usd: NotRequired[Optional["Configuration.ModifyParamsTippingUsd"]]

    class ModifyParamsTippingUsd(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyParamsTippingSgd(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyParamsTippingSek(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyParamsTippingNzd(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyParamsTippingNok(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyParamsTippingMyr(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyParamsTippingHkd(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyParamsTippingGbp(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyParamsTippingEur(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyParamsTippingDkk(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyParamsTippingCzk(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyParamsTippingChf(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyParamsTippingCad(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyParamsTippingAud(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyParamsBbposWiseposE(TypedDict):
        splashscreen: NotRequired[Optional[Union[Literal[""], str]]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

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
