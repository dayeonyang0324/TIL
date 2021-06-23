#10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    
    maxi = 0
    for number in numbers:
        if number > maxi:
            maxi = number
    
    print('#{} {}'.format(tc, maxi))