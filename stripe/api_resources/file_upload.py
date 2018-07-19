from __future__ import absolute_import, division, print_function

import stripe
from stripe import api_requestor, util
from stripe.api_resources.abstract import ListableAPIResource


class FileUpload(ListableAPIResource):
    OBJECT_NAME = 'file_upload'

    @classmethod
    def api_base(cls):
        return stripe.upload_api_base

    @classmethod
    def class_url(cls):
        return '/v1/files'

    @classmethod
    def create(cls, api_key=None, api_version=None, stripe_account=None,
               **params):
        requestor = api_requestor.APIRequestor(
            api_key, api_base=cls.api_base(), api_version=api_version,
            account=stripe_account)
        url = cls.class_url()
        supplied_headers = {
            "Content-Type": "multipart/form-data"
        }
        response, api_key = requestor.request(
            'post', url, params=params, headers=supplied_headers)
        return util.convert_to_stripe_object(response, api_key, api_version,
                                             stripe_account)
