# 2156

# 2579번과 유사한 문제
N = int(input())
podo = [0 for _ in range(100001)]
for i in range(N):
    podo[i] = int(input())

dp = [0 for _ in range(100001)]
dp[0] = podo[0]
dp[1] = podo[1] + podo[0]
# 2579 다른점1. 계단처럼 시작점이 필요하지 않으므로 바로 전 단계만도 고려해준다
dp[2] = max(podo[0] + podo[2], podo[1] + podo[2], dp[1])
for i in range(3, N):
    # 2579 다른점2. 마찬가지로 시작점이 중요하지 않으므로 바로 전 단계만도 고려해준다.
    dp[i] = max(dp[i-3] + podo[i-1] + podo[i], dp[i-2] + podo[i], dp[i-1])

print(max(dp))
