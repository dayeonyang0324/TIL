import sys
sys.stdin = open('input.txt')

N = int(input())
people = []
for i in range(N):
    x, y = map(int, input().split())
    people.append([x, y])


result = []
for i in range(N):
    cnt = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            cnt += 1
    result.append(cnt)
print(*result)