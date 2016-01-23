import unittest

class ExpectedFailureTestCase(unittest.TestCase):
    
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(True, False, "broken")

if __name__ == "__main__":
    unittest.main()
