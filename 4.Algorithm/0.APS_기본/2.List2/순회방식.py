
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

N = 3
M = 3


# 행 우선 순회
for i in range(N):
    for j in range(M):
        print(arr[i][j])

# 행 우선 순회 역
for i in range(N):
    for j in range(M-1, -1, -1):
        print(arr[i][j])


# 열 우선 순회
for i in range(M):
    for j in range(N):
        print(arr[j][i])

# 열 우선 순회 역
for i in range(M-1, -1, -1):
    for j in range(N):
        print(arr[j][i])


# 지그재그 순회
for i in range(N):
    for j in range(M):
        print(arr[i][j + (M-1-2*j) * (i % 2)])


# 전치행렬
for i in range(N):
    for j in range(N):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]