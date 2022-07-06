# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import error
from stripe import util
from stripe.api_resources import Customer
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods
from stripe.six.moves.urllib.parse import quote_plus


@nested_resource_class_methods("source_transaction", operations=["list"])
class Source(CreateableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "source"

    @classmethod
    def _cls_verify(
        cls,
        source,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/sources/{source}/verify".format(
                source=util.sanitize_id(source)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_verify")
    def verify(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/sources/{source}/verify".format(
                source=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    def detach(self, idempotency_key=None, **params):
        token = util.utf8(self.id)

        if hasattr(self, "customer") and self.customer:
            extn = quote_plus(token)
            customer = util.utf8(self.customer)
            base = Customer.class_url()
            owner_extn = quote_plus(customer)
            url = "%s/%s/sources/%s" % (base, owner_extn, extn)
            headers = util.populate_headers(idempotency_key)

            self.refresh_from(self.request("delete", url, params, headers))
            return self

        else:
            raise error.InvalidRequestError(
                "Source %s does not appear to be currently attached "
                "to a customer object." % token,
                "id",
            )

    def source_transactions(self, **params):
        """source_transactions is deprecated, use Source.list_source_transactions instead."""
        return self.request(
            "get", self.instance_url() + "/source_transactions", params
        )
