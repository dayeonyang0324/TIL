# 18870

# 시간초과
N = int(input())
nums = list(map(int, input().split()))

result = [0] * N
for i in range(N):
    cnt = 0
    sample =[]
    for j in range(N):
        if nums[i] > nums[j]:
            # 중복 제거를 위해 리스트 만들어서 넣고 갯수 세기
            if nums[j] not in sample:
                sample.append(nums[j])
                cnt += 1
    result[i] += cnt

print(*result)


# 성공(중복과 정렬, 딕셔너리 사용)
N = int(input())
nums = list(map(int, input().split()))
# 리스트를 중복없이 순서대로 정렬한 후
new_nums = sorted(set(nums))

# 해당 숫자들의 위치가 결국 결과값이 된다. (3번째에 있다면 작은 수는 2개)
result = {new_nums[i] : i for i in range(len(new_nums))}
for i in nums:
    print(result[i], end=' ')
