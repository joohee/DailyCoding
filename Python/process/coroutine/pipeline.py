from follow import follow
def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line

# tail -f | grep python
logfile = open('access-log')
loglines = follow(logfile)
pylines = grep('python', loglines)

for line in pylines:
    print(line)

