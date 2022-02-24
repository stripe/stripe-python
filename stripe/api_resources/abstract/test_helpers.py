from __future__ import absolute_import, division, print_function


def test_helpers(cls):
    def test_helpers_getter(self):
        return self.TestHelpers(self)

    cls.TestHelpers._resource_cls = cls
    cls.test_helpers = property(test_helpers_getter)
    return cls
