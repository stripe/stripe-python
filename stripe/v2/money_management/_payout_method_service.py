# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._payout_method_archive_params import (
        PayoutMethodArchiveParams,
    )
    from stripe.params.v2.money_management._payout_method_disable_params import (
        PayoutMethodDisableParams,
    )
    from stripe.params.v2.money_management._payout_method_list_params import (
        PayoutMethodListParams,
    )
    from stripe.params.v2.money_management._payout_method_retrieve_params import (
        PayoutMethodRetrieveParams,
    )
    from stripe.params.v2.money_management._payout_method_unarchive_params import (
        PayoutMethodUnarchiveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._payout_method import PayoutMethod


class PayoutMethodService(StripeService):
    def list(
        self,
        params: Optional["PayoutMethodListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PayoutMethod]":
        """
        List objects that adhere to the PayoutMethod interface.
        """
        return cast(
            "ListObject[PayoutMethod]",
            self._request(
                "get",
                "/v2/money_management/payout_methods",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["PayoutMethodListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PayoutMethod]":
        """
        List objects that adhere to the PayoutMethod interface.
        """
        return cast(
            "ListObject[PayoutMethod]",
            await self._request_async(
                "get",
                "/v2/money_management/payout_methods",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["PayoutMethodRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutMethod":
        """
        Retrieve a PayoutMethod object.
        """
        return cast(
            "PayoutMethod",
            self._request(
                "get",
                "/v2/money_management/payout_methods/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["PayoutMethodRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutMethod":
        """
        Retrieve a PayoutMethod object.
        """
        return cast(
            "PayoutMethod",
            await self._request_async(
                "get",
                "/v2/money_management/payout_methods/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def archive(
        self,
        id: str,
        /,
        params: Optional["PayoutMethodArchiveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutMethod":
        """
        Archive a `PayoutMethod`. Archiving prevents the Payout Method from being used for outbound payments
        or transfers and omits it from normal list results. To restore list visibility, use the
        [unarchive endpoint](https://docs.stripe.com/api/v2/money-management/payout-methods/unarchive).
        """
        return cast(
            "PayoutMethod",
            self._request(
                "post",
                "/v2/money_management/payout_methods/{id}/archive".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def archive_async(
        self,
        id: str,
        /,
        params: Optional["PayoutMethodArchiveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutMethod":
        """
        Archive a `PayoutMethod`. Archiving prevents the Payout Method from being used for outbound payments
        or transfers and omits it from normal list results. To restore list visibility, use the
        [unarchive endpoint](https://docs.stripe.com/api/v2/money-management/payout-methods/unarchive).
        """
        return cast(
            "PayoutMethod",
            await self._request_async(
                "post",
                "/v2/money_management/payout_methods/{id}/archive".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def disable(
        self,
        id: str,
        /,
        params: Optional["PayoutMethodDisableParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutMethod":
        """
        Disable a `PayoutMethod`. Disabling temporarily prevents the Payout Method from being used for outbound
        payments or transfers while keeping it in normal list results. To re-enable it, complete setup again by
        [creating an Outbound Setup Intent](https://docs.stripe.com/api/v2/money-management/outbound-setup-intents/create).
        """
        return cast(
            "PayoutMethod",
            self._request(
                "post",
                "/v2/money_management/payout_methods/{id}/disable".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def disable_async(
        self,
        id: str,
        /,
        params: Optional["PayoutMethodDisableParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutMethod":
        """
        Disable a `PayoutMethod`. Disabling temporarily prevents the Payout Method from being used for outbound
        payments or transfers while keeping it in normal list results. To re-enable it, complete setup again by
        [creating an Outbound Setup Intent](https://docs.stripe.com/api/v2/money-management/outbound-setup-intents/create).
        """
        return cast(
            "PayoutMethod",
            await self._request_async(
                "post",
                "/v2/money_management/payout_methods/{id}/disable".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def unarchive(
        self,
        id: str,
        /,
        params: Optional["PayoutMethodUnarchiveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutMethod":
        """
        Unarchive a `PayoutMethod`. Unarchiving restores the Payout Method to normal list results and clears
        only its archived state. It doesn't guarantee that the Payout Method can be used.
        """
        return cast(
            "PayoutMethod",
            self._request(
                "post",
                "/v2/money_management/payout_methods/{id}/unarchive".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def unarchive_async(
        self,
        id: str,
        /,
        params: Optional["PayoutMethodUnarchiveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutMethod":
        """
        Unarchive a `PayoutMethod`. Unarchiving restores the Payout Method to normal list results and clears
        only its archived state. It doesn't guarantee that the Payout Method can be used.
        """
        return cast(
            "PayoutMethod",
            await self._request_async(
                "post",
                "/v2/money_management/payout_methods/{id}/unarchive".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
