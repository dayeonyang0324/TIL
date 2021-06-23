[TOC]

# 🎄CSS

> 스타일, 레이아웃 등을 통해 HTML이 사용자에게 어떻게 표시 되는지를 지정하는 언어
>
> 사용자에게 문서(HTML)를 표시하는 방법을 지정하는 언어

<br>

## 1. CSS 구문

- 구문은 선택자와 함께 열린다. 
- 스타일을 지정할 html 요소를 선택. 
- 다음 중괄호가 있는데 이 안에는 속성과 값 쌍 형태를 가지는 하나 또는 그 이상의 선언(declaration)이 있다. 
- 각 쌍은 우리가 선택한 요소의 속성을 지정하고 속성에 부여할 값을 지정한다.

<br>

**선언문** 

- 속성 (Property)
  - 사람이 읽을 수 있는 식별자로, 어떤 (글꼴, 너비, 배경색 등) 스타일 기능을 변경할지 나타냅니다.
- 값 (Value)
  - 각 속성에는 값을 부여한다.
  - 값은 어떻게 (글꼴을 이걸로, 배경 색을 저걸로 등)스타일 기능을 변경할 건지 나타낸다.

<br>

**CSS 정의 방법**

1. `Inline style`
2. 내부 참조 (`Embedding style`)
3. 외부 참조 (`Link style`)

<br>

---

<br>

## 2. CSS Selector

> 선택자는 스타일을 지정할 웹 페이지의 HTML 요소를 대상으로 하는 데 사용

**클래스(class) 선택자**

- 클래스 선택자는 마침표( .) 문자로 시작 하며 해당 클래스가 적용된 문서의 모든 항목을 선택

<br>

**아이디(id) 선택자**

- 아이디 선택자는 `#` 문자로 시작하며 기본적으로 클래스 선택자와 같은 방식으로 사용
- 그러나 아이디는 문서 당 한 번만 사용할 수 있으며 요소에는 단일 id값만 적용 할 수 있다
- 문서에서 동일한 아이디를 여러 번 사용해도 동작하나 그렇게 하면 안된다.

<br>

**결합자**(combinators)

- 자손 결합자
  - 셀렉터A  ` `(공백) 셀렉터B
  - 셀렉터A의 모든 후손 요소(level n) 중 셀렉터B와 일치하는 요소 선택
- 자식 결합자
  - 셀렉터A `>` 셀렉터B
  - 셀렉터A의 모든 자식 요소(level 1) 중 셀렉터B와 일치하는 요소 선택
- 일반 형제 결합자
  - 셀렉터A `~` 셀렉터B
  - 셀렉터A의 형제 요소 중 셀렉터A 뒤에 위치하는 셀렉터B 요소를 **모두** 선택
- 인접 형제 결합자
  - 셀렉터A `+` 셀렉터B
  - 셀렉터A의 형제 요소 중 셀렉터A 바로 뒤에 위치하는 셀렉터B 요소를 선택
  - **단, A와 B 사이에 다른 요소가 존재하면 선택되지 않음**

<br>

**적용 우선순위**

1. `!important`
   - 다른 사람들의 코드에서 발견할 때 그 의미를 알 수 있는 것은 좋다.
   - 하지만 반드시 필요한 경우가 아니면 절대 사용하지 않는 것이 좋다.
   - `!important` 는 cascading이 정상적으로 작동하는 방식을 변경하므로, CSS 스타일 문제를 해결하기가 어렵습니다.
2. inline style
3. id 선택자
   - id는 대부분의 다른 선택자보다 우선순위가 높기 때문에 다루기가 어려워 질 수 있다.
   - 대부분의 경우 id 보다는 모두  class 선택자로 작성하는 것이 좋다.
   - 만약 문서 내 `링크 이동`이나 `for`를 사용하는 특별한 경우에만 아이디를 사용한다.
4. class 선택자
5. 요소 선택자
6. 소스 순서

<br>

---

<br>

## 3. CSS 단위

**(상대) 크기 단위**

