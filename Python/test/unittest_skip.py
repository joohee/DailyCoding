import unittest
import sys

class MyTest(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    #@unittest.skipIf(mylib.__version__ < (1, 3), "not supported in the library version")
    def test_format(self):
        print("test_format")
        # Tests that work for only a certain version of the library
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "required, windows")
    def test_windows_support(self):
        pass

if __name__ == "__main__":
    unittest.main()
