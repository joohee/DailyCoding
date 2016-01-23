import unittest

class FooTest(unittest.TestCase):
    
    def setUp(self):
        print("FooTest setup begin")
        print("FooTest setup end")

    def tearDown(self):
        print("FooTest tearDown begin")
        print("FooTest tearDown end")

    def testA(self):
        print("FooTest:testA")
        argFoo = 123
        argBar = 456

        self.assertGreater(argFoo, argBar, "Foo is less than Bar")
        self.assertGreater(argBar, argFoo, "Foo is greater than Bar")

    def testB(self):
        print("FooTest:testB")


if __name__ == '__main__':
    unittest.main()

