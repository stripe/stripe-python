import unittest
import subprocess
import os


class WholesomeTests(unittest.TestCase):

    def test_pep8(self):
        code_dir = os.path.join(os.path.dirname(__file__), '..')

        rc = subprocess.call(('pep8', code_dir))

        if rc:
            self.fail('Code is not pep 8 compliant')

if __name__ == '__main__':
    unittest.main()
