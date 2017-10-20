from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource


class Dispute(CreateableAPIResource, ListableAPIResource,
              UpdateableAPIResource):
    OBJECT_NAME = 'dispute'

    def close(self, idempotency_key=None):
        url = self.instance_url() + '/close'
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request('post', url, {}, headers))
        return self
