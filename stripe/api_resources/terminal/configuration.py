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
            Optional["Configuration.CreateBbposWiseposEParams"]
        ]
        expand: NotRequired[Optional[List[str]]]
        tipping: NotRequired[
            Optional[Union[Literal[""], "Configuration.CreateTippingParams"]]
        ]
        verifone_p400: NotRequired[
            Optional["Configuration.CreateVerifoneP400Params"]
        ]

    class CreateVerifoneP400Params(TypedDict):
        splashscreen: NotRequired[Optional[Union[Literal[""], str]]]

    class CreateTippingParams(TypedDict):
        aud: NotRequired[Optional["Configuration.CreateTippingAudParams"]]
        cad: NotRequired[Optional["Configuration.CreateTippingCadParams"]]
        chf: NotRequired[Optional["Configuration.CreateTippingChfParams"]]
        czk: NotRequired[Optional["Configuration.CreateTippingCzkParams"]]
        dkk: NotRequired[Optional["Configuration.CreateTippingDkkParams"]]
        eur: NotRequired[Optional["Configuration.CreateTippingEurParams"]]
        gbp: NotRequired[Optional["Configuration.CreateTippingGbpParams"]]
        hkd: NotRequired[Optional["Configuration.CreateTippingHkdParams"]]
        myr: NotRequired[Optional["Configuration.CreateTippingMyrParams"]]
        nok: NotRequired[Optional["Configuration.CreateTippingNokParams"]]
        nzd: NotRequired[Optional["Configuration.CreateTippingNzdParams"]]
        sek: NotRequired[Optional["Configuration.CreateTippingSekParams"]]
        sgd: NotRequired[Optional["Configuration.CreateTippingSgdParams"]]
        usd: NotRequired[Optional["Configuration.CreateTippingUsdParams"]]

    class CreateTippingUsdParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateTippingSgdParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateTippingSekParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateTippingNzdParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateTippingNokParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateTippingMyrParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateTippingHkdParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateTippingGbpParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateTippingEurParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateTippingDkkParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateTippingCzkParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateTippingChfParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateTippingCadParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateTippingAudParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class CreateBbposWiseposEParams(TypedDict):
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
                Union[Literal[""], "Configuration.ModifyBbposWiseposEParams"]
            ]
        ]
        expand: NotRequired[Optional[List[str]]]
        tipping: NotRequired[
            Optional[Union[Literal[""], "Configuration.ModifyTippingParams"]]
        ]
        verifone_p400: NotRequired[
            Optional[
                Union[Literal[""], "Configuration.ModifyVerifoneP400Params"]
            ]
        ]

    class ModifyVerifoneP400Params(TypedDict):
        splashscreen: NotRequired[Optional[Union[Literal[""], str]]]

    class ModifyTippingParams(TypedDict):
        aud: NotRequired[Optional["Configuration.ModifyTippingAudParams"]]
        cad: NotRequired[Optional["Configuration.ModifyTippingCadParams"]]
        chf: NotRequired[Optional["Configuration.ModifyTippingChfParams"]]
        czk: NotRequired[Optional["Configuration.ModifyTippingCzkParams"]]
        dkk: NotRequired[Optional["Configuration.ModifyTippingDkkParams"]]
        eur: NotRequired[Optional["Configuration.ModifyTippingEurParams"]]
        gbp: NotRequired[Optional["Configuration.ModifyTippingGbpParams"]]
        hkd: NotRequired[Optional["Configuration.ModifyTippingHkdParams"]]
        myr: NotRequired[Optional["Configuration.ModifyTippingMyrParams"]]
        nok: NotRequired[Optional["Configuration.ModifyTippingNokParams"]]
        nzd: NotRequired[Optional["Configuration.ModifyTippingNzdParams"]]
        sek: NotRequired[Optional["Configuration.ModifyTippingSekParams"]]
        sgd: NotRequired[Optional["Configuration.ModifyTippingSgdParams"]]
        usd: NotRequired[Optional["Configuration.ModifyTippingUsdParams"]]

    class ModifyTippingUsdParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyTippingSgdParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyTippingSekParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyTippingNzdParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyTippingNokParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyTippingMyrParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyTippingHkdParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyTippingGbpParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyTippingEurParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyTippingDkkParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyTippingCzkParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyTippingChfParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyTippingCadParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyTippingAudParams(TypedDict):
        fixed_amounts: NotRequired[Optional[List[int]]]
        percentages: NotRequired[Optional[List[int]]]
        smart_tip_threshold: NotRequired[Optional[int]]

    class ModifyBbposWiseposEParams(TypedDict):
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
