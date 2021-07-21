# 2579

N = int(input())

# 리스트 범위 안 정해놓으면 '런타임 에러' 발생
stair = [0 for _ in range(301)]
for i in range(N):
    stair[i] = int(input())

# dp 초기화
dp = [0 for _ in range(301)]
dp[0] = stair[0]  # 바닥부터 시작 1번 계단까지 최댓값
dp[1] = stair[1] + stair[0]  # 2번 계딘까지 최댓값
# 3번 계단까지 가는 2가지 방법 중 최댓값
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])
# 그 이후 계단으로 가는 방법 (마지막 계단 포함이므로 현재 계단 더하기)
for i in range(3, N):
    # 2가지 방법(3칸전에서 한칸 뛰고 전칸 현재칸, 뛰고 전칸 현재칸 오는지)
    dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

# 마지막 칸이 최종값
print(dp[N-1])
