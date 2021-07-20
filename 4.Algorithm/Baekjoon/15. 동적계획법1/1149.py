# 1149

N = int(input())
table = []  # 2차원 배열로 정렬
for _ in range(N):
    table.append(list(map(int, input().split())))

# 첫번째 행을 제외하고 두번째 행부터 시작
for i in range(1, N):
    # 0, 1, 2(빨, 초, 파)에 해당하는 열을 기준으로
    # 이전 행의 현재 열을 제외하고 최솟값을 더해 값을 할당한다.
    # 2행의 0(빨간색) 열이라면 1행의 1, 2(초록, 파랑)의 최솟값을 골라 더해준다
    # 이렇게 해서 마지막 행에는 가능한 값들의 최솟값이 들어있고 이중에 최솟값을 고르면 된다
    table[i][0] += min(table[i-1][1], table[i-1][2])
    table[i][1] += min(table[i-1][0], table[i-1][2])
    table[i][2] += min(table[i-1][0], table[i-1][1])

print(min(table[N-1]))
