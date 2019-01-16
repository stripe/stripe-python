from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract.api_resource import APIResource


class DeletableAPIResource(APIResource):
    def delete(self, **params):
        self.refresh_from(self.request("delete", self.instance_url(), params))
        return self
