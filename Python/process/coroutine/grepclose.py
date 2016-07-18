from coroutine import coroutine

'''
	execution test
	>>> from grepclose import grep
	>>> g = grep("python")
	Looking for  python
	>>> g.send("python generators rocks!")
	python generators rocks!
	>>> g.throw(RuntimeError, "You"re host")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "/Users/a1100007/Dev/joey/github/DailyCoding/Python/process/coroutine/grepclose.py", line 8, in grep
	    line = (yield)
	RuntimeError: You're host
'''
@coroutine
def grep(pattern):
    print("Looking for ", pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line)
    except GeneratorExit:
        print("Going away. Goodbye")

