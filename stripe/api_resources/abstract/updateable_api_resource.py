from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract.api_resource import APIResource
from stripe.six.moves.urllib.parse import quote_plus


class UpdateableAPIResource(APIResource):
    @classmethod
    def modify(cls, sid, **params):
        url = "%s/%s" % (cls.class_url(), quote_plus(util.utf8(sid)))
        return cls._static_request("post", url, params=params)

    def save(self, idempotency_key=None):
        """
        The `save` method is deprecated and will be removed in a future major version of the library.

        Use the class method `modify` on the resource instead.
        """
        updated_params = self.serialize(None)
        if updated_params:
            self._request_and_refresh(
                "post",
                self.instance_url(),
                idempotency_key=idempotency_key,
                params=updated_params,
            )
        else:
            util.logger.debug("Trying to save already saved object %r", self)
        return self
