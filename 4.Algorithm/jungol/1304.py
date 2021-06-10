# 1304

n = int(input())
# 행 우선 수열을 만들고
for i in range(1, n+1):
    # 열 수열을 만들어 값을 증가시킨다
    for j in range(n):
        print((n * j) + i, end=' ')
    print()