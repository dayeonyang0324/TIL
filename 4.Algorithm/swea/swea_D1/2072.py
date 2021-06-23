#10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성
T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    
    total = 0
    for number in numbers:
        if number % 2:
            total += number
        
    print('#{} {}'.format(tc, total))