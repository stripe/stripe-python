# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.file import File


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

    class BbposWiseposE(StripeObject):
        splashscreen: Optional[ExpandableField["File"]]

    class Offline(StripeObject):
        enabled: Optional[bool]

    class Tipping(StripeObject):
        class Aud(StripeObject):
            fixed_amounts: Optional[List[int]]
            percentages: Optional[List[int]]
            smart_tip_threshold: Optional[int]

        class Cad(StripeObject):
            fixed_amounts: Optional[List[int]]
            percentages: Optional[List[int]]
            smart_tip_threshold: Optional[int]

        class Chf(StripeObject):
            fixed_amounts: Optional[List[int]]
            percentages: Optional[List[int]]
            smart_tip_threshold: Optional[int]

        class Czk(StripeObject):
            fixed_amounts: Optional[List[int]]
            percentages: Optional[List[int]]
            smart_tip_threshold: Optional[int]

        class Dkk(StripeObject):
            fixed_amounts: Optional[List[int]]
            percentages: Optional[List[int]]
            smart_tip_threshold: Optional[int]

        class Eur(StripeObject):
            fixed_amounts: Optional[List[int]]
            percentages: Optional[List[int]]
            smart_tip_threshold: Optional[int]

        class Gbp(StripeObject):
            fixed_amounts: Optional[List[int]]
            percentages: Optional[List[int]]
            smart_tip_threshold: Optional[int]

        class Hkd(StripeObject):
            fixed_amounts: Optional[List[int]]
            percentages: Optional[List[int]]
            smart_tip_threshold: Optional[int]

        class Myr(StripeObject):
            fixed_amounts: Optional[List[int]]
            percentages: Optional[List[int]]
            smart_tip_threshold: Optional[int]

        class Nok(StripeObject):
            fixed_amounts: Optional[List[int]]
            percentages: Optional[List[int]]
            smart_tip_threshold: Optional[int]

        class Nzd(StripeObject):
            fixed_amounts: Optional[List[int]]
            percentages: Optional[List[int]]
            smart_tip_threshold: Optional[int]

        class Sek(StripeObject):
            fixed_amounts: Optional[List[int]]
            percentages: Optional[List[int]]
            smart_tip_threshold: Optional[int]

        class Sgd(StripeObject):
            fixed_amounts: Optional[List[int]]
            percentages: Optional[List[int]]
            smart_tip_threshold: Optional[int]

        class Usd(StripeObject):
            fixed_amounts: Optional[List[int]]
            percentages: Optional[List[int]]
            smart_tip_threshold: Optional[int]

        aud: Optional[Aud]
        cad: Optional[Cad]
        chf: Optional[Chf]
        czk: Optional[Czk]
        dkk: Optional[Dkk]
        eur: Optional[Eur]
        gbp: Optional[Gbp]
        hkd: Optional[Hkd]
        myr: Optional[Myr]
        nok: Optional[Nok]
        nzd: Optional[Nzd]
        sek: Optional[Sek]
        sgd: Optional[Sgd]
        usd: Optional[Usd]
        _inner_class_types = {
            "aud": Aud,
            "cad": Cad,
            "chf": Chf,
            "czk": Czk,
            "dkk": Dkk,
            "eur": Eur,
            "gbp": Gbp,
            "hkd": Hkd,
            "myr": Myr,
            "nok": Nok,
            "nzd": Nzd,
            "sek": Sek,
            "sgd": Sgd,
            "usd": Usd,
        }

    class VerifoneP400(StripeObject):
        splashscreen: Optional[ExpandableField["File"]]

    bbpos_wisepos_e: Optional[BbposWiseposE]
    id: str
    is_account_default: Optional[bool]
    livemode: bool
    object: Literal["terminal.configuration"]
    offline: Optional[Offline]
    tipping: Optional[Tipping]
    verifone_p400: Optional[VerifoneP400]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
    def _cls_delete(cls, sid: str, **params: Any) -> "Configuration":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Configuration",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Any) -> "Configuration":
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
        **params: Any
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
    def modify(cls, id, **params: Any) -> "Configuration":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Configuration",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Configuration":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "bbpos_wisepos_e": BbposWiseposE,
        "offline": Offline,
        "tipping": Tipping,
        "verifone_p400": VerifoneP400,
    }
