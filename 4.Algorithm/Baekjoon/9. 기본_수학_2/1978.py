# 1978

N = int(input())
nums = list(map(int, input().split()))
# 주어진 숫자 리스트를 만들지만 1이 있으면 제외시킨다
if 1 in nums:
    nums.remove(1)

result = 0  # 소수 갯수 결과값
for num in nums:
    cnt = 0
    # 소수를 구하기 위해서는 2부터 자신보다 작은 수로 나눠봐야한다
    for i in range(2, num):
        # 2~자신보다 1 작은 수로 나눠서 나머지가 0이라면 카운트 (4라면 2가 약수로 나머지 0)
        if num % i == 0:
            cnt += 1
    # 나눠지는 수가 없다면 소수이므로 결과값에 저장
    if cnt == 0:
        result += 1

print(result)
