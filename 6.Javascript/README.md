# Javascript

<hr>

### 1. variables-and-identifiers

##### 1. 변수 선언 키워드 (let, const)

| let                         | const                       |
| --------------------------- | --------------------------- |
| 재할당 할 수 있는 변수 선언 | 재할당 할 수 없는 변수 선언 |
| 재선언 불가능               | 재선언 불가능               |
| 블록 스코프                 | 블록 스코프                 |

- var(함수 스코프) : 재선언 재할당 모두 가능하지만 사용 권장하지 않음

<br>

### 2. types-and-operators

##### 1. 데이터 타입 

| 원시 타입                            | 참조 타입                            |
| ------------------------------------ | ------------------------------------ |
| 객체가 아닌 기본 타입                | 객체 타입의 자료형                   |
| 변수에 해당 타입의 값이 담김         | 변수에 해당 객체의 참조 값이 담김    |
| 다른 변수에 복사 시 실제 값이 복사됨 | 다른 변수에 복사 시 참조 값이 복사됨 |

<br>

##### 2. 원시 타입

- 숫자 타입 - 0, -0, NaN 항상 거짓
- 문자열 타입 - [] 항상거짓
- undefined - js가 자동으로 할당, typeof 연산자 결과는 undefined
- null - 개발자가 할당, typeof 연산자 결과는 object
- 불리언 타입

<br>

##### 3. 참조 타입

- 함수 
- 배열 - 음수 인덱싱 불가능하다
- 객체

<br>

##### 4. 연산자

- **할당 연산자** : 오른쪽 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자

  - += , -= , /= , ++, --

- **비교 연산자** : 피연산자들을 비교해서 결과값을 불리언으로 반환하는 연산자

  - < , >

- **동등 비교 연산자(==)** : 두 피연산자가 같은 값으로 평가되는지 비교 후 불리언값 반환 (암묵적 타입 변환을 통해 타입을 일치시켜 값 비교)

- **일치 비교 연산자(===)** : 두 피연산자가 같은 값으로 평가되는지 비교 후 불리언값 반환 (두 비교 대상의 타입과 값이 모두 같은지 비교)

- **논리 연산자** : 

  - and &&
  - or ||
  - not !

- **삼항 연산자** : 세 개의 피연산자를 사용 (조건식이 참이면 : 앞의 값 사용, 아니면 : 뒤의 값 사용)

  ```js
  const result = Math.PI > 4 ? 'Yes' : 'No'
  console.log(result) // Nope
  
  console.log(true ? 1 : 2) // 1
  console.log(false ? 1: 2) // 2
  ```

<br>

### 3. conditions-and-loops

##### 1. 조건문

```js
if (condition) {
    do something
} else if (condition) {
    do something
} else {
    do something
}
```

```js
switch (expression) {
    case 'first value' : {
        do something
        break
    }
    case 'second value' : {
        do something
        break
    }
    default : {
        do something
    }
}
```

<br>

##### 2. 반복문 - while

```js
while (condition) {
    do something
}
```

<br>

##### 3. 반복문 - for

```js
// 최초 1회 진행; 매 반복 시행 전 진행; 매 반복 시행 이후 진행
for (initialization; condition; expression) {
    do something
}
```

<br>

##### 4. 반복문 - for ... in 

- 객체의 속성, 배열도 순회 가능함

```js
const capitals = {
    korea :'서울', 
    france :'파리'
}

for (let capital in capitals) {
    console.log(capital)  // korea, france
}
```

<br>

##### 5. 반복문 - for ... of

- 반복 가능한 객체를 순회하며 값을 꺼냄

```js
const fruits = ['딸기', '바나나']

for (let fruit of fruits) {
    console.log(fruit) // 딸기, 바나나
}
```

<br>

### 4. functions

##### 1. 함수 선언식

- 함수의 이름과 함께 정의

```js
function add(num1, num2) {
    return num1 + num2
}

const result = add(1, 2)
console.log(result) // 3
```

##### 2. 함수 표현식

- 함수의 표현식 내에서 정의, 함수의 이름 생략하고 익명 함수로 정의

```js
const add = function (num1, num2) {
    return num1 + num2
}

const result = add(1, 2)
console.log(result) // 3
```

<br>

```js
const greeting = function (name='NO') {
    console.log(`hi, ${name}`) 
}

greeting()  // hi, NO
```

<br>

##### 호이스팅

- 함수 선언식으로 선언한 함수는 함수 호출 이후에 선언해도 동작

```js
add(2, 7)

function add (num1, num2) {
    return num1 + num2
}
```

<br>

##### 3. 화살표 함수

- function 키워드 생략 가능
- 매개변수가 하나라면 () 생략 가능
- 몸통이 표현식 하나라면 {}과 return 생략 가능

```js
const arrow = function (name) {
    return 'hello'
}

// 1
const arrow = (name) => {return 'hello'}

// 2
const arrow = name => {return 'hello'}

// 3
const arrow = name => 'hello'
```

