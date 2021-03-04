import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    num = [list(map(int, input().split())) for _ in range(N)]

    maxi = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            num_sum = 0
            for k in range(M):
                for l in range(M):
                    num_sum += num[i + k][j + l]
            if num_sum > maxi:
                maxi = num_sum
    print('#{} {}'.format(tc, maxi))