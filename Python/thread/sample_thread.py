import threading
from queue import Queue
import time

print_lock = threading.Lock()

def exampleJob(worker):
    """
        thread lock을 잡고 메세지를 출력합니다. 
    """
    time.sleep(0.5)

    with print_lock:
        print("name: {}, worker: {}".format(threading.current_thread().name, worker))

def threader():
    """
        Queue에서 worker를 꺼내와서 thread를 실행합니다.   
    """
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()

"""
    테스트로 작업할 thread 10개를 생성하고, 
    20개의 worker를 Queue에 넣습니다. 

    q.join()코드를 통해 Queue가 빌 때 까지 기다렸다가 종료하게 됩니다. 
"""

q = Queue()

for x in range(10):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

start = time.time()

for worker in range(20):
    q.put(worker)

q.join()

print('Entire job took:', time.time()-start)
