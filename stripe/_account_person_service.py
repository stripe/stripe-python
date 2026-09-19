# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._person import Person
    from stripe._request_options import RequestOptions
    from stripe.params._account_person_create_params import (
        AccountPersonCreateParams,
    )
    from stripe.params._account_person_delete_params import (
        AccountPersonDeleteParams,
    )
    from stripe.params._account_person_list_params import (
        AccountPersonListParams,
    )
    from stripe.params._account_person_retrieve_params import (
        AccountPersonRetrieveParams,
    )
    from stripe.params._account_person_update_params import (
        AccountPersonUpdateParams,
    )


class AccountPersonService(StripeService):
    def delete(
        self,
        account_id: str,
        id: str,
        /,
        params: Optional["AccountPersonDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Person":
        """
        Deletes an existing person's relationship to the account's legal entity. Any person with a relationship for an account can be deleted through the API, except if the person is the representative. If your integration is using the executive parameter, you cannot delete the only verified executive on file.
        """
        return cast(
            "Person",
            self._request(
                "delete",
                "/v1/accounts/{account_id}/persons/{id}".format(
                    account_id=sanitize_id(account_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def delete_async(
        self,
        account_id: str,
        id: str,
        /,
        params: Optional["AccountPersonDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Person":
        """
        Deletes an existing person's relationship to the account's legal entity. Any person with a relationship for an account can be deleted through the API, except if the person is the representative. If your integration is using the executive parameter, you cannot delete the only verified executive on file.
        """
        return cast(
            "Person",
            await self._request_async(
                "delete",
                "/v1/accounts/{account_id}/persons/{id}".format(
                    account_id=sanitize_id(account_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        account_id: str,
        id: str,
        /,
        params: Optional["AccountPersonRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Person":
        """
        Retrieves an existing person.
        """
        return cast(
            "Person",
            self._request(
                "get",
                "/v1/accounts/{account_id}/persons/{id}".format(
                    account_id=sanitize_id(account_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        account_id: str,
        id: str,
        /,
        params: Optional["AccountPersonRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Person":
        """
        Retrieves an existing person.
        """
        return cast(
            "Person",
            await self._request_async(
                "get",
                "/v1/accounts/{account_id}/persons/{id}".format(
                    account_id=sanitize_id(account_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        account_id: str,
        id: str,
        /,
        params: Optional["AccountPersonUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Person":
        """
        Updates an existing person.
        """
        return cast(
            "Person",
            self._request(
                "post",
                "/v1/accounts/{account_id}/persons/{id}".format(
                    account_id=sanitize_id(account_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        account_id: str,
        id: str,
        /,
        params: Optional["AccountPersonUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Person":
        """
        Updates an existing person.
        """
        return cast(
            "Person",
            await self._request_async(
                "post",
                "/v1/accounts/{account_id}/persons/{id}".format(
                    account_id=sanitize_id(account_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def list(
        self,
        id: str,
        /,
        params: Optional["AccountPersonListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Person]":
        """
        Returns a list of people associated with the account's legal entity. The people are returned sorted by creation date, with the most recent people appearing first.
        """
        return cast(
            "ListObject[Person]",
            self._request(
                "get",
                "/v1/accounts/{id}/persons".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        id: str,
        /,
        params: Optional["AccountPersonListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Person]":
        """
        Returns a list of people associated with the account's legal entity. The people are returned sorted by creation date, with the most recent people appearing first.
        """
        return cast(
            "ListObject[Person]",
            await self._request_async(
                "get",
                "/v1/accounts/{id}/persons".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        id: str,
        /,
        params: Optional["AccountPersonCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Person":
        """
        Creates a new person.
        """
        return cast(
            "Person",
            self._request(
                "post",
                "/v1/accounts/{id}/persons".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        id: str,
        /,
        params: Optional["AccountPersonCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Person":
        """
        Creates a new person.
        """
        return cast(
            "Person",
            await self._request_async(
                "post",
                "/v1/accounts/{id}/persons".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
