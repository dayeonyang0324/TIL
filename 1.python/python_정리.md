### Python 정리

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

  #### while문 예시

  ```python
  #1부터 입력한 수까지 더하기
  
  a = int(input())
  total = 0
  ad = 0
  
  #ad > a일때 while문 종료
  while ad <= a:
      total += ad
      ad += 1
      
  print(total) 
  ```

  ```python
  #1의 자리수부터 한 줄씩 나타나게 하기
  
  a = int(input())
  
  #a가 0이 되면 while문 종료
  while a > 0:
      print(a % 10)
      a = a // 10
  ```

  

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


