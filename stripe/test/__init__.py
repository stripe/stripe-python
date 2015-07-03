import pkgutil
import unittest2


def all_names():
    for _, modname, _ in pkgutil.iter_modules(__path__):
        if modname.startswith('test_'):
            yield 'stripe.test.' + modname


def all():
    return unittest2.defaultTestLoader.loadTestsFromNames(all_names())


def unit():
    unit_names = [name for name in all_names() if 'integration' not in name]
    return unittest2.defaultTestLoader.loadTestsFromNames(unit_names)
