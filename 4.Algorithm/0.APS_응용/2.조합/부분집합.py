A = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

# 모든 부분집합 구하기
for i in range(1 << 10):
    s = 0
    for j in range(10):
        if i & (1 << j):
            s += A[j]
    # 부분집합의 합이 0이라면 부분집합 출력
    if s == 0:
        for j in range(10):
            if i & (1 << j):
                print(A[j], end=' ')
        print()