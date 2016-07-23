from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1517927
    for i in range(len(a)):
        a[i] = -a[i]


if __name__ == '__main__':
    num = Value('d', 0.0)               # 'd' means double precision float.
    arr = Array('i', range(10))         # 'i' means signed integer.

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])

