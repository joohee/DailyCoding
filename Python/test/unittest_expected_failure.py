import unittest

class ExpectedFailureTestCase(unittest.TestCase):
    ''' fail할 것을 가정하고 생성한 function예제입니다.
        
        unittest.TestCase를 Arugment로 갖고 생성한 클래스의 메소드를 실행합니다.
    '''
    
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(True, False, "broken")

if __name__ == "__main__":
    unittest.main()
