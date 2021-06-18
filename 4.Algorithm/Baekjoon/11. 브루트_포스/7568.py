import sys
sys.stdin = open('input.txt')

N = int(input())
people = []
for i in range(N):
    x, y = map(int, input().split())
    people.append([x, y])


# 사람들의 몸무게와 키를 비교해야함
result = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    result.append(cnt)
print(*result)