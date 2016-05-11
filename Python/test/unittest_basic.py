import unittest

class TestStringMethods(unittest.TestCase):
    ''' unittest.TestCase 를 이용하여 UnitTest를 시행합니다.

        아래 function들은 사용 에제입니다.
    '''

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
