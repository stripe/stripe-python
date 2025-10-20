# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.identity._blocklist_entry import BlocklistEntry
    from stripe.params.identity._blocklist_entry_create_params import (
        BlocklistEntryCreateParams,
    )
    from stripe.params.identity._blocklist_entry_disable_params import (
        BlocklistEntryDisableParams,
    )
    from stripe.params.identity._blocklist_entry_list_params import (
        BlocklistEntryListParams,
    )
    from stripe.params.identity._blocklist_entry_retrieve_params import (
        BlocklistEntryRetrieveParams,
    )


class BlocklistEntryService(StripeService):
    def list(
        self,
        params: Optional["BlocklistEntryListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[BlocklistEntry]":
        """
        Returns a list of BlocklistEntry objects associated with your account.

        The blocklist entries are returned sorted by creation date, with the most recently created
        entries appearing first.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#block-list)
        """
        return cast(
            "ListObject[BlocklistEntry]",
            self._request(
                "get",
                "/v1/identity/blocklist_entries",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["BlocklistEntryListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[BlocklistEntry]":
        """
        Returns a list of BlocklistEntry objects associated with your account.

        The blocklist entries are returned sorted by creation date, with the most recently created
        entries appearing first.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#block-list)
        """
        return cast(
            "ListObject[BlocklistEntry]",
            await self._request_async(
                "get",
                "/v1/identity/blocklist_entries",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "BlocklistEntryCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "BlocklistEntry":
        """
        Creates a BlocklistEntry object from a verification report.

        A blocklist entry prevents future identity verifications that match the same identity information.
        You can create blocklist entries from verification reports that contain document extracted data
        or a selfie.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#add-a-blocklist-entry)
        """
        return cast(
            "BlocklistEntry",
            self._request(
                "post",
                "/v1/identity/blocklist_entries",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "BlocklistEntryCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "BlocklistEntry":
        """
        Creates a BlocklistEntry object from a verification report.

        A blocklist entry prevents future identity verifications that match the same identity information.
        You can create blocklist entries from verification reports that contain document extracted data
        or a selfie.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#add-a-blocklist-entry)
        """
        return cast(
            "BlocklistEntry",
            await self._request_async(
                "post",
                "/v1/identity/blocklist_entries",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["BlocklistEntryRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "BlocklistEntry":
        """
        Retrieves a BlocklistEntry object by its identifier.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#block-list)
        """
        return cast(
            "BlocklistEntry",
            self._request(
                "get",
                "/v1/identity/blocklist_entries/{id}".format(
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
        params: Optional["BlocklistEntryRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "BlocklistEntry":
        """
        Retrieves a BlocklistEntry object by its identifier.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#block-list)
        """
        return cast(
            "BlocklistEntry",
            await self._request_async(
                "get",
                "/v1/identity/blocklist_entries/{id}".format(
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
        params: Optional["BlocklistEntryDisableParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "BlocklistEntry":
        """
        Disables a BlocklistEntry object.

        After a BlocklistEntry is disabled, it will no longer block future verifications that match
        the same information. This action is irreversible. To re-enable it, a new BlocklistEntry
        must be created using the same verification report.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#disable-a-blocklist-entry)
        """
        return cast(
            "BlocklistEntry",
            self._request(
                "post",
                "/v1/identity/blocklist_entries/{id}/disable".format(
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
        params: Optional["BlocklistEntryDisableParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "BlocklistEntry":
        """
        Disables a BlocklistEntry object.

        After a BlocklistEntry is disabled, it will no longer block future verifications that match
        the same information. This action is irreversible. To re-enable it, a new BlocklistEntry
        must be created using the same verification report.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#disable-a-blocklist-entry)
        """
        return cast(
            "BlocklistEntry",
            await self._request_async(
                "post",
                "/v1/identity/blocklist_entries/{id}/disable".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
