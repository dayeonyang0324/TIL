# 1
N, M = map(int, input().split())
card = list(map(int, input().split()))

total = 0
result = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            total = card[i] + card[j] + card[k]
            result.append(total)

result.sort()
result.reverse()
for i in range(len(result)):
    if result[i] <= M:
        print(result[i])
        break


###############################################
# 2
N, M = map(int, input().split())
card = list(map(int, input().split()))

total = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if card[i] + card[j] + card[k] > M:
                continue
            else:
                total = max(total, card[i] + card[j] + card[k])
print(total)