<br>

### 5. arrays-and-objects

##### 1. 배열 method (1)

| method          |                                         |
| --------------- | --------------------------------------- |
| reverse         | 원본 배열 요소들의 순서를 반대로 정렬   |
| push & pop      | 배열의 가장 뒤에 요소를 추가, 제거      |
| unshift & shift | 배열의 가장 앞에 요소를 추가, 제거      |
| includes        | 배열에 특정 값 존재하는지 참, 거짓 반환 |
| indexOf         | 배열에 특정 값 존재하는지 인덱스 반환   |
| join            | 배열의 모든 요소를 구분자 이용해 연결   |

- reverse

```js
const num = [1, 2, 3]
num.reverse()
console.log(num) // [3, 2, 1]
```

- push & pop

```js
const num = [1, 2, 3]
num.push(100)
console.log(num) // [1, 2, 3, 100]

num.pop()
console.log(num) // [1, 2, 3]
```

- unshift & shift

```js
const num = [1, 2, 3]

num.unshift(100)
console.log(num) // [100, 1, 2, 3]

num.shift()
console.log(num) // [1, 2, 3]
```

- include

```js
const num = [1, 2, 3]
console.log(num.includes(1)) // true
console.log(num.includes(100)) // false
```

- indexOf

```js
const num = [1, 2, 3]
let result

result = num.indexOf(3) // 2
console.log(result)

result = num.indexOf(100)  // 없으면 -1 반환 
console.log(result)
```

- join 

```js
const num = [1, 2, 3]
let result 

result = num.join() 
console.log(result)  // 1, 2, 3

result = num.join('') 
console.log(result)  // 123

result = num.join('.') 
console.log(result)  // 1 2 3

result = num.join('-') 
console.log(result)  // 1-2-3
```

<br>

##### 2. 배열 method (2)

| method  |                                                         |
| ------- | ------------------------------------------------------- |
| forEach | 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행          |
| map     | 콜백 함수 반환 값을 요소로 하는 새로운 배열 반환        |
| filter  | 콜백 함수 반환 값이 참인 요소들만 모아 새로운 배열 반환 |
| reduce  | 콜백 함수 반환 값들을 하나의 값에 누적 후 반환          |
| find    | 콜백 함수 반환 값이 참이면 해당 요소를 반환             |
| some    | 배열 요소 하나라도 판별 함수 통과하면 참을 반환         |
| every   | 배열의 모든 요소가 판별 함수 통과하면 참을 반환         |

- forEach

```js
const ssafy = ['광주', '서울', '구미', '대전']

ssafy.forEach((region, index) => {
    console.log(region, index)
}) 
// 광주 0
// 서울 1
// 구미 2
// 대전 3
```

- map

```js
const num = [1, 2, 3]

const doubleNum = num.map((num) => {
    return num * 2
})

console.log(doubleNum)  // [2, 4, 6]
```

- filter

```js
const num = [1, 2, 3]

const oddNum = num.filter((num, index) => {
    return num % 2
})

console.log(oddNum)  // 1, 3
```

- reduce - 반환값을 하나의 값(acc)에 누적 후 반환, initialValue 초기값

```js
const num = [1, 2, 3]

const result = num.reduce((acc, num) => {
    return acc + num
}, 0) // 초기값 0으로 설정

console.log(result) // 6
```

- find

```js
const avers = [
    {name:'tony', age:'45'},
    {name:'steve', age:'32'},
]

const result = avers.find((aver) => {
    return aver.name === 'tony'
})

console.log(result) // {name:'tony', age:'45'}
```

- some 

```js
const num = [1, 3, 5]

const evenNum = num.some((num) => {
    return num % 2 === 0
})

console.log(evenNum) // false

const oddNum = num.some((num) => {
    return num % 2 === 0
})

console.log(oddNum) // true
```

- every

```js
const num = [2, 4, 6]

const evenNum = num.every((num) => {
    return num % 2 === 0
})

console.log(evenNum) // true

const oddNum = num.every((num) => {
    return num % 2 === 0
})

console.log(oddNum) // false
```

<br>

##### # 배열 순회 방법 비교

```js
const ssafy = ['광주', '서울', '구미', '대전']

# for loop : 모든 브라우저 지원, 인덱스 활용해 배열 요소에 접근
for (let i = 0; i <= ssafy.length; i++) {
    console.log(i, ssafy[i])
}
// 0, 광주
// 1, 서울
// 2, 구미
// 3, 대전

# 인덱스 없이 배열의 요소에 바로 접근 가능
for (region of ssafy) {
    console.log(region)  // 광주, 서울, 구미, 대전
}

# break, continue 사용 불가능
ssafy.forEach((region, i) => {
    console.log(i, region)
})
// 0, 광주
// 1, 서울
// 2, 구미
// 3, 대전
```





























