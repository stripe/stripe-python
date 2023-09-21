# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import api_resources, oauth, util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
    nested_resource_class_methods,
)
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.person import Person


@nested_resource_class_methods("capability")
@nested_resource_class_methods("external_account")
@nested_resource_class_methods("login_link")
@nested_resource_class_methods("person")
class Account(
    CreateableAPIResource["Account"],
    DeletableAPIResource["Account"],
    ListableAPIResource["Account"],
    UpdateableAPIResource["Account"],
):
    """
    This is an object representing a Stripe account. You can retrieve it to see
    properties on the account like its current requirements or if the account is
    enabled to make live charges or receive payouts.

    For Custom accounts, the properties below are always returned. For other accounts, some properties are returned until that
    account has started to go through Connect Onboarding. Once you create an [Account Link](https://stripe.com/docs/api/account_links)
    for a Standard or Express account, some parameters are no longer returned. These are marked as **Custom Only** or **Custom and Express**
    below. Learn about the differences [between accounts](https://stripe.com/docs/connect/accounts).
    """

    OBJECT_NAME = "account"
    business_profile: Optional[StripeObject]
    business_type: Optional[
        Literal["company", "government_entity", "individual", "non_profit"]
    ]
    capabilities: Optional[StripeObject]
    charges_enabled: Optional[bool]
    company: Optional[StripeObject]
    controller: Optional[StripeObject]
    country: Optional[str]
    created: Optional[int]
    default_currency: Optional[str]
    details_submitted: Optional[bool]
    email: Optional[str]
    external_accounts: Optional[ListObject[Any]]
    future_requirements: Optional[StripeObject]
    id: str
    individual: Optional["Person"]
    metadata: Optional[Dict[str, str]]
    object: Literal["account"]
    payouts_enabled: Optional[bool]
    requirements: Optional[StripeObject]
    settings: Optional[StripeObject]
    tos_acceptance: Optional[StripeObject]
    type: Optional[Literal["custom", "express", "standard"]]
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "Account":
        return cast(
            "Account",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def _cls_delete(cls, sid: str, **params: Any) -> "Account":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Account",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Any) -> "Account":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["Account"]:
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

    @classmethod
    def _cls_persons(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/accounts/{account}/persons".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_persons")
    def persons(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "get",
            "/v1/accounts/{account}/persons".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_reject(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/accounts/{account}/reject".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_reject")
    def reject(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/accounts/{account}/reject".format(
                account=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    # We are not adding a helper for capabilities here as the Account object already has a
    # capabilities property which is a hash and not the sub-list of capabilities.

    @classmethod
    def retrieve(cls, id=None, api_key=None, **params):
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def modify(cls, id=None, **params):
        url = cls._build_instance_url(id)
        return cls._static_request("post", url, params=params)

    @classmethod
    def _build_instance_url(cls, sid):
        if not sid:
            return "/v1/account"
        base = cls.class_url()
        extn = quote_plus(sid)
        return "%s/%s" % (base, extn)

    def instance_url(self):
        return self._build_instance_url(self.get("id"))

    def deauthorize(self, **params):
        params["stripe_user_id"] = self.id
        return oauth.OAuth.deauthorize(**params)

    def serialize(self, previous):
        params = super(Account, self).serialize(previous)
        previous = previous or self._previous or {}

        for k, v in iter(self.items()):
            if (
                k == "individual"
                and isinstance(v, api_resources.Person)
                and k not in params
            ):
                params[k] = v.serialize(previous.get(k, None))

        return params

    @classmethod
    def retrieve_capability(
        cls,
        account: str,
        capability: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/accounts/{account}/capabilities/{capability}".format(
                account=util.sanitize_id(account),
                capability=util.sanitize_id(capability),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def modify_capability(
        cls,
        account: str,
        capability: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/accounts/{account}/capabilities/{capability}".format(
                account=util.sanitize_id(account),
                capability=util.sanitize_id(capability),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_capabilities(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/accounts/{account}/capabilities".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def create_external_account(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/accounts/{account}/external_accounts".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_external_account(
        cls,
        account: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/accounts/{account}/external_accounts/{id}".format(
                account=util.sanitize_id(account), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def modify_external_account(
        cls,
        account: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/accounts/{account}/external_accounts/{id}".format(
                account=util.sanitize_id(account), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def delete_external_account(
        cls,
        account: str,
        id: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "delete",
            "/v1/accounts/{account}/external_accounts/{id}".format(
                account=util.sanitize_id(account), id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_external_accounts(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/accounts/{account}/external_accounts".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def create_login_link(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/accounts/{account}/login_links".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def create_person(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/accounts/{account}/persons".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def retrieve_person(
        cls,
        account: str,
        person: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/accounts/{account}/persons/{person}".format(
                account=util.sanitize_id(account),
                person=util.sanitize_id(person),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def modify_person(
        cls,
        account: str,
        person: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/accounts/{account}/persons/{person}".format(
                account=util.sanitize_id(account),
                person=util.sanitize_id(person),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def delete_person(
        cls,
        account: str,
        person: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "delete",
            "/v1/accounts/{account}/persons/{person}".format(
                account=util.sanitize_id(account),
                person=util.sanitize_id(person),
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def list_persons(
        cls,
        account: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/accounts/{account}/persons".format(
                account=util.sanitize_id(account)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
