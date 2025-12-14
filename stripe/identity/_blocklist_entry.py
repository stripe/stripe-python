# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, Optional, cast, overload
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.identity._verification_report import VerificationReport
    from stripe.identity._verification_session import VerificationSession
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


class BlocklistEntry(
    CreateableAPIResource["BlocklistEntry"],
    ListableAPIResource["BlocklistEntry"],
):
    """
    A BlocklistEntry represents an entry in our identity verification blocklist.
    It helps prevent fraudulent users from repeatedly attempting verification with similar information.
    When you create a BlocklistEntry, we store data from a specified VerificationReport,
    such as document details or facial biometrics.
    This allows us to compare future verification attempts against these entries.
    If a match is found, we categorize the new verification as unverified.

    To learn more, see [Identity Verification Blocklist](https://docs.stripe.com/identity/review-tools#block-list)
    """

    OBJECT_NAME: ClassVar[Literal["identity.blocklist_entry"]] = (
        "identity.blocklist_entry"
    )
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    disabled_at: Optional[int]
    """
    Time at which you disabled the BlocklistEntry. Measured in seconds since the Unix epoch.
    """
    expires_at: Optional[int]
    """
    Time at which the BlocklistEntry expires. Measured in seconds since the Unix epoch.
    """
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["identity.blocklist_entry"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    status: Literal["active", "disabled", "redacted"]
    """
    The current status of the BlocklistEntry.
    """
    type: Literal["document", "selfie"]
    """
    The type of BlocklistEntry.
    """
    verification_report: Optional[ExpandableField["VerificationReport"]]
    """
    The verification report the BlocklistEntry was created from.
    """
    verification_session: Optional[ExpandableField["VerificationSession"]]
    """
    The verification session the BlocklistEntry was created from.
    """

    @classmethod
    def create(
        cls, **params: Unpack["BlocklistEntryCreateParams"]
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
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["BlocklistEntryCreateParams"]
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
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def _cls_disable(
        cls, id: str, **params: Unpack["BlocklistEntryDisableParams"]
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
            cls._static_request(
                "post",
                "/v1/identity/blocklist_entries/{id}/disable".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def disable(
        id: str, **params: Unpack["BlocklistEntryDisableParams"]
    ) -> "BlocklistEntry":
        """
        Disables a BlocklistEntry object.

        After a BlocklistEntry is disabled, it will no longer block future verifications that match
        the same information. This action is irreversible. To re-enable it, a new BlocklistEntry
        must be created using the same verification report.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#disable-a-blocklist-entry)
        """
        ...

    @overload
    def disable(
        self, **params: Unpack["BlocklistEntryDisableParams"]
    ) -> "BlocklistEntry":
        """
        Disables a BlocklistEntry object.

        After a BlocklistEntry is disabled, it will no longer block future verifications that match
        the same information. This action is irreversible. To re-enable it, a new BlocklistEntry
        must be created using the same verification report.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#disable-a-blocklist-entry)
        """
        ...

    @class_method_variant("_cls_disable")
    def disable(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["BlocklistEntryDisableParams"]
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
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_disable_async(
        cls, id: str, **params: Unpack["BlocklistEntryDisableParams"]
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
            await cls._static_request_async(
                "post",
                "/v1/identity/blocklist_entries/{id}/disable".format(
                    id=sanitize_id(id)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def disable_async(
        id: str, **params: Unpack["BlocklistEntryDisableParams"]
    ) -> "BlocklistEntry":
        """
        Disables a BlocklistEntry object.

        After a BlocklistEntry is disabled, it will no longer block future verifications that match
        the same information. This action is irreversible. To re-enable it, a new BlocklistEntry
        must be created using the same verification report.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#disable-a-blocklist-entry)
        """
        ...

    @overload
    async def disable_async(
        self, **params: Unpack["BlocklistEntryDisableParams"]
    ) -> "BlocklistEntry":
        """
        Disables a BlocklistEntry object.

        After a BlocklistEntry is disabled, it will no longer block future verifications that match
        the same information. This action is irreversible. To re-enable it, a new BlocklistEntry
        must be created using the same verification report.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#disable-a-blocklist-entry)
        """
        ...

    @class_method_variant("_cls_disable_async")
    async def disable_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["BlocklistEntryDisableParams"]
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
                    id=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["BlocklistEntryListParams"]
    ) -> ListObject["BlocklistEntry"]:
        """
        Returns a list of BlocklistEntry objects associated with your account.

        The blocklist entries are returned sorted by creation date, with the most recently created
        entries appearing first.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#block-list)
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
        cls, **params: Unpack["BlocklistEntryListParams"]
    ) -> ListObject["BlocklistEntry"]:
        """
        Returns a list of BlocklistEntry objects associated with your account.

        The blocklist entries are returned sorted by creation date, with the most recently created
        entries appearing first.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#block-list)
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
        cls, id: str, **params: Unpack["BlocklistEntryRetrieveParams"]
    ) -> "BlocklistEntry":
        """
        Retrieves a BlocklistEntry object by its identifier.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#block-list)
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["BlocklistEntryRetrieveParams"]
    ) -> "BlocklistEntry":
        """
        Retrieves a BlocklistEntry object by its identifier.

        Related guide: [Identity Verification Blocklist](https://docs.stripe.com/docs/identity/review-tools#block-list)
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def class_url(cls):
        return "/v1/identity/blocklist_entries"
