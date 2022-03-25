from __future__ import absolute_import, division, print_function

from stripe import error, util, six
from stripe.six.moves.urllib.parse import quote_plus
from stripe.api_resources.abstract import APIResource


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

        if not isinstance(id, six.string_types):
            raise error.InvalidRequestError(
                "Could not determine which URL to request: %s instance "
                "has invalid ID: %r, %s. ID should be of type `str` (or"
                " `unicode`)" % (type(self).__name__, id, type(id)),
                "id",
            )

        id = util.utf8(id)
        base = self.class_url()
        extn = quote_plus(id)
        return "%s/%s" % (base, extn)


def test_helpers(cls):
    """
    test_helpers decorator adds a test_helpers property and
    wires the parent resource class to the nested TestHelpers class.

    Should only be used on types that inherit from APIResource.

    @test_helpers
    class Foo(APIResource):
      class TestHelpers(APIResourceTestHelpers):
    """

    def test_helpers_getter(self):
        return self.TestHelpers(self)

    if not issubclass(cls, APIResource):
        raise ValueError(
            "Could not apply @test_helpers decorator to %r."
            " The class should a subclass of APIResource." % cls
        )

    cls.TestHelpers._resource_cls = cls
    cls.TestHelpers._static_request = cls._static_request
    cls.TestHelpers._static_request_stream = cls._static_request_stream

    cls.test_helpers = property(test_helpers_getter)
    return cls
