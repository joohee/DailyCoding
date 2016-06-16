### Chapter 4

- collections library
1. Counter 
2. ChainMap
3. OrderedDict
	- defaultdict 을 통해 기본값을 설정할 수 있음. 하지 않으면 KeyError 발생. 
4. Deque - double ended queue.
	- slice 참조 지원하지 않음.(d[1:2]는 지원하지 않음.)
	- rotate() 함수 지원, 왼쪽 혹은 오른쪽으로 회전 가능. (-1: 왼쪽으로 1칸, 1: 오른쪽으로 1칸. 여러 칸 회전 가능.) 
6. heapq - Heap Queue. 우선순위 큐. 리스트 중의 최소값이 항상 리스트의 맨 앞 요소가 된다. 
	- heapify() - list -> heap queue로 정렬함. 
	- heappushpop(queue, item) : 값 추가 후 최소값 제거 
	- heapreplace(queue, item) : 최소값 제거 후 값 추가 
7. bisect - 이진 탐색 알고리즘 
8. array 
9. weakref
	- 참조 중인 객체는 삭제하지 않으나, 참조된 객체가 필요없다고 판단하면 해제하는 것 -> GC 에 의해 삭제.
	- WeakValueDictionary 일반 참조가 아닌 약한 참조로 저장 
10. enum (from 3.4)
	- 예제 
```
    >>> import enum
	>>> class Spam(enum.Enum):
	...     HAM = 1
	...     EGG = 2
	...     BACON = 3
	...
	>>> Spam.EGG
	<Spam.EGG: 2>
```
	- @enum.unique 설정하면 Enum 값이 같은 경우 에러가 난다. 
11. pprint - 사전이나 리스트 등의 객체를 보기쉽게 출력. 
12. itertools - 반복자 연산을 위해 사용한다. 
	- accumulate() : default 는 합을 구한다. 
	- permutations() : 순열 생성
	- combinations() : 조합 생성 
	- combinations_with_replacement() : 중복 포함 조합 생성. 
	- product(): direct product. 하나씩 뽑아서 짝을 짓는다. 
	- filter() : 특정 조건을 만족하는 값만 반환. 
	- filterfalse() : 특정 조건을 만족하지 "않는" 값만 반환. 
	- compress(data, selectors) : selector 값이 참에 해당될 때만 반환. 
	- count() : 등차수열 반환 
	- isslice() : 지정된 범위의 값을 얻는 반복자 생성. 
	- dropwhile() : 조건에 만족하는 값은 drop 하고 나머지 반환하여 반복자 생성.  
	- takewhile() : 조건에 만족하는 값만 반환하는 반복자 생성. 
	- repeat() : 지정 값 반복.
	- cycle() : 객체의 모든 값을 반복. 
	- groupby() : 같은 값을 그룹으로 묶어서 반환하는 반복자 생성. key를 함수로 지정 가능. 
	- zip() : 여러 개의 iterator 에서 값을 하나씩 얻엉서 tuple요소로 반환. 행과 열을 교환하는 함수로 사용 가능. 가장 짧은 iterator 가 끝나면 종료. 
	- zip_longest() : 길이가 가장 긴 iterator 의 값도 모두 사용할 수 있도록 함. 
	- map() : 반복자의 값에 함수를 적용하여 다른 값으로 변환하여 번환. 
	- starmap() : 객체를 지정한다는 점을 제외하고는 map과 동일. (args 형식이 다ㅡㄹㅁ. )
	- tee() : 반복자의 값을 여러번 반복하여 반환. 

