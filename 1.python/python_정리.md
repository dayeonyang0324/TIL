- `True`와 `False`로 이뤄진 `bool` 타입

- `bool(value)` 하면 `True`와 `False` 가 출력된다.

- `False`의 경우: [], 0, {}, 0.0, ’’, (), None

- `True`의 경우: `False` 경우 제외 전부. 어떤 값이나 type 이든 비어있지 않고 무언가가 존재 하면 `True`이다. 예로, `[False]`, `[0]`, `' '` 등 도 전부 `True`이다.

- set `set`은 중괄호`{}`를 통해 만들며, 순서가 없고 중복된 값이 없다.

  ```python
  list_a = [2, 1, 2, 3, 1, 1, 2]
  list(set(list_a))
  ```

- list (리스트): `[value1, value2, value3]`

- 리스트는 대괄호 `[]`로 만들 수 있다.

  값에 대한 접근: `list[i]`

- `dictionary`: {key1: value1, key2: value2, key3: value3, …}

  ### while 문: `while True:`

  `while` 문은 조건식이 `True` 인 경우 반복적으로 코드를 실행

  종료조건을 반드시 설정해줘야 한다.

  ### `for`문: `for value in sequence:`

  정해진 범위 내 (시퀀스) 에서 순차적으로 코드를 실행

  범위가 이미 정해져 있기 때문에, 종료조건을 설정해주지 않아도 된다.

  - index와 for문
    - `enumerate(iterable)`: index와 value를 반환하는 함수
    - `for index, value in enumerate(iterable)`
  - dictionary 반복문
    - `for key in dict:` key 반환 및 반복
    - `for key in dict.keys()`: key 반환 및 반복
    - `for value in dict.values()`: value 반환 및 반복
    - `for key, value in dict.items()` : key와 value 반환 및 반복

- 몫 //

- 나머지 %



#### while문 예시

```python
#1부터 입력한 수까지 더하기

a = int(input())
total = 0
ad = 0

while ad <= a:
    total += ad
    ad += 1
    
print(total) 

```

```python
#1의 자리수부터 한 줄씩 나타나게 하기

a = int(input())

while a > 0:
    print(a % 10)
    a = a // 10
```



### enumerate()

- 리스트의 인덱스와 값을 함께 추출

  ```python
  lunch = ['짜장면', '초밥', '피자', '햄버거']
  
  for index, value in enumerate(lunch):
      print(index, value)
  ```

  


### Break

- `for`나 `while`에서 반복문을 종료



### Continue

- 그냥 지나간다..
- `pass`는 아무것도 안한다.. continue는 해당 값만 빼고 진행이지만 pass는 신경 안 쓰고 그냥 출력한다.

```python
for i in range(6):
    if i % 2 == 0:
        continue
    print(f'{i}는 홀수다')
    
#이런식으로 하면 1, 3, 5의 값만 출력된다. 2, 4는 그냥 넘어간다.
```



#### 리스트 안의 딕셔너리에서 해당하는 key의 value값 구하기

- 리스트의 i는 각각의 딕셔너리에 해당하고 i의 `index` 를 구하면 된다.

```python
def dict_list_sum(ages):
    result = 0
    for i in ages:
        result += i['age']
        return result 

    
dict_list_sum([{'name':'kim', 'age':12},{'name':'lee', 'age':4}])

# [{'name':'kim', 'age':12},{'name':'lee', 'age':4}] 이것이 list
# {'name':'kim', 'age':12} 이거랑 {'name':'lee', 'age':4} 이거는 i 값임.
#  리스트 안의 i, 즉 {}에 있는 값에 대해서 i의 index인 age를 더하는 것임.
```

```python
#다른 방법으로는 list의 key값을 가져올 수 있다
age_list = ages['age']
age_list = ages.get('age')

```



#### 딕셔너리에서 조건에 맞는 키와 벨류만 그대로 뽑아오기

```python
dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45, '중국': 200}

{k:v for k, v in dusts.items() if v > 80}
#결과 : {'대전': 82, '중국': 200}
```





#### 리스트 안의 리스트를 뽑아서 딕셔너리 만들기

```python
temperatures = [ [9, 3], [11, -3], [7, -3] ]

def turn(temperatures):
    maximum = []
    minimum = []
    result = {}
    for temperature in temperatures:
        maximum += [temperature[0]]
        minimum += [temperature[1]]
    result['maxi'] = maximum
    result['mini'] = minimum
    return result
    
```



#### 수에서는 Total = 0 이지만 문자에서 Total = ''로 시작하면 된다!!

- 그 밖에도 `{}, []`에 넣고 싶으면 `total = {}, []` 로 시작한다.

```python
def get_secret_word(words):
    total = ''
    for word in words:
        total += chr(word)
    return total


get_secret_word([83, 115, 65, 102, 89])
```



#### 문자에서 한개의 알파벳만 제외하기 = 조건의 알파벳만 빼고 나머지 더하기

