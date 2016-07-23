from multiprocessing import Process, Lock, current_process


def f(l, i):
    print(current_process().name)
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
