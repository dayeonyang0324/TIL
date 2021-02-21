# 숫자와 문자 변환 함수
# int, str이 있지만 만들 수 있다.

# 기본 리셋된 값에 문자열의 요소 하나하나를 넣고 10을 곱하고 다음 요소를 더해준다
# 10을 곱하고 계속 다음 요소를 넣어주는 과정을 반복한다.

def atoi(num_str):
    value = 0

    for i in range(len(num_str)):
        value *= 10
        value += ord(num_str[i]) - ord('0')

    return value

# 문자 '1234' 넣으면 숫자 1234가 출력됨