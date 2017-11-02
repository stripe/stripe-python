from __future__ import absolute_import, division, print_function

import os
import unittest2


def all():
    path = os.path.dirname(os.path.realpath(__file__))
    return unittest2.defaultTestLoader.discover(path)


def resources():
    path = os.path.dirname(os.path.realpath(__file__))
    return unittest2.defaultTestLoader.discover(
        os.path.join(path, "resources"))
