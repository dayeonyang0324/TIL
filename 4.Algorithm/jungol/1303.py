# 1303
n, m = map(int, input().split())
# print(n, m)
for i in range(n):
    for j in range(1, m+1):
        # m 갯수만큼 가로로 출력되고 세로줄에는 1에 m을 더한만큼 증가하는 규칙이 있다
        print((m*i)+j, end=' ')
    print()
