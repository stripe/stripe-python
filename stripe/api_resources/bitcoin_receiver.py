import urllib

from stripe import util
from stripe.api_resources.customer import Customer
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource


class BitcoinReceiver(CreateableAPIResource, UpdateableAPIResource,
                      DeletableAPIResource, ListableAPIResource):
    OBJECT_NAME = 'bitcoin_receiver'

    def instance_url(self):
        token = util.utf8(self.id)
        extn = urllib.quote_plus(token)

        if hasattr(self, 'customer'):
            customer = util.utf8(self.customer)
            base = Customer.class_url()
            cust_extn = urllib.quote_plus(customer)
            return "%s/%s/sources/%s" % (base, cust_extn, extn)
        else:
            base = BitcoinReceiver.class_url()
            return "%s/%s" % (base, extn)

    @classmethod
    def class_url(cls):
        return '/v1/bitcoin/receivers'
