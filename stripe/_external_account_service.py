# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._bank_account import BankAccount
from stripe._card import Card
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Dict, List, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict


class ExternalAccountService(StripeService):
    class CreateParams(TypedDict):
        default_for_currency: NotRequired[bool]
        """
        When set to true, or if this is the first external account added in this currency, this account becomes the default external account for its currency.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        external_account: str
        """
        Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's external account details (with the options shown below).
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """

    class DeleteParams(TypedDict):
        pass

    class ListParams(TypedDict):
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        object: NotRequired[Literal["bank_account", "card"]]
        """
        Filter external accounts according to a particular object type.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
        account_holder_name: NotRequired[str]
        """
        The name of the person or business that owns the bank account.
        """
        account_holder_type: NotRequired[
            "Literal['']|Literal['company', 'individual']"
        ]
        """
        The type of entity that holds the account. This can be either `individual` or `company`.
        """
        account_type: NotRequired[
            Literal["checking", "futsu", "savings", "toza"]
        ]
        """
        The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`.
        """
        address_city: NotRequired[str]
        """
        City/District/Suburb/Town/Village.
        """
        address_country: NotRequired[str]
        """
        Billing address country, if provided when creating card.
        """
        address_line1: NotRequired[str]
        """
        Address line 1 (Street address/PO Box/Company name).
        """
        address_line2: NotRequired[str]
        """
        Address line 2 (Apartment/Suite/Unit/Building).
        """
        address_state: NotRequired[str]
        """
        State/County/Province/Region.
        """
        address_zip: NotRequired[str]
        """
        ZIP or postal code.
        """
        default_for_currency: NotRequired[bool]
        """
        When set to true, this becomes the default external account for its currency.
        """
        documents: NotRequired["ExternalAccountService.UpdateParamsDocuments"]
        """
        Documents that may be submitted to satisfy various informational requests.
        """
        exp_month: NotRequired[str]
        """
        Two digit number representing the card's expiration month.
        """
        exp_year: NotRequired[str]
        """
        Four digit number representing the card's expiration year.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        name: NotRequired[str]
        """
        Cardholder name.
        """

    class UpdateParamsDocuments(TypedDict):
        bank_account_ownership_verification: NotRequired[
            "ExternalAccountService.UpdateParamsDocumentsBankAccountOwnershipVerification"
        ]
        """
        One or more documents that support the [Bank account ownership verification](https://support.stripe.com/questions/bank-account-ownership-verification) requirement. Must be a document associated with the bank account that displays the last 4 digits of the account number, either a statement or a check.
        """

    class UpdateParamsDocumentsBankAccountOwnershipVerification(TypedDict):
        files: NotRequired[List[str]]
        """
        One or more document ids returned by a [file upload](https://stripe.com/docs/api#create_file) with a `purpose` value of `account_requirement`.
        """

    def delete(
        self,
        id: str,
        params: "ExternalAccountService.DeleteParams" = {},
        options: RequestOptions = {},
    ) -> Union[BankAccount, Card]:
        """
        Delete a specified external account for a given account.
        """
        return cast(
            Union[BankAccount, Card],
            self._request(
                "delete",
                "/v1/external_accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def delete_async(
        self,
        id: str,
        params: "ExternalAccountService.DeleteParams" = {},
        options: RequestOptions = {},
    ) -> Union[BankAccount, Card]:
        """
        Delete a specified external account for a given account.
        """
        return cast(
            Union[BankAccount, Card],
            await self._request_async(
                "delete",
                "/v1/external_accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "ExternalAccountService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Union[BankAccount, Card]:
        """
        Retrieve a specified external account for a given account.
        """
        return cast(
            Union[BankAccount, Card],
            self._request(
                "get",
                "/v1/external_accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "ExternalAccountService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Union[BankAccount, Card]:
        """
        Retrieve a specified external account for a given account.
        """
        return cast(
            Union[BankAccount, Card],
            await self._request_async(
                "get",
                "/v1/external_accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "ExternalAccountService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Union[BankAccount, Card]:
        """
        Updates the metadata, account holder name, account holder type of a bank account belonging to
        a connected account and optionally sets it as the default for its currency. Other bank account
        details are not editable by design.

        You can only update bank accounts when [account.controller.requirement_collection is application, which includes <a href="/connect/custom-accounts">Custom accounts](https://stripe.com/api/accounts/object#account_object-controller-requirement_collection).

        You can re-enable a disabled bank account by performing an update call without providing any
        arguments or changes.
        """
        return cast(
            Union[BankAccount, Card],
            self._request(
                "post",
                "/v1/external_accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "ExternalAccountService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Union[BankAccount, Card]:
        """
        Updates the metadata, account holder name, account holder type of a bank account belonging to
        a connected account and optionally sets it as the default for its currency. Other bank account
        details are not editable by design.

        You can only update bank accounts when [account.controller.requirement_collection is application, which includes <a href="/connect/custom-accounts">Custom accounts](https://stripe.com/api/accounts/object#account_object-controller-requirement_collection).

        You can re-enable a disabled bank account by performing an update call without providing any
        arguments or changes.
        """
        return cast(
            Union[BankAccount, Card],
            await self._request_async(
                "post",
                "/v1/external_accounts/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def list(
        self,
        params: "ExternalAccountService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Union[BankAccount, Card]]:
        """
        List external accounts for an account.
        """
        return cast(
            ListObject[Union[BankAccount, Card]],
            self._request(
                "get",
                "/v1/external_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "ExternalAccountService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Union[BankAccount, Card]]:
        """
        List external accounts for an account.
        """
        return cast(
            ListObject[Union[BankAccount, Card]],
            await self._request_async(
                "get",
                "/v1/external_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "ExternalAccountService.CreateParams",
        options: RequestOptions = {},
    ) -> Union[BankAccount, Card]:
        """
        Create an external account for a given connected account.
        """
        return cast(
            Union[BankAccount, Card],
            self._request(
                "post",
                "/v1/external_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ExternalAccountService.CreateParams",
        options: RequestOptions = {},
    ) -> Union[BankAccount, Card]:
        """
        Create an external account for a given connected account.
        """
        return cast(
            Union[BankAccount, Card],
            await self._request_async(
                "post",
                "/v1/external_accounts",
                base_address="api",
                params=params,
                options=options,
            ),
        )
