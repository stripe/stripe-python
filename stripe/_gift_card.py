# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Optional, Union, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._gift_card_operation import GiftCardOperation
    from stripe.params._gift_card_activate_params import GiftCardActivateParams
    from stripe.params._gift_card_cashout_params import GiftCardCashoutParams
    from stripe.params._gift_card_check_balance_params import (
        GiftCardCheckBalanceParams,
    )
    from stripe.params._gift_card_create_params import GiftCardCreateParams
    from stripe.params._gift_card_reload_params import GiftCardReloadParams
    from stripe.params._gift_card_retrieve_params import GiftCardRetrieveParams
    from stripe.params._gift_card_void_operation_params import (
        GiftCardVoidOperationParams,
    )


class GiftCard(CreateableAPIResource["GiftCard"]):
    """
    Represents third-party gift cards that can be used as a payment method through Stripe.
    """

    OBJECT_NAME: ClassVar[Literal["gift_card"]] = "gift_card"
    brand: Union[Literal["svs"], str]
    """
    The brand of the gift card.
    """
    exp_month: Optional[int]
    """
    The expiration month of the gift card.
    """
    exp_year: Optional[int]
    """
    The expiration year of the gift card.
    """
    fingerprint: str
    """
    Uniquely identifies this particular gift card number. You can use this attribute to check whether two gift cards are the same.
    """
    id: str
    """
    Unique identifier for the object.
    """
    last4: Optional[str]
    """
    The last four digits of the gift card number.
    """
    last_operation: Optional[ExpandableField["GiftCardOperation"]]
    """
    The last operation performed on this gift card.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["gift_card"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """

    @classmethod
    def _cls_activate(
        cls, id: str, /, **params: Unpack["GiftCardActivateParams"]
    ) -> "GiftCardOperation":
        """
        Activates a third-party gift card and optionally sets its balance.
        """
        return cast(
            "GiftCardOperation",
            cls._static_request(
                "post",
                "/v1/gift_cards/{id}/activate".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def activate(
        id: str, /, **params: Unpack["GiftCardActivateParams"]
    ) -> "GiftCardOperation":
        """
        Activates a third-party gift card and optionally sets its balance.
        """
        ...

    @overload
    def activate(
        self, **params: Unpack["GiftCardActivateParams"]
    ) -> "GiftCardOperation":
        """
        Activates a third-party gift card and optionally sets its balance.
        """
        ...

    @class_method_variant("_cls_activate")
    def activate(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["GiftCardActivateParams"]
    ) -> "GiftCardOperation":
        """
        Activates a third-party gift card and optionally sets its balance.
        """
        return cast(
            "GiftCardOperation",
            self._request(
                "post",
                "/v1/gift_cards/{id}/activate".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_activate_async(
        cls, id: str, /, **params: Unpack["GiftCardActivateParams"]
    ) -> "GiftCardOperation":
        """
        Activates a third-party gift card and optionally sets its balance.
        """
        return cast(
            "GiftCardOperation",
            await cls._static_request_async(
                "post",
                "/v1/gift_cards/{id}/activate".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def activate_async(
        id: str, /, **params: Unpack["GiftCardActivateParams"]
    ) -> "GiftCardOperation":
        """
        Activates a third-party gift card and optionally sets its balance.
        """
        ...

    @overload
    async def activate_async(
        self, **params: Unpack["GiftCardActivateParams"]
    ) -> "GiftCardOperation":
        """
        Activates a third-party gift card and optionally sets its balance.
        """
        ...

    @class_method_variant("_cls_activate_async")
    async def activate_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["GiftCardActivateParams"]
    ) -> "GiftCardOperation":
        """
        Activates a third-party gift card and optionally sets its balance.
        """
        return cast(
            "GiftCardOperation",
            await self._request_async(
                "post",
                "/v1/gift_cards/{id}/activate".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_cashout(
        cls, id: str, /, **params: Unpack["GiftCardCashoutParams"]
    ) -> "GiftCardOperation":
        """
        Cashout a third-party gift card by zeroing its balance.
        """
        return cast(
            "GiftCardOperation",
            cls._static_request(
                "post",
                "/v1/gift_cards/{id}/cashout".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def cashout(
        id: str, /, **params: Unpack["GiftCardCashoutParams"]
    ) -> "GiftCardOperation":
        """
        Cashout a third-party gift card by zeroing its balance.
        """
        ...

    @overload
    def cashout(
        self, **params: Unpack["GiftCardCashoutParams"]
    ) -> "GiftCardOperation":
        """
        Cashout a third-party gift card by zeroing its balance.
        """
        ...

    @class_method_variant("_cls_cashout")
    def cashout(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["GiftCardCashoutParams"]
    ) -> "GiftCardOperation":
        """
        Cashout a third-party gift card by zeroing its balance.
        """
        return cast(
            "GiftCardOperation",
            self._request(
                "post",
                "/v1/gift_cards/{id}/cashout".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_cashout_async(
        cls, id: str, /, **params: Unpack["GiftCardCashoutParams"]
    ) -> "GiftCardOperation":
        """
        Cashout a third-party gift card by zeroing its balance.
        """
        return cast(
            "GiftCardOperation",
            await cls._static_request_async(
                "post",
                "/v1/gift_cards/{id}/cashout".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def cashout_async(
        id: str, /, **params: Unpack["GiftCardCashoutParams"]
    ) -> "GiftCardOperation":
        """
        Cashout a third-party gift card by zeroing its balance.
        """
        ...

    @overload
    async def cashout_async(
        self, **params: Unpack["GiftCardCashoutParams"]
    ) -> "GiftCardOperation":
        """
        Cashout a third-party gift card by zeroing its balance.
        """
        ...

    @class_method_variant("_cls_cashout_async")
    async def cashout_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["GiftCardCashoutParams"]
    ) -> "GiftCardOperation":
        """
        Cashout a third-party gift card by zeroing its balance.
        """
        return cast(
            "GiftCardOperation",
            await self._request_async(
                "post",
                "/v1/gift_cards/{id}/cashout".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_check_balance(
        cls, id: str, /, **params: Unpack["GiftCardCheckBalanceParams"]
    ) -> "GiftCardOperation":
        """
        Checks the balance of a third-party gift card.
        """
        return cast(
            "GiftCardOperation",
            cls._static_request(
                "post",
                "/v1/gift_cards/{id}/check_balance".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def check_balance(
        id: str, /, **params: Unpack["GiftCardCheckBalanceParams"]
    ) -> "GiftCardOperation":
        """
        Checks the balance of a third-party gift card.
        """
        ...

    @overload
    def check_balance(
        self, **params: Unpack["GiftCardCheckBalanceParams"]
    ) -> "GiftCardOperation":
        """
        Checks the balance of a third-party gift card.
        """
        ...

    @class_method_variant("_cls_check_balance")
    def check_balance(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["GiftCardCheckBalanceParams"]
    ) -> "GiftCardOperation":
        """
        Checks the balance of a third-party gift card.
        """
        return cast(
            "GiftCardOperation",
            self._request(
                "post",
                "/v1/gift_cards/{id}/check_balance".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_check_balance_async(
        cls, id: str, /, **params: Unpack["GiftCardCheckBalanceParams"]
    ) -> "GiftCardOperation":
        """
        Checks the balance of a third-party gift card.
        """
        return cast(
            "GiftCardOperation",
            await cls._static_request_async(
                "post",
                "/v1/gift_cards/{id}/check_balance".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def check_balance_async(
        id: str, /, **params: Unpack["GiftCardCheckBalanceParams"]
    ) -> "GiftCardOperation":
        """
        Checks the balance of a third-party gift card.
        """
        ...

    @overload
    async def check_balance_async(
        self, **params: Unpack["GiftCardCheckBalanceParams"]
    ) -> "GiftCardOperation":
        """
        Checks the balance of a third-party gift card.
        """
        ...

    @class_method_variant("_cls_check_balance_async")
    async def check_balance_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["GiftCardCheckBalanceParams"]
    ) -> "GiftCardOperation":
        """
        Checks the balance of a third-party gift card.
        """
        return cast(
            "GiftCardOperation",
            await self._request_async(
                "post",
                "/v1/gift_cards/{id}/check_balance".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def create(cls, **params: Unpack["GiftCardCreateParams"]) -> "GiftCard":
        """
        Creates a gift card object.
        """
        return cast(
            "GiftCard",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["GiftCardCreateParams"]
    ) -> "GiftCard":
        """
        Creates a gift card object.
        """
        return cast(
            "GiftCard",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def _cls_reload(
        cls, id: str, /, **params: Unpack["GiftCardReloadParams"]
    ) -> "GiftCardOperation":
        """
        Reloads a third-party gift card by adding the specified amount to its balance.
        """
        return cast(
            "GiftCardOperation",
            cls._static_request(
                "post",
                "/v1/gift_cards/{id}/reload".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def reload(
        id: str, /, **params: Unpack["GiftCardReloadParams"]
    ) -> "GiftCardOperation":
        """
        Reloads a third-party gift card by adding the specified amount to its balance.
        """
        ...

    @overload
    def reload(
        self, **params: Unpack["GiftCardReloadParams"]
    ) -> "GiftCardOperation":
        """
        Reloads a third-party gift card by adding the specified amount to its balance.
        """
        ...

    @class_method_variant("_cls_reload")
    def reload(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["GiftCardReloadParams"]
    ) -> "GiftCardOperation":
        """
        Reloads a third-party gift card by adding the specified amount to its balance.
        """
        return cast(
            "GiftCardOperation",
            self._request(
                "post",
                "/v1/gift_cards/{id}/reload".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_reload_async(
        cls, id: str, /, **params: Unpack["GiftCardReloadParams"]
    ) -> "GiftCardOperation":
        """
        Reloads a third-party gift card by adding the specified amount to its balance.
        """
        return cast(
            "GiftCardOperation",
            await cls._static_request_async(
                "post",
                "/v1/gift_cards/{id}/reload".format(id=sanitize_id(id)),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def reload_async(
        id: str, /, **params: Unpack["GiftCardReloadParams"]
    ) -> "GiftCardOperation":
        """
        Reloads a third-party gift card by adding the specified amount to its balance.
        """
        ...

    @overload
    async def reload_async(
        self, **params: Unpack["GiftCardReloadParams"]
    ) -> "GiftCardOperation":
        """
        Reloads a third-party gift card by adding the specified amount to its balance.
        """
        ...

    @class_method_variant("_cls_reload_async")
    async def reload_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["GiftCardReloadParams"]
    ) -> "GiftCardOperation":
        """
        Reloads a third-party gift card by adding the specified amount to its balance.
        """
        return cast(
            "GiftCardOperation",
            await self._request_async(
                "post",
                "/v1/gift_cards/{id}/reload".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["GiftCardRetrieveParams"]
    ) -> "GiftCard":
        """
        Retrieves a third-party gift card object.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["GiftCardRetrieveParams"]
    ) -> "GiftCard":
        """
        Retrieves a third-party gift card object.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def _cls_void_operation(
        cls, id: str, /, **params: Unpack["GiftCardVoidOperationParams"]
    ) -> "GiftCardOperation":
        """
        Voids a previously performed gift card operation.
        """
        return cast(
            "GiftCardOperation",
            cls._static_request(
                "post",
                "/v1/gift_cards/{id}/void_operation".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def void_operation(
        id: str, /, **params: Unpack["GiftCardVoidOperationParams"]
    ) -> "GiftCardOperation":
        """
        Voids a previously performed gift card operation.
        """
        ...

    @overload
    def void_operation(
        self, **params: Unpack["GiftCardVoidOperationParams"]
    ) -> "GiftCardOperation":
        """
        Voids a previously performed gift card operation.
        """
        ...

    @class_method_variant("_cls_void_operation")
    def void_operation(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["GiftCardVoidOperationParams"]
    ) -> "GiftCardOperation":
        """
        Voids a previously performed gift card operation.
        """
        return cast(
            "GiftCardOperation",
            self._request(
                "post",
                "/v1/gift_cards/{id}/void_operation".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_void_operation_async(
        cls, id: str, /, **params: Unpack["GiftCardVoidOperationParams"]
    ) -> "GiftCardOperation":
        """
        Voids a previously performed gift card operation.
        """
        return cast(
            "GiftCardOperation",
            await cls._static_request_async(
                "post",
                "/v1/gift_cards/{id}/void_operation".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def void_operation_async(
        id: str, /, **params: Unpack["GiftCardVoidOperationParams"]
    ) -> "GiftCardOperation":
        """
        Voids a previously performed gift card operation.
        """
        ...

    @overload
    async def void_operation_async(
        self, **params: Unpack["GiftCardVoidOperationParams"]
    ) -> "GiftCardOperation":
        """
        Voids a previously performed gift card operation.
        """
        ...

    @class_method_variant("_cls_void_operation_async")
    async def void_operation_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["GiftCardVoidOperationParams"]
    ) -> "GiftCardOperation":
        """
        Voids a previously performed gift card operation.
        """
        return cast(
            "GiftCardOperation",
            await self._request_async(
                "post",
                "/v1/gift_cards/{id}/void_operation".format(
                    id=sanitize_id(self._data.get("id"))
                ),
                params=params,
            ),
        )
