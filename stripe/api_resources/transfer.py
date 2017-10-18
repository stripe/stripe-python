from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods('reversal', operations=['create', 'retrieve',
                                                       'update', 'list'])
class Transfer(CreateableAPIResource, UpdateableAPIResource,
               ListableAPIResource):
    OBJECT_NAME = 'transfer'

    def cancel(self):
        self.refresh_from(self.request('post',
                          self.instance_url() + '/cancel'))
