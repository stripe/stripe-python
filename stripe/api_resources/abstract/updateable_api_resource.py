from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract.api_resource import APIResource
from urllib.parse import quote_plus


class UpdateableAPIResource(APIResource):
    @classmethod
    def modify(cls, sid, **params):
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))

        def _format_values(original_data):
            '''
            Local function that will format the params before passing them to the API 
            this is done do users can input an empyt list and it will be sent as ''
            '''
            new_dict = {}

            for current_key, current_value in original_data.items():
                if isinstance(current_value, dict):
                    new_dict[current_key] = _format_values(current_value)
                elif isinstance(current_value, list) and len(current_value) == 0:
                    #if we are given an empty list
                    new_dict[current_key] = ""
                else:
                    #if we are at the end of the search add the value as is 
                    new_dict[current_key] = current_value

            return new_dict

        return cls._static_request("post", url, params=_format_values(params))

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
