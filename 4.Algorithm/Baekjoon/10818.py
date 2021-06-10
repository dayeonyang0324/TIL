
n = int(input())
num = list(map(int, input().split()))

# 갱신해줄 최대, 최소값을 변수로 두고 for문 사용
maxi = num[0]
mini = num[0]
for i in num:
    if i > maxi:
        maxi = i
    elif i < mini:
        mini = i

print(mini, maxi, end='')
