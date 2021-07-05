# 7568

# 사람들의 몸무게와 키 리스트
N = int(input())
people = []
for i in range(N):
    x, y = map(int, input().split())
    people.append([x, y])

result = []
for i in range(N):
    cnt = 1
    for j in range(N):
        # 몸무게, 키가 둘다 크지 않다면 나보다 덩치 큰 사람 다음이 내 등수가 된다
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    result.append(cnt)
print(*result)
