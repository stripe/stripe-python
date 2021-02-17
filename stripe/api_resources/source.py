# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import error
from stripe import util
from stripe.api_resources import Customer
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import VerifyMixin
from stripe.api_resources.abstract import nested_resource_class_methods
from urllib.parse import quote_plus


@nested_resource_class_methods("source_transaction", operations=["list"])
class Source(CreateableAPIResource, UpdateableAPIResource, VerifyMixin):
    OBJECT_NAME = "source"

    def detach(self, idempotency_key=None, **params):
        if hasattr(self, "customer") and self.customer:
            extn = quote_plus(self.id)
            base = Customer.class_url()
            owner_extn = quote_plus(self.customer)
            url = "%s/%s/sources/%s" % (base, owner_extn, extn)
            headers = util.populate_headers(idempotency_key)

            self.refresh_from(self.request("delete", url, params, headers))
            return self

        else:
            raise error.InvalidRequestError(
                "Source %s does not appear to be currently attached "
                "to a customer object." % self.id,
                "id",
            )

    def source_transactions(self, **params):
        """source_transactions is deprecated, use Source.list_source_transactions instead."""
        return self.request(
            "get", self.instance_url() + "/source_transactions", params
        )
