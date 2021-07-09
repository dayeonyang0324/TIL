# 11650

N = int(input())
table = []
for _ in range(N):
    a, b = map(int, input().split())
    table.append([a, b])

table.sort()

for i in range(N):
    print(*table[i])
