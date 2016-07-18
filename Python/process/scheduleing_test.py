def countdown_task(n):
    while n > 0: 
        print(n)
        yield
        n -= 1

from collections import deque
tasks = deque([
        countdown_task(5),
        countdown_task(10),
        countdown_task(15)
    ])

def scheduler(tasks):
    while tasks:
        task = tasks.popleft()
        try:
            next(task)
            tasks.append(task)
        except StopIteration:
            pass

scheduler(tasks)
