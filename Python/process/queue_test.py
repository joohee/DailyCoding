def consumer(input_q):
    while True:
        item = input_q.get()
        print("item: ", item)
        input_q.task_done()

def producer(sequence, output_q):
    for item in sequence:
        output_q.put(item)

if __name__ == '__main__':
    from multiprocessing import Process, JoinableQueue
    q = JoinableQueue()

    cons_p = Process(target=consumer, args=(q,))
    cons_p.daemon = True
    cons_p.start()

    sequence = range(100)
    producer(sequence, q)
    
    q.join()
