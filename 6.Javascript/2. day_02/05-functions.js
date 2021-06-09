/*
	[함수 선언식 연습]
	
	인자의 길이에 따라 true 혹은 false를 반환하는 함수 `isValid`를 작성하세요.
	- `password` 인자의 값의 길이가 8 미만이면 false를 반환합니다.
	- `password` 인자의 값의 길이가 8 이상이면 true를 반환합니다.
	- 함수는 선언식으로 작성합니다.
	- 예시) isValid('abcd')  // false
*/

// 1
function isValid (word) {
	if (word.length >= 8) {
		return true
	} else {
		return false
	}
}

// 2
function isValid2 (word) {
	return word.length >= 8
}

console.log(isValid('password'))
console.log(isValid2('password'))


/*
	[함수 표현식 연습]
	
	문자열로 구성된 배열을 특정 문자를 기준으로 하나의 문자열로 합치는 함수 `join`을 작성하세요.
	- 첫번째 인자 `array`는 문자열로 구성된 배열입니다.
	- 두번째 인자 `separator`는 문자열입니다.
	- 함수는 표현식으로 작성합니다.
	- 예시) join(['010', '1234', '5678'], '-')  // '010-1234-5678'
*/

const myJoin = function (array, separator) {
	let result = ''

	for (let idx = 0; idx < array.length; idx++) {
		// let word = array[idx]
		const word = array[idx]
		result += word
		if (idx < array.length - 1) {
			result += separator
		}
	}

	return result
}

console.log(myJoin(['010', '1234', '5678'], '-'))




/*
	[함수 기본인자 연습]
	
	주문을 받아서 주문서를 반환하는 함수 `makeOrder`를 작성하세요.
	- 첫번째 인자 `menu`는 문자열입니다.
	- 두번째 인자 `size`는 문자열이며, 기본인자는 'regular'입니다.
	- 함수는 각 인자를 속성으로 갖는 객체를 반환합니다.
	
	예시) makeOrder('mocha') // { menu: 'mocha', size: 'regular' }
*/

const makeOrder = function (menu, size = 'regular') {
	return { menu: menu, size: size }
}

console.log(makeOrder('mocha'))



/*
	[화살표 함수 연습]
	
	- 아래 celsiusToFahrenheit 함수는 섭씨 온도를 화씨 온도로 바꾸는 함수입니다. 
  - 선언식으로 작성된 함수를 "화살표 함수"로 다시 작성해보세요.
	
  function celsiusToFahrenheit (celsius) {
		const fahrenheit = celsius * 9/5 + 32
		return fahrenheit
	}

*/

function celsiusToFahrenheit (celsius) {
	// const fahrenheit = celsius * 9/5 + 32
	return celsius * 9/5 + 32
}

// 1단계
const celsiusToFahrenheit = (celsius) => {
	const fahrenheit = celsius * 9/5 + 32
	return fahrenheit
}

// 2단계
const celsiusToFahrenheit = celsius => {
	const fahrenheit = celsius * 9/5 + 32
	return fahrenheit
}

// 3단계
const celsiusToFahrenheit = celsius => celsius * 9/5 + 32
