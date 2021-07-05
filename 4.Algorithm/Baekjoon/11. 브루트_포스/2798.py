# 2798

# 1 모든 카드배열의 합을 넣고 정렬한 후 가까운 최댓값 선택
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
# 2 가능한 카드 배열의 합을 구하면서 바로 최댓값 뽑기
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
