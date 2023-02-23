# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

import stripe
from stripe import oauth, six
from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods
from stripe.six.moves.urllib.parse import quote_plus


@nested_resource_class_methods(
    "external_account",
    operations=["create", "retrieve", "update", "delete", "list"],
)
@nested_resource_class_methods(
    "capability",
    operations=["retrieve", "update", "list"],
    resource_plural="capabilities",
)
@nested_resource_class_methods("login_link", operations=["create"])
@nested_resource_class_methods(
    "person",
    operations=["create", "retrieve", "update", "delete", "list"],
)
class Account(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
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

    @classmethod
    def _cls_persons(
        cls,
        account,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
    def persons(self, idempotency_key=None, **params):
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
        account,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
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
    def reject(self, idempotency_key=None, **params):
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
        sid = util.utf8(sid)
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

        for k, v in six.iteritems(self):
            if (
                k == "individual"
                and isinstance(v, stripe.api_resources.Person)
                and k not in params
            ):
                params[k] = v.serialize(previous.get(k, None))

        return params
