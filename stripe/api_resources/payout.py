from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource


class Payout(CreateableAPIResource, UpdateableAPIResource,
             ListableAPIResource):
    OBJECT_NAME = 'payout'

    def cancel(self):
        self.refresh_from(self.request('post',
                          self.instance_url() + '/cancel'))
