from __future__ import absolute_import, division, print_function


class VerifyMixin(object):
    def verify(self, idempotency_key=None, **params):
        url = self.instance_url() + "/verify"
        return self._request(
            "post", url, idempotency_key=idempotency_key, params=params
        )
