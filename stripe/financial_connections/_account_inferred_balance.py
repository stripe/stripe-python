# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from typing import ClassVar, Dict, List
from typing_extensions import Literal, NotRequired, Unpack


class AccountInferredBalance(ListableAPIResource["AccountInferredBalance"]):
    """
    A historical balance for the account on a particular day. It may be sourced from a balance snapshot provided by a financial institution, or inferred using transactions data.
    """

    OBJECT_NAME: ClassVar[
        Literal["financial_connections.account_inferred_balance"]
    ] = "financial_connections.account_inferred_balance"

    class ListParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    as_of: int
    """
    The time for which this balance was calculated, measured in seconds since the Unix epoch. If the balance was computed by Stripe and not provided directly by a financial institution, it will always be 23:59:59 UTC.
    """
    current: Dict[str, int]
    """
    The balances owed to (or by) the account holder.

    Each key is a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase.

    Each value is a integer amount. A positive amount indicates money owed to the account holder. A negative amount indicates money owed by the account holder.
    """
    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["financial_connections.account_inferred_balance"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """

    @classmethod
    def list(
        cls, **params: Unpack["AccountInferredBalance.ListParams"]
    ) -> ListObject["AccountInferredBalance"]:
        """
        Lists the recorded inferred balances for a Financial Connections Account.
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
        cls, **params: Unpack["AccountInferredBalance.ListParams"]
    ) -> ListObject["AccountInferredBalance"]:
        """
        Lists the recorded inferred balances for a Financial Connections Account.
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
