from __future__ import absolute_import, division, print_function

from stripe import api_requestor, util
from stripe.api_resources.abstract.api_resource import APIResource
from stripe.six.moves.urllib.parse import quote_plus


class DeletableAPIResource(APIResource):

    @classmethod
    def _remove(cls, url, api_key=None, stripe_version=None,
                stripe_account=None, **params):
        requestor = api_requestor.APIRequestor(api_key,
                                               api_version=stripe_version,
                                               account=stripe_account)
        response, api_key = requestor.request('delete', url, params)
        return util.convert_to_stripe_object(response, api_key, stripe_version,
                                             stripe_account)

    @classmethod
    def remove(cls, sid, **params):
        url = "%s/%s" % (cls.class_url(), quote_plus(util.utf8(sid)))
        return cls._remove(url, **params)

    def delete(self, **params):
        self.refresh_from(self.request('delete', self.instance_url(), params))
        return self
