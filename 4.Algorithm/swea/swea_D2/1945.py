#N=2^a x 3^b x 5^c x 7^d x 11^e
#N이 주어질 때 a, b, c, d, e 를 출력하라.

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counter = [0]*5
    
    while N > 1:
        if N % 2 == 0:
            N = N // 2
            counter[0] += 1
        if N % 3 ==0:
            N = N // 3
            counter[1] += 1
        if N % 5 == 0:
            N = N // 5
            counter[2] += 1
        if N % 7 == 0:
            N = N // 7
            counter[3] += 1
        if N % 11 == 0:
            N = N // 11
            counter[4] += 1
    print('#{}'.format(tc), *counter)