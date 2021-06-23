#10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
#(소수점 첫째 자리에서 반올림한 정수를 출력한다.)

T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    
    total = 0
    for number in numbers:
        total += number
    result = round(total / len(numbers),)
    
    print('#{} {}'.format(tc, result))