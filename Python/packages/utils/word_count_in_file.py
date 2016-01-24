import time
from collections import Counter

def count(inputfile, outputfile):
    cnt = Counter()

    print("start..")
    before = time.time()
    try:
        with open(inputfile, 'r') as rf:
            for line in rf:
                for word in line.split(' '):
                    cnt[word] += 1

        with open(outputfile, 'w') as wf:
            for k, v in cnt.most_common():
                wf.write("{} {}\n".format(k, v))

    except FileNotFoundError:
        print("invalid inputfile", inputfile)

    after = time.time()
    print("done... elapse time: {0:2.2f} sec".format(after-before))

if __name__ == "__main__":
    inputfile = input("insert input file name: (default: input.txt)")
    outputfile = input("insert output file name: (default: output.txt)")

    if len(inputfile) == 0:
        inputfile = 'input.txt'
    if len(outputfile) == 0:
        outputfile = 'output.txt'
        
    count(inputfile, outputfile)
