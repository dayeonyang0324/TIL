# 1932

N = int(input())
table = []
for i in range(N):
    # 왼쪽 정렬된 삼각형으로 만들기 위해 값이 없는 자리에는 0으로 채웠다
    table.append(list(map(int, input().split())) + [0] * (N-1-i))


# 두번째 행부터 순회를 하면서
for i in range(1, N):
    # 열을 살펴본다
    for j in range(0, i+1):
        # 삼각형에서는 왼쪽 위, 오른쪽 위지만 왼쪽으로 쏠린 삼각형에서는 왼쪽위, 바로 위 자리가 된다
        # 왼쪽 위, 자신의 바로 위에서 최댓값을 찾아 값을 더해준다
        table[i][j] += max(table[i-1][j-1], table[i-1][j])

# 맨 마지막 행에서 최댓값을 찾는다
print(max(table[N-1]))
