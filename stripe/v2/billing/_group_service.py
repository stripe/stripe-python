# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._encode import _coerce_v2_params
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing._group_cancel_params import GroupCancelParams
    from stripe.params.v2.billing._group_create_params import GroupCreateParams
    from stripe.params.v2.billing._group_list_params import GroupListParams
    from stripe.params.v2.billing._group_retrieve_params import (
        GroupRetrieveParams,
    )
    from stripe.params.v2.billing._group_update_params import GroupUpdateParams
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._group import Group
    from stripe.v2.billing.groups._invoice_service import InvoiceService
    from stripe.v2.billing.groups._spend_modifier_rule_service import (
        SpendModifierRuleService,
    )

_subservices = {
    "invoices": [
        "stripe.v2.billing.groups._invoice_service",
        "InvoiceService",
    ],
    "spend_modifier_rules": [
        "stripe.v2.billing.groups._spend_modifier_rule_service",
        "SpendModifierRuleService",
    ],
}


class GroupService(StripeService):
    invoices: "InvoiceService"
    spend_modifier_rules: "SpendModifierRuleService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()

    def list(
        self,
        params: Optional["GroupListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Group]":
        """
        List Billing Groups.
        """
        return cast(
            "ListObject[Group]",
            self._request(
                "get",
                "/v2/billing/groups",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["GroupListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Group]":
        """
        List Billing Groups.
        """
        return cast(
            "ListObject[Group]",
            await self._request_async(
                "get",
                "/v2/billing/groups",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "GroupCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Group":
        """
        Create a BillingGroup.
        """
        return cast(
            "Group",
            self._request(
                "post",
                "/v2/billing/groups",
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {
                        "billing_settings": {
                            "payment_method_options": {
                                "card": {
                                    "mandate_options": {
                                        "amount": "int64_string",
                                    },
                                },
                            },
                        },
                    },
                ),
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "GroupCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Group":
        """
        Create a BillingGroup.
        """
        return cast(
            "Group",
            await self._request_async(
                "post",
                "/v2/billing/groups",
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {
                        "billing_settings": {
                            "payment_method_options": {
                                "card": {
                                    "mandate_options": {
                                        "amount": "int64_string",
                                    },
                                },
                            },
                        },
                    },
                ),
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["GroupRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Group":
        """
        Retrieve a BillingGroup.
        """
        return cast(
            "Group",
            self._request(
                "get",
                "/v2/billing/groups/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["GroupRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Group":
        """
        Retrieve a BillingGroup.
        """
        return cast(
            "Group",
            await self._request_async(
                "get",
                "/v2/billing/groups/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        /,
        params: Optional["GroupUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Group":
        """
        Update a BillingGroup.
        """
        return cast(
            "Group",
            self._request(
                "post",
                "/v2/billing/groups/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {
                        "billing_settings": {
                            "payment_method_options": {
                                "card": {
                                    "mandate_options": {
                                        "amount": "int64_string",
                                    },
                                },
                            },
                        },
                    },
                ),
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        /,
        params: Optional["GroupUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Group":
        """
        Update a BillingGroup.
        """
        return cast(
            "Group",
            await self._request_async(
                "post",
                "/v2/billing/groups/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {
                        "billing_settings": {
                            "payment_method_options": {
                                "card": {
                                    "mandate_options": {
                                        "amount": "int64_string",
                                    },
                                },
                            },
                        },
                    },
                ),
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        /,
        params: Optional["GroupCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Group":
        """
        Cancel a BillingGroup.
        """
        return cast(
            "Group",
            self._request(
                "post",
                "/v2/billing/groups/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        /,
        params: Optional["GroupCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Group":
        """
        Cancel a BillingGroup.
        """
        return cast(
            "Group",
            await self._request_async(
                "post",
                "/v2/billing/groups/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
