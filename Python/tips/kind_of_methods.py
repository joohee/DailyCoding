import time 

class UTIL(): 
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
    

