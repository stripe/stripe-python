import os
import pkgutil
import unittest2


def all_names():
    for _, modname, _ in pkgutil.iter_modules(__path__):
        if modname.startswith('test_'):
            yield 'tests.' + modname


def all():
    path = os.path.dirname(os.path.realpath(__file__))
    return unittest2.defaultTestLoader.discover(path)


def unit():
    unit_names = [name for name in all_names() if 'integration' not in name]
    return unittest2.defaultTestLoader.loadTestsFromNames(unit_names)
