import time 

class UTIL(): 
    ''' UTIL class를 예로 들어, 클래스 상속 시 클래스 변수의 값이 
    어떻게 동작하는 지 알려주기 위한 예제입니다. 
    UTIL class를 상속받은 UTIL2 class의 인스턴스 변수는 독립적입니다. 

    말 그대로 class 변수이므로, 
    다시 인스턴스를 생성하여 @classmethod를 통해 변수의 값을 변경하면, 
    기존에 생성한 instance의 값도 변경됩니다. 
    '''
    util_version = "1.0"

    @staticmethod
    def now():
        t = time.localtime();
        print("time", t)

    @classmethod 
    def set_version(cls, version):
        cls.util_version = version

    def get_version(self):
        return self.util_version

class UTIL2(UTIL):
    pass

if __name__ == "__main__":
    # use static method - it's not necessary to create instance.
    print(UTIL.now())

    util = UTIL()
    util2 = UTIL2()

    # try to change class variable.
    util.set_version("2.0")
    util2.set_version("3.0")
    
    print("util's version", util.get_version())
    print("util2's version", util2.get_version())

    # try to change class variable with the same UTIL instance.
    util_again = UTIL()
    util_again.set_version("2.1")
    
    # all of two changed variable.
    print("util's version", util.get_version())
    print("util_again's version", util_again.get_version())
    

