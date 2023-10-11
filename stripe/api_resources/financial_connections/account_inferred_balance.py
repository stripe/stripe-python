# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.list_object import ListObject
from typing import Any, Dict, Optional
from typing_extensions import Literal


class AccountInferredBalance(ListableAPIResource["AccountInferredBalance"]):
    """
    A historical balance for the account on a particular day. It may be sourced from a balance snapshot provided by a financial institution, or inferred using transactions data.
    """

    OBJECT_NAME = "financial_connections.account_inferred_balance"
    as_of: int
    current: Dict[str, int]
    id: str
    object: Literal["financial_connections.account_inferred_balance"]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["AccountInferredBalance"]:
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
