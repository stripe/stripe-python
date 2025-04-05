# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TYPE_CHECKING
from warnings import warn

warn(
    """
    The stripe.api_resources.privacy.redaction_job package is deprecated, please change your
    imports to import from stripe.privacy directly.
    From:
      from stripe.api_resources.privacy.redaction_job import RedactionJob
    To:
      from stripe.privacy import RedactionJob
    """,
    DeprecationWarning,
    stacklevel=2,
)
if not TYPE_CHECKING:
    from stripe.privacy._redaction_job import (  # noqa
        RedactionJob,
    )
