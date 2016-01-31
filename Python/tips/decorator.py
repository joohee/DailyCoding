import time
import datetime

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

