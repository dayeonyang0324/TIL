# 9461

T = int(input())
for _ in range(T):
    N = int(input())

    # dp를 가능한 N의 범위로 초기화한다
    dp = [0] * 101

    # 1, 5번째 합이 6번의 값이 된다.(5 차이나는 피보나치 유형)
    dp[1], dp[2], dp[3], dp[4] = 1, 1, 1, 2

    for i in range(5, N + 1):
        dp[i] = dp[i - 5] + dp[i - 1]

    print(dp[N])
