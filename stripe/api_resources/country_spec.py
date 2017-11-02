from __future__ import absolute_import, division, print_function

from stripe.api_resources import abstract


class CountrySpec(abstract.ListableAPIResource):
    OBJECT_NAME = 'country_spec'

    @classmethod
    def class_name(cls):
        return 'country_spec'