**px**

- 모니터 해상도의 한 화소인 '픽셀'을 기준
- 픽셀의 크기는 변하지 않기 때문에 고정적인 단위

**%**

- 백분율 단위
- 가변적인 레이아웃에서 자주 사용

**em**

- em은 상속의 영향 받음, rem은 최상위 요소(html)를 기준으로 결정됨.
- 상황에 따라 각기 다른 값을 가질 수 있다.

**rem**

- 최상위 요소인 html(root em)을  절대 단위를 기준으로 삼음. 상속의 영향을 받지 않음.
- 상속에 영향을 받지 않기 때문에 대부분의 경우 `rem` 을 많이 사용한다.

**viewport**

- (스크롤을 내리지 않은 상태에서) 웹 페이지를 방문한 유저에게 현재 보이는 웹 컨텐츠의 영역
- viewport를 기준으로한 상대적인 사이즈
- 주로 스마트폰이나 테블릿 디바이스의 화면을 일컫는 용어로 사용된다.
- vw, vh

<br>

**색상 표현 단위**

1. 색상 키워드
   - 색상 키워드는 대소문자를 구분하지 않는 식별자로, red, blue, black처럼 특정 색을 나타낸다
2. RGB 색상 (r, g, b, a)
   - 빨강, 초록, 파랑을 통해 특정 색을 표현
   - 16진수 표기법이나 함수형 표기법으로 사용
   - a는 alpha(투명도)가 추가된 것
3. HSL 색상
   - 색상, 채도, 명도를 통해 특정 색상을 표현
   - a는 alpha(투명도)가 추가된 것

<br>

---

<br>

## 4. Box Model

> 웹 디자인은 contents를 담을 box model을 정의하고 CSS 속성을 통해 스타일(배경, 폰트와 텍스트 등)과 위치 및 정렬을 지정하는 것.

- 모든 HTML 요소는 box 형태로 되어있다.
- 하나의 박스는 네 부분(영역)으로 이루어 진다.
  - content / padding / border / margin

<br>

1. Content
   - 글이나 이미지, 비디오 등 요소의 실제 내용
2. Padding (안쪽 여백)
   - Border(테두리) 안쪽의 내부 여백
   - 배경색, 이미지 지정 가능
3. Border
4. Margin (바깥쪽 여백)
   - 테두리 바깥의 외부 여백
   - 배경색 지정 불가

<br>

**마진 상쇄**

- block의 top 및 bottom margin이 때로는 (결합되는 마진 중 크기가) 가장 큰 한 마진으로 결합(combine, **상쇄**(collapsed))된다.

<br>

---

<br>

## 5. Display

> display CSS 속성은 요소를 블록과 인라인 요소 중 어느 쪽으로 처리할지와 함께 자식 요소를 배치할 때 사용할 레이아웃을 설정한다.

**block**

- 쌓이는 박스
- 요소는 블록 요소 상자를 생성하여 일반 흐름에서 요소 앞뒤에 줄 바꿈을 생성한다.
- 블록 레벨 요소안에 인라인 레벨 요소가 들어갈 수 있다.

<br>

**inline**

- 줄바꿈이 일어나지 않는 행의 일부 요소
- content 너비만큼 가로 폭을 차지
- width, height, margin-top, margin-bottom을 지정할 수 없음
- 상하 여백은 line-height로 지정

<br>

**inline-block**

- inline 처럼 텍스트 흐름대로 나열, block처럼 박스 형태이기 block 속성 사용가능

<br>

**none**

- 해당 요소를 화면에서 사라지게 하며 요소의 공간조차 사라지게 한다.
- `visibility: hidden;`은 해당 요소를 화면에서 사라지게는 하나 공간은 사라지지 않는다.

<br>

---

<br>

## 6. Position

**박스의 위치 속성 & 값**

- position
  - static / absolute / relative / fixed
  - z-index

<br>

💡**기본 개념**

1. static (기본 위치)
   - 모든 태그의 기본
   - 태그의 default 값
