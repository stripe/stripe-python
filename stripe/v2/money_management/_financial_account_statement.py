# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Optional
from typing_extensions import Literal


class FinancialAccountStatement(StripeObject):
    """
    A Financial Account Statement represents a monthly statement for a Financial Account.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.financial_account_statement"]
    ] = "v2.money_management.financial_account_statement"

    class FilesByCurrency(StripeObject):
        class DownloadUrl(StripeObject):
            expires_at: str
            """
            The time at which the URL expires, in ISO 8601 format (UTC).
            """
            url: str
            """
            The URL to download the file.
            """

        content_type: str
        """
        The MIME type of the file.
        """
        download_url: DownloadUrl
        """
        The download URL and expiration.
        """
        size: int
        """
        The size of the file in bytes.
        """
        _inner_class_types = {"download_url": DownloadUrl}
        _field_encodings = {"size": "int64_string"}

    class Period(StripeObject):
        end_date: str
        """
        The end of the statement period (inclusive), as a UTC-aligned ISO 8601 date
        (e.g., "2026-05-31"). For example, a May 2026 statement has end_date "2026-05-31",
        meaning all transactions up to and including May 31st UTC are included.
        """
        start_date: str
        """
        The start of the statement period (inclusive), as a UTC-aligned ISO 8601 date (e.g., "2026-05-01").
        """

    created: str
    """
    Time at which the statement was created, in ISO 8601 format (UTC).
    """
    ending_balance: UntypedStripeObject[Amount]
    """
    Available balance at the end of the statement period.
    """
    files_by_currency: Optional[UntypedStripeObject[FilesByCurrency]]
    """
    Currency-specific files and file metadata. Null by default, populated by specifying include=files_by_currency in the Retrieve endpoint.
    """
    financial_account: str
    """
    The Financial Account this statement belongs to.
    """
    id: str
    """
    Unique identifier for the statement.
    """
    livemode: bool
    """
    True if the object exists in live mode, false if in test mode.
    """
    object: Literal["v2.money_management.financial_account_statement"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    period: Period
    """
    The time period covered by this statement.
    """
    restated_by: Optional[str]
    """
    The ID of the statement that replaced this one. Only present on statements that have been restated.
    """
    restated_statement: Optional[str]
    """
    The ID of the statement this one replaces. Only present on restatements.
    """
    starting_balance: UntypedStripeObject[Amount]
    """
    Available balance at the start of the statement period.
    """
    status: Literal["active", "restated"]
    """
    The status of the statement. A statement is "active" by default.
    When a statement is replaced by a restatement, its status becomes "restated".
    """
    _inner_class_types = {
        "files_by_currency": FilesByCurrency,
        "period": Period,
    }
