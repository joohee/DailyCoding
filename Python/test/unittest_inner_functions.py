import unittest

class InnerFunctionsTestCase(unittest.TestCase):
    '''숫자 및 String에 대한 예제를 생성하여 실행합니다. 

        uniitest.main() function을 통해 실행합니다. 
    '''

    def test_abs(self):
        plusNum = 3
        minusNum = -3
        self.assertEqual(plusNum, abs(minusNum), "plusNum != minusNum")
        self.assertEqual(abs(plusNum), abs(minusNum), "plusNum != minusNum")

    def test_all(self):
        list = [1, 2, 3, 4]
        self.assertEqual(all(list), True, "all of list are true")

    def test_any(self):
        list_1 = [0, 1, 2, 3]
        list_2 = [0, ""]

        self.assertEqual(any(list_1) ,True)
        self.assertEqual(any(list_2), False)

    def test_chr(self):
        num = 97
        self.assertEqual(chr(97), 'a')

    def test_dir(self):
        self.assertGreater(len(dir([1,2,3])), 0)

    def test_divmod(self):
        quotient, remainder = divmod(7, 3)
        self.assertEqual(quotient, 2)
        self.assertEqual(remainder, 1)

    def test_enumerate(self):
        numA = 97
        list = ['a', 'b', 'c']
        for order, value in enumerate(list):
                # order 0 -> a, order 1 -> b, order 2 -> c
                self.assertEqual(value, chr(numA + order))

    def test_eval(self):
        result = 1 + 2
        self.assertEqual(result, eval('1+2'))

    def test_filter(self):
        filtered = filter(lambda x : x > 0, [-1, -2, 3, 4, 5, -6])
        self.assertEqual(list(filtered), [3,4,5])

    def test_hex(self):
        num = 123
        hexNum = '0x7b'
        self.assertEqual(hex(num), hexNum)

    def test_id(self):
        a = 1
        b = a
        self.assertEqual(id(a), id(b))

    def test_int(self):
        num1 = 3
        num2 = 3.4
        num3_by2 = '1000'

        self.assertEqual(int(num1), num1) 
        self.assertEqual(int(num2), num1)
        self.assertEqual(int(num3_by2, 2), 8)

    def test_isinstance(self):
        class Person:
            pass

        a = Person()
        self.assertEqual(isinstance(a, Person), True)
        
        b = 3
        self.assertEqual(isinstance(b, Person), False)

    def test_lambda(self):
        sum = lambda x, y: x + y
        self.assertEqual(sum(1,2), 3)

        l = [lambda x, y: x + y, lambda x, y: x * y]
        self.assertEqual(l[0](2, 3), 5)
        self.assertEqual(l[1](2, 3), 6)

    def test_len(self):
        self.assertEqual(len("python"), 6)
        self.assertEqual(len([1,2,3]), 3)

    def test_list(self):
        listed = list("python")
        self.assertEqual(listed[1], 'y')

        a = [1,2,3]
        b = list(a)
        # list is copied and returned. so they have different ids.
        self.assertNotEqual(id(a), id(b))

    def test_max(self):
        self.assertEqual(max([1,2,3]), 3)
        self.assertEqual(max("python"), "y")

    def test_min(self):
        self.assertEqual(min([1,2,3]), 1)
        self.assertEqual(min("python"), "h")

    def test_oct(self):
        num = 34
        octed = '0o42'
        self.assertEqual(oct(num), octed)

    def test_open(self):
        self.assertRaises(FileNotFoundError, lambda: open('aaa.txt', 'r'))

        f = open('bbb.txt', 'w')
        self.assertEqual(f.name, 'bbb.txt')
        f.close()

    def test_repr(self):
        # print object itself. not string. 
        self.assertEqual(repr('hi'.upper()), "'HI'")
        self.assertEqual(eval(repr('hi'.upper())), 'HI')

        self.assertRaises(NameError, lambda: eval(str('hi'.upper())))

    def test_sorted(self):
        result = sorted([5, 2, 3, 1])
        self.assertEqual(result[0], 1)
        result2 = sorted("python")
        self.assertEqual(result2[0], 'h')

        # different with sort() method of list
        a = [4,2,3]
        result = a.sort()
        self.assertEqual(result, None)
        self.assertEqual(a[0], 2)

    def test_str(self):
        self.assertEqual(str(3), '3')
        self.assertEqual(str('hi'), 'hi')
        self.assertNotEqual(str('hi'), "'hi'")

    def test_tuple(self):
        tupled = tuple([1,2,3,4])
        self.assertEqual(isinstance(tupled, tuple), True)

    def test_type(self):
        self.assertEqual(isinstance('abc', str), True)
        self.assertEqual(isinstance([], list), True)

    def test_zip(self):
        zipped = list(zip([1,2,3], [4,5,6]))
        self.assertEqual(zipped[0], (1,4)) 
        self.assertEqual(zipped[1], (2,5)) 
        self.assertEqual(zipped[2], (3,6)) 
            



if __name__ == "__main__":
    unittest.main()