```python
word = input()

# apple 입력하면 a 만 빼고 pple가 출력되게 하는 for 문
result = ''

for char in word:
    if char != 'a':
        result += char
        
print(result)
```



#### 문자 순서 거꾸로 뒤집기

```python
word = input()

#입력한 값을 거꾸로 뒤집기 for문
result = ''
for i in word:
    result = i + result
print(result)
```



#### 단어 앞뒤로 하나씩 비교하기

- 앞뒤 `[1:-1]`로 비교하기

```python
#while 문으로 비교하기
def is_pal_while(word):
    while len(word) > 1:
        if word[0] == word[-1]:
            word = word[1:-1]
        else:
            return False
    return True
    

#재귀로 비교하기
def is_pal_while(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return is_pal_while(word[1:-1])
        else: 
            return False
```



# 오답노트

- 모든 요소가 참이거나 비어있으면 True를 반환하는 함수 만들기(practice1 #2)

```python
def my_all(numbers):
    result = True
    #리스트의 요소들을 순회
    for number in numbers:
        if not number:
            return False
    return True
```

```python
print(my_all([])) #True
print(my_all([1, 2, 5, '6'])) #True
print(my_all([[], 2, 5, '6'])) #False
```



- 2차원 리스트를 반복하여 숫자의 합 반환하는 함수(exercise3 #1)

```python
#index로 접근해서 풀기 - 행렬성분이라 생각하고 계산하기!
def sum_list_index(numbers):
    total = 0
    #range(0, 3) = 0, 1, 2
    #모든 배열 길이만큼 반복
    for i in range(len(numbers)):
        #내부 배열 길이만큼 반복
        for j in range(len(numbers[i])):
            #전체 배열 돌린후 내부 배열 돌리기
            total += numbers[i][j]
    return total
```

```python
#while문으로 풀기
def sum_list(numbers):
    i = 0
    result = 0
    while i < len(numbers):
        j = 0
        while j < len(numbers[i]):
            result += numbers[i][j]
            j += 1
        i += 1
    return result
```

```python
print(sum_list_index([[1, 4], [10, 5], [20, 30]]))
```



- 주어진 문자열(text)에서 제시된 알파벳(alphabet)의 등장 위치를 리스트로 반환하는 함수. 해당 알파벳이 등장하지 않으면 -1 반환 (exercise4 #1)

```python
def my_find(text, alphabet):
    result = []
    for idx, word in enumerate(text):
        if word == alphabet:
            result.append(idx)
    return result if result else -1 
```

```python
print(my_find('apple', 'p')) #[1,2]
print(my_find('a', 'p')) #-1
```



- 주어진 학생 n과 출석한 학생명부 students 문자열이 있다. 결석한 학생들로 구성된 문자열을 반환 (exercise4 #2)

```python
def check(n, students):
    students = list(map(int, students.split()))
    result = []
    for i in range(1, n+1):
        if i not in students:
            result.append(str(i))
    return ' '.join(result)
```

```python
print(check(7, '1 3 5')) # 2 4 6 7
```



- for문 2번 사용해서 1 / 12 / 123 / 1234 와 같은 식으로 계단 만들기 = 줄 세우기 안에 또 다른 줄세우기 (workshop2 #3)

```python
for i in range(1, number + 1):
    for j in range(1, i+1):
        print(j, end='')
    print()
```



- 혈액형 분류하기 - 리스트를 전달받아 키는 혈액형의 종류, value는 사람 수인 딕셔너리로 반환하는 함수 만들기 (workshop5 #2)

```python
def count_blood(kinds):
    result = {}
    for kind in kinds:
        if kind in result.keys():
            result[kind] += 1
        else:
            result[kind] = 1
    return result             
```

```python
count_blood([
     'A', 'B', 'A', 'O', 'AB', 'AB',
     'O', 'A', 'B', 'O', 'B', 'AB',
 ])
```



- 중복되는 문자를 리스트로 반환하기 (workshop6 #1)

```python
def duplicated_letters(words):
    result = []
    for word in words:
        if words.count(word) >= 2:
            if word not in result:
                result += word            
    return result    
```

```python
duplicated_letters('apple') #['p']
duplicated_letters('banana') #['a', 'n']
```



- 리스트에 나타나는 연속적인 숫자에서 하나만 남기고 삭제하는 함수 (workshop6 #3)

```python
def lonely(numbers):
    total = [numbers[0]]
    for number in numbers:
        if total[-1] != number:
            total.append(number)
    return total
```

```python
lonely([1, 1, 3, 3, 0, 1, 1]) #[1, 3, 0, 1]
lonely([4, 4, 4, 3, 3]) #[4, 3]
```



- 중복되지 않은 숫자들의 리스트 요소들의 합(exercise5 #2)

```python
def sum_of_repeat_number(numbers):
    for number in numbers:
        #number의 개수가 2이상이면 삭제
        if number == number:
            count_num = numbers.count(number)
            for i in range(count_num):
                numbers.remove(number)
        return sum(numbers)
```

```python
print(sum_of_repeat_number([4, 4, 7, 8, 10])) #25
```







