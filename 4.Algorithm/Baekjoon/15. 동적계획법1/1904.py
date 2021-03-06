# 1904

# dp 길이를 N으로, dp[0]부터 접근했더니 런타임 에러가 떴다.
# 가능한 모든 길이인 1,000,000으로 주어주고 인덱스를 1부터 사용하기위해 +1을 했더니 해결되었다.

# 갖고 있는 타일은 00, 1 두 종류
N = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

# 1 2 3 5 8 피보나치 - 메모리 초과가 되지 않게 15746을 나눠 연산값을 넣어준다.
for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N])
