from __future__ import absolute_import, division, print_function

from stripe import error
from urllib.parse import quote_plus


class APIResourceTestHelpers:
    """
    The base type for the TestHelper nested classes.
    Handles request URL generation for test_helper custom methods.
    Should be used in combination with the @test_helpers decorator.

    @test_helpers
    class Foo(APIResource):
      class TestHelpers(APIResourceTestHelpers):
    """

    def __init__(self, resource):
        self.resource = resource

    @classmethod
    def _static_request(cls, *args, **kwargs):
        return cls._resource_cls._static_request(*args, **kwargs)

    @classmethod
    def _static_request_stream(cls, *args, **kwargs):
        return cls._resource_cls._static_request_stream(*args, **kwargs)

    @classmethod
    def class_url(cls):
        if cls == APIResourceTestHelpers:
            raise NotImplementedError(
                "APIResourceTestHelpers is an abstract class.  You should perform "
                "actions on its subclasses (e.g. Charge, Customer)"
            )
        # Namespaces are separated in object names with periods (.) and in URLs
        # with forward slashes (/), so replace the former with the latter.
        base = cls._resource_cls.OBJECT_NAME.replace(".", "/")
        return "/v1/test_helpers/%ss" % (base,)

    def instance_url(self):
        id = self.resource.get("id")

        if not isinstance(id, str):
            raise error.InvalidRequestError(
                "Could not determine which URL to request: %s instance "
                "has invalid ID: %r, %s. ID should be of type `str` (or"
                " `unicode`)" % (type(self).__name__, id, type(id)),
                "id",
            )

        base = self.class_url()
        extn = quote_plus(id)
        return "%s/%s" % (base, extn)
