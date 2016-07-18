'''
    execution test
	>>> g = grep('python')
	>>> next(g)
	Looking for  python
    >>> g.send('Yeah, but no, but yeah, but no')
    >>> g.send("A series of tubes")
    >>> g.send("python generators rocks!")
    python generators rocks!
	>>> quit()

'''
def grep(pattern):
    print ("Looking for ", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)


