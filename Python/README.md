## join

```python
stack = 'abc'
print(''.join(stack))
>> abc
```



## index()

()안의 값을 입력하면 index 중 맨 앞에 있는 index를 찾아준다.

```python
arr = [1, 2, 3, 3, 4, 5, 6]
arr.index(3)
>> 2
```

## numpy.where()

index() 하나만 찾아주니 전부를 찾아보자.

알고리즘을 풀면서 좋은 방법인지는 모르겠다.

```python
import numpy
a = [1, 2, 3, 3, 3, 4, 5, 6]
a = numpy.array(a)	# 먼저 리스트를 배열로 변환시켜 준다. list to array
print(numpy.where(a == 3))
>> (array([2, 3, 4], dtype=int64),)
```

## pow

제곱, 제곱근, 세제곱, 세제곱 등등

```python
pow(2, 3)	// 2의 3승
>> 8
pow(100, 2)	// 100의 2승
>> 10000
pow(100, (1/2)) // 100의 제곱근
>> 10
pow(1000, (1/3)) // 1000의 세제곱근
>> 10
```

## sqrt

제곱근

```python
import math
math.sqrt(16)
>> 4.0
```

## lower() / upper()

lower(): 문자를 소문자로 바꿔줌

upper(): 문자를 대문자로 바꿔줌

```python
a = "Hello World"
print(a.lower())
>>> hello world
print(a.upper())
>>> HELLO WORLD
```

## f-string

python 3.6 이상부터 사용 가능

```python
s = 'coffee'
n = 5
result = f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요'
print(result)
```

## find (찾을 문자, 찾기 시작할 위치)

문자열 중에 특정 문자를 찾을때

```python
s = '가나다라 마바사아 자차카타 파하'
s.find('마')
# 5
s.find('가')
# 0
s.find('가',5)
# -1
```

## startswith(시작하는 문자, 시작 지점)

문자열이 특정문자로 시작하는지 여부 확인

```python
s = '가나다라 마바사아 자차카타 파하'
s.startswith('가')
# True
s.startswith('마')
# False

s.startswith('마',s.find('마')) #find는 '마' 의 시작지점을 알려줌 : 5
# True
s.startswith('마',1)
# False
```

## endswith (끝나는 문자, 문자열의 시작, 문자열의 끝)

```python
s = '가나다라 마바사아 자차카타 파하'
s.endswith('마')
# False
s.endswith('하')
# True

s.endswith('마',0,10)
# False
s.endswith('마',0,6)
# True
```

## sort()

- list로 정렬된 상태로 변경
- list만을 위한 메소드
- 오름차순 정렬: sort()
- 내림차순 정렬:sort(reverse=True)

## sorted()

- 기존의  list를 변경하는 것이 아니라 정렬된 새로운 list를 반환
- Dictionary 객체도 가능
- 오름차순 정렬: sorted()
- 내림차순 정렬: sorted(reverse=True)
- key=lambda를 사용하면  tuple 형식으로 바뀜

List

```python
a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]
b = sorted(a)
# b = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
c = sorted(a, key=lambda x:x[0])
# c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
d = sorted(a, key=lambda x:x[1])
# d = [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]
f = sorted(a, key=lambda x:-x[1])
# f = [(5, 2), (1, 2), (5, 1), (0, 1), (3, 0)]
```

Dictionary

```python
student = {
    'a': [1, 2],
    'b': [2, 3],
    'c': [3, 1]
}
print(sorted(student.items(), key=lambda x: -x[1][1]))
print(sorted(student.items(), key=lambda x: -ord(x[0])))
# [('b', [2, 3]), ('a', [1, 2]), ('c', [3, 1])]
# [('c', [3, 1]), ('b', [2, 3]), ('a', [1, 2])]
```

## isdigit()

문자열이 숫자인지 아닌지 True, False return해줌

## isalpha()

문자열이 문자인지 아닌지 True, False return 해줌