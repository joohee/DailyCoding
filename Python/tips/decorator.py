import time
import datetime

''' decorator (@...)를 이용하여 Java의 AOP 같은 역할을 할 수 있다.

    decorator 로 elapsed_time() function을 등록하면, 
    아래와 같은 결과가 나온다. 

    ⇒  python decorator.py
    start 2016-05-04 16:51:38
    hello
    end 2016-05-04 16:51:38
    Elapsed time: 0.000106 sec.
'''
def elapsed_time(functor):
    def decorated():
        start = time.time()
        start_value = datetime.datetime.fromtimestamp(start)
        print("start", start_value.strftime('%Y-%m-%d %H:%M:%S'))
        functor()
        end = time.time()
        end_value = datetime.datetime.fromtimestamp(end)
        print("end", end_value.strftime('%Y-%m-%d %H:%M:%S'))
        print("Elapsed time: {0:2.6f} sec.".format((end-start)))
    return decorated

@elapsed_time
def hello():
    print('hello')

if __name__ == '__main__':
    hello()

