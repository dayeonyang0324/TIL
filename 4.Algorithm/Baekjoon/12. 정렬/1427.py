# 1427

nums = list(input())
nums.sort()
nums.reverse()
print(''.join(nums))

# sorted 사용 방법도 있음
new_num = sorted(nums, reverse=True)
