# 11651

N = int(input())
table = []
for _ in range(N):
    a, b = map(int, input().split())
    table.append([b, a])

table.sort()

for i in range(N):
    print(table[i][1], table[i][0])
