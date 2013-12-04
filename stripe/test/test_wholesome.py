import unittest
import subprocess
import os
import sys


class WholesomeTests(unittest.TestCase):

    def test_pep8(self):
        if sys.version_info >= (3, 0):
            self.skipTest('2to3 may not return pep8 compliant code')

        code_dir = os.path.join(os.path.dirname(__file__), '..')

        rc = subprocess.call(('pep8', code_dir))

        if rc:
            self.fail('Code is not pep 8 compliant')

if __name__ == '__main__':
    unittest.main()
