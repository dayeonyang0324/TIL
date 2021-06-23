# A사 : 1리터당 P원의 돈을 내야 한다.
# B사 : 기본 사용요금이 Q원이고, 월간 사용량이 R리터 이하인 경우 요금은 기본 요금만 청구된다. 하지만 R 리터보다 많은 양을 사용한 경우 초과량에 대해 1리터당 S원의 요금을 더 내야 한다.
# 한 달간 사용하는 수도의 양이 W리터라고 할 때, 요금이 더 저렴한 회사를 골라 그 요금을 출력하는 프로그램을 작성하라.

T = int(input())
for tc in range(1, T+1):
    p, q, r, s, w = list(map(int, input().split()))
    
    print('#{}'.format(tc), end=' ')
    A = p * w
    if w <= r:
        B = q
    else:
        B = q + (w-r) * s
    
    if A < B:
        print(A)
    else:
        print(B)