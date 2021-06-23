T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    num = [list(map(int, input().split())) for _ in range(N)]

    # M칸이 반복되면서 움직임
    maxi = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            num_sum = 0
            for k in range(M):
                for l in range(M):
                    num_sum += num[i + k][j + l]  # M칸의 모든 합들을 더함
            if num_sum > maxi:  # 합들 중에서 가장 큰 값 선택
                maxi = num_sum
    print('#{} {}'.format(tc, maxi))