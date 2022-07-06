# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

import stripe
from stripe import oauth, six
from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import custom_method
from stripe.api_resources.abstract import nested_resource_class_methods
from stripe.six.moves.urllib.parse import quote_plus


@custom_method("persons", http_verb="get")
@custom_method("reject", http_verb="post")
@nested_resource_class_methods(
    "capability",
    operations=["retrieve", "update", "list"],
    resource_plural="capabilities",
)
@nested_resource_class_methods(
    "external_account",
    operations=["create", "retrieve", "update", "delete", "list"],
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
    OBJECT_NAME = "account"

    def persons(self, idempotency_key=None, **params):
        url = "/v1/accounts/{account}/persons".format(
            account=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        resp = self.request("get", url, params, headers)
        stripe_object = util.convert_to_stripe_object(resp)
        stripe_object._retrieve_params = params
        return stripe_object

    def reject(self, idempotency_key=None, **params):
        url = "/v1/accounts/{account}/reject".format(
            account=util.sanitize_id(self.get("id"))
        )
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

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
        return cls._static_request("post", url, **params)

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
