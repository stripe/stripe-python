import pkgutil
import unittest


def all_names():
    for _, modname, _ in pkgutil.iter_modules(__path__):
        if modname.startswith('test_'):
            yield 'stripe.test.' + modname


def all():
    return unittest.defaultTestLoader.loadTestsFromNames(all_names())


def unit():
    unit_names = [name for name in all_names() if 'integration' not in name]
    return unittest.defaultTestLoader.loadTestsFromNames(unit_names)
