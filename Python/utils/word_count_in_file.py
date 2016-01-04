import time
from collections import Counter

cnt = Counter()

print("start..")
before = time.time()
with open('input.txt', 'r') as rf:
    for line in rf:
        for word in line.split(' '):
            cnt[word] += 1

with open('output.txt', 'w') as wf:
    for k, v in cnt.most_common():
        wf.write("{} {}\n".format(k, v))

after = time.time()

print("done... elapse time: " + str(after-before) + " sec")
