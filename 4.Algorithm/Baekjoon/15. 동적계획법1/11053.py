# 11053

N = int(input())
nums = list(map(int, input().split()))

# 초기 리스트값 생성
dp = [1 for _ in range(1000)]
# 리스트 하나씩 돌고
for i in range(N):
    # 이전 위치까지 돌면서
    for j in range(0, i):
        # 현재 수보다 작은 수들이 있다면
        if nums[i] > nums[j]:
            # 그 수에 해당하는 값+1이나 현재값의 최댓값이 현재 위치의 값
            # for문을 돌면서 계속 리셋되기 때문에 새로운 값이 나와도 현재값과 비교할 수 있음
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
