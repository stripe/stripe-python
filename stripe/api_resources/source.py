from __future__ import absolute_import, division, print_function

import warnings

from stripe import util
from stripe.api_resources import Customer
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import VerifyMixin
from stripe.six.moves.urllib.parse import quote_plus


class Source(CreateableAPIResource, UpdateableAPIResource, VerifyMixin):
    OBJECT_NAME = 'source'

    def detach(self, idempotency_key=None, **params):
        if hasattr(self, 'customer') and self.customer:
            extn = quote_plus(util.utf8(self.id))
            customer = util.utf8(self.customer)
            base = Customer.class_url()
            owner_extn = quote_plus(customer)
            url = "%s/%s/sources/%s" % (base, owner_extn, extn)
            headers = util.populate_headers(idempotency_key)

            self.refresh_from(self.request('delete', url, params, headers))
            return self

        else:
            raise NotImplementedError(
                "This source object does not appear to be currently attached "
                "to a customer object.")

    def delete(self, **params):
        warnings.warn("The `Source.delete` method is deprecated and will "
                      "be removed in future versions. Please use the "
                      "`Source.detach` method instead",
                      DeprecationWarning)
        self.detach(**params)

    def source_transactions(self, **params):
        return self.request(
            'get', self.instance_url() + '/source_transactions', params)
