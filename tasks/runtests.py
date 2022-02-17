from tests.base import *
from tests.tests_httpbin import *


def run_bin_tests():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(Test1stBin)
    unittest.TextTestRunner(verbosity=2).run(test_suite)
