# 2581

mini = int(input())
maxi = int(input())

# 모든 소수를 출력하기 위해 리스트를 만든다
result = []
for num in range(mini, maxi+1):
    cnt = 0
    # 1보다 큰 수여야 소수의 조건 만족한다
    # 나머지는 1978과 유사함
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
                break  # break로 for 문을 끝내줘야 시간초과가 뜨지 않음
        if cnt == 0:
            result.append(num)

# if len(result) == 0일떄로 하면 런타임 에러 발생
if len(result) > 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)
