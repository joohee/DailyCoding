import time
from collections import Counter

""" input file 에 있는 파일의 단어 출현 빈도수를 기록합니다. 

    도움말을 보려면 아래와 같이 입력하세요. 
        pydoc word_count_in_file
    HTML 파일로 생성하려면 아래와 같이 입력하세요. 
        pydoc -w word_count_in_file

"""
def count(inputfile, outputfile):
    """ count(inputfile, outputfile) 에서
    inputfile은 line 단위로 문장이 기록되어 있으며, 
    collections.Counter 클래스를 이용하여 
    각각의 발생 빈도수를 기록합니다. 

    Returns:
        count() 메소드 호출할 때 기록한 outputfile 이름에 
        결과값을 line 단위로 기록합니다. 

    Exception:
        FileNotFound - inputfile을 찾을 수 없을 때 발생합니다. 

    """
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
