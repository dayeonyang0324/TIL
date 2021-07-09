# 2108

# input 사용시 시간초과 => sys.stdin.readline()로 변경하여 통과
import sys

N = int(sys.stdin.readline())
nums = list(int(sys.stdin.readline()) for _ in range(N))
nums.sort()

# avg
print('{:.0f}'.format(sum(nums) / N))

# mid
print(nums[N//2])

# many
cnt = {}
for i in nums:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

size = max(cnt.values())
result = []
for k, v in cnt.items():
    if v == size:
        result.append(k)

if len(result) >= 2:
    print(result[1])
else:
    print(result[0])

# 시간 더 줄이고 싶으면 counter 사용하는 방법도 있음
# from collections import Counter
# cnt = Counter(nums).most_common()
# if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
#     print(cnt[1][0])
# else:
#     print(cnt[0][0])

# range
print(nums[-1] - nums[0])