2. relative (상대 위치)
   - 기본 위치(static)를 기준으로 좌표 속성을 사용해 위치 이동
3. absolute (절대 위치)
   - static 이 아닌 부모/조상 요소를 기준으로 좌표 속성 만큼 이동
   - 부모 요소를 찾아가고 나아가 없다면 body에 붙는다.
4. fixed (고정 위치)
   - 부모/조상 요소와 관계없이 브라우저의 viewport를 기준으로 좌표 속성 만큼 이동
   - 스크롤을 내리거나 올려도 화면에서 사라지지 않고 항상 같은 곳에 위치

<br>

**absolute**

- `absolute`는 원래 위치해 있었던 과거 위치에 있던 공간은 더 이상 존재하지 않는다는 점이 특징이다.
- 즉, 다른 모든 것과는 별개로 독자적인 곳에 놓이게 된다.
- 대체 언제 쓸까?
  - 페이지의 다른 요소의 위치와 간섭하지 않는 격리된 사용자 인터페이스 기능을 만들 수 있다.
  - 팝업 정보 상자 및 제어 메뉴, 롤오버 패널, 페이지 어느 곳에서나 끌어서 놓기할 수 있는 유저 인터페이스 페이지 등

<br>

# 🎄CSS Layout

> 웹페이지에 포함되는 요소들을 어떻게 취합하고 그것들이 어느 위치에 놓일 것인지를 제어한다.

<br>

## 1. float

> 한 요소(element)가 정상 흐름(normal flow)으로부터 빠져 텍스트 및 인라인(inline) 요소가 그 주위를 감싸 자기 컨테이너의 좌,우측을 따라 배치되어야 함을 지정한다.

**clearfix**

- float 요소와 다른 텍스트가아닌 block 요소간의 레이아웃 깨짐을 막기 위해 다음과 같이 작성한다.

  ```css
  /* float 속성을 적용한 요소의 부모요소에 적용한다. */
  /* 부모 태그 다음에 가상 요소(::after)로 내용이 빈(content:"") 블럭(display: block;)을 만들고 */
  /* 이 가상요소는 float left,right(both)를 초기화 한다는 뜻 */
  
  .clearfix::after {
    content: "";
    display: block;
    clear: both;
  }
  ```

<br>

**정리**

- flexbox 및 그리드 레이아웃과 같은 기술이 나오기 이전에 float는 열 레이아웃을 만드는데 사용되었다.
- mdn에서는 더 새롭고 나은 레이아웃 기술이 나와있으므로 레거시 레이아웃 기술로 분류해놓기도 했다.
- 결국 원래 텍스트 블록 내에서 float 이미지를 위한 역할로 돌아간 것이다.
- 여전히 사용하는 경우도 있다. (ex. naver nav bar)

<br>

## 2. flexbox

> 일명 flexbox라 불리는 Flexible Box module은 flexbox 인터페이스 내의 아이템 간 공간 배분과 강력한 정렬 기능을 제공하기 위한 1차원 레이아웃 모델로 설계되었다.
>
> 웹페이지의 컨테이너에 아이템의 폭과 높이 또는 순서를 변경해서 웹페이지의 사용 가능한 공간을 최대한 채우고 이를 디바이스 종류에 따라 유연하게 반영하도록 하는 개념



<img width="947" alt="Screen Shot 2020-08-12 at 4 53 25 PM" src="https://user-images.githubusercontent.com/18046097/89989904-8b76c300-dcbc-11ea-8427-051cce03807c.png">

<br>

**핵심 개념**

- 요소
  - flex container
  - flex items
- 축
  - maix axis (주축)
  - cros axis (교차축)

<br>

**flex container**

- flexbox 레이아웃을 형성하는 가장 기본적인 모델
- flexbox가 놓여있는 영역
- flex 컨테이너를 생성하려면 영역 내의 컨테이너 요소의 display 값을 flex 혹은 inline-flex로 지정
- flex 컨테이너를 선언시 아래와 같이 기본 값이 지정
  - item은 행으로 나열
  - item은 주축의 시작 선에서 시작
  - item은 교차축의 크기를 채우기 위해 늘어남
  - `flex-wrap` 속성은 `nowrap`으로 지정

<br>

```
Tip !

justify - main axis
align - cross axis

content - 여러 줄
items - 한 줄
self - 개별 요소
```

<br>

**flex-direction**

>  쌓이는 방향 설정 (main-axis 의 방향만 바뀜. flex 는 single-direction layout concept 이기 때문)

- row (기본값)
  - 가로로 요소가 쌓임
  - row 는 주축의 방향을 왼쪽에서 오른쪽으로 흐르게 한다.
- row-reverse
- column
  - 세로로 요소가 쌓임
  - column 은 주축의 방향을 위에서 아래로 흐르게 한다.
- column-reverse

<br>

**flex-wrap**

>  item들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정

- nowrap (기본 값)
  - 모든 아이템들 한 줄에 나타내려고 함 (그래서 자리가 없어도 튀어나옴)
- wrap : 넘치면 그 다음 줄로
- wrap-reverse : 넘치면 그 윗줄로 (역순)

<br>

**flex-flow**

>  flex-direction 과 flex-wrap 의 shorthand

```css
flex-flow: row nowrap;
```

<br>

**justify-content**

> main axis 정렬
>
> `flex-direction: row` 기준으로 작성됨

- flex-start (기본 값)
  - 시작 지점에서 쌓임(왼쪽 → 오른쪽)
- flex-end
  - 쌓이는 방향이 반대 (`flex-direction: row-reverse` 와는 다르다. 아이템의 순서는 그대로 정렬만 우측에 되는 것.)
- center
- space-between
  - 좌우 정렬 (item 들 간격 동일)
- space-around
  - 균등 좌우 정렬 (내부 요소 여백은 외곽 여백의 2배)
- space-evenly
  - 균등 정렬 (내부 요소 여백과 외각 여백 모두 동일)

<br>

**align-items**

> cross axis 여러 줄 정렬
>
> `flex-direction: row` 기준으로 작성됨

- stretch (기본 값)
  - 컨테이너를 가득 채움
- flex-start
  - 위
- flex-end
  - 아래
- center
- baseline
  - item 내부의 text에 기준선을 맞춤

<br>

**align-self**

> align-items 와 동일 (단, 개별 item 에 적용)

- auto (기본 값)
- flex-start
- flex-end
- center
- baseline
- stretch
  - 부모 컨테이너에 자동으로 맞춰서 늘어난다. (Stretch 'auto'-sized items to fit the container)

<br>

**order**

- 기본 값 : 0
- 작은 숫자 일수록 앞(왼쪽)으로 이동.

<br>

**flex-grow**

- 기본 값 : 0
- 주축에서 남는 공간을 항목들에게 분배하는 방법
- 각 아이템의 상대적 비율을 정하는 것이 아님
- 음수는 불가능

<br>

---

<br>

## 3. Bootstrap

> The most popular HTML, CSS, and JS library in the world.

- 트위터에서 시작된 오픈 소스 프론트엔드 라이브러리
- 웹 페이지에서 많이 쓰이는 요소를 거의 전부 내장하고 있다.
- 디자인을 할 시간이 크게 줄어들고, 여러 웹 브라우저를 지원하기 위한 크로스 브라우징에 골머리를 썩일 필요가 없다.

- 웹 브라우저 크기에 따라 자동으로 정렬되는 "그리드 시스템"을 지원하며,
- *"one souce multi use"* → 반응형 웹 디자인을 추구한다.

<br>

**Responsive web design**

- layout은 방문자의 화면 해상도를 고려하여야 한다.
- 스마트폰이나 태블릿 등 모바일 기기는 화면이 작기 때문에 가독성에 더욱 신경써야 한다. 
- 보통 웹사이트가 축소되어 가로 스크롤 없이 콘텐츠를 볼 수 있으나 글자가 너무 작아지기 때문이다.
- 데스크탑용, 테블릿용, 모바일용 웹사이트를 별도 구축할 수도 있지만 One Source Multi Use의 관점에서 올바른 해결책은 아니다.
- 반응형 웹 디자인(Responsive Web Design)은 화면 해상도에 따라 가로폭이나 배치를 변경하여 가독성을 높여 이러한 문제를 해결한다.
- 즉, 하나의 웹사이트를 구축하여 다양한 디바이스의 화면 해상도에 최적화된 웹사이트를 제공하는 것이다. 

<br>

---

<br>

## 4. Bootstrap Grid System

**Grid System**

- 부트스트랩의 grid system 은 containers, rows 그리고 columns 를 사용해서 컨텐츠를 레이아웃하고 정렬한다.
- 모바일 우선 flexbox grid 를 사용하여 12개의 column 시스템을 가지고 있다.
- 왜 12 columns 일까 ?
  - 12는 약수가 가장 많기 때문에 한 줄에 표시할 수 있는 종류가 제일 많다.
- 다음과 같은 구조로 사용한다.
  - .container > .row > col-*

<br>

**.row**

- row 는 columns 의 wrapper 이다.
- 각 column 에는 공간 사이를 제어하기 위한 좌우 padding 값이 있는데 이를 `gutter` 라고도 한다.
  - row 의 margin 값과 gutter 를 제거하려면 .row 에 `.no-gutters` class 를 사용한다.

<br>

**.col /  .col-***

- column class 는 row 당 가능한 12개 중 사용하려는 columns 수를 나타낸다.
- columns 너비는 백분율로 설정 되므로 항상 부모 요소를 기준으로 유동적으로 크기가 조정된다.
- grid layout 에서 내용은 반드시 columns 안에 있어야 하며 그리고 오직 columns 만 row 의 바로 하위 자식 일 수 있다.

<br>

**offset**

- `offset-*` 은 지정한 만큼의 column 공간을 무시하고 다음 공간부터 컨텐츠를 적용한다.

<br>

**Nesting**

- .row > .col-* > .row > .col-* 의 방식으로 중첩 사용 가능하다.

<br>

**Grid breakpoints**

- 부트스트랩 grid system 은 다양한 디바이스에서 적용하기 위해 특정 px 조건에 대한 지점을 정해 두었는데 이를 breakpoints 라고 한다.
- 부트스트랩은 대부분의 크기를 정의하기 위해 em 또는 rem 을 사용하지만 px 는 그리드  breakpoint 에 사용된다. (뷰포트 너비가 픽셀 단위이고 글꼴 크기에 따라 변하지 않기 때문)

<br>

# 🎄RESET CSS

> 모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 세트
>
> HTML5 Element, Typograph, Table, List 등의 요소들에 일관성있게 스타일을 적용 시키는 기본 단계

<br>

## 1. 사용 배경

- 모든 브라우저는 각자의 `user agent stylesheet` 를 가지고 있는데 (웹사이트를 보다 읽기 편하게 하기 위해)
- 문제는 이 설정이 브라우저마다 상이하다는 것

<br>

## 2. 종류

**Normalize CSS**

> gentle solution

- W3C 의 표준을 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정한다.
- 경우에 따라 IE 또는 EDGE 는 표준에 따라 수정할 수 없는 경우도 있는데, 이 경우 Normalize 는 IE 또는 EDGE 의 스타일을 나머지 브라우저에 적용시킨다.
- 실제 bootstrap 에서는 normalize.css를 자체적으로 커스텀해서 `bootstrap-reboot.css` 라는 이름으로 사용한다.

<br>

**Reset CSS**

>  aggressive solution

- 브라우저의 기본 스타일이 전혀 필요 없다는 방식으로 접근한다.
- 따라서 브라우저의 user agent와 함께 제공되는 모든 스타일을 재설정한다.
- Reset CSS의 문제점은 너무나 많은 선택자가 엉켜있고, 불필요한 오버라이드가 많이 발생하며 디버깅 시 제대로 읽을 수 없다.

<br>

